from keres import *


class Királynő(Feladat):
    def __init__(self, k, c):
        self.kezdő = k#sakk tabla kezdo allapota
        self.cél = c#cel allapot
        self.S = 8#lehelyezendo kiralynok

    def célteszt(self, állapot):
        return állapot[self.S] == self.cél #

    def rákövetkező(self, állapot):
        lépések = []#allapotok halmaza
        s = állapot[self.S] #
        for i in range(1, 9):#lerak i
            # op alkalmazasi elofeltetele
            előfeltétel = True #elofeltetel eleinte True
            for m in range(1, s):#a megelezo sorok bejarasa
                if i != állapot[m - 1] and abs(m - s) != abs(állapot[m - 1] - i): #ha az elozo sor oszlopa nem egyenlo a mostanival
                                                                                #es nem atlosak akkor marad igaz a feltetel
                    előfeltétel = True
                else:#egyeb esetben pedig hamissa valik es kilepunk a ciklusbol
                    előfeltétel = False
                    break

            if előfeltétel:#operator alkalmazasi fuggvenye
                állapot_uj = list(állapot)
                állapot_uj[s - 1] = i#tabla s-1.soraban az i. oszlopba helyezzuk a kiralynot
                állapot_uj[self.S] += 1#a seged elemet noveljuk a listaban
                lépések.append(("s-sor i-dik oszlop", tuple(állapot_uj)))

        return lépések


if __name__ == '__main__':
    k = Királynő((0, 0, 0, 0, 0, 0, 0, 0, 1), 9)
