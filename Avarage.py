mahasiswa = {
    "10121001": "Asep",
    "10121002": "Budi",
    "10121003": "Cecep"
}

nilai = {
    "10121001": [50, 70, 40, 80],
    "10121002": [78, 78, 80, 65],
    "10121003": [57, 88, 67, 69]
}

def rata_mahasiswa(nim):
    scores = nilai[nim]
    return sum(scores) / len(scores)

def rata_mk():
    jumlah_mk = len(next(iter(nilai.values())))
    rata = []
    for i in range(jumlah_mk):
        total = sum(scores[i] for scores in nilai.values())
        rata.append(total / len(nilai))
    return rata

while True:
    print("\n =====>>>>> MENU PILIHAN <<<<<=====")
    print("1. Lihat data Asep")
    print("2. Lihat data Budi")
    print("3. Lihat data Cecep")
    print("4. Keluar")
    
    pilihan = input("Masukkan pilihan (1-4): ")
    
    if pilihan in ["1","2","3"]:
        nim = list(mahasiswa.keys())[int(pilihan)-1]
        nama = mahasiswa[nim]
        scores = nilai[nim]
        
        rata = rata_mahasiswa(nim)
        
        rata_mk_list = rata_mk()
        mk_terendah = min(range(len(rata_mk_list)), key=lambda i: rata_mk_list[i])
        
        print(f"\n Data {nama}: {scores}")
        print(f"Rata-rata {nama}: {round(rata,2)}")
        print(f"Mata Kuliah Nilai Terkecil: MK{mk_terendah+1} (Nilai: {round(rata_mk_list[mk_terendah],2)})")
        
    elif pilihan == "4":
        print("Program telah kelar cuy, Alhamdulillah!.")
        break
    else:
        print("Pilihan yang Anda pilih tidak valid, coba lagi yaa.")