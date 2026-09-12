"""
1. LIST - AKSES & MANIPULASI
"""

data_list = ["Wesa", 21, "Batam", 3.75, "Informatika", 2023]
print("List awal          :", data_list)
print("Elemen pertama     :", data_list[0])
print("Elemen terakhir    :", data_list[-1])
print("Slicing [1:5:2]    :", data_list[1:5:2])

print("\n-- Sebelum manipulasi --")
print(data_list)

data_list.append("Selesai")                    # tambah di akhir
data_list.insert(1, "NIM123")                  # sisip di posisi tertentu
data_list.extend(["Tambahan1", "Tambahan2"])   # gabung banyak elemen
data_list.pop()                                 # hapus elemen terakhir
data_list.remove("Batam")                       # hapus elemen tertentu berdasarkan nilai

print("\n-- Sesudah manipulasi --")
print(data_list)
