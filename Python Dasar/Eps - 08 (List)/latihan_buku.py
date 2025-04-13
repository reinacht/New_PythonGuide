<<<<<<< HEAD
books = []

while True:
    print(10*'=', 'BUKU' ,10*'=')
    title = input("\nJudul Buku   : ")
    author = input("Penulis      : ")
    date_release = input("Tahun Terbit : ")

    book = [title, author, date_release]
    books.append(book)
    print('\n')

    for count, buch in enumerate(books, 1): 
        print('\n',20*'-')
        print(f"Buku ke-{count}")
        print(f"Judul Buku   : {buch[0]}")
        print(f"Penulis      : {buch[1]}")
        print(f"Tahun Terbit : {buch[2]}")
        print(20*'-')


    val = input("\nMau Lanjut? y/n :")
    if val == 'n':
        break

=======
books = []

while True:
    print(10*'=', 'BUKU' ,10*'=')
    title = input("\nJudul Buku   : ")
    author = input("Penulis      : ")
    date_release = input("Tahun Terbit : ")

    book = [title, author, date_release]
    books.append(book)
    print('\n')

    for count, buch in enumerate(books, 1): 
        print('\n',20*'-')
        print(f"Buku ke-{count}")
        print(f"Judul Buku   : {buch[0]}")
        print(f"Penulis      : {buch[1]}")
        print(f"Tahun Terbit : {buch[2]}")
        print(20*'-')


    val = input("\nMau Lanjut? y/n :")
    if val == 'n':
        break

>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16
print(7*'=', 'PROGRAM SELESAI' ,7*'=')