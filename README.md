# Bot Pencatat Keuangan WhatsApp

Bot WhatsApp sederhana untuk mencatat transaksi keuangan pribadi (pemasukan dan pengeluaran) langsung dari chat. Dibuat menggunakan `pywabot` untuk integrasi dengan WhatsApp dan Google Gemini untuk pemrosesan bahasa alami.

## Fitur

- **Pencatatan Transaksi**: Catat pemasukan dan pengeluaran menggunakan bahasa sehari-hari.
- **Laporan Keuangan**: Dapatkan laporan lengkap semua transaksi.
- **Cek Saldo**: Lihat saldo terkini dengan cepat.
- **Interaksi AI**: Bot dapat memberikan respons natural berkat Google Gemini.

## Teknologi

- **Python**: Bahasa pemrograman utama.
- **pywabot**: Library untuk menghubungkan dan mengontrol WhatsApp.
- **Google Gemini**: Model AI untuk mengekstrak informasi transaksi dari pesan dan memberikan respons.

## Instalasi

1.  **Clone repositori ini:**
    ```bash
    git clone <url-repositori-anda>
    cd <nama-folder-repositori>
    ```

2.  **Install dependensi:**
    Pastikan Anda memiliki Python 3.8+ terinstal.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Konfigurasi Environment Variables:**
    Buat file `.env` di direktori root proyek dan isi dengan variabel berikut:
    ```
    GEMINI_API_KEY="API_KEY_GEMINI_ANDA"
    PYWABOT_API_KEY="API_KEY_PYWABOT_ANDA"
    ```
    - `GEMINI_API_KEY`: Dapatkan dari [Google AI Studio](https://aistudio.google.com/app/apikey).
    - `PYWABOT_API_KEY`: Dapatkan dari [situs pywabot](https://pywabot.com/).

## Cara Menjalankan Bot

1.  Jalankan skrip utama:
    ```bash
    python bot.py
    ```

2.  Saat pertama kali dijalankan, Anda akan diminta untuk memasukkan nomor telepon Anda (dengan format `628...`).

3.  Anda akan menerima kode pairing di aplikasi WhatsApp Anda. Masukkan kode tersebut di terminal.

4.  Setelah berhasil terhubung, bot siap menerima pesan.

## Perintah yang Tersedia

- `/laporan`: Menampilkan seluruh riwayat transaksi.
- `/saldo`: Menampilkan sisa saldo saat ini.

Anda juga bisa langsung menuliskan transaksi dalam bahasa natural, contohnya:
- "kemarin beli kopi 25 ribu"
- "dapat gaji 5 juta"
- "bayar listrik 150rb dan beli pulsa 50rb"