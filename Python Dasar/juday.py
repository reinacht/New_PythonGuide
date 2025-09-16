import random
import os
os.system('cls')

# Introduction Section
print(14*"=","JUDOL",14*"=")
name = input("\nMasukkan nama Anda terlebih dahulu : ")
valueIs = input(f"Sudah siapkah Anda {name} bermain Judol? (y/n) : ").lower()
humanOrNot = input("Mau AI atau Manusia? (a/m) : ").lower()

print("\n",14*"="+"======="+14*"=")
balance = 0

# Guessing Section
while True:
    # cowards
    if valueIs == "n":
        print(f"\nSepertinya Aku mencium bau seorang PENGECUT HAHAHA. Nama Anda akan saya ingat sebagai pengecut, {name}\n")
        break
    
    # Input your balance
    if humanOrNot == 'm':
        if balance == 0:
            balance_temp = int(input("\nMasukkan Balance Anda (minimal 5000) : "))
            balance += balance_temp

    # Input range nums and declaration var
    # Input human
    x = int(input("\nMasukkan range angka yang ingin Anda tebak : "))
    y = int(input("Masukkan range angka yang ingin Anda tebak : "))
    num = random.randint(x, y)
    range_num = y - x + 1
    attempts = 0
    
    # Input AI
    attempts_ai = 0
    g_nums_less = []
    g_nums_more = []
    guess_ai = random.randint(x, y)

    print("\n",14*"="+"======="+14*"=")   


    # Definition Function
    # AI Function
    def ai_guessing(attempts_ai, g_nums_less, g_nums_more, guess_ai):
        while True:
            # AI Guess
            if guess_ai == num:
                attempts_ai += 1
                print(f"GG AI, Attempts : {attempts_ai}, num : {num}")
                break

            elif guess_ai > num:
                attempts_ai += 1
                print(f"Guess : {guess_ai} +")

                # Searching for the smallest number
                g_nums_more.append(guess_ai)
                min_m = g_nums_more[0]
                for i in g_nums_more:
                    if i < min_m:
                        min_m = i

                if len(g_nums_less) == 0:
                    guess_ai = random.randint(x, min_m-1)
                elif len(g_nums_less) != 0:
                    guess_ai = random.randint(maks_l+1, min_m-1)
                

            elif guess_ai < num:
                attempts_ai += 1
                print(f"Guess : {guess_ai} -")

                # Searching for the greatest number
                g_nums_less.append(guess_ai)
                maks_l = g_nums_less[0]
                for i in g_nums_less:
                    if i > maks_l:
                        maks_l = i

                if len(g_nums_more) == 0:
                    guess_ai = random.randint(maks_l+1, y)
                elif len(g_nums_more) != 0:
                    guess_ai = random.randint(maks_l+1, min_m-1)


    # Human Function
    def human_guessing(x, y, num, range_num, attempts, balance):
        while True:
            guess = int(input(f"\nSilakan masukkan tebakan Anda dari {x} sampai {y} : "))

            # Guess with saldo
            if balance == 5000 or balance > 5000:
                if guess > num:
                    print("Tebakan Anda kebesaran kocak!")
                    balance -= 5000
                    attempts += 1    

                elif guess < num:
                    print("Tebakan Anda kekecilan kocak!")
                    balance -= 5000
                    attempts += 1    

                if guess == num:
                    attempts += 1    
                    balance -= 5000

                    if range_num <= 1000:
                        rewards = 100000
                    elif range_num > 1000:
                        rewards = 1000000

                    if attempts > 10:
                        print("kocak")
                        rewards /= 10
                        balance += rewards
                    else:
                        balance += rewards
                    balance_game = balance

                    print(f"\nTebakan Anda benar! Selamat Jackpot {name}! (Attempts : {attempts})")
                    print(f"Anda mendapatkan uang sebesar {rewards:,}".replace(",", ".")+"!", f"Saldo Anda kini {balance_game:,}".replace(",", "."))
                    return balance_game

            # If balance is less than 5k
            elif balance < 5000:
                print(f"Maaf, tapi sepertinya Saldo Anda tidak cukup kocak! ({balance})")
                break


    # Run the program
    if humanOrNot == 'a':
        ai_guessing(attempts_ai, g_nums_less, g_nums_more, guess_ai)
    elif humanOrNot == 'm': 
        balance_game = human_guessing(x, y, num, range_num, attempts, balance)
        balance = balance_game
            

    # Next Game
    nextGame = input(f"\nMau Lanjut? (y/n) : ").lower()
    if nextGame == "n":
        break
    

