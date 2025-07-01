#!/bin/bash

# TikTok Video Generator Platform - Startup Script
# Bu script platformu başlatmak için gerekli tüm adımları gerçekleştirir

set -e  # Hata durumunda scripti durdur

echo "🎬 TikTok Video Generator Platform Başlatılıyor..."
echo "=================================================="

# Sanal ortamı kontrol et
if [ ! -d "tiktok_env" ]; then
    echo "❌ Sanal ortam bulunamadı. Lütfen önce setup_environment.py'yi çalıştırın."
    exit 1
fi

# Sanal ortamı aktive et
echo "🔄 Sanal ortam aktive ediliyor..."
source tiktok_env/bin/activate

# Python sürümünü kontrol et
echo "🐍 Python sürümü: $(python --version)"

# Gerekli dizinleri oluştur
echo "📁 Gerekli dizinler oluşturuluyor..."
mkdir -p generated_videos
mkdir -p temp
mkdir -p backups
mkdir -p logs

# Test scriptini çalıştır
echo "🧪 Platform testi yapılıyor..."
if python test_platform.py; then
    echo "✅ Platform testi başarılı!"
else
    echo "❌ Platform testi başarısız. Lütfen hataları kontrol edin."
    exit 1
fi

echo ""
echo "🚀 Platform hazır! Kullanılabilir komutlar:"
echo ""
echo "1. Tek video oluştur:"
echo "   python tiktok_generator.py --single --category motivasyon"
echo ""
echo "2. 10 video oluştur:"
echo "   python tiktok_generator.py --count 10"
echo ""
echo "3. Tüm 365 videoyu oluştur:"
echo "   python tiktok_generator.py --all"
echo ""
echo "4. Belirli bir kategoride video oluştur:"
echo "   python tiktok_generator.py --category bilim --count 5"
echo ""
echo "5. Platform durumunu kontrol et:"
echo "   python tiktok_generator.py --status"
echo ""
echo "6. Yardım için:"
echo "   python tiktok_generator.py --help"
echo ""
echo "📊 Detaylı kullanım için README.md dosyasını okuyun."
echo ""

# Kullanıcıdan komut al
read -p "🎯 Bir komut çalıştırmak ister misiniz? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Hangi işlemi yapmak istiyorsunuz?"
    echo "1) Tek video oluştur (test)"
    echo "2) 5 video oluştur"
    echo "3) Tüm 365 videoyu oluştur"
    echo "4) Platform durumunu göster"
    echo "5) Manuel komut gir"
    
    read -p "Seçiminiz (1-5): " choice
    
    case $choice in
        1)
            echo "🎬 Test videosu oluşturuluyor..."
            python tiktok_generator.py --single --category motivasyon
            ;;
        2)
            echo "🎬 5 video oluşturuluyor..."
            python tiktok_generator.py --count 5
            ;;
        3)
            echo "🎬 365 video oluşturma işlemi başlatılıyor..."
            echo "⚠️  Bu işlem uzun sürebilir. Devam etmek istediğinizden emin misiniz?"
            read -p "Devam et? (y/N): " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                python tiktok_generator.py --all
            else
                echo "İşlem iptal edildi."
            fi
            ;;
        4)
            echo "📊 Platform durumu kontrol ediliyor..."
            python tiktok_generator.py --status
            ;;
        5)
            read -p "Komutunuzu girin: " user_command
            eval "$user_command"
            ;;
        *)
            echo "Geçersiz seçim."
            ;;
    esac
else
    echo "👋 Platform hazır durumda. İstediğiniz zaman yukarıdaki komutları kullanabilirsiniz."
fi

echo ""
echo "🎉 TikTok Video Generator Platform başarıyla başlatıldı!"