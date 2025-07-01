# 🎬 TikTok Video Generator Platform

365 günlük otomatik TikTok video üretim sistemi. Yapay zeka destekli içerik oluşturma, ses sentezi ve görsel efektlerle dikkat çekici videolar üretir.

## ✨ Özellikler

- **365 Günlük İçerik**: Her gün için farklı kategori ve konularda içerik
- **Yapay Zeka Seslendirme**: Text-to-Speech ile Türkçe ses üretimi
- **Otomatik Görsel Oluşturma**: Gradyan, geometrik ve özel arka planlar
- **Çoklu Kategori**: Motivasyon, bilim, teknoloji, tarih, sağlık ve daha fazlası
- **Viral İçerik Optimizasyonu**: Trend anahtar kelimeler ve hooks
- **Paralel İşleme**: Çoklu video eşzamanlı üretimi
- **TikTok Formatı**: 1080x1920 çözünürlük, 15-60 saniye süre
- **Detaylı Raporlama**: JSON ve metin formatında sonuç raporları

## 📋 Gereksinimler

### Sistem Gereksinimleri
- Python 3.8+
- FFmpeg
- 4GB+ RAM
- 10GB+ boş disk alanı

### İşletim Sistemleri
- ✅ Linux (Ubuntu, Debian, CentOS, Fedora)
- ✅ macOS
- ⚠️ Windows (manuel kurulum gerekli)

## 🚀 Hızlı Kurulum

### 1. Otomatik Kurulum (Önerilen)
```bash
git clone https://github.com/your-repo/tiktok-generator.git
cd tiktok-generator
python setup_environment.py
```

### 2. Manuel Kurulum

#### Linux (Ubuntu/Debian):
```bash
# Sistem bağımlılıkları
sudo apt-get update
sudo apt-get install -y ffmpeg git python3-pip python3-dev
sudo apt-get install -y espeak espeak-data libespeak1 libespeak-dev

# Python paketleri
pip install -r requirements.txt
```

#### macOS:
```bash
# Homebrew ile
brew install ffmpeg git python3 espeak

# Python paketleri
pip install -r requirements.txt
```

## 🎯 Kullanım

### Hızlı Test (5 Video)
```bash
python tiktok_generator.py --quick-test
```

### Tam Sürüm (365 Video)
```bash
python tiktok_generator.py
```

### Özel Parametreler
```bash
# Belirli gün aralığı
python tiktok_generator.py --start-day 1 --end-day 30

# Çıktı dizini belirleme
python tiktok_generator.py --output-dir my_videos

# Eşzamanlı video sayısı
python tiktok_generator.py --concurrent 5

# Yardım
python tiktok_generator.py --help
```

## 📁 Proje Yapısı

```
tiktok-generator/
├── tiktok_generator.py      # Ana platform dosyası
├── content_templates.py     # İçerik şablonları
├── setup_environment.py     # Kurulum scripti
├── requirements.txt         # Python bağımlılıkları
├── config.py               # Yapılandırma ayarları
├── README.md               # Bu dosya
├── tiktok_videos/          # Üretilen videolar
├── generated_backgrounds/   # Arka plan görüntüleri
├── generated_overlays/     # Metin katmanları
├── temp_files/             # Geçici dosyalar
└── logs/                   # Log dosyaları
```

## 🎨 İçerik Kategorileri

### 📈 Motivasyon
- Başarı hikayeleri
- Günlük rutinler
- Hedef belirleme
- Pozitif düşünce

### 🔬 Bilim
- Evren gerçekleri
- Beyin sırları
- Teknoloji haberleri
- Doğa mucizələri

### 📚 Eğitim
- Öğrenme teknikleri
- Hafıza geliştirme
- Dil öğrenme
- Matematik ipuçları

### 💡 Girişimcilik
- İş fikirleri
- Para kazanma yolları
- Pazarlama stratejileri
- Başarı hikayeleri

### 🏥 Sağlık
- Beslenme ipuçları
- Egzersiz faydaları
- Mental sağlık
- Doğal tedaviler

### 🧠 Psikoloji
- İnsan davranışları
- Mutluluk bilimi
- İlişki ipuçları
- Zihin oyunları

## ⚙️ Yapılandırma

`config.py` dosyasında ayarları özelleştirebilirsiniz:

```python
# Video Ayarları
VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
VIDEO_FPS = 30

# TTS Ayarları
TTS_RATE = 150
TTS_VOLUME = 0.9
TTS_LANGUAGE = "tr"

# Platform Ayarları
MAX_CONCURRENT_VIDEOS = 3
OUTPUT_DIRECTORY = "tiktok_videos"
```

