"""
6. COMPREHENSION & UTILITAS
"""

angka_1_20 = list(range(1, 21))

# List comprehension
list_genap = [n for n in angka_1_20 if n % 2 == 0]
list_kuadrat = [n ** 2 for n in angka_1_20]
print("Angka genap (1-20)  :", list_genap)
print("Angka kuadrat (1-20):", list_kuadrat)

# Dict comprehension
dict_genap_ganjil = {n: ("genap" if n % 2 == 0 else "ganjil") for n in range(1, 11)}
print("\nDict genap/ganjil (1-10):")
print(dict_genap_ganjil)

# Set comprehension
kalimat = "Belajar Python itu Menyenangkan dan Bermanfaat"
huruf_unik = {huruf for huruf in kalimat.lower() if huruf.isalpha()}
print("\nKalimat        :", kalimat)
print("Huruf unik     :", sorted(huruf_unik))
