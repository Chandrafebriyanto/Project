# Project CRUD Mahasiswa

![Lisensi MIT](https://img.shields.io/badge/license-MIT-blue.svg)

Ini adalah proyek aplikasi web sederhana untuk mengelola data mahasiswa. Aplikasi ini dibangun menggunakan PHP native dengan beberapa teknologi frontend modern dan menerapkan operasi dasar _Create, Read, Update, Delete_ (CRUD).

##  Demo

![Tangkapan Layar Aplikasi](https://i.ibb.co/68f2R0N/Screenshot-2024-03-04-122557.png)
*Tampilan antarmuka utama dari aplikasi manajemen data mahasiswa.*

##  Daftar Isi

- [Fitur Utama](#fitur-utama)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Instalasi dan Pengaturan](#instalasi-dan-pengaturan)
- [Struktur Folder](#struktur-folder)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

## Fitur Utama

- **Tambah Data Mahasiswa**: Menambahkan data mahasiswa baru ke dalam database.
- **Tampilkan Data Mahasiswa**: Menampilkan seluruh data mahasiswa dalam bentuk tabel yang rapi.
- **Ubah Data Mahasiswa**: Memperbarui informasi mahasiswa yang sudah ada.
- **Hapus Data Mahasiswa**: Menghapus data mahasiswa dari database.
- **Pencarian Data**: Fitur pencarian untuk memfilter mahasiswa berdasarkan nama.
- **Desain Responsif**: Antarmuka yang dapat beradaptasi dengan baik di berbagai ukuran layar.

## Teknologi yang Digunakan

- **Backend**:
  - PHP 8.1
  - MySQL / MariaDB (melalui XAMPP)

- **Frontend**:
  - HTML5
  - CSS3
  - Bootstrap 5 (untuk styling dan komponen UI)
  - JavaScript (untuk interaktivitas)

- **Tools**:
  - XAMPP (untuk lingkungan server lokal)
  - Composer (opsional, jika ada dependensi PHP)
  - Git & GitHub (untuk kontrol versi)

## Instalasi dan Pengaturan

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di lingkungan lokal Anda.

**Prasyarat**:
- Pastikan Anda sudah menginstal XAMPP (atau server lokal sejenis seperti WAMP/MAMP).
- Web browser (misalnya, Chrome, Firefox).

**Langkah-langkah**:

1.  **Clone Repositori**
    Buka terminal atau Git Bash, lalu clone repositori ini ke dalam folder `htdocs` di direktori instalasi XAMPP Anda.
    ```bash
    git clone [https://github.com/Chandrafebriyanto/Project.git](https://github.com/Chandrafebriyanto/Project.git)
    ```

2.  **Mulai Server Apache dan MySQL**
    Buka XAMPP Control Panel dan jalankan modul Apache serta MySQL.

3.  **Setup Database**
    - Buka browser dan akses `http://localhost/phpmyadmin`.
    - Buat database baru dengan nama `mahasiswa_db` (atau nama lain yang Anda inginkan).
    - Impor file `mahasiswa_db.sql` yang ada di dalam folder `database` proyek ini ke dalam database yang baru saja Anda buat. Ini akan membuat tabel `mahasiswa` beserta strukturnya.

4.  **Konfigurasi Koneksi Database**
    - Buka file `functions.php` di dalam folder `config`.
    - Sesuaikan detail koneksi database jika diperlukan (nama host, user, password, dan nama database) agar sesuai dengan pengaturan XAMPP Anda.
    ```php
    $conn = mysqli_connect("localhost", "root", "", "mahasiswa_db");
    ```

5.  **Jalankan Aplikasi**
    - Buka web browser Anda.
    - Akses URL berikut: `http://localhost/Project/` (sesuaikan `Project` dengan nama folder proyek Anda jika berbeda).
    - Aplikasi sekarang siap digunakan.

## Struktur Folder

Berikut adalah gambaran umum struktur folder dari proyek ini:


/Project
├── assets/
│   ├── css/
│   │   └── style.css       # File CSS kustom
│   └── js/
│       └── script.js       # File JavaScript
├── config/
│   └── functions.php       # Koneksi database dan fungsi utama
├── database/
│   └── mahasiswa_db.sql    # File dump SQL untuk database
├── public/
│   ├── tambah.php          # Halaman tambah data
│   ├── ubah.php            # Halaman ubah data
│   └── hapus.php           # Logika hapus data
├── index.php               # Halaman utama (menampilkan data)
└── README.md               # File dokumentasi ini


## Kontribusi

Kontribusi dari siapa pun sangat diterima. Jika Anda ingin berkontribusi, silakan lakukan _fork_ pada repositori ini, buat _branch_ baru, dan ajukan _pull request_.

1.  Fork repositori ini.
2.  Buat branch fitur baru (`git checkout -b fitur/FiturBaru`).
3.  Commit perubahan Anda (`git commit -m 'Menambahkan FiturBaru'`).
4.  Push ke branch tersebut (`git push origin fitur/FiturBaru`).
5.  Buka Pull Request.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detail lebih lanjut.