## 📊 Çıktı Formatı

### Video Özellikleri
- **Çözünürlük**: 1080x1920 (TikTok formatı)
- **Süre**: 15-60 saniye
- **Format**: MP4 (H.264)
- **Ses**: AAC, 44.1kHz
- **FPS**: 30

### Dosya Yapısı
```
tiktok_videos/
├── video_001_motivasyon.mp4
├── video_002_bilim.mp4
├── video_003_teknoloji.mp4
├── generation_report.json
└── summary.txt
```

## 📈 Raporlama

### JSON Raporu (`generation_report.json`)
```json
{
  "generation_date": "2024-01-01T12:00:00",
  "stats": {
    "total_videos": 365,
    "successful_videos": 360,
    "failed_videos": 5,
    "categories": {
      "motivasyon": 52,
      "bilim": 45,
      "teknoloji": 38
    }
  },
  "results": [...]
}
```

### Metin Raporu (`summary.txt`)
```
TikTok Video Üretim Raporu
==================================================

Toplam Video: 365
Başarılı: 360
Başarısız: 5
Başarı Oranı: %98.6
Süre: 2:15:30

Kategoriler:
  motivasyon: 52 video
  bilim: 45 video
  teknoloji: 38 video
```

## 🔧 Sorun Giderme

### FFmpeg Bulunamıyor
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg
```

### Python Paket Hataları
```bash
# Pip güncelle
pip install --upgrade pip

# Sanal ortam kullan
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### Bellek Hataları
```bash
# Eşzamanlı video sayısını azalt
python tiktok_generator.py --concurrent 1

# Swap alanı artır (Linux)
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### Ses Síkıntıları
```bash
# Linux için espeak kur
sudo apt-get install espeak espeak-data

# macOS için
brew install espeak
```

## 🎛️ Gelişmiş Kullanım

### Özel İçerik Şablonları
`content_templates.py` dosyasına yeni kategoriler ekleyebilirsiniz:

```python
CONTENT_CATEGORIES["yeni_kategori"] = {
    "titles": ["Başlık 1", "Başlık 2"],
    "scripts": ["Script 1", "Script 2"]
}
```

### API Entegrasyonları
Trend konuları için API anahtarları ekleyin:

```python
# config.py
OPENAI_API_KEY = "your_key_here"
GOOGLE_API_KEY = "your_key_here"
```

### Toplu İşleme
```bash
# Aylık batch'ler halinde
for month in {1..12}; do
    start=$((($month-1)*30+1))
    end=$(($month*30))
    python tiktok_generator.py --start-day $start --end-day $end --output-dir "month_$month"
done
```

## 📱 TikTok'a Yükleme İpuçları

### Optimum Yükleme Zamanları
- Hafta içi: 6-10, 19-22
- Hafta sonu: 9-11, 19-21

### Hashtag Stratejisi
Platform otomatik olarak trend hashtagler ekler:
- `#keşfet` `#viral` `#trending`
- Kategori specific: `#motivasyon` `#bilim` `#teknoloji`
- Lokasyon: `#türkiye` `#istanbul`

### İçerik Optimizasyonu
- İlk 3 saniye kritik
- Güçlü hook'lar kullanın
- Clear CTA (Call to Action)
- Düzenli yükleme

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/YeniOzellik`)
3. Commit yapın (`git commit -am 'Yeni özellik eklendi'`)
4. Push yapın (`git push origin feature/YeniOzellik`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasını inceleyin.

## 🆘 Destek

### Sorunlar
GitHub Issues sayfasında sorun bildirebilirsiniz.

### İletişim
- Email: support@tiktokgenerator.com
- Discord: [TikTok Generator Community]
- Telegram: [@tiktokgenerator]

## 🚀 Gelecek Özellikler

- [ ] Yapay zeka ile özel görsel üretimi (DALL-E, Midjourney)
- [ ] Canlı trend takibi (Twitter, Google Trends API)
- [ ] Batch video editing
- [ ] Otomatik TikTok upload
- [ ] A/B testing için çoklu versiyon üretimi
- [ ] Analytics entegrasyonu
- [ ] Voice cloning desteği
- [ ] Çoklu dil desteği

## ⭐ Değerlendirme

Eğer bu proje işinize yaradıysa, lütfen ⭐ vererek destek olun!

---

**Not**: Bu araç eğitim ve araştırma amaçlıdır. TikTok'un topluluk kurallarına uygun içerik ürettiğinizden emin olun.
