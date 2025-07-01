#!/usr/bin/env python3
"""
TikTok Video Generator Platform - Test Script
Bu script platformun temel fonksiyonlarını test eder.
"""

import sys
import json
import asyncio
from pathlib import Path

def test_imports():
    """Gerekli kütüphanelerin import edilip edilemediğini test eder."""
    print("🔍 Kütüphane importları test ediliyor...")
    
    try:
        import moviepy
        print("✅ MoviePy başarıyla import edildi")
    except ImportError as e:
        print(f"❌ MoviePy import edilemedi: {e}")
        return False
    
    try:
        import cv2
        print("✅ OpenCV başarıyla import edildi")
    except ImportError as e:
        print(f"❌ OpenCV import edilemedi: {e}")
        return False
    
    try:
        import numpy
        print("✅ NumPy başarıyla import edildi")
    except ImportError as e:
        print(f"❌ NumPy import edilemedi: {e}")
        return False
    
    try:
        from PIL import Image
        print("✅ Pillow başarıyla import edildi")
    except ImportError as e:
        print(f"❌ Pillow import edilemedi: {e}")
        return False
    
    try:
        import gtts
        print("✅ gTTS başarıyla import edildi")
    except ImportError as e:
        print(f"❌ gTTS import edilemedi: {e}")
        return False
    
    return True

def test_config():
    """Konfigürasyon dosyasını test eder."""
    print("\n📋 Konfigürasyon dosyası test ediliyor...")
    
    config_path = Path("config.json")
    if not config_path.exists():
        print("❌ config.json dosyası bulunamadı")
        return False
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        print("✅ Konfigürasyon dosyası başarıyla yüklendi")
        
        # Temel alanları kontrol et
        required_keys = ['platform', 'video_settings', 'content', 'generation']
        for key in required_keys:
            if key not in config:
                print(f"❌ Konfigürasyonda '{key}' anahtarı eksik")
                return False
        
        print(f"✅ Platform: {config['platform']['name']} v{config['platform']['version']}")
        print(f"✅ Video çözünürlüğü: {config['video_settings']['resolution']['width']}x{config['video_settings']['resolution']['height']}")
        print(f"✅ Toplam video sayısı: {config['generation']['total_videos']}")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Konfigürasyon dosyası geçersiz JSON: {e}")
        return False
    except Exception as e:
        print(f"❌ Konfigürasyon dosyası okunamadı: {e}")
        return False

def test_content_templates():
    """İçerik şablonlarını test eder."""
    print("\n📝 İçerik şablonları test ediliyor...")
    
    try:
        from content_templates import CONTENT_CATEGORIES
        print("✅ İçerik şablonları başarıyla import edildi")
        
        print(f"✅ Toplam kategori sayısı: {len(CONTENT_CATEGORIES)}")
        
        for category, templates in CONTENT_CATEGORIES.items():
            if 'titles' not in templates or 'scripts' not in templates:
                print(f"❌ '{category}' kategorisinde eksik şablon")
                return False
            print(f"✅ {category}: {len(templates['titles'])} başlık, {len(templates['scripts'])} script")
        
        return True
        
    except ImportError as e:
        print(f"❌ İçerik şablonları import edilemedi: {e}")
        return False
    except Exception as e:
        print(f"❌ İçerik şablonları test edilemedi: {e}")
        return False

def test_main_platform():
    """Ana platform dosyasını test eder."""
    print("\n🚀 Ana platform dosyası test ediliyor...")
    
    try:
        from tiktok_generator import TikTokPlatform, VideoContent
        print("✅ Ana platform sınıfları başarıyla import edildi")
        
        # Platform instance oluştur
        platform = TikTokPlatform()
        print("✅ Platform instance başarıyla oluşturuldu")
        
        return True
        
    except ImportError as e:
        print(f"❌ Ana platform import edilemedi: {e}")
        return False
    except Exception as e:
        print(f"❌ Ana platform test edilemedi: {e}")
        return False

def test_directories():
    """Gerekli dizinleri test eder."""
    print("\n📁 Dizin yapısı test ediliyor...")
    
    required_dirs = ['generated_videos', 'temp', 'backups']
    
    for dir_name in required_dirs:
        dir_path = Path(dir_name)
        if not dir_path.exists():
            try:
                dir_path.mkdir(parents=True, exist_ok=True)
                print(f"✅ '{dir_name}' dizini oluşturuldu")
            except Exception as e:
                print(f"❌ '{dir_name}' dizini oluşturulamadı: {e}")
                return False
        else:
            print(f"✅ '{dir_name}' dizini mevcut")
    
    return True

async def main():
    """Ana test fonksiyonu."""
    print("🎬 TikTok Video Generator Platform - Test Scripti")
    print("=" * 50)
    
    tests = [
        ("Kütüphane İmportları", test_imports),
        ("Konfigürasyon", test_config),
        ("İçerik Şablonları", test_content_templates),
        ("Ana Platform", test_main_platform),
        ("Dizin Yapısı", test_directories),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🧪 {test_name} testi başlatılıyor...")
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} testi başarılı")
            else:
                print(f"❌ {test_name} testi başarısız")
        except Exception as e:
            print(f"❌ {test_name} testi hata ile sonuçlandı: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Sonuçları: {passed}/{total} test başarılı")
    
    if passed == total:
        print("🎉 Tüm testler başarılı! Platform kullanıma hazır.")
        print("\n🚀 Platform kullanımı için:")
        print("   python tiktok_generator.py --help")
        return True
    else:
        print("⚠️  Bazı testler başarısız. Lütfen hataları düzeltin.")
        return False

if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)