#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TikTok Video Content Templates
365 günlük çeşitli içerik şablonları
"""

CONTENT_CATEGORIES = {
    "motivasyon": {
        "titles": [
            "Başarı için yapman gereken 5 şey",
            "Hayatını değiştirecek günlük rutinler",
            "Zorluklarla başa çıkmanın sırları",
            "Kendine güvenin böyle artırılır",
            "Hedeflerine ulaşmanın yolları",
            "Başarılı insanların alışkanlıkları",
            "Sabah rutini nasıl yapılır",
            "Motivasyonunu kaybetme",
            "İç sesini susturmanın yolları",
            "Başarısızlıktan ders çıkarma"
        ],
        "scripts": [
            "Başarılı olmak istiyorsan, her sabah bu 5 şeyi yap: 1) Erkenden kalk 2) Hedeflerini gözden geçir 3) Spor yap 4) Kitap oku 5) Pozitif düşün. Bu alışkanlıklar hayatını tamamen değiştirecek.",
            "Zorluklarla karşılaştığında unutma: Her zorluk seni daha güçlü yapar. Pes etme, çünkü en karanlık anlar şafaktan hemen öncedir. Sen her şeyi başarabilirsin!",
            "Başarının sırrı: %1 ilham, %99 ter. Hayal kurmak yetmez, harekete geç! Bugün küçük bir adım at, yarın büyük değişiklikleri gör.",
            "Kendine inanmıyorsan kimse inanmaz. Aynaya bak ve söyle: 'Ben başarırım, ben değerliyim, ben güçlüyüm.' Pozitif iç sesin hayatını değiştirir.",
            "Başarısızlık başarının karşıtı değil, bir parçasıdır. Her düştüğünde daha güçlü kalkarsın. Vazgeçmek sadece kaybedenlerin seçimidir."
        ]
    },
    
    "bilim": {
        "titles": [
            "Evrenin şaşırtıcı gerçekleri",
            "Beynimizin bilinmeyen sırları",
            "Teknolojinin gelecekteki hali",
            "Doğanın mucizevi örnekleri",
            "Yapay zekanın şaşırtıcı yetenekleri",
            "Uzayın gizemli olayları",
            "İnsan vücudunun muhteşem özellikleri",
            "Bilimin açıklayamadığı fenomenler",
            "Gelecekteki buluşlar",
            "Kuantum fiziğinin sırları"
        ],
        "scripts": [
            "Biliyor muydun ki beynin sadece %10'unu kullanıyoruz? Bu efsane tamamen yanlış! Beyninin %100'ünü kullanıyorsun, sadece aynı anda değil. MRI taramaları bunu kanıtlıyor.",
            "Evrenin %95'i karanlık madde ve karanlık enerjidir. Yani gördüğümüz her şey evrenin sadece %5'i! Bu ne kadar şaşırtıcı değil mi?",
            "Yapay zeka artık sanat eseri yaratıyor, müzik besteliyoor ve hatta şiir yazıyor. GPT modelleri insanlardan ayırt edilemeyen metinler üretiyor. Gelecek şimdiden burada!",
            "Okyanusların %80'i henüz keşfedilmedi. Aya gitmek okyanusların derinliklerini keşfetmekten daha kolay! Denizlerde hangi canlılar yaşıyor acaba?",
            "İnsan DNA'sının %99.9'u diğer insanlarla aynı. Sadece %0.1'lik fark seni benzersiz yapıyor. Sen gerçekten özelsin!"
        ]
    },
    
    "tarih": {
        "titles": [
            "Tarihin değiştiren anları",
            "Ünlü kişilerin bilinmeyen hikayeleri",
            "Antik medeniyetlerin sırları",
            "Tarihi değiştiren buluşlar",
            "Kayıp şehirlerin gizemleri",
            "Osmanlı'nın bilinmeyen yönleri",
            "İkinci Dünya Savaşı'nın sırları",
            "Antik Roma'nın günlük yaşamı",
            "Mısır piramitlerinin gizemleri",
            "Anadolu'nun eski medeniyetleri"
        ],
        "scripts": [
            "Kleopatra, Mısır'ın son firavunu, aslında Yunan asıllıydı ve Mısır dilini bile bilmiyordu. Tarihte bildiğimiz pek çok şey aslında efsane!",
            "Osmanlı İmparatorluğu'nda kadınlar erkeklerden daha iyi eğitim alabiliyordu. Topkapı Sarayı'ndaki kütüphane Avrupa'nın en zenginlerindendi.",
            "Antik Roma'da fast food vardı! Thermopolium denilen yerler bugünkü fast food restoranları gibiydi. Roma'da yaşam şaşırtıcı derecede moderndi.",
            "Büyük Piramit 4500 yıl boyunca dünyanın en yüksek yapısıydı. İçindeki odaların sıcaklığı yıl boyunca 20 derece sabit kalır. Bu nasıl mümkün?",
            "Anadolu, insanlık tarihinin beşiği. Göbekli Tepe, Stonehenge'den 6000 yıl eski! Türkiye toprakları binlerce yıllık medeniyetlere ev sahipliği yapmış."
        ]
    },
    
    "teknoloji": {
        "titles": [
            "Gelecekteki teknolojiler",
            "Akıllı telefonların bilinmeyenleri",
            "İnternetin karanlık sırları",
            "Sosyal medyanın psikolojik etkileri",
            "Blockchain ve kripto paraların geleceği",
            "Sanal gerçeklik dünyası",
            "Yapay zeka nasıl öğreniyor",
            "Quantum bilgisayarların gücü",
            "5G teknolojisinin etkileri",
            "Elektrikli araçların geleceği"
        ],
        "scripts": [
            "Akıllı telefonun Apollo 11'den milyonlarca kat daha güçlü! Cebindeki telefon NASA'nın aya gitmek için kullandığı bilgisayardan çok daha gelişmiş.",
            "Blockchain sadece Bitcoin değil! Gelecekte oy verme, sağlık kayıtları, emlak işlemleri blockchain ile yapılacak. Merkezi olmayan internetin kapıları açılıyor.",
            "Sanal gerçeklik 2030'da günlük yaşamın parçası olacak. Evden çıkmadan dünyanın her yerini gezebilecek, arkadaşlarınla sanal dünyalarda buluşabileceksin.",
            "Yapay zeka şimdiden hastalıkları doktorlardan daha erken teşhis ediyor. GPT modelleri milyarlarca kelimeyi analiz ederek insan gibi düşünmeyi öğreniyor.",
            "Quantum bilgisayarlar bugünkü süperbilgisayarların milyon kat hızlı olacak! Şifreleme, ilaç geliştirme, hava tahmini tamamen değişecek."
        ]
    },
    
    "yaşam_hikayeleri": {
        "titles": [
            "Sıfırdan zirveye başarı hikayeleri",
            "Başarısızlıktan başarıya dönüşümler",
            "Gençlerde milyoner olan insanlar",
            "Hayat değiştiren kararlar",
            "İlham verici kadın hikayeleri",
            "Sporcu başarı hikayeleri",
            "Sanatçıların mücadele hikayeleri",
            "Girişimcilik maceraları",
            "Engelleri aşan insanlar",
            "Hayallerini gerçekleştiren gençler"
        ],
        "scripts": [
            "Elon Musk PayPal'ı sattıktan sonra tüm parasını SpaceX ve Tesla'ya yatırdı. Neredeyse iflas etti ama pes etmedi. Şimdi dünyanın en zengin insanı!",
            "Oprah Winfrey yoksulluk içinde büyüdü ama okumayı seviyordu. Kitaplar hayatını değiştirdi. Şimdi milyarlarca dolarlık medya imparatorluğunun sahibi.",
            "Steve Jobs Apple'dan kovuldu ama vazgeçmedi. Pixar'ı kurdu ve sonra Apple'a geri döndü. iPhone ile dünyayı değiştirdi. Asla pes etme!",
            "J.K. Rowling tek başına anne olarak kafelerde Harry Potter yazıyordu. 12 yayınevi kitabını reddetti ama o yazmaya devam etti. Sabır ve azim her şeyi mümkün kılar.",
            "Michael Jordan lise basketbol takımından kovulmuştu. 'Başarısızlık beni motive eder' diyordu. Çalışkanlık ve azimle tarihin en iyi basketbolcusu oldu."
        ]
    },
    
    "sağlık": {
        "titles": [
            "Vücudunuzun bilinmeyen yetenekleri",
            "Sağlıklı yaşamın sırları",
            "Beslenme hakkında doğru bilgiler",
            "Egzersizin mucizevi etkileri",
            "Uykunun önemini biliyor musunuz",
            "Stresin vücuda etkileri",
            "Bağışıklık sistemini güçlendirme",
            "Su içmenin faydaları",
            "Doğal tedavi yöntemleri",
            "Mental sağlığın önemi"
        ],
        "scripts": [
            "İnsan vücudu günde 25 milyon yeni hücre üretiyor! Bu demek oluyor ki sen sürekli yenileniyorsun. Sağlıklı beslenirsen, vücudun mucizeler yaratabilir.",
            "Günde 8 saat uyku, sadece dinlenmek için değil! Uyurken beynin toksinleri temizliyor ve anıları düzenliyor. Kaliteli uyku = kaliteli yaşam.",
            "30 dakika yürüyüş kalp krizi riskini %30 azaltıyor! Egzersiz vücudun doğal antidepresan üretmesini sağlıyor. Hareket et, mutlu ol!",
            "Stres vücudunda yangı yaratıyor ve hastalıklara davetiye çıkarıyor. Nefes egzersizleri, meditasyon ve pozitif düşünce bağışıklığını güçlendiriyor.",
            "Günde 2 litre su içmek cildi gençleştiriyor, metabolizmayı hızlandırıyor ve beyin fonksiyonlarını artırıyor. Su yaşamın kaynağı!"
        ]
    },
    
    "psikoloji": {
        "titles": [
            "İnsan zihninin şaşırtıcı sırları",
            "Mutluluğun bilimsel formülü",
            "Beynin aldatıcı oyunları",
            "Pozitif düşüncenin gücü",
            "Alışkanlık oluşturmanın psikolojisi",
            "Sosyal medyanın zihin üzerindeki etkisi",
            "Empati ve duygusal zeka",
            "Korku ve kaygıyla başa çıkma",
            "Yaratıcılığı artırmanın yolları",
            "İlişkilerde psikoloji"
        ],
        "scripts": [
            "Beynin sadece yaklaşık 5% karar verme sürecinde bilinçli! Geri kalan %95'i bilinçaltında gerçekleşiyor. Sen ne kadar bilinçlisin?",
            "21 gün tekrar ettiğin her şey alışkanlık haline geliyor. Beynin nöral yolları değişiyor ve yeni davranış otomatikleşiyor. Güçlü ol, değiş!",
            "Pozitif düşünce sadece motivasyon değil, bilimsel gerçek! Optimist insanlar %15 daha uzun yaşıyor ve kalp hastalığı riski %50 daha az.",
            "Sosyal medya dopamin salgılayarak bağımlılık yaratıyor. Beğeni, yorum ve paylaşım beyni uyarıyor. Dijital detoks zihinsel sağlık için şart!",
            "Empati yaşanan deneyim gibi beynin aynı bölgelerini aktive ediyor. Sen başkasının acısını hissettiğinde, gerçekten o acıyı yaşıyorsun."
        ]
    },
    
    "doğa": {
        "titles": [
            "Doğanın inanılmaz mucizeleleri",
            "Hayvanların süper güçleri",
            "İklim değişikliğinin etkileri",
            "Yok olmakta olan türler",
            "Okyanuslardaki gizemli yaşam",
            "Ormanların önemi",
            "Bitkilerin şaşırtıcı yetenekleri",
            "Doğal afetlerin bilimi",
            "Çevreyi koruma yolları",
            "Doğada yaşam mücadelesi"
        ],
        "scripts": [
            "Bir ahtapot 8 beyne sahip! Her tentaküründe ayrı bir beyin var ve bağımsız düşünebiliyor. Doğa ne kadar şaşırtıcı değil mi?",
            "Amazon ormanları dünyanın %20 oksijenini üretiyor. Bu yüzden 'Dünyanın akciğerleri' deniyor. Ormanları korumak hepimizin sorumluluğu!",
            "Arılar kaybolsa, insanlık 4 yıl içinde yok olur! Arılar bitkilerin %80'ini tozlaştırıyor. Küçük arılar, büyük etki.",
            "Balina şarkıları binlerce kilometre uzaktan duyulabiliyor! Okyanuslar dev iletişim ağı gibi. Deniz canlıları nasıl haberleşiyor acaba?",
            "Kaktüsler çölde 2 yıl su içmeden yaşayabiliyor! Adaptasyon yetenekleri inanılmaz. Doğa her zorluğa çözüm buluyor."
        ]
    },
    
    "eğitim": {
        "titles": [
            "Öğrenmenin en etkili yolları",
            "Hafızayı güçlendirme teknikleri",
            "Dil öğrenmenin sırları",
            "Okuma hızını artırma",
            "Matematik korkusunu yenme",
            "Eğitimde teknoloji kullanımı",
            "Yaratıcı düşünce geliştirme",
            "Sınav kaygısıyla başa çıkma",
            "Etkili not alma teknikleri",
            "Geleceğin meslekleri"
        ],
        "scripts": [
            "Pomodoro tekniği: 25 dakika çalış, 5 dakika ara ver. Beyin bu şekilde daha verimli çalışıyor ve odaklanma süresi artıyor.",
            "Yeni bilgi öğrenmenin en iyi yolu tekrar! 1. gün, 3. gün, 1. hafta, 1. ay tekrar et. Spaced repetition hafızayı güçlendiriyor.",
            "Dil öğrenmenin sırrı günlük 15 dakika pratik! Çocuklar da böyle öğreniyor. Tutarlılık mükemmellikten daha önemli.",
            "Okurken sesli oku! Hem görsel hem işitsel hafıza çalışıyor. Anlama oranı %40 artıyor. Sesli okuma süper güç!",
            "Matematik sadece ezber değil, mantık oyunu! Günlük hayattan örnekler kullan. Pizza dilimi kesri, market alışverişi yüzde hesabı!"
        ]
    },
    
    "girişimcilik": {
        "titles": [
            "Başarılı girişimcilerin sırları",
            "İş fikrini nasıl bulursun",
            "Para kazanmanın yolları",
            "Genç girişimciler",
            "Dijital çağda iş kurma",
            "Başarısız olmaktan korkma",
            "Pazarlama stratejileri",
            "Yatırım almanın yolları",
            "Online para kazanma",
            "Freelancing rehberi"
        ],
        "scripts": [
            "En büyük şirketler garajlarda kuruldu! Apple, Google, Amazon hep küçük başladı. Sen de büyük hayalleri olan küçük adımlarla başla!",
            "İyi iş fikri: Bir problemi çöz! Uber ulaşım problemini, Airbnb konaklama problemini çözdü. Hangi problemi sen çözebilirsin?",
            "Başarısızlık öğretmendir! %90 startup başarısız oluyor ama deneyim kazanıyorlar. Her başarısızlık seni başarıya bir adım daha yaklaştırıyor.",
            "Sosyal medya ücretsiz pazarlama aracı! İyi içerik üret, takipçi kazan, ürün sat. TikTok, Instagram, YouTube hepsi fırsat!",
            "Para parayı çeker! İlk kazancını yatırıma dönüştür. Birikim, yatırım, büyüme. Compound effect mucizeler yaratır."
        ]
    }
}

TRENDING_HASHTAGS = [
    "#keşfet", "#viral", "#trending", "#fyp", "#foryou", 
    "#türkiye", "#istanbul", "#ankara", "#izmir",
    "#motivasyon", "#başarı", "#ilham", "#pozitif",
    "#bilim", "#teknoloji", "#eğitim", "#öğren",
    "#sağlık", "#spor", "#yaşam", "#mutluluk",
    "#girişimcilik", "#iş", "#para", "#yatırım",
    "#sanat", "#müzik", "#film", "#kitap",
    "#doğa", "#seyahat", "#yemek", "#moda"
]

VIRAL_KEYWORDS = [
    "şaşırtıcı", "inanılmaz", "muhteşem", "harika", "mükemmel",
    "gizli", "sır", "gerçek", "bilinmeyen", "gizemli",
    "viral", "trend", "popüler", "meşhur", "ünlü",
    "yeni", "modern", "gelişmiş", "ileri", "teknolojik",
    "kolay", "hızlı", "etkili", "basit", "pratik",
    "özel", "benzersiz", "farklı", "nadir", "seçkin",
    "güçlü", "etkili", "başarılı", "kazanan", "şampiyon",
    "akıllı", "zeki", "yetenekli", "ustaca", "profesyonel"
]

CONTENT_HOOKS = [
    "Bunu bilmiyordunuz:",
    "İnanmayacaksınız ama:",
    "Şaşıracaksınız:",
    "Gerçek şu ki:",
    "Size söylenen yalan:",
    "Kimse söylemiyor ama:",
    "Uzmanlar diyor ki:",
    "Araştırmalar gösteriyor:",
    "Bilim insanları keşfetti:",
    "Son dakika:"
]

def get_random_content(category: str, day: int) -> dict:
    """Belirtilen kategori için rastgele içerik döndür"""
    import random
    
    if category not in CONTENT_CATEGORIES:
        category = random.choice(list(CONTENT_CATEGORIES.keys()))
    
    cat_data = CONTENT_CATEGORIES[category]
    
    title = random.choice(cat_data["titles"])
    script = random.choice(cat_data["scripts"])
    
    # Viral hook ekle
    hook = random.choice(CONTENT_HOOKS)
    enhanced_script = f"{hook} {script}"
    
    # Hashtag'ler ekle
    hashtags = random.sample(TRENDING_HASHTAGS, random.randint(5, 10))
    
    return {
        "title": title,
        "script": enhanced_script,
        "hashtags": hashtags,
        "category": category,
        "viral_score": random.randint(7, 10)  # Viral olma potansiyeli
    }

def get_daily_theme(day: int) -> str:
    """Günlük tema belirle"""
    themes = {
        1: "motivasyon",    # Pazartesi - Hafta başı motivasyonu
        2: "teknoloji",     # Salı - Tech Tuesday
        3: "sağlık",        # Çarşamba - Wellness Wednesday  
        4: "eğitim",        # Perşembe - Throwback Thursday (öğrenme)
        5: "girişimcilik",  # Cuma - Freelance Friday
        6: "yaşam_hikayeleri", # Cumartesi - Weekend stories
        0: "psikoloji"      # Pazar - Self-care Sunday
    }
    
    weekday = day % 7
    return themes.get(weekday, "motivasyon")

if __name__ == "__main__":
    # Test
    import json
    
    print("📋 İçerik Kategorileri:")
    for i, category in enumerate(CONTENT_CATEGORIES.keys(), 1):
        print(f"{i}. {category}")
    
    print(f"\n📊 Toplam {len(CONTENT_CATEGORIES)} kategori")
    print(f"📊 Toplam {sum(len(cat['titles']) for cat in CONTENT_CATEGORIES.values())} başlık şablonu")
    print(f"📊 Toplam {sum(len(cat['scripts']) for cat in CONTENT_CATEGORIES.values())} script şablonu")
    
    # Örnek içerik
    print("\n📝 Örnek içerik:")
    sample_content = get_random_content("motivasyon", 1)
    print(json.dumps(sample_content, ensure_ascii=False, indent=2))