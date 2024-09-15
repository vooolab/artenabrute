<div align="center">
  <img src="https://raw.githubusercontent.com/vooolab/voscan/main/git-images/banner.jpeg" style="width: 350px;"/>
</div>

<h1 align="center">
ArtenaBrute v1.0 Demo
</h1>
https://artensatokenmarket.com/ için geliştirilmiş bir "Brute Force" aracıdır. Bu araç, belirttiğiniz e-posta adresi ve kelime listesi (wordlist) parametrelerini kullanarak hedef sistem üzerinde şifre deneme saldırıları gerçekleştirir.
<h2 align="center">
Kurulum
</h2>
<h3>GitHub Kurulumu</h3>
<b>Termux</b>
<pre>pkg install python
git clone https://github.com/vooolab/artenabrute/
cd voscan
python setup.py
python atrenabrute.py --help</pre>
<b>Linux Dağıtımları</b>
<pre>sudo apt-get update
sudo apt-get install python3 python3-pip
git clone https://github.com/vooolab/atrenabrute/
cd voscan
python3 setup.py
python3 atrenabrute.py --help</pre>
<b>

<h3>Kullanım</h3>
<pre>python atrenabrute.py --mail [mail adresi] -w [Wordlist Yolu]</pre>

- `-m/--mail` Mail adresini belirtin.
- `-w/--wordlist` Wordlist belirtin.
- `-oc/--oc` Kaç tanede bir çıktı almak istiyorsunuz? Örneğin `-oc 100` her 100 denemede sizi bilgilendirir.

Örnek:
<pre>python voscan.py -u www.mudp.gov.bd -d df</pre>
Not: Eğer Wordlist dosyanız yoksa "-d df" yazarak default olarak voscan wordlistini belirtebilirsiniz.

<h2 align="center">
Ekran Görüntüsü
</h2>
<div align="center">
  <img src="https://raw.githubusercontent.com/vooolab/voscan/main/git-images/ss1.png"/>
</div>

<h2 align="center">
Taglar
</h2>
artensatokenmarket, bruteforce
