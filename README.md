# Email Crawler 

Alat sederhana untuk mendeteksi dan mengekstrak alamat email dari halaman website.  
Dikembangkan oleh [HanX-ID](https://github.com/HanX-ID)

## Fitur
- Mengambil seluruh konten HTML dari sebuah URL
- Mendeteksi alamat email menggunakan regex
- Menampilkan dan menyimpan hasil ke file `hasil_email.txt`

## Persyaratan
- Python 3
- Paket tambahan:
  - `requests`
  - `beautifulsoup4`

## Instalasi (Termux/Linux)

```bash
pkg update && pkg install python git -y
pip install requests beautifulsoup4

git clone https://github.com/HanX-ID/email-craw
cd email-craw
python main.py
```
`Penggunaan`

Setelah menjalankan script, masukkan URL target. Contoh:
```
Masukkan URL website [contoh: https://example.com] : https://kompas.com
```
Hasil pencarian email akan ditampilkan di layar dan disimpan di file hasil_email.txt.

`Contoh Output`

[+] Mengambil konten dari: https://kompas.com

[+] Ditemukan 3 alamat email:
 - redaksi@kompas.com
 - support@kompas.com
 - info@kompas.com

[+] Hasil disimpan ke file: hasil_email.txt
