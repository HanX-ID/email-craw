import requests
import re
from bs4 import BeautifulSoup

def cari_email(url):
    try:
        print(f"[+] Mengambil konten dari: {url}")
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        teks = soup.get_text()

        pola_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        hasil = re.findall(pola_email, teks)
        hasil_unik = list(set(hasil))

        if hasil_unik:
            print(f"\n[+] Ditemukan {len(hasil_unik)} alamat email:")
            for email in hasil_unik:
                print(" -", email)

            with open("hasil_email.txt", "w") as f:
                for email in hasil_unik:
                    f.write(email + "\n")
            print("\n[+] Hasil disimpan ke file: hasil_email.txt")
        else:
            print("[-] Tidak ditemukan alamat email di halaman tersebut.")
    except Exception as e:
        print("[-] Gagal mengambil halaman:", e)

url_target = input("Masukkan URL website [contoh: https://example.com] : ")
cari_email(url_target)