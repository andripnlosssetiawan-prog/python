# program Cek kondisi Nilai
nama = input("Nama siswa  : ")
nilai = int(input("Nilai ujian : "))
hadir = input("hadir 80%? (ya/tidak): ")

# Operator perbandingan
print()
print("=== HASIL CEK ===")
print("Nilai >= 75 :", nilai >= 75)
print("Nilai >= 90 :", nilai >= 90)
print("Nilai antara 75-89:", nilai >= 75 and nilai <= 89)

