# program operator assignment dalam python

angka1_1014 = int (input ("Input angka-1:"))
angka2_1014 = int (input ("Input angka-2:"))

print("\nNilai awal angka1 =", angka1_1014)
print("Nilai awal angka2 =", angka2_1014)

# Assignement biasa
hasil_1014 = angka1_1014
print("\nAssignment Biasa (=)")
print("Hasil =", hasil_1014)

# Assignment penambahan
hasil_1014 = angka1_1014
hasil_1014 += angka2_1014
print("\nAssignment Penambahan (+=)")
print("Hasil =", hasil_1014)

# Assignment pengurangan
hasil_1014 = angka1_1014
hasil_1014 -= angka2_10-14
print("\nAssignment Pengurangan (-=)")
print("Hasil =", hasil_1014)

# Assignment perkalian
hasil_1014 = angka1_1014
hasil_1014 = angka2_1014
print("\nAssignment Perkalian (*=)")
print("Hasil =", hasil_1014)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_1014 != 0:
    hasil_1014 = angka1_1014
    hasil_1014 /= angka2_1014
    print("\nAssignment Pembagian (/=)")
    print("Hasil =", hasil_1014)
    # Operator tambahan
    hasil_1014 = angka1_1014
    hasil_1014 //= angka2_1014
    print("\nAssignment Pembagian Bulat (//=)")
    print("Hasil =", hasil_1014)
    hasil_1014 = angka1_1014
    hasil_1014 %= angka2_1014
    print("\nAssignment Sisa Bagi (%=)")
    print("Hasil =", hasil_1014)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0.")
    
# Operator tambahan: assignment perpangkatan
hasil_1014 = angka1_1014
hasil_1014 **= angka2_1014
print("\nAssignment Perpangkatan (**=)")
print("Hasil =", hasil_1014) 