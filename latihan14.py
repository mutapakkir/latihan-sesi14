def buat_nota(barang, harga, jumlah):
    total = harga * jumlah
    nota = f"=====NOTA===== \n\nBarang: {barang}\nHarga: {harga}\nJumlah: {jumlah}\nTotal: {total}\n"
    return nota

def simpan_nota(nota):
    with open("nota.txt", "a") as file:
        file.write(nota)
        file.write("\n")

def main():
    while True:
        print("Selamat datang di aplikasi kasir")
        barang = input("Masukkan nama barang  ")
        
        
        harga = float(input("Masukkan harga barang: "))
        jumlah = int(input("Masukkan jumlah barang: "))

        nota = buat_nota(barang, harga, jumlah)
        simpan_nota(nota)
main()