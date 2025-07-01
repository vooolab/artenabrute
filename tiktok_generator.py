#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TikTok Video Generator Platform
365 günlük otomatik video üretim sistemi
"""

import os
import sys
import json
import random
import asyncio
import aiohttp
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any
import argparse
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
import time

# Video ve ses işleme
try:
    from moviepy import VideoFileClip, AudioFileClip, ImageClip, CompositeVideoClip, TextClip
    from moviepy import vfx, afx
except ImportError:
    print("MoviePy bulunamadı. Yükleniyor...")
    os.system("pip install moviepy")
    from moviepy import VideoFileClip, AudioFileClip, ImageClip, CompositeVideoClip, TextClip
    from moviepy import vfx, afx

# Text-to-Speech
try:
    import pyttsx3
    import gtts
except ImportError:
    print("TTS kütüphaneleri bulunamadı. Yükleniyor...")
    os.system("pip install pyttsx3 gtts")
    import pyttsx3
    import gtts

# Resim işleme
try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
    import cv2
    import numpy as np
except ImportError:
    print("Görsel işleme kütüphaneleri bulunamadı. Yükleniyor...")
    os.system("pip install Pillow opencv-python numpy")
    from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
    import cv2
    import numpy as np

# Web scraping ve API istekleri
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Web scraping kütüphaneleri bulunamadı. Yükleniyor...")
    os.system("pip install requests beautifulsoup4")
    import requests
    from bs4 import BeautifulSoup

@dataclass
class VideoContent:
    """Video içeriği veri sınıfı"""
    title: str
    script: str
    keywords: List[str]
    category: str
    duration: int  # saniye
    background_type: str  # 'image', 'video', 'generated'
    text_style: str
    voice_type: str

class ContentGenerator:
    """İçerik üretici sınıfı"""
    
    def __init__(self):
        self.categories = [
            "motivasyon", "yaşam_hikayeleri", "bilim", "teknoloji", 
            "tarih", "kültür", "spor", "sanat", "müzik", "doğa",
            "seyahat", "yemek", "moda", "sağlık", "eğitim", "komedi",
            "ilham_verici", "felsefe", "psikoloji", "girişimcilik"
        ]
        
        self.content_templates = {
            "motivasyon": [
                "Başarılı insanların 5 ortak özelliği",
                "Hayatını değiştirecek basit alışkanlıklar",
                "Zorluklarla başa çıkmanın 3 yolu",
                "Hedeflerine ulaşmak için yapman gerekenler"
            ],
            "bilim": [
                "Evrenin şaşırtıcı gerçekleri",
                "Beynimizin bilinmeyen yetenekleri",
                "Teknolojinin gelecekteki hali",
                "Doğanın mucizevi örnekleri"
            ],
            "tarih": [
                "Tarihin değiştiren anları",
                "Ünlü kişilerin bilinmeyen hikayeleri",
                "Antik medeniyetlerin sırları",
                "Tarihi değiştiren buluşlar"
            ]
        }
        
        self.trending_keywords = []
        self.update_trending_keywords()
    
    def update_trending_keywords(self):
        """Trend anahtar kelimeleri güncelle"""
        try:
            # Twitter/X API alternatifi olarak basit trend listesi
            self.trending_keywords = [
                "viral", "keşfet", "trending", "popüler", "yeni",
                "şaşırtıcı", "inanılmaz", "muhteşem", "eğlenceli",
                "bilmiyordunuz", "gizli", "sır", "gerçek", "ilginç"
            ]
        except Exception as e:
            logging.warning(f"Trend kelimeler güncellenemedi: {e}")
    
    def generate_content(self, day: int) -> VideoContent:
        """Belirtilen gün için içerik üret"""
        category = random.choice(self.categories)
        
        # Kategori bazlı başlık şablonları
        if category in self.content_templates:
            base_title = random.choice(self.content_templates[category])
        else:
            base_title = f"İlginç {category} gerçekleri"
        
        # Trend kelimeler ekle
        trending_word = random.choice(self.trending_keywords)
        title = f"{trending_word.capitalize()} | {base_title}"
        
        # Script oluştur
        script = self.generate_script(category, base_title)
        
        # Keywords
        keywords = [category, trending_word] + random.sample(self.trending_keywords, 3)
        
        return VideoContent(
            title=title,
            script=script,
            keywords=keywords,
            category=category,
            duration=random.randint(15, 60),  # 15-60 saniye arası
            background_type=random.choice(["image", "video", "generated"]),
            text_style=random.choice(["modern", "classic", "bold", "elegant"]),
            voice_type=random.choice(["female", "male", "robotic"])
        )
    
    def generate_script(self, category: str, base_title: str) -> str:
        """Kategori bazlı script üret"""
        scripts = {
            "motivasyon": [
                "Hayatta başarılı olmak istiyorsan, önce kendine inanman gerekiyor. Her gün küçük adımlarla hedefinize yaklaşın. Unutmayın, en büyük başarılar küçük başlangıçlardan doğar.",
                "Zorluklar karşısında pes etmeyin. Her zorluk, sizi daha güçlü yapacak bir fırsattır. Bugün attığınız her adım, yarının başarısının temelidir.",
                "Başarının sırrı, sürekli öğrenmeye devam etmektir. Kendinizi geliştirin, yeni şeyler deneyin ve asla öğrenmeyi bırakmayın."
            ],
            "bilim": [
                "Bilim insanları son araştırmalarda şaşırtıcı bulgular elde etti. Bu keşifler, dünya hakkındaki anlayışımızı tamamen değiştirebilir.",
                "Evrenin derinliklerinde saklı sırlar, bilim insanlarını hâlâ şaşırtmaya devam ediyor. İşte en ilginç bulgular.",
                "Teknoloji dünyasında yaşanan son gelişmeler, gelecekte hayatımızı nasıl değiştireceğini gösteriyor."
            ],
            "tarih": [
                "Tarihte yaşanan bu olay, dünya tarihinin akışını tamamen değiştirdi. İşte bu olayın bilinmeyen detayları.",
                "Antik medeniyetlerin bıraktığı izler, bugün bile bilim insanlarını şaşırtmaya devam ediyor.",
                "Bu tarihi kişiliğin hayatı, dönemin koşullarını anlamak için mükemmel bir örnek."
            ]
        }
        
        if category in scripts:
            return random.choice(scripts[category])
        else:
            return f"{category.capitalize()} hakkında ilginç bilgiler ve gerçekler sizleri bekliyor. Bu konuda bilmeniz gereken önemli detaylar."

class TextToSpeech:
    """Metinden sese dönüştürme sınıfı"""
    
    def __init__(self):
        self.tts_engine = pyttsx3.init()
        self.setup_voice()
    
    def setup_voice(self):
        """Ses ayarlarını yapılandır"""
        voices = self.tts_engine.getProperty('voices')
        if voices:
            # Türkçe ses varsa kullan
            for voice in voices:
                if 'tr' in voice.id.lower() or 'turkish' in voice.name.lower():
                    self.tts_engine.setProperty('voice', voice.id)
                    break
            else:
                # Varsayılan ses kullan
                self.tts_engine.setProperty('voice', voices[0].id)
        
        # Hız ve ses tonunu ayarla
        self.tts_engine.setProperty('rate', 150)  # Konuşma hızı
        self.tts_engine.setProperty('volume', 0.9)  # Ses seviyesi
    
    def text_to_speech(self, text: str, output_file: str, voice_type: str = "female"):
        """Metni sese dönüştür"""
        try:
            # Ses tipine göre ayarla
            voices = self.tts_engine.getProperty('voices')
            if voices:
                if voice_type == "female" and len(voices) > 1:
                    self.tts_engine.setProperty('voice', voices[1].id)
                else:
                    self.tts_engine.setProperty('voice', voices[0].id)
            
            # Ses dosyasını oluştur
            self.tts_engine.save_to_file(text, output_file)
            self.tts_engine.runAndWait()
            
            # Alternatif olarak gTTS kullan (internet bağlantısı gerekli)
            try:
                tts = gtts.gTTS(text=text, lang='tr', slow=False)
                temp_file = output_file.replace('.wav', '_gtts.mp3')
                tts.save(temp_file)
                
                # MP3'ü WAV'a dönüştür
                os.system(f"ffmpeg -i {temp_file} {output_file} -y")
                os.remove(temp_file)
            except:
                pass  # İnternet yoksa yerel TTS kullan
            
            return output_file
        except Exception as e:
            logging.error(f"TTS hatası: {e}")
            return None

class VisualGenerator:
    """Görsel üretici sınıfı"""
    
    def __init__(self):
        self.colors = [
            "#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FECA57",
            "#FF9FF3", "#54A0FF", "#5F27CD", "#00D2D3", "#FF9F43"
        ]
        
        self.gradients = [
            ["#667eea", "#764ba2"], ["#f093fb", "#f5576c"],
            ["#4facfe", "#00f2fe"], ["#43e97b", "#38f9d7"],
            ["#fa709a", "#fee140"], ["#a8edea", "#fed6e3"]
        ]
    
    def create_background_image(self, width: int = 1080, height: int = 1920, style: str = "gradient") -> str:
        """Arka plan görüntüsü oluştur"""
        img = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(img)
        
        if style == "gradient":
            # Gradyan arka plan
            gradient_colors = random.choice(self.gradients)
            for i in range(height):
                ratio = i / height
                r1, g1, b1 = self.hex_to_rgb(gradient_colors[0])
                r2, g2, b2 = self.hex_to_rgb(gradient_colors[1])
                
                r = int(r1 + (r2 - r1) * ratio)
                g = int(g1 + (g2 - g1) * ratio)
                b = int(b1 + (b2 - b1) * ratio)
                
                draw.line([(0, i), (width, i)], fill=(r, g, b))
        
        elif style == "geometric":
            # Geometrik şekiller
            base_color = random.choice(self.colors)
            img = Image.new('RGB', (width, height), color=base_color)
            draw = ImageDraw.Draw(img)
            
            # Rastgele daireler ekle
            for _ in range(random.randint(5, 15)):
                x = random.randint(0, width)
                y = random.randint(0, height)
                radius = random.randint(50, 200)
                color = random.choice(self.colors)
                alpha_color = self.hex_to_rgb(color) + (100,)
                
                overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
                overlay_draw = ImageDraw.Draw(overlay)
                overlay_draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=alpha_color)
                img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
        
        # Dosyayı kaydet
        output_path = f"generated_backgrounds/bg_{int(time.time())}.png"
        os.makedirs("generated_backgrounds", exist_ok=True)
        img.save(output_path, quality=95)
        
        return output_path
    
    def hex_to_rgb(self, hex_color: str) -> tuple:
        """Hex rengi RGB'ye dönüştür"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def create_text_overlay(self, text: str, width: int = 1080, height: int = 1920, style: str = "modern") -> str:
        """Metin bindirmesi oluştur"""
        # Şeffaf görüntü oluştur
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Font ayarları
        try:
            if style == "bold":
                font_size = 80
                font_color = "white"
                stroke_width = 4
                stroke_fill = "black"
            elif style == "elegant":
                font_size = 70
                font_color = "#FFD700"
                stroke_width = 2
                stroke_fill = "#8B4513"
            else:  # modern
                font_size = 75
                font_color = "white"
                stroke_width = 3
                stroke_fill = "#333333"
            
            # Sistem fontunu kullan
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
            except:
                font = ImageFont.load_default()
            
            # Metni ortala
            words = text.split()
            lines = []
            current_line = ""
            
            for word in words:
                test_line = current_line + " " + word if current_line else word
                bbox = draw.textbbox((0, 0), test_line, font=font)
                if bbox[2] - bbox[0] < width - 100:  # 50px margin
                    current_line = test_line
                else:
                    if current_line:
                        lines.append(current_line)
                        current_line = word
                    else:
                        lines.append(word)
            
            if current_line:
                lines.append(current_line)
            
            # Satırları çiz
            total_height = len(lines) * (font_size + 20)
            start_y = (height - total_height) // 2
            
            for i, line in enumerate(lines):
                bbox = draw.textbbox((0, 0), line, font=font)
                text_width = bbox[2] - bbox[0]
                x = (width - text_width) // 2
                y = start_y + i * (font_size + 20)
                
                # Gölge efekti
                draw.text((x+3, y+3), line, font=font, fill="black")
                # Ana metin
                draw.text((x, y), line, font=font, fill=font_color, stroke_width=stroke_width, stroke_fill=stroke_fill)
        
        except Exception as e:
            logging.error(f"Metin oluşturma hatası: {e}")
            # Basit metin
            draw.text((50, height//2), text, fill="white")
        
        output_path = f"generated_overlays/text_{int(time.time())}.png"
        os.makedirs("generated_overlays", exist_ok=True)
        img.save(output_path)
        
        return output_path

class VideoEditor:
    """Video editörü sınıfı"""
    
    def __init__(self):
        self.output_dir = Path("generated_videos")
        self.output_dir.mkdir(exist_ok=True)
        
        self.temp_dir = Path("temp_files")
        self.temp_dir.mkdir(exist_ok=True)
    
    def create_video(self, content: VideoContent, day: int) -> str:
        """İçerikten video oluştur"""
        try:
            # Ses dosyası oluştur
            tts = TextToSpeech()
            audio_file = self.temp_dir / f"audio_{day}.wav"
            tts.text_to_speech(content.script, str(audio_file), content.voice_type)
            
            if not audio_file.exists():
                logging.error(f"Ses dosyası oluşturulamadı: {audio_file}")
                return None
            
            # Görsel öğeler oluştur
            visual_gen = VisualGenerator()
            
            # Arka plan
            bg_image = visual_gen.create_background_image(style=content.text_style)
            
            # Metin overlay
            text_overlay = visual_gen.create_text_overlay(content.title, style=content.text_style)
            
            # Video oluştur
            audio_clip = AudioFileClip(str(audio_file))
            duration = audio_clip.duration
            
            # Arka plan klipini oluştur
            bg_clip = ImageClip(bg_image, duration=duration)
            bg_clip = bg_clip.resize((1080, 1920))  # TikTok boyutları
            
            # Metin overlay klipini oluştur
            text_clip = ImageClip(text_overlay, duration=duration)
            text_clip = text_clip.resize((1080, 1920))
            
            # Efektler ekle
            bg_clip = bg_clip.with_effects([vfx.FadeIn(1), vfx.FadeOut(1)])
            text_clip = text_clip.with_effects([vfx.FadeIn(0.5), vfx.FadeOut(0.5)])
            
            # Klipleri birleştir
            final_clip = CompositeVideoClip([bg_clip, text_clip])
            final_clip = final_clip.set_audio(audio_clip)
            
            # Video dosyasını kaydet
            output_file = self.output_dir / f"video_{day:03d}_{content.category}.mp4"
            final_clip.write_videofile(
                str(output_file),
                fps=30,
                codec='libx264',
                audio_codec='aac',
                temp_audiofile=str(self.temp_dir / 'temp_audio.m4a'),
                remove_temp=True
            )
            
            # Temporary dosyaları temizle
            audio_clip.close()
            final_clip.close()
            
            # Geçici dosyaları sil
            if audio_file.exists():
                audio_file.unlink()
            
            logging.info(f"Video oluşturuldu: {output_file}")
            return str(output_file)
            
        except Exception as e:
            logging.error(f"Video oluşturma hatası (Gün {day}): {e}")
            return None

class TikTokPlatform:
    """Ana TikTok platformu sınıfı"""
    
    def __init__(self, output_dir: str = "tiktok_videos"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Log ayarları
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('tiktok_generator.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        # Bileşenler
        self.content_generator = ContentGenerator()
        self.video_editor = VideoEditor()
        
        # İstatistikler
        self.stats = {
            "total_videos": 0,
            "successful_videos": 0,
            "failed_videos": 0,
            "categories": {},
            "start_time": None,
            "end_time": None
        }
    
    def generate_daily_content(self, day: int) -> Dict[str, Any]:
        """Günlük içerik üret"""
        try:
            # İçerik oluştur
            content = self.content_generator.generate_content(day)
            
            # Video oluştur
            video_path = self.video_editor.create_video(content, day)
            
            if video_path:
                self.stats["successful_videos"] += 1
                if content.category not in self.stats["categories"]:
                    self.stats["categories"][content.category] = 0
                self.stats["categories"][content.category] += 1
                
                return {
                    "day": day,
                    "success": True,
                    "content": content,
                    "video_path": video_path,
                    "file_size": os.path.getsize(video_path) if os.path.exists(video_path) else 0
                }
            else:
                self.stats["failed_videos"] += 1
                return {
                    "day": day,
                    "success": False,
                    "error": "Video oluşturulamadı"
                }
                
        except Exception as e:
            self.stats["failed_videos"] += 1
            logging.error(f"Gün {day} için içerik oluşturma hatası: {e}")
            return {
                "day": day,
                "success": False,
                "error": str(e)
            }
    
    async def generate_all_videos(self, start_day: int = 1, end_day: int = 365, max_concurrent: int = 3):
        """Tüm videoları oluştur"""
        self.stats["start_time"] = datetime.now()
        logging.info(f"365 günlük TikTok video üretimi başlatılıyor...")
        
        semaphore = asyncio.Semaphore(max_concurrent)
        
        async def generate_with_semaphore(day):
            async with semaphore:
                loop = asyncio.get_event_loop()
                with ThreadPoolExecutor() as executor:
                    result = await loop.run_in_executor(executor, self.generate_daily_content, day)
                return result
        
        tasks = []
        for day in range(start_day, end_day + 1):
            task = asyncio.create_task(generate_with_semaphore(day))
            tasks.append(task)
            
            # Progress göster
            if day % 10 == 0:
                logging.info(f"Gün {day} için görev oluşturuldu...")
        
        # Tüm görevleri çalıştır
        results = []
        completed = 0
        total = len(tasks)
        
        for task in asyncio.as_completed(tasks):
            result = await task
            results.append(result)
            completed += 1
            
            if completed % 10 == 0 or completed == total:
                progress = (completed / total) * 100
                logging.info(f"İlerleme: {completed}/{total} (%{progress:.1f})")
        
        self.stats["end_time"] = datetime.now()
        self.stats["total_videos"] = len(results)
        
        # Sonuçları kaydet
        self.save_results(results)
        
        return results
    
    def save_results(self, results: List[Dict[str, Any]]):
        """Sonuçları kaydet"""
        # JSON raporu
        report = {
            "generation_date": datetime.now().isoformat(),
            "stats": self.stats,
            "results": results
        }
        
        with open(self.output_dir / "generation_report.json", "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        # Metin raporu
        duration = self.stats["end_time"] - self.stats["start_time"]
        
        with open(self.output_dir / "summary.txt", "w", encoding="utf-8") as f:
            f.write("TikTok Video Üretim Raporu\n")
            f.write("="*50 + "\n\n")
            f.write(f"Toplam Video: {self.stats['total_videos']}\n")
            f.write(f"Başarılı: {self.stats['successful_videos']}\n")
            f.write(f"Başarısız: {self.stats['failed_videos']}\n")
            f.write(f"Başarı Oranı: %{(self.stats['successful_videos']/self.stats['total_videos']*100):.1f}\n")
            f.write(f"Süre: {duration}\n\n")
            
            f.write("Kategoriler:\n")
            for category, count in self.stats["categories"].items():
                f.write(f"  {category}: {count} video\n")
        
        logging.info("Raporlar kaydedildi.")

def main():
    """Ana fonksiyon"""
    parser = argparse.ArgumentParser(description='365 Günlük TikTok Video Üretici')
    parser.add_argument('--start-day', type=int, default=1, help='Başlangıç günü (varsayılan: 1)')
    parser.add_argument('--end-day', type=int, default=365, help='Bitiş günü (varsayılan: 365)')
    parser.add_argument('--output-dir', type=str, default='tiktok_videos', help='Çıktı dizini')
    parser.add_argument('--concurrent', type=int, default=3, help='Eşzamanlı video sayısı')
    parser.add_argument('--quick-test', action='store_true', help='Hızlı test (5 video)')
    
    args = parser.parse_args()
    
    if args.quick_test:
        args.end_day = 5
        args.concurrent = 2
        print("Hızlı test modu: 5 video üretilecek")
    
    # Platform oluştur
    platform = TikTokPlatform(args.output_dir)
    
    print("🎬 TikTok Video Üretim Platformu")
    print("=" * 50)
    print(f"📅 Gün aralığı: {args.start_day} - {args.end_day}")
    print(f"📁 Çıktı dizini: {args.output_dir}")
    print(f"⚡ Eşzamanlı: {args.concurrent}")
    print("=" * 50)
    
    # Video üretimini başlat
    try:
        results = asyncio.run(platform.generate_all_videos(
            start_day=args.start_day,
            end_day=args.end_day,
            max_concurrent=args.concurrent
        ))
        
        print("\n✅ Video üretimi tamamlandı!")
        print(f"📊 Başarılı: {platform.stats['successful_videos']}")
        print(f"❌ Başarısız: {platform.stats['failed_videos']}")
        print(f"📁 Videolar: {args.output_dir}/")
        
    except KeyboardInterrupt:
        print("\n⏹️ Kullanıcı tarafından durduruldu.")
    except Exception as e:
        print(f"\n❌ Hata: {e}")
        logging.error(f"Ana hata: {e}")

if __name__ == "__main__":
    main()