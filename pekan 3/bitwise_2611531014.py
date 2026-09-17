# Program ini menggunakan fungsi input()

print("\n==========================================")
print("3. OPERATOR BITWISE")
print("==========================================")

angka1_1014 = int(input("Masukkan angka bitwise-1: "))
angka2_1014 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_1014, "| biner =", bin(angka1_1014))
print("angka2 =", angka2_1014, "| biner =", bin(angka2_1014))

# Bitwise AND
hasil_1014 = angka1_1014 & angka2_1014
print("\nBitwise AND (&)")
print(angka1_1014, "&", angka2_1014, "=", hasil_1014)
print("Biner hasil =", bin(hasil_1014))
print("Biner hasil (8 bit) =", format(hasil_1014, "08b"))

# Bitwise OR
hasil_1014 = angka1_1014 | angka2_1014
print("\nBitwise OR (|)")
print(angka1_1014, "|", angka2_1014, "=", hasil_1014)
print("Biner hasil =", bin(hasil_1014))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise XOR
hasil_1014 = angka1_1014 ^ angka2_1014
print("\nBitwise XOR (^)")
print(angka1_1014, "^", angka2_1014, "=", hasil_1014)
print("Biner hasil =", bin(hasil_1014))
print("Biner hasil (8 bit) =", format(hasil_1014, "08b"))

# Bitwise NOT
hasil_1014 = ~angka1_1014
print("\nBitwise NOT (~)")
print("~", angka1_1014, "=", hasil_1014)
print("Biner hasil =", bin(hasil_1014))
print("Biner hasil (8 bit) =", format(hasil_1014, "08b"))

# Bitwise geser kiri
jumlah_geser = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_1014 = angka1_1014 << jumlah_geser
print("\nBitwise geser kiri (<<)")
print(angka1_1014, "<<", jumlah_geser, "=", hasil_1014)
print("Biner hasil =", bin(hasil_1014))
print("Biner hasil (8 bit) =", format(hasil_1014, "08b"))

# Bitwise geser kanan
hasil_1014 = angka1_1014 >> jumlah_geser
print("\nBitwise geser kanan (>>)")
print(angka1_1014, ">>", jumlah_geser, "=", hasil_1014)
print("Biner hasil =", bin(hasil_1014))
print("Biner hasil (8 bit) =", format(hasil_1014, "08b"))