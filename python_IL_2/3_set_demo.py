"""
3. SET - KEUNIKAN & OPERASI HIMPUNAN
"""

set_a = {"Python", "Java", "C++", "JavaScript", "PHP"}
set_b = {"Java", "PHP", "Kotlin", "Go", "JavaScript"}

print("Set A                  :", set_a)
print("Set B                  :", set_b)
print("Union (|)              :", set_a | set_b)
print("Intersection (&)       :", set_a & set_b)
print("Difference A - B       :", set_a - set_b)
print("Difference B - A       :", set_b - set_a)
print("Symmetric Difference ^ :", set_a ^ set_b)

# Menunjukkan duplikat otomatis hilang
list_duplikat = ["A", "B", "A", "C", "B", "D", "A"]
set_unik = set(list_duplikat)
print("\nList dengan duplikat   :", list_duplikat)
print("Setelah jadi set (unik):", set_unik)
