# kalkulator.py

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: pembagian dengan nol"
    return a / b

def main():
    print("=== Kalkulator Sederhana ===")
    a = float(input("Masukkan angka pertama: "))
    operator = input("Operator (+ - * / %): ")
    b = float(input("Masukkan angka kedua: "))

    operasi = {
    "+": tambah,
    "-": kurang,
    "*": kali,
    "/": bagi,
    "%": modulus
    }

    if operator in operasi:
        hasil = operasi[operator](a, b)
        print("Hasil:", hasil)
    else:
        print("Operator tidak valid!")

if __name__ == "__main__":
    main()
def modulus(a, b):
    if b == 0:
        return "Error: pembagian dengan nol"
    return a % b
