def sezar_shifrlash(matn, aylantirish):
    shifrlangan_matn = ""
    for harf in matn:
        if harf.isalpha():
            k = ord(harf) + aylantirish
            if harf.islower():
                if k > ord('z'):
                    k -= 26
                elif k < ord('a'):
                    k += 26
            elif harf.isupper():
                if k > ord('Z'):
                    k -= 26
                elif k < ord('A'):
                    k += 26
            shifrlangan_matn += chr(k)
        else:
            shifrlangan_matn += harf
    return shifrlangan_matn


def sezar_ochish(shifrlangan_matn, aylantirish):
    return sezar_shifrlash(shifrlangan_matn, -aylantirish)


def Javob(matn, aylantirish):
    shifrlangan_matn = sezar_shifrlash(matn, aylantirish)
    print("Deshifrlangan matn:", shifrlangan_matn)

    original_matn = sezar_ochish(shifrlangan_matn, aylantirish)
    print("Shifrlangan matn:", original_matn)

urinish_soni = 0
while True:
    urinish_soni += 1
    # Matn va aylantirishni istalgan qiymatga o'zgartiring
    matn = input("Shifrlangan matnni kiriting: ")
    aylantirish = int(input("Harflar surilish sonini kiriting: "))  # Sezar shifrlash usulida ko'proq harflar
    # oldinga surilib shifrlanadi. Shuning uchun bu yerda siz deshifrlash uchun minus sonini kiritishingiz kerak

    javob = input("Shifrmatn topildimi:Yes/No: ").lower()
    if javob == "no":
        continue
    elif javob == "yes":
        print(f"Shifrmatnni topgan bo'lsangiz, Tabriklayman!!!\n"
              f"Shifrmatnni {urinish_soni} ta urinishda topdingiz")
        break




