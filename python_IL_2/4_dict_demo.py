"""
4. DICTIONARY - KEY/VALUE DASAR
"""

mahasiswa = {
    "nama": "Wesa",
    "nim": "3312301001",
    "angkatan": 2023,
    "kota": "Batam"
}
print("Dictionary awal        :", mahasiswa)

# Tambah key baru
mahasiswa["jurusan"] = "Sistem Informasi"
# Ubah nilai key
mahasiswa["kota"] = "Batam Kota"
# Hapus key
del mahasiswa["angkatan"]

print("Dictionary setelah diubah:", mahasiswa)

print("\nKeys  :", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items :", mahasiswa.items())

print("\nIterasi key: value")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")
