

class EdedTap:

    def __init__(self):
        self.eded_al = ""



    def yoxla(self):
        while True:
            self.eded_al = input("Zehmet olmasa 3 reqemli musbet eded daxil edin: ")


            if len(self.eded_al) == 3 and self.eded_al.isdigit() and int(self.eded_al) > 0:
                return True
            else:
                print("Xeta 3 reqemli eded daxil edin ")


    def cemi(self):

         cem = sum(int(i) for i in self.eded_al)
         print(f"Senin yazdigin ededlerin cemi {cem} edir")

    def hasili(self):

        hasil = 1
        for i in self.eded_al:
            hasil *=int(i)
        print(f"senin yazdigin ededlerin hasili {hasil} edir")

    def tersine(self):

        self.ters = self.eded_al[::-1]
        print(f"senin daxil etdiyin ededlerin ters cevrimi {self.ters}")

    def palidrom(self):

        if self.ters == self.eded_al:
            print(f"Sizin qeyd etdiyiniz {self.eded_al} palidrom ededidir")
        else:
            print(f"Sizin qeyd etdiyiniz {self.eded_al} palidrom deyil ")


eded = EdedTap()

if eded.yoxla():
    eded.cemi()
    eded.hasili()
    eded.tersine()
    eded.palidrom()







