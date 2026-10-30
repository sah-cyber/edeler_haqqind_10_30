# İstifadəçidən 3 rəqəmli ədəd daxil etməsini istə.
#
# Proqram aşağıdakıları etsin:
#
# Ədədin rəqəmlərinin cəmini tapsın.
#
# Ədədin rəqəmlərinin hasilini tapsın.
#
# Ədədi tərsinə çevirsin.
#
# Ədədin palindrom olub-olmadığını yoxlasın.
from math import prod


def eded_tap_yoxla():
    try:



        eded_al = input("Zehmet olmasa 3 reqemli  eded daxil edin:")

        if len(eded_al) == 3:
            print(len(eded_al))
            ededler = list(eded_al)
            print(ededler)
            cem = sum(int(i) for i in ededler)
            print(f"senin yazdigin ededlerin cemi {cem} edir")
            bolum = cem / 2
            print(f"senin yazdigin ededlerin 2 e bolumu {int(bolum)} edir")

            hasil = 1
            for i in ededler:
                hasil *=int(i)
            print(f"senin yazdigin ededlerin hasili {hasil} edir")

            tersine =''.join(reversed(ededler))
            print(f"senin yazdigin ededin tersine cevrimi {tersine}")

            if eded_al == tersine:
                print(f"Senin yazdigin {eded_al} reqemi polidromdur")
            else:
                print(f"Senin yazdigin {eded_al} reqemi polidrom deyil")



        else:
            print("zehemt olmasa reqem 3 reqemli olsun ")



    except ValueError:
        print("Xeta secimi duzgun edin")

eded_tap_yoxla()