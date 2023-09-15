# Muhammad Qaffal Al Fifaiz
# H071231032
# Tugas Praktikum Pekan Kedua

masukan = input("\nPilih jenis kelamin Anda:\n1. Pria\n2. Wanita\n")
if masukan.isdigit():
    gender = int(masukan)
    
    if 1 <= gender <=2:
        match gender:
            case 1:
                tinggiCM = float(input("\nMasukkan tinggi badan Anda (cm): "))
                berat = float(input("Masukkan berat badan Anda (kg): "))
                tinggiM = tinggiCM / 100
                BMI = berat/(tinggiM**2)
                ket = ""
                if BMI < 18:
                    ket += "Underweight"
                elif 18 <= BMI < 24:
                    ket += "Normal"
                elif 24 <= BMI < 27:
                    ket += "Overweight"
                else:
                    ket += "Obese"
            
                print(f"\nAnda tergolong {ket} dengan BMI {BMI:.2f}")

            case 2:
                tinggiCM = float(input("\nMasukkan tinggi badan Anda (cm): "))
                berat = float(input("Masukkan berat badan Anda (kg): "))
                tinggiM = tinggiCM / 100
                BMI = berat/(tinggiM**2)
                ket = ""
                if BMI < 17:
                    ket += "Underweight"
                elif 17 <= BMI < 24:
                    ket += "Normal"
                elif 24 <= BMI < 28:
                    ket += "Overweight"
                else:
                    ket += "Obese"

                print(f"\nAnda tergolong {ket} dengan BMI {BMI:.2f}")
    
            case _:
                print("Invalid input.")
    else:
        print("\nJumlah jenis kelamin hanyalah 2 (dua).\nJika kurang atau lebih dari itu, saya sarankan Anda ke RSJ.")
else:
    print("\nInvalid input.")