"""
4. List dan Akses Elemen
"""

daftar_transportasi = ["Motor", "Mobil", "Bus", "Angkot", "Sepeda"]

print("=== 4. List dan Akses Elemen ===")
print("List awal            :", daftar_transportasi)
print("Elemen pertama        :", daftar_transportasi[0])
print("Elemen ketiga         :", daftar_transportasi[2])
print("Elemen terakhir       :", daftar_transportasi[-1])

daftar_transportasi.append("Kapal")
print("Setelah append 'Kapal':", daftar_transportasi)

daftar_transportasi.remove("Angkot")
print("Setelah remove 'Angkot':", daftar_transportasi)

item_terhapus = daftar_transportasi.pop()
print(f"Setelah pop (menghapus '{item_terhapus}'):", daftar_transportasi)
