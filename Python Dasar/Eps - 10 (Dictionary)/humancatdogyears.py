<<<<<<< HEAD
# menghitung umur manusia, kucing dan anjing

def countYearsHCD(humanYears):
    # umur kucing dan anjing
    catYears = 0
    dogYears = 0
    if humanYears < 2:
        catYears += 15
        dogYears += 15
    elif humanYears == 2:
        catYears += 15 + 9
        dogYears += 15 + 9
    elif humanYears > 2:
        catYears = (humanYears - 2) * 4 + 24
        dogYears = (humanYears - 2) * 5 + 24
        
    listResult = [humanYears, catYears, dogYears] 
    return listResult
    
    
humanYears = int(input("Masukkan Umur Manusia : "))

human, cat, dog = countYearsHCD(humanYears)

print(f"{human} Tahun setara dengan : ")
print(f"Jika di umur Kucing : {cat}")
=======
# menghitung umur manusia, kucing dan anjing

def countYearsHCD(humanYears):
    # umur kucing dan anjing
    catYears = 0
    dogYears = 0
    if humanYears < 2:
        catYears += 15
        dogYears += 15
    elif humanYears == 2:
        catYears += 15 + 9
        dogYears += 15 + 9
    elif humanYears > 2:
        catYears = (humanYears - 2) * 4 + 24
        dogYears = (humanYears - 2) * 5 + 24
        
    listResult = [humanYears, catYears, dogYears] 
    return listResult
    
    
humanYears = int(input("Masukkan Umur Manusia : "))

human, cat, dog = countYearsHCD(humanYears)

print(f"{human} Tahun setara dengan : ")
print(f"Jika di umur Kucing : {cat}")
>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16
print(f"Jika di umur Anjing : {dog}")