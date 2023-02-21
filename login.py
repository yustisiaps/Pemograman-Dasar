nama = "Yustisia Pratiwi Suhastri"
kunci = "18111001"
ulang='y'

while ulang == 'y':
    username = str(input("Masukan Username : "))
    password = str(input("Masukan Password : "))
    if username == nama and password == kunci:
        print("Password Benar")
    elif username == nama or password == kunci:
        print("password atau username salah")
    else :
        print("password salah")

    print()
    ulang = str(input("input username dan password lagi ? y/t:"))
    print()
