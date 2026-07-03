#!/usr/bin/env python3
"""
Video-to-Shorts Uygulaması - Başlangıç Scripti
Bu script otomatik olarak tüm gereksinimleri yükler ve uygulamayı başlatır.
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Komut çalıştır"""
    print(f"\n{'='*60}")
    print(f"📋 {description}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(cmd, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Hata: {description} başarısız oldu")
        return False

def main():
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║     🎬 Video-to-Shorts Uygulaması Başlatıcısı 🎬         ║
    ║    Uzun videoları otomatik olarak şortslara çevir       ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    
    # Python version kontrolü
    if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 8):
        print("❌ Python 3.8+ gerekli")
        sys.exit(1)
    
    print(f"✅ Python versiyonu: {sys.version}")
    
    # Gereksinimleri yükle
    if not run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Python paketleri yükleniyor..."
    ):
        print("\n⚠️ Paket yüklemede hata oluştu. Lütfen manuel olarak çalıştırın:")
        print(f"{sys.executable} -m pip install -r requirements.txt")
    
    # Klasörleri oluştur
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    
    print("\n✅ Klasörler hazırlandı")
    
    # Uygulamayı başlat
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║  🚀 Uygulama başlatılıyor...                             ║
    ║  🌐 Web tarayıcınızda şunu açın:                         ║
    ║     http://localhost:5000                                ║
    ║  ⛔ Uygulamayı durdurmak için: Ctrl+C                   ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    
    run_command(f"{sys.executable} app.py", "Flask uygulaması çalıştırılıyor")

if __name__ == '__main__':
    main()