def cekTahun(tahun):
    return tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)

def cekHariDalamBulan(tahun, bulan):
    hariDalamBulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if bulan == 2 and cekTahun(tahun):
        return 29
    return hariDalamBulan[bulan - 1]

def cekMulaiHari(tahun, bulan):
    if bulan < 3:
        bulan += 12
        tahun -= 1
    K = tahun % 100
    J = tahun // 100
    hari = 1
    f = hari + 13 * (bulan + 1) // 5 + K + K // 4 + J // 4 + 5 * J
    return (f % 7 + 5) % 7  # Penyesuaian agar Senin = 0

def printKalendar(tahun, bulan):
    namaBulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                   "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    
    namaHari = ["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"]

    hariBesar = {
        (1, 1): "Tahun Baru",
        (5, 1): "Hari Buruh Nasional",
        (5, 2): "Hari Pendidikan Nasional",
        (5, 20): "Hari Kebangkitan Nasional",
        (6, 1): "Hari Lahir Pancasila",
        (8, 17): "Hari Kemerdekaan",
        (10, 1): "Hari Kesaktian Pancasila",
        (10, 28): "Hari Sumpah Pemuda",
        (11, 10): "Hari Pahlawan",
        (12, 22): "Hari Ibu",
        (12, 25): "Hari Natal"
    }
    
    hariDalamBulan = cekHariDalamBulan(tahun, bulan)
    mulaiHari = cekMulaiHari(tahun, bulan)
    
    print(f"{namaBulan[bulan - 1]} {tahun}".center(20))
    print(" ".join(namaHari))
    
    print("    " * mulaiHari, end="")
    
    keteranganLibur = []
    
    for hari in range(1, hariDalamBulan + 1):
        if (bulan, hari) in hariBesar:
            print(f"{hari:3}*", end=" ")
            keteranganLibur.append(f"{hari} {namaBulan[bulan - 1]}: {hariBesar[(bulan, hari)]}")
        else:
            print(f"{hari:3}", end=" ")
        mulaiHari += 1
        if mulaiHari == 7:
            mulaiHari = 0
            print()
    if mulaiHari != 0:
        print()
    
    if keteranganLibur:
        print("\nHari Besar Nasional:")
        for ket in keteranganLibur:
            print(ket)

def main():
    while True:
        print("\nMenu:")
        print("1. Input Tahun dan Bulan")
        print("2. Keluar")
        pilihan = input("Pilih opsi (1 atau 2): ")
        
        if pilihan == "1":
            try:
                tahun = int(input("Masukkan tahun (misal, 2024): "))
                bulan = int(input("Masukkan bulan (1-12): "))
                
                if bulan < 1 or bulan > 12:
                    print("Bulan harus antara 1 dan 12")
                else:
                    printKalendar(tahun, bulan)
            except ValueError:
                print("Input harus berupa angka.")
        elif pilihan == "2":
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()