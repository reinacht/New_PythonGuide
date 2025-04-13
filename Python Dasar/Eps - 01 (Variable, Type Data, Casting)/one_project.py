<<<<<<< HEAD
# tugas 1
# user bisa bayar hutang jika saldo cukup
# user tidak akan bisa bayar jika saldo tidak cukup

saldo_awal = 7000
saldo_tambahan = input('Mau nambah berapa? :')
saldo_tambahan = int(saldo_tambahan)

saldo_total = saldo_awal + saldo_tambahan
hutang = 100_000


# proses logic

if saldo_total >= hutang:
    saldo_akhir = saldo_total - hutang
    print("Selamat Hutang Anda sudah Lunas!")
    print("Sisa Saldo Anda :", saldo_akhir)
else:
    print("Maaf, Saldo Anda tidak cukup untuk membayar Hutang!")
=======
# tugas 1
# user bisa bayar hutang jika saldo cukup
# user tidak akan bisa bayar jika saldo tidak cukup

saldo_awal = 7000
saldo_tambahan = input('Mau nambah berapa? :')
saldo_tambahan = int(saldo_tambahan)

saldo_total = saldo_awal + saldo_tambahan
hutang = 100_000


# proses logic

if saldo_total >= hutang:
    saldo_akhir = saldo_total - hutang
    print("Selamat Hutang Anda sudah Lunas!")
    print("Sisa Saldo Anda :", saldo_akhir)
else:
    print("Maaf, Saldo Anda tidak cukup untuk membayar Hutang!")
>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16
    print("Saldo Anda :", saldo_total)