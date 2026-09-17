#Buat program untuk operator aritmatika dalam python
angka1_1014 = int(input("Input angka-1_1014: "))
angka2_1014 = int (input("Input angka-2_1014: "))

#penjumlahan
hasil_1014 = angka1_1014 + angka2_1014
print("\nOperator Penjumlahan")
print ("Hasil =", hasil_1014)

#pengurangan 
hasil_1014 = angka1_1014 - angka2_1014
print("\nOperator Pengurangan")
print ("Hasil =", hasil_1014)

# perkalian
hasil_1014 = angka1_1014 * angka2_1014
print("\nOperator Perkalian")
print ("Hasil =", hasil_1014)
 
# pembagian, pembagian bulat, dan sisa bagi
if angka2_1014 != 0:
    hasil_1014 = angka1_1014/ angka2_1014
    print("\nOperator Pembagian")
    print ("Hasil =", hasil_1014)

    hasil_1014 = angka1_1014 // angka2_1014
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_1014)
    
    hasil_1014 = angka1_1014 % angka2_1014
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_1014)
else:
    print("Angka kedua tidak boleh bernilai 0.")
    
# Pangkat
hasil_1014 = angka1_1014 ** angka2_1014
print("\nOperator Pangkat")
print("Hasil =", hasil_1014)