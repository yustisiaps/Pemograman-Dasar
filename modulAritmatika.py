# nama file : modulAritmatika
import aritmatika1

def main():
    a = int(input('Masukan nilai a : '))
    b = int(input('Masukan nilai b : '))

    print('a\t: %d' %a)
    print('b\t: %d' %b)

    print('a+b\t: %d' % aritmatika1.tambah(a, b))
    print('a-b\t: %d' % aritmatika1.kurang(a, b))
    print('a*b\t: %d' % aritmatika1.kali(a, b))
    print('a/b\t: %d' % aritmatika1.bagi(a, b))

if __name__=="__main__":
    main()



