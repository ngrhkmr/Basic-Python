def sapa():
    inputan= input("apakah lanjut (yes/no): " )
    if inputan == "no":
        print("no")
    else:
        sapa()
sapa()


