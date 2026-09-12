"""
7. KEANGGOTAAN & PENCARIAN SEDERHANA
"""

data_list = ["Wesa", "NIM123", 21, 3.75, "Informatika", 2023, "Selesai", "Tambahan1"]
set_a = {"Python", "Java", "C++", "JavaScript", "PHP"}

item_dicari_list = "Informatika"
item_dicari_set = "Python"

if item_dicari_list in data_list:
    posisi = data_list.index(item_dicari_list)
    print(f"'{item_dicari_list}' ditemukan di list pada indeks {posisi}")
else:
    print(f"'{item_dicari_list}' tidak ditemukan di list")

if item_dicari_set in set_a:
    print(f"'{item_dicari_set}' ADA di set_a")
else:
    print(f"'{item_dicari_set}' TIDAK ADA di set_a")

# Ringkasan keberadaan beberapa item sekaligus
daftar_cek = ["Java", "Ruby", "PHP", "Swift"]
print("\nRingkasan pengecekan pada set_a:")
for item in daftar_cek:
    status = "ADA" if item in set_a else "TIDAK ADA"
    print(f"- {item}: {status}")
