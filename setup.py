import pkgutil
import subprocess
import requests
import os
import random
import string
from urllib.parse import urlparse
import shutil


version_url = "https://raw.githubusercontent.com/vooolab/artenabrute/main/version.txt"

requirements = [
	"argparse",
	"asyncio",
	"aiohttp",
	"colorama"
]

green = "\033[32m"
reset = "\033[0m"
red = "\033[31m"
cyan = "\033[36m"
reset = "\033[0m"

orange = "\033[38;2;255;165;0m"
pref =  f"  [  {orange}KURULUYOR{reset}  ] "
spref = f"  [   {green}KURULDU{reset}   ] "
epref = f"  [    {red}HATA{reset}     ] "
syspref = f"  [   {cyan}SISTEM{reset}    ] "

def printf(*args):
	print(pref, *args)

def printc(*args):
	print(" ", *args)

def uline(*args):
	# Önceki satırı temizle ve yeni metni yaz
	print("\033[2K", end="\r", flush=True)  # Önceki satırı temizle
	print(*args, end="\r", flush=True)   # Yeni metni yaz

def read_version_file():
    """version.txt dosyasındaki mevcut sürümü oku ve döndür."""
    try:
        with open("version.txt", "r") as file:
            version = file.read().strip()
            return version
    except FileNotFoundError:
        pass
    except Exception as e:
        pass
        
def update():
    response = requests.get(version_url)
    if response.status_code == 200:
        try:
            current_version = read_version_file()
            new_version = response.text.strip()
            
            if new_version > current_version:
                print(f"{syspref}Güncelleme Mevcut {red}{current_version}{reset} -> {green}{new_version}{reset}")
            
        except:
        	pass
    else:
        print(f"{epref}İstek başarısız oldu, durum kodu: {response.status_code}")

update()

printc("Python Modülleri İşleme Alındı!")
printc("-"*31)
installed_modules = {module.name for module in pkgutil.iter_modules()}
for requirement in requirements:
	if requirement not in installed_modules:
		uline(f"{pref}{requirement.ljust(14)}")
		result = subprocess.run(["pip", "install", requirement], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		if result.returncode == 0:
			print(f"{spref}{requirement.ljust(14)}")
			installed_modules.add(requirement)
		else:
			if "No matching distribution found" in result.stderr.decode().strip():
				print(f"{epref}'{requirement}' modülü indirilemedi.")
			else:
				print(f"{epref}'{requirement}' modülü indirilemedi. Hata: {result.stderr.decode().strip()}")
	else:
		print(f"{spref}{requirement.ljust(14)}")

success_module = set()  # success_module değişkenini küme olarak tanımla
for requirement in requirements:
	if requirement in installed_modules:
		success_module.add(requirement)

printc("-"*31)
print(f"{syspref}Kurulum Tamamlandı!")
