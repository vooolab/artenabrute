#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TikTok Video Generator - Environment Setup Script
Sistem gereksinimlerini kontrol eder ve eksik paketleri kurar
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

def check_python_version():
    """Python versiyonunu kontrol et"""
    print("🐍 Python versiyonu kontrol ediliyor...")
    version = sys.version_info
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 veya üzeri gerekli!")
        print(f"   Mevcut versiyon: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Uygun")
    return True

def check_system_dependencies():
    """Sistem bağımlılıklarını kontrol et"""
    print("\n🔧 Sistem bağımlılıkları kontrol ediliyor...")
    
    dependencies = {
        'ffmpeg': 'Video işleme için gerekli',
        'git': 'Git işlemleri için gerekli'
    }
    
    missing = []
    
    for dep, desc in dependencies.items():
        if shutil.which(dep):
            print(f"✅ {dep} - Bulundu")
        else:
            print(f"❌ {dep} - Bulunamadı ({desc})")
            missing.append(dep)
    
    return missing

def install_system_dependencies():
    """Sistem bağımlılıklarını kur"""
    print("\n📦 Sistem bağımlılıkları kuruluyor...")
    
    system = platform.system().lower()
    
    if system == "linux":
        # Ubuntu/Debian
        if shutil.which("apt-get"):
            commands = [
                "sudo apt-get update",
                "sudo apt-get install -y ffmpeg git python3-pip python3-dev",
                "sudo apt-get install -y espeak espeak-data libespeak1 libespeak-dev",
                "sudo apt-get install -y festival festvox-kalpc16k",
                "sudo apt-get install -y libavcodec-extra libavformat-dev libswscale-dev"
            ]
        # CentOS/RHEL/Fedora
        elif shutil.which("yum") or shutil.which("dnf"):
            package_manager = "dnf" if shutil.which("dnf") else "yum"
            commands = [
                f"sudo {package_manager} update -y",
                f"sudo {package_manager} install -y ffmpeg git python3-pip python3-devel",
                f"sudo {package_manager} install -y espeak espeak-devel",
                f"sudo {package_manager} install -y festival"
            ]
        else:
            print("❌ Desteklenmeyen Linux dağıtımı!")
            return False
            
    elif system == "darwin":  # macOS
        if shutil.which("brew"):
            commands = [
                "brew update",
                "brew install ffmpeg git python3",
                "brew install espeak"
            ]
        else:
            print("❌ Homebrew bulunamadı! Lütfen önce Homebrew'i kurun: https://brew.sh")
            return False
            
    elif system == "windows":
        print("❌ Windows için otomatik kurulum desteklenmiyor!")
        print("   Lütfen manuel olarak şunları kurun:")
        print("   - FFmpeg: https://ffmpeg.org/download.html")
        print("   - Git: https://git-scm.com/download/win")
        return False
    else:
        print(f"❌ Desteklenmeyen işletim sistemi: {system}")
        return False
    
    for cmd in commands:
        print(f"🔄 Çalıştırılıyor: {cmd}")
        try:
            result = subprocess.run(cmd.split(), check=True, capture_output=True, text=True)
            print(f"✅ Başarılı")
        except subprocess.CalledProcessError as e:
            print(f"❌ Hata: {e}")
            print(f"   Stdout: {e.stdout}")
            print(f"   Stderr: {e.stderr}")
            return False
    
    return True

def install_python_packages():
    """Python paketlerini kur"""
    print("\n📚 Python paketleri kuruluyor...")
    
    # Pip'i güncelle
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        print("✅ pip güncellendi")
    except subprocess.CalledProcessError:
        print("⚠️ pip güncellemesi başarısız")
    
    # requirements.txt'den paketleri kur
    requirements_file = Path("requirements.txt")
    if requirements_file.exists():
        try:
            cmd = [sys.executable, "-m", "pip", "install", "-r", str(requirements_file)]
            subprocess.run(cmd, check=True)
            print("✅ Python paketleri kuruldu")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Python paket kurulumu başarısız: {e}")
            return False
    else:
        print("❌ requirements.txt bulunamadı!")
        return False

