def konversi_hari(x):
    tahun = x // 365
    sisa1 = x % 365
    bulan = sisa1 // 30
    hari = sisa1 % 30
    return tahun, bulan, hari

x = int(input("Masukkan jumlah hari proyek: "))
tahun, bulan, hari = konversi_hari(x)
print(f"{x} hari = {tahun} tahun, {bulan} bulan, {hari} hari")

tahun_ini = int(input("Masukkan tahun ke berapa sekarang: "))
bulan_ini = int(input("Masukkan bulan ke berapa sekarang: "))
hari_ini = int(input("Masukkan hari ke berapa sekarang: "))

print(f"Tahun sekarang: {tahun_ini}, Bulan sekarang: {bulan_ini}, Hari sekarang: {hari_ini}")