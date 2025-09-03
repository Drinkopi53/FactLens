# FactLens

## Deskripsi
FactLens adalah aplikasi web sederhana yang memanfaatkan kekuatan Google Gemini API untuk membuat laporan yang komprehensif dan terverifikasi fakta tentang topik tertentu. Pengguna cukup memasukkan topik, dan FactLens akan menghasilkan laporan terstruktur yang dapat diunduh sebagai file Markdown.

Aplikasi ini dibangun dengan Python dan Streamlit, menyediakan antarmuka yang bersih dan ramah pengguna untuk berinteraksi dengan model AI.

## Instalasi
Untuk menjalankan FactLens secara lokal, ikuti langkah-langkah berikut:

1.  **Clone Repositori:**
    ```bash
    git clone https://github.com/username/factlens.git
    cd factlens
    ```

2.  **Buat dan Aktifkan Virtual Environment (Disarankan):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Di Windows, gunakan `venv\Scripts\activate`
    ```

3.  **Instal Dependensi:**
    Pastikan Anda memiliki file `requirements.txt` di direktori Anda, lalu jalankan:
    ```bash
    pip install -r requirements.txt
    ```

## Penggunaan
Setelah instalasi selesai, Anda dapat menjalankan aplikasi menggunakan Streamlit.

1.  **Jalankan Aplikasi:**
    ```bash
    streamlit run app.py
    ```
    Aplikasi akan terbuka di tab browser baru.

2.  **Dapatkan Google AI Studio API Key:**
    - Kunjungi [Google AI Studio](https://aistudio.google.com/).
    - Buat API key baru di project Anda.

3.  **Gunakan Aplikasi:**
    - Masukkan API key Anda ke dalam field "Enter your Google AI Studio API Key:".
    - Masukkan topik yang ingin Anda teliti di field "Enter the topic you want to research:".
    - Klik tombol "Generate Report".
    - Tunggu beberapa saat hingga laporan dibuat.
    - Laporan akan ditampilkan di layar, dan Anda dapat mengunduhnya dengan mengklik tombol "Download Report as MD".

## Kontribusi
Saat ini, kontribusi tidak terbuka untuk umum. Namun, Anda dapat melakukan fork pada repositori ini dan memodifikasinya sesuai kebutuhan Anda.

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).
