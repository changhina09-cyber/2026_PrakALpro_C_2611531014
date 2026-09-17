# Program nilai boolean

#memasukkan nilai boolean
#input tidak peka terhadap huruf besar dan kecil
a1 = input("Input nilai boolean-1 (True/False):").strip().lower() == "true"
a2 = input("Input nilai boolean-2 (True/False):").strip().lower() == "true"

print("\nA1 =", a1_1014)
print("A2 =", a2_1014)

# Konjungsi: bernilai True jika keduanya True
hasil = a1_1014 and a2_1014
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_1014)

# Disjungsi: bernilai True jika salah satunya True
hasil_1014 = a1_1014 or a2_1014
print("\nKonjungsi (OR)")
print("A1 or A2 =", hasil_1014)

# Negasi A1: membalik nilai A1
hasil_1014 = not a1_1014
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_1014)

# Negasi A2: membalik nilai A2
hasil_1014 = not a2_1014
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_1014)

# XOR: bernilai True jika kedua nilai berbeda
hasil_1014 = a1_1014 != a2_1014
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_1014)