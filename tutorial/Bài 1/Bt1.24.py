txt = input("nhap mot chu cai bat ky:")
    
def CheckVowel(txt):
    Vowels = "aeiou"
    return txt in Vowels

if(CheckVowel(txt)):
    print("chu cai ban nhap la nguyen am")
else:
    print("chu cai ban nhap khong la nguyen am")
