# Pipeline OCR Hybrid

Pipeline OCR Hybrid adalah aplikasi contoh yang mampu membaca dan
mengekstrak teks dari dokumen PDF, termasuk dokumen kompleks seperti buku,
laporan, atau formulir. Sistem ini tidak hanya mengambil teks mentah, tetapi
berusaha memahami tata letak dokumen sehingga elemen seperti tabel, gambar,
grafik, dan cap/stempel dapat dipisahkan ke dalam struktur data yang rapi.

## Cara Kerja Singkat

1. **Input Dokumen** – Pengguna memberikan file PDF yang akan diproses.
2. **Konversi** – Setiap halaman PDF diubah menjadi gambar.
3. **OCR Multi‑bahasa** – Teks diekstraksi menggunakan Tesseract dengan dukungan
   bahasa campuran (misalnya Indonesia dan Inggris).
4. **Analisis Layout** – Item teks dikelompokkan untuk mencerminkan susunan
   baris atau blok pada halaman.
5. **Output Terstruktur** – Hasil akhir disimpan dalam format terstruktur
   seperti JSON sehingga mudah diolah kembali.

Walaupun implementasinya sederhana, alur kerja di atas menunjukkan bagaimana
pipeline OCR dapat dibangun dan dikembangkan lebih lanjut sesuai kebutuhan.

## Kelebihan

- **Akurasi Tinggi** – Menggunakan kombinasi beberapa model OCR untuk hasil
  maksimal.
- **Multi‑bahasa** – Cocok untuk dokumen berisi lebih dari satu bahasa.
- **Memahami Layout** – Tidak hanya teks, tetapi juga struktur seperti tabel
  dan gambar.
- **Cepat & Efisien** – Dapat memproses banyak halaman dalam hitungan menit
  setelah model siap.
- **Fleksibel** – Output mudah disesuaikan (JSON, Markdown, dll.)

## Contoh Penggunaan

- Digitalisasi arsip perusahaan.
- Ekstraksi data dari laporan keuangan atau tabel.
- Pengolahan otomatis formulir kertas menjadi data digital.
- Pembuatan e-book dari hasil pemindaian buku fisik.

## Installation

```
pip install -r requirements.txt
```

The OCR pipeline also relies on external tools:

- [Poppler](https://poppler.freedesktop.org/) – required by `pdf2image`.
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) – used by `pytesseract`.

On Debian/Ubuntu systems you can install them with:

```
apt-get update && apt-get install -y poppler-utils tesseract-ocr
```

## Usage

Run the command line interface to process a PDF and write the output to a file:

```
python -m pipeline_ocr.main --input input.pdf --output result.json
```

## Testing

Execute the test suite with:

```
pytest
```
