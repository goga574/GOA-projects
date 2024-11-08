name = input("what is your name?:")

surname = input("what is your surname?:")

print("გამარჯობა! მოგესალმებათ GOA ბანკი" + " " + name + " " + surname)

print("ქვემოთ მოცემული ვარიანტებიდან რომლის არჩვა გსურთ?")

print(" ")

print("1)ბარათზე თანხის შეტანა")

print(" ")

print("2)ბარათიდან თანხის გამოტანა")

print(" ")

print("3)მობილურზე თანხის შეტანა")

print(" ")

print("4)სესხის დაფარვა")    

print(" ")

print("5)სესხის აღება")

print(" ")

print("6)კომუნალურები")

print(" ")




archevani = input("რომლის არჩევა გსურთ?  არჩევანი დააფიქსირეთ ნომრით:")

if archevani == "1":
    print("თვენი არჩევანი არის ბარათზე თანხის შეტანა ")
    shetanili_tanxa = input("რა ოდენობის თანხის შეტანა გსურთ?")
    print("თვენი ბარათი შეივსო" + " " + str(shetanili_tanxa))
    print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")

elif archevani == "2":
    print("თვენი არჩევანი არის ბარათიდან თნხის გამოტანა")
    gamotanili_tanxa = input("რა ოდენობის თანხის გამოტანა გსურთ?")
    print("თვენი ბარათიდან გამოიტანეთ" + " " + str(gamotanili_tanxa))
    print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")

elif archevani == "3":
    print("მობილურზე თანხის შეტანა")
    mobilurze_shetanili_tanxa = input("რა ოდენობის თნხის შეტანა გსურთ?")
    print("თვენი ანგარიში შეივსო" + " " + str(mobilurze_shetanili_tanxa))
    print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")

elif archevani == "4":
    print("სესხის დაფარვა")
    shetanili_tanxa = input("რა ოდენობის თნხით გსურთ დაფაროთ სესხი?")
    print("თვენი სესხი დაიფარა" + " " + str(shetanili_tanxa))
    print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")

elif archevani == "5":
    print("სესხის აღება")
    agebuli_tanxa = input("რა ოდენობის თნხის აღბა გსურთ?")
    print("თქვენ მიიღეთ" + " " + str(agebuli_tanxa))
    print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")

elif archevani == "6":
    print("კომუნალურები")
    print("1)გაზი")
    print("2)წყალი")
    print("3)ელექტრო ენერგია")
    print("4)ინტერნეტი")
    komunalurebi = input("რომელი კომუნალკურის გადახდა გსურთ?")
    print("თქვენ შეიტანეთ" + " " + komunalurebi)
    if komunalurebi == "1":
        print("თქვენ აირჩიეთ გაზი")
        gazi = input("")



    


   



#ღილაკი რომელიც აარჩვინებს ფუნქციას






