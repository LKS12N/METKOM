#Tugas 1 Hukum inersia
def hukum_inersia():
    print("Hukum Newton 1: Hukum Inersia")

    massa = float(input("Masukkan massa benda (kg): "))
    kecepatan = float(input("Masukkan kecepatan benda (m/s): "))

    if kecepatan == 0:
        print("Benda diam")
    else:
        print("Benda bergerak lurus dengan kecepatan konstan")

hukum_inersia()

#Tugas 1 Hukum Percepatan
def hukum_gaya_percepatan():
    print("Hukum Newton 2: Hukum Gaya dan Percepatan")

    massa = float(input("Masukkan massa benda (kg): "))
    gaya = float(input("Masukkan gaya yang dikenakan (N): "))

    percepatan = gaya / massa

    print(f"Percepatan benda={percepatan} m/s^2")

hukum_gaya_percepatan()

#Tugas 1 Hukum Aksi dan Reaksi
def hukum_aksi_reaksi():
    print("Hukum Newton 3: Hukum Aksi dan Reaksi")

    gaya = float(input("Masukkan gaya yang dikenakan (N): "))

    reaksi = -gaya

    print(f"Benda bergerak dengan gaya {gaya} N dan reaksi {reaksi} N")

hukum_aksi_reaksi()