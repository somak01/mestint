from keres import *


class Tornyok(Feladat):

    def __init__(self,kezdőállapot, cél):
        self.kezdő = kezdőállapot
        self.cél = cél

    def célteszt(self, állapot):
        return állapot == self.cél




    def rákövetkező(self, állapot):
        lépések = []#lehetseges lepesek listaja, kezdetben ures
        for melyik in range(0, 3):#for ciklus amelyben a karikat valasztjuk ki
            for hova in ['P', 'Q', 'R']:#for ciklus amelyben a karika celjat
                alk_felt = True#alkalmazasi feltetel kezdetben True-ra allitva
                # a melyiket - hova operator alkalmazasi feltetel vizsgalata:
                if állapot[melyik] != hova: #ha a cel torony nem a korong jelenlegi tornya
                    for i in range(0, melyik):#for ciklus amely vegig fut a korongokon egeszen a melyik korongig
                        if állapot[i] != hova and állapot[i] != állapot[melyik]:#ha kissebb korong nincs a melyik korong tornyan, es kissebb korong nincs a hova rudon
                            alk_felt = True #akkor marad true a feltetel
                        else:
                            alk_felt = False #egyeb esetben false es kilepunk
                            break
                else:
                    alk_felt = False #a hova a melyiknek a tornya akkor is hamis lesz a feltetel

                if alk_felt:#ha az alkalmazasi feltetelek teljesultek, hozzadjuk a lepesekhez az uj allapotot
                    állapot_uj = list(állapot)
                    állapot_uj[melyik] = hova
                    állapot_uj2 = tuple(állapot_uj)
                    lépések.append(("atrak",állapot_uj2))
        return lépések


if __name__ == "__main__":
    tor = Tornyok(('P','P','P'), ('R', 'R', 'R'))