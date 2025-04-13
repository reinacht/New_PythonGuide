<<<<<<< HEAD
# program yang akan menghitung asupan gizi dalam sehari
while True:
    print("="*10,"Hitung Kebutuhanmu","="*10,"\n")

    # input from user
    mainInformations = {}

    def mainInput():
        gender = str(input("Masukkan Gender (LK/PR) : "))
        age = int(input("Masukkan Usia (tahun) : "))
        weight = float(input("Masukkan Berat Badan (kg) : "))
        height = float(input("Masukkan Tinggi Badan (cm) : "))

        mainInformations.update({"gender" : gender, "age" : age, "weight" : weight, "height" : height})
        mainInformations["age"] = str(mainInformations["age"]) + "years"
        mainInformations["weight"] = str(mainInformations["weight"]) + "kg"
        mainInformations["height"] = str(mainInformations["height"]) + "cm"

        return gender, age, weight, height, mainInformations


    # fungsi utama
    def countNutrients(gender, age, weight, height):
        if gender == "LK":
            caloriesNeed = int(66 + (13.7 * weight) + (5 * height) - (6.8 * age))
            return caloriesNeed
        elif gender == "PR":
            caloriesNeed = int(655 + (9.6 * weight) + (1.8 * height) - (4.7 * age))
            return caloriesNeed
        
    def macroNutrients(totalCalories):
        dictNutr = {}
        carbohydrate = (55/100) * totalCalories // 4
        proteins = (20/100) * totalCalories // 4
        lipid = (25/100) * totalCalories // 9

        dictNutr.update({"carbohydrate" : carbohydrate, "proteins" : proteins, "lipid" : lipid})
        return dictNutr
    

    # pencetakan hasil
    def output(informations, nutrients):
        print("="*10,"Hasil Perhitungan","="*10,"\n")

        print("Ini adalah informasi yang Anda berikan : ")
        for key, value in informations.items():
            print(f"{key} = {value}")

        print("\nBerdasarkan Informasi yang Anda berikan, berikut adalah macro nutrients yang Anda butuhkan dalam sehari : \n")
        for key, value in nutrients.items():
            print(f"{key} = {value} gram")

    # run the program
    gender, age, weight, height, mainInformations = mainInput() # input
    
    ## cek gender
    if gender != "LK" and "PR":
        print(f"\nMaaf, Gender {gender} tidak ada di dunia ini. Silakan coba kembali dengan gender yang tersedia woi kontol!\n")
        break

    totalCalories = countNutrients(gender, age, weight, height)
    totalNutrients = macroNutrients(totalCalories)
    mainInformations.update({"kalori" : str(totalCalories)+"kkal"})

    output(mainInformations, totalNutrients) # output



    # tambahan program berdasarkan aktivitas
    condition = str(input("\nMau hitung berdasarkan aktivitas? (y/n) : "))

    if condition == "y":
        activity = str(input("\nMasukkan Aktivitas hari ini (SR, R, S, B, SB) : "))
        def activityCount(activity, totalCalories):
            if activity == "SR":
                totalCalories *= 1.2 
            elif activity == "R":
                totalCalories *= 1.375 
            elif activity == "S":
                totalCalories *= 1.55 
            elif activity == "B":
                totalCalories *= 1.725 
            elif activity == "SB":
                totalCalories *= 1.9 
            else:
                return print("Masukkan opsi yang sesuai bodoh!")
            
            return totalCalories
        
        totalCaloriesActivity = activityCount(activity, totalCalories)
        totalNutrientsActivity = macroNutrients(totalCaloriesActivity)
        mainInformations.update({"kalori" : str(totalCaloriesActivity)+"kkal"})
        
        # dengan aktivitas
        output(mainInformations, totalNutrientsActivity)

    else:
        print("="*10,"Program Selesai","="*10,"\n")





            
=======
# program yang akan menghitung asupan gizi dalam sehari
while True:
    print("="*10,"Hitung Kebutuhanmu","="*10,"\n")

    # input from user
    mainInformations = {}

    def mainInput():
        gender = str(input("Masukkan Gender (LK/PR) : "))
        age = int(input("Masukkan Usia (tahun) : "))
        weight = float(input("Masukkan Berat Badan (kg) : "))
        height = float(input("Masukkan Tinggi Badan (cm) : "))

        mainInformations.update({"gender" : gender, "age" : age, "weight" : weight, "height" : height})
        mainInformations["age"] = str(mainInformations["age"]) + "years"
        mainInformations["weight"] = str(mainInformations["weight"]) + "kg"
        mainInformations["height"] = str(mainInformations["height"]) + "cm"

        return gender, age, weight, height, mainInformations


    # fungsi utama
    def countNutrients(gender, age, weight, height):
        if gender == "LK":
            caloriesNeed = int(66 + (13.7 * weight) + (5 * height) - (6.8 * age))
            return caloriesNeed
        elif gender == "PR":
            caloriesNeed = int(655 + (9.6 * weight) + (1.8 * height) - (4.7 * age))
            return caloriesNeed
        
    def macroNutrients(totalCalories):
        dictNutr = {}
        carbohydrate = (55/100) * totalCalories // 4
        proteins = (20/100) * totalCalories // 4
        lipid = (25/100) * totalCalories // 9

        dictNutr.update({"carbohydrate" : carbohydrate, "proteins" : proteins, "lipid" : lipid})
        return dictNutr
    

    # pencetakan hasil
    def output(informations, nutrients):
        print("="*10,"Hasil Perhitungan","="*10,"\n")

        print("Ini adalah informasi yang Anda berikan : ")
        for key, value in informations.items():
            print(f"{key} = {value}")

        print("\nBerdasarkan Informasi yang Anda berikan, berikut adalah macro nutrients yang Anda butuhkan dalam sehari : \n")
        for key, value in nutrients.items():
            print(f"{key} = {value} gram")

    # run the program
    gender, age, weight, height, mainInformations = mainInput() # input
    
    ## cek gender
    if gender != "LK" and "PR":
        print(f"\nMaaf, Gender {gender} tidak ada di dunia ini. Silakan coba kembali dengan gender yang tersedia woi kontol!\n")
        break

    totalCalories = countNutrients(gender, age, weight, height)
    totalNutrients = macroNutrients(totalCalories)
    mainInformations.update({"kalori" : str(totalCalories)+"kkal"})

    output(mainInformations, totalNutrients) # output



    # tambahan program berdasarkan aktivitas
    condition = str(input("\nMau hitung berdasarkan aktivitas? (y/n) : "))

    if condition == "y":
        activity = str(input("\nMasukkan Aktivitas hari ini (SR, R, S, B, SB) : "))
        def activityCount(activity, totalCalories):
            if activity == "SR":
                totalCalories *= 1.2 
            elif activity == "R":
                totalCalories *= 1.375 
            elif activity == "S":
                totalCalories *= 1.55 
            elif activity == "B":
                totalCalories *= 1.725 
            elif activity == "SB":
                totalCalories *= 1.9 
            else:
                return print("Masukkan opsi yang sesuai bodoh!")
            
            return totalCalories
        
        totalCaloriesActivity = activityCount(activity, totalCalories)
        totalNutrientsActivity = macroNutrients(totalCaloriesActivity)
        mainInformations.update({"kalori" : str(totalCaloriesActivity)+"kkal"})
        
        # dengan aktivitas
        output(mainInformations, totalNutrientsActivity)

    else:
        print("="*10,"Program Selesai","="*10,"\n")





            
>>>>>>> cd1aaeb9d87aeb86de2fca0ed17417b15189fc16
