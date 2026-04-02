# Program FizzBuzz dengan opsi interaktif
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return "Pilihan yang anda pilih tidak termasuk dalam kategori keduanya"

# Bagian 1: tampilkan angka 1–100
for i in range(1, 101):
    print(f"{i} -> {fizzbuzz(i)}")

# Bagian 2: interaktif cek angka
while True:
    x = input("Masukkan angka untuk dicek (atau ketik 'exit' untuk keluar): ")
    if x.lower() == "exit":
        print("Program selesai.")
        break
    if x.isdigit():
        x = int(x)
        print(f"Hasil untuk {x} adalah: {fizzbuzz(x)}")
    else:
        print("Input tidak valid, silakan masukkan angka atau 'exit'.")