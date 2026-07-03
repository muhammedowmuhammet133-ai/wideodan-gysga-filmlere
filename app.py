#!/usr/bin/env python3
import os
import sys
from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import cv2
import numpy as np
from moviepy.editor import VideoFileClip
import traceback

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv', 'webm'}
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500 MB
SHORT_DURATION = 60  # 60 seconds per short

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Create directories
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def detect_scenes(video_path, threshold=27):
    """Video sahnelerini tespit et"""
    try:
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        
        scenes = []
        prev_gray = None
        frame_count = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Resize for faster processing
            small_frame = cv2.resize(frame, (320, 240))
            gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
            
            if prev_gray is not None:
                diff = cv2.absdiff(prev_gray, gray)
                mean_diff = np.mean(diff)
                
                if mean_diff > threshold:
                    scenes.append(frame_count / fps)
            
            prev_gray = gray
            frame_count += 1
        
        cap.release()
        return scenes
    except Exception as e:
        print(f"Scene detection error: {e}")
        return []

def create_shorts(video_path, output_folder):
    """Videoyu şortslara böl"""
    try:
        video = VideoFileClip(video_path)
        duration = video.duration
        
        shorts_info = []
        short_count = 0
        current_time = 0
        
        while current_time < duration:
            end_time = min(current_time + SHORT_DURATION, duration)
            
            # Video klipini kes
            short_clip = video.subclip(current_time, end_time)
            
            # Dosya adı oluştur
            filename = f"short_{short_count + 1:03d}.mp4"
            filepath = os.path.join(output_folder, filename)
            
            # MP4 olarak kaydet
            print(f"Writing {filename}...")
            short_clip.write_videofile(
                filepath,
                verbose=False,
                logger=None,
                codec='libx264',
                audio_codec='aac'
            )
            
            short_clip.close()
            
            shorts_info.append({
                'filename': filename,
                'duration': int(end_time - current_time),
                'number': short_count + 1
            })
            
            current_time = end_time
            short_count += 1
        
        video.close()
        return shorts_info
    
    except Exception as e:
        print(f"Error creating shorts: {e}")
        raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload_video():
    try:
        if 'video' not in request.files:
            return jsonify({'error': 'Video dosyası bulunamadı'}), 400
        
        file = request.files['video']
        if file.filename == '':
            return jsonify({'error': 'Dosya seçilmedi'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Desteklenmeyen dosya formatı'}), 400
        
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Video işlemeye başla
        shorts_info = create_shorts(filepath, OUTPUT_FOLDER)
        
        # Orijinal dosyayı sil
        try:
            os.remove(filepath)
        except:
            pass
        
        return jsonify({
            'success': True,
            'shorts': shorts_info,
            'message': f'{len(shorts_info)} adet short video oluşturuldu'
        })
    
    except Exception as e:
        print(f"Upload error: {e}")
        traceback.print_exc()
        return jsonify({'error': f'Hata: {str(e)}'}), 500

@app.route('/api/shorts/<filename>')
def download_short(filename):
    try:
        return send_file(
            os.path.join(OUTPUT_FOLDER, filename),
            as_attachment=True,
            mimetype='video/mp4'
        )
    except Exception as e:
        return jsonify({'error': 'Dosya bulunamadı'}), 404

@app.route('/api/status')
def status():
    return jsonify({'status': 'Uygulama çalışıyor'})

if __name__ == '__main__':
    print("🎬 Video-to-Shorts Uygulaması Başlatılıyor...")
    print("Web adresi: http://localhost:5000")
    app.run(debug=True, port=5000)