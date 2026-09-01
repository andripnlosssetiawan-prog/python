berat = int(input("masukan Berat Badan Anda (kg): "))
tinggi = float(input("masukan Tinggi Badan Anda (cm): "))

BMI = berat / ((tinggi/100)**2)

if (BMI < 18.5) :
    kategori = "kurus (underweight)"
    keterangan = "perlu tambah berat badan"
elif (BMI < 24.9) :
    kategori = "normal (ideal)"
    keterangan = "memepertahankan gaya hidup sehat"
elif (BMI < 29.9) :
    kategori ="Gemuk (Overweight)"
    keterangan = "Perlu olahraga lebih"
else :
    kategori = "Obesitas"
    keterangan = "konsultasi dokter"

print("Nilai BMI : ",BMI)
print("kstegori : ", kategori)
print("keterangan : ", keterangan)