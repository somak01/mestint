from keres import *


class Korsó(Feladat):
    def __init__(self,ke,c):
        self.kezdő=ke#kezdoallapot
        self.cél=c#cel allapot
        self.max1=8#elso kancso maximuma
        self.max2=5#masodik kancso maximuma
        self.max3=3#harmadik kancso maximuma

    def célteszt(self, állapot):
        return állapot[0]==self.cél or állapot[1]==self.cél #ha az elso kancso vagy a masodik kancso cel allapotban van akkor igaz

    def rákövetkező(self, állapot):
        a1,a2,a3=állapot#allapotbol kinyerjuk az 1, 2, 3 kancsok erteket
        lépések=list()#lehetseges lepesek listaja, egyelore uresen

        if a1 > 0 and a2 < self.max2:#elsobol a masodik kancsoba valo toltes
            T = min(a1, self.max2 - a2)#az elso korso tartalmanak es a masodik korso ures helyenek maximuma
            lépések.append(("a1-bol a2-be", (a1 - T, a2 + T, a3)))

        if a1 > 0 and a3 < self.max3:#elsobol a harmadikba
            T = min(a1, self.max3 - a3) #az elso korso tartalmanak es a harmadik korso ures helyenek maximuma
            lépések.append(("a1-bol a3-be", (a1 - T, a2, a3 + T)))

        if a2 > 0 and a3 < self.max3:#masodikbol a harmadikba
            T = min(a2, self.max3 - a3)#a masodik korso tartalmanak es a harmadik korso ures helyenek a maximuma
            lépések.append(("a2-bol a3-ba", (a1, a2 - T, a3 + T)))

        if a2 > 0 and a1 < self.max1:#masodikbol az elsobe
            T = min(a2, self.max1 - a1) #a masodik korso tartalmanak es az elso korso ures helyenek maximuma
            lépések.append(("a2-bol a1-be", (a1 + T, a2 - T, a3)))

        if a3 > 0 and a2 < self.max2:#harmadikbol masodikba
            T = min(a3, self.max2 - a2)#a harmadik korso tartalma es a masodik korso ures helyenek maximuma
            lépések.append(("a3-bol a2-be", (a1, a2 + T, a3 - T)))

        if a3 > 0 and a1 < self.max1:#harmadikbol az elsobe
            T = min(a3, self.max1 - a1)#a harmadik korso tartalma es a masodik korso ures helyenek maximuma
            lépések.append(("a3-bol a1-be", (a1 + T, a2, a3 - T)))


        return lépések







if __name__ == '__main__':
    k = Korsó((8, 0, 0), 4)
    meg = szélességi_fakeresés(k)
    utam  = meg.út()
    print(utam)
    még = mélységi_fakeresés(k)
    ütem = még.út()
    print(ütem)