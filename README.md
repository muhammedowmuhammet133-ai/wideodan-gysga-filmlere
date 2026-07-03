# 🎬 Video to Shorts

Uzun videoları otomatik olarak kısa şortslara (60 saniye) çeviren modern web uygulaması.

## ✨ Özellikler

- ✅ **Otomatik Video Bölme** - Uzun videoları 60 saniyelik şortslara böler
- ✅ **Sahne Tespit** - OpenCV ile akıllı sahne algılama
- ✅ **Modern Arayüz** - Güzel ve kullanımı kolay web arayüzü
- ✅ **Sürükle-Bırak** - Videoyu direkt sürükle bırak ile yükle
- ✅ **Toplu İndirme** - Tüm şortları tek tıkla indir
- ✅ **Hızlı İşlem** - Optimized video işleme

## 📋 Gereksinimler

- **Python 3.8+**
- **FFmpeg** (video işleme için)
- İnternet bağlantısı

## 🚀 Hızlı Başlangıç

### Windows:

```bash
# 1. Repository'yi indir veya klonla
git clone https://github.com/yourusername/wideodan-gysga-filmlere.git
cd wideodan-gysga-filmlere

# 2. run.py'ı çalıştır (otomatik kurulum yapacak)
python run.py

# 3. Tarayıcıda aç: http://localhost:5000
```

### Mac/Linux:

```bash
# 1. Repository'yi indir veya klonla
git clone https://github.com/yourusername/wideodan-gysga-filmlere.git
cd wideodan-gysga-filmlere

# 2. run.py'ı çalıştır (otomatik kurulum yapacak)
python3 run.py

# 3. Tarayıcıda aç: http://localhost:5000
```

## 📖 Kullanım

1. **Video Seç**
   - "Dosya Seç" butonuna tıkla veya sürükle-bırak yap
   - Desteklenen formatlar: MP4, AVI, MOV, MKV, WebM
   - Maksimum boyut: 500MB

2. **İşlemeye Başla**
   - "Yükle & İşle" butonuna tıkla
   - İşlem tamamlanana kadar bekle (video uzunluğuna göre değişir)

3. **İndir**
   - Oluşturulan şortları "İndir" butonuyla indir
   - Her short video 60 saniye olacak

## 🔧 Manuel Kurulum

Eğer `run.py` çalışmazsa:

```bash
# Virtual environment oluştur (opsiyonel ama tavsiye)
python -m venv venv

# Aktif et
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Gereksinimleri yükle
pip install -r requirements.txt

# Uygulamayı başlat
python app.py
```

## 📁 Dosya Yapısı

```
wideodan-gysga-filmlere/
├── app.py              # Ana Flask uygulaması
├── run.py              # Başlangıç scripti
├── requirements.txt    # Python bağımlılıkları
├── README.md           # Bu dosya
├── templates/
│   └── index.html      # Web arayüzü
├── uploads/            # Yüklenen videolar (otomatik oluşturulur)
└── outputs/            # Oluşturulan shorts (otomatik oluşturulur)
```

## ⚙️ Ayarlar

`app.py` dosyasında aşağıdaki ayarları değiştirebilirsin:

```python
SHORT_DURATION = 60        # Her short'un süresi (saniye)
MAX_FILE_SIZE = 500 * 1024 * 1024  # Maksimum dosya boyutu
PORT = 5000               # Web sunucusu portu
```

## 🐛 Sorun Giderme

### "FFmpeg bulunamadı" hatası

**Windows:**
- https://ffmpeg.org/download.html adresinden indir
- Sistem PATH'e ekle

**Mac:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

### Port zaten kullanımda

`app.py`'de port numarasını değiştir:
```python
app.run(port=5001)  # 5000 yerine 5001 kullan
```

### Video işlemesi çok yavaş

- Daha küçük bir video dosyası test et
- Bilgisayarın boş olduğundan emin ol
- `app.py`'de `SHORT_DURATION` değerini artır

## 📝 Lisans

MIT License - Serbestçe kullan ve modifiye et

## 👨‍💻 Geliştirici

Bu proje AI tarafından oluşturulmuştur.

## 🤝 Katkılar

Katılmak istiyorsan, pull request gönder veya issue aç!

## 📞 Destek

Sorun yaşıyorsan:
1. README'yi oku
2. GitHub Issues'de sor
3. Sorun detaylarını ve hata mesajını paylaş

---

**Keyifli videoları şortsa çevirmeyi!** 🎉