def create_directories():
    """Gerekli dizinleri oluştur"""
    print("\n📁 Dizinler oluşturuluyor...")
    
    directories = [
        "tiktok_videos",
        "generated_videos", 
        "generated_backgrounds",
        "generated_overlays",
        "temp_files",
        "logs",
        "exports"
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ {directory}/")
    
    return True

def test_installation():
    """Kurulumu test et"""
    print("\n🧪 Kurulum test ediliyor...")
    
    try:
        # Test imports
        print("📦 Paket importları test ediliyor...")
        import moviepy
        print("✅ moviepy")
        
        import PIL
        print("✅ PIL")
        
        import cv2
        print("✅ opencv")
        
        import numpy
        print("✅ numpy")
        
        import pyttsx3
        print("✅ pyttsx3")
        
        try:
            import gtts
            print("✅ gtts")
        except ImportError:
            print("⚠️ gtts (internet gerektiriyor)")
        
        # Test ffmpeg
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ ffmpeg")
        else:
            print("❌ ffmpeg test başarısız")
            return False
        
        print("\n✅ Tüm testler başarılı!")
        return True
        
    except ImportError as e:
        print(f"❌ Import hatası: {e}")
        return False
    except Exception as e:
        print(f"❌ Test hatası: {e}")
        return False

def create_config_file():
    """Yapılandırma dosyası oluştur"""
    print("\n⚙️ Yapılandırma dosyası oluşturuluyor...")
    
    config = """# TikTok Video Generator - Yapılandırma

# Video Ayarları
VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
VIDEO_FPS = 30
VIDEO_CODEC = "libx264"
AUDIO_CODEC = "aac"

# TTS Ayarları
TTS_RATE = 150
TTS_VOLUME = 0.9
TTS_LANGUAGE = "tr"

# Görsel Ayarları
BACKGROUND_STYLES = ["gradient", "geometric", "solid"]
TEXT_STYLES = ["modern", "classic", "bold", "elegant"]
FONT_SIZES = [60, 70, 80, 90]

# Platform Ayarları
MAX_CONCURRENT_VIDEOS = 3
OUTPUT_DIRECTORY = "tiktok_videos"
TEMP_DIRECTORY = "temp_files"

# API Anahtarları (isteğe bağlı)
# OPENAI_API_KEY = "your_key_here"
# GOOGLE_API_KEY = "your_key_here"

# Trend Takibi
USE_TRENDING_TOPICS = True
UPDATE_TRENDS_DAILY = True

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = "logs/tiktok_generator.log"
"""
    
    with open("config.py", "w", encoding="utf-8") as f:
        f.write(config)
    
    print("✅ config.py oluşturuldu")

def main():
    """Ana kurulum fonksiyonu"""
    print("🎬 TikTok Video Generator - Kurulum Başlatılıyor")
    print("=" * 60)
    
    # Python versiyonu kontrol
    if not check_python_version():
        sys.exit(1)
    
    # Sistem bağımlılıkları kontrol
    missing_deps = check_system_dependencies()
    
    if missing_deps:
        print(f"\n⚠️ Eksik bağımlılıklar: {', '.join(missing_deps)}")
        
        install_choice = input("\n❓ Otomatik kurulum yapılsın mı? (y/n): ").lower()
        if install_choice in ['y', 'yes', 'evet', 'e']:
            if not install_system_dependencies():
                print("❌ Sistem bağımlılıkları kurulamadı!")
                sys.exit(1)
        else:
            print("❌ Eksik bağımlılıkları manuel olarak kurun ve tekrar deneyin.")
            sys.exit(1)
    
    # Python paketleri kur
    if not install_python_packages():
        print("❌ Python paketleri kurulamadı!")
        sys.exit(1)
    
    # Dizinleri oluştur
    create_directories()
    
    # Yapılandırma dosyası oluştur
    create_config_file()
    
    # Kurulumu test et
    if test_installation():
        print("\n🎉 Kurulum başarıyla tamamlandı!")
        print("\n📋 Kullanım:")
        print("   Hızlı test: python tiktok_generator.py --quick-test")
        print("   Tam sürüm: python tiktok_generator.py")
        print("   Yardım:    python tiktok_generator.py --help")
        
        # Demo çalıştırma önerisi
        demo_choice = input("\n❓ Demo video oluşturmak ister misiniz? (y/n): ").lower()
        if demo_choice in ['y', 'yes', 'evet', 'e']:
            print("\n🚀 Demo başlatılıyor...")
            os.system("python tiktok_generator.py --quick-test")
    else:
        print("❌ Kurulum test edilemedi! Lütfen hataları düzeltin.")
        sys.exit(1)

if __name__ == "__main__":
    main()