def solution(N):
    # write your code in Python 3.6
    biner = str(bin(int(N))[2:])
    conter = 0
    hasil = 0
    gan = False
    for i in biner: #melooping untuk melihat isi string biner
        if i == '1': #cek jika indeks yang dipanggil isinya adalah 1
            if hasil<conter: #mengecek jumlah 0 sebelumnya apakah lebih kecil dari simpanan
                hasil = conter # memasukkan hasil dengan hasil 0 terbesar
            gan =True #membuat nilai gan true agar memberitahu bahwa sudah dibaca angka 1 
            conter = 0 #mereset nilai conter agar diisi dengan jumlah 0 yang baru jika ada
        elif gan: #jika sudah ada dibaca 1 dan selanjutnya bukan 1
            conter +=1 #menambahkan 1 pada simpnan yaitu conter
    return hasil #mengembalikan hasil

