# program biodata siswa
print("=" * 35)
print("FROM BIODATA SISWA")
print("=") * 35

nama = input("nama lengkap         :   ")
kelas= input("kelas                :   ")
umur = intput("umur (tahun)       :   ")
tinggi = float(input("tinggi (cm):")

print()
print("=" * 35)
print("  DATA TERSIMPAN")
print("=" * 35)
print("nama" :", nama)
print("kelas :", kelas)
print(umur   :", umur, "tahun")
print("tinggi:", tinggi, "cm")
print("sudah dewasa":",umur >= 17)