def input_angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input harus berupa angka!")

def input_matrix(baris, kolom, nama):
    print(f"\nMasukkan elemen matrix {nama}:")
    return [[input_angka(f"[{i}][{j}] = ") for j in range(kolom)] for i in range(baris)]

def tampilkan_matrix(matrix):
    for row in matrix:
        print(row)

def operasi_matrix(A, B, operasi):
    return [[operasi(A[i][j], B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]

def perkalian(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) 
             for j in range(len(B[0]))] 
             for i in range(len(A))]

while True:
    print("\n ===>>> MENU MATRIX <<<===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("0. Exit")

    pilihan = input_angka("Pilihlah menu yang Anda inginkan: ")

    if pilihan == 0:
        print("Alhamdulillah program kelar cuy!")
        break
    if pilihan not in [1, 2, 3]:
        print("Menu yang Anda pilih tidak valid! Harus kembali ke awal.")
        continue

    if pilihan in [1, 2]:
        baris = input_angka("Masukkan jumlah baris: ")
        kolom = input_angka("Masukkan jumlah kolom: ")
        A = input_matrix(baris, kolom, "A")
        B = input_matrix(baris, kolom, "B")

        print("\n Matrix A:")
        tampilkan_matrix(A)
        print("\n Matrix B:")
        tampilkan_matrix(B)

        if pilihan == 1:
            print("\n Hasil Penjumlahan:")
            tampilkan_matrix(operasi_matrix(A, B, lambda x, y: x + y))
        else:
            print("\n Hasil Pengurangan:")
            tampilkan_matrix(operasi_matrix(A, B, lambda x, y: x - y))

    elif pilihan == 3:
        baris_A = input_angka("Masukkan jumlah baris matriks A: ")
        kolom_A = input_angka("Masukkan jumlah kolom matriks A: ")
        A = input_matrix(baris_A, kolom_A, "A")

        baris_B = input_angka("Masukkan jumlah baris matriks B: ")
        kolom_B = input_angka("Masukkan jumlah kolom matriks B: ")
        B = input_matrix(baris_B, kolom_B, "B")

        print("\n Matrix A:")
        tampilkan_matrix(A)
        print("\n Matrix B:")
        tampilkan_matrix(B)

        if kolom_A != baris_B:
            print("Perkalian tidak bisa! (jumlah kolom A harus sama dengan jumlah baris B karena merupakan aturan dari matematika matrix tersebut)")
        else:
            print("\n Hasil Perkalian:")
            hasil = perkalian(A, B)
            tampilkan_matrix(hasil)