"""
5. NESTED STRUCTURES
"""

daftar_buku = [
    {"judul": "Belajar Python Dasar", "penulis": "Andi Wijaya", "tahun": 2018},
    {"judul": "Pemrograman Web Modern", "penulis": "Budi Santoso", "tahun": 2021},
    {"judul": "Algoritma dan Struktur Data", "penulis": "Citra Dewi", "tahun": 2015},
    {"judul": "Machine Learning untuk Pemula", "penulis": "Dedi Kurniawan", "tahun": 2022},
]

print("Semua judul buku:")
for buku in daftar_buku:
    print("-", buku["judul"])

tahun_minimal = 2018
buku_terbaru = [b["judul"] for b in daftar_buku if b["tahun"] >= tahun_minimal]
print(f"\nBuku terbit >= {tahun_minimal}:")
for judul in buku_terbaru:
    print("-", judul)
