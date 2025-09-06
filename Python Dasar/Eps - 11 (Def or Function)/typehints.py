'''Type Hints'''
# adalah variabel dgn jenis tertentu yang dimasukkan ke dalam fungsi

# Kasus 1
def count(num:int): # berarti argumennya harus tertipe int
    hasil = num*9
    return hasil
    
print(count(9))


# Kasus 2
def expand(num:int, square:int) -> int: # berarti argumen dan output returnnya harus bertipe int
    hasil = num**square
    return hasil
    
print(expand(7, 8))


# Kasus 3
def printText(text:str, num:int) -> str: # berarti 1 argumen str, 1 int dan output returnnya harus bertipe str 
    numStr = str(num)
    hasil = text, numStr
    return hasil

print(printText("Lunar", 7))
