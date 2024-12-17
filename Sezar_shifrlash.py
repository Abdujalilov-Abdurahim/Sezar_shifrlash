def sezar_shifrlash(mattox, shift):
    shifrlangan_matn = ''
    for harf in mattox:
        if harf.isalpha():  # Faqatgina harflarni qabul qilish
            son = ord(harf) + shift
            if harf.isupper():  # Katta harflar uchun
                if son > ord('Z'):
                    son -= 26  # Harflar soni tartibida 26 ta kichik
                elif son < ord('A'):
                    son += 26
            elif harf.islower():  # Kichik harflar uchun
                if son > ord('z'):
                    son -= 26
                elif son < ord('a'):
                    son += 26
            shifrlangan_matn += chr(son)
        else:
            shifrlangan_matn += harf
    return shifrlangan_matn

def sezar_ayratish(shifrlangan_matn, shift):
    return sezar_shifrlash(shifrlangan_matn, -shift)

# Matn va almashtirish qiymatini olish
matn = input("Matn kiriting: ")
almashtirish = int(input("Almashtirish qiymatini kiriting: "))

# Shifrlash va qaytarish
shifrlangan_matn = sezar_shifrlash(matn, almashtirish)
print("Shifrlangan matn: ", shifrlangan_matn)

# matn_qaytarilgan = sezar_ayratish(shifrlangan_matn, almashtirish)
# print("Qaytarilgan matn: ", matn_qaytarilgan)