# Program operator keanggotaan dan identitas

print("============================") 
print("1. OPERATOR KEANGGOTAAN")
print("============================")

# Input beberapa data yang dipisahkan dengan koma
input_data_1014 = input("Masukkan beberapa angka, pisahkan dengan koma:")

# Mengubah input menjadi list integer
data_1014 = [int(angka.strip()) for angka_1014 in input_data.split(",")]

nilai_dicari_1014 = int(input("Masukkan angka yang ingin dicari:"))

# Operator in
hasil_1014 = nilai_dicari_1014 in data_1014
print("\nOperator keanggotaan IN")
print(nilai_dicari_1014, "in data =", hasil_1014)

#Operator not in
hasil_1014 = nilai_dicari_1014 not in data_1014
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_1014, "not in", data_1014, "=", hasil_1014)

print("\n==========================================")
print("2. OPERATOR IDENTITAS")
print("==========================================")

# objek1 menggunakan list dari input pengguna
objek1_1014 = data_1014

# objek2 merujuk pada objek yang sama dengan objek1
objek2_1014 = objek1_1014

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_1014 = data.copy()

print("objek1 =", objek1_1014)
print("objek2 =", objek2_1014)
print("objek3 =", objek3_1014)

# Operator is
hasil_1014 = objek1_1014 is objek2_1014
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_1014)

# Operator is not
hasil_1014 = objek1_1014 is not objek3_1014
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_1014)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_1014 is objek3_1014)
print("objek1 == objek3 =", objek1_1014 == objek3_1014)