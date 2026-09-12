"""
2. TUPLE - IMMUTABILITY & UNPACKING
"""

data_tuple = ("Informatika", "Batam", 2023, 3.75, "Aktif")
print("Tuple              :", data_tuple)
print("Panjang tuple      :", len(data_tuple))
print("Akses indeks ke-2  :", data_tuple[2])

# Unpacking minimal 3 variabel dengan *rest
prodi, kota, *rest = data_tuple
print("\nUnpacking:")
print("prodi  =", prodi)
print("kota   =", kota)
print("rest   =", rest)

a, b, c, d, e = data_tuple
print("\nUnpacking penuh 5 variabel:")
print(f"a={a}, b={b}, c={c}, d={d}, e={e}")
