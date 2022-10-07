from  keres import *

class Kancsó(Feladat):
    def __init__(self,k,c):
        self.kezdő=k
        self.cél=c
        self.Max1=8
        self.Max2=5
        self.Max3=3

    def célteszt(self, állapot): # állapot= (a_1 ,a_2 ,a_3 )
        return állapot[0]==self.cél or állapot[1]==self.cél or állapot[2]==self.cél

    def rákövetkező(self, állapot):
        lépések=list()
        k1,k2,k3=állapot  # k1=állapot[0]

        if k1>0 and k2<self.Max2: # tölt_1_2 operátor alkalmazási előfeltétele
            T=min(k1,self.Max2-k2)
            lépések.append(("k1-ből tölt k2-be",(k1-T,k2+T,k3)))

        if k1>0 and k3<self.Max3: # tölt_1_3 operátor alkalmazási előfeltétele
            T=min(k1,self.Max3-k3)
            lépések.append(("k1-ből tölt k3-be",(k1-T,k2,k3+T)))


        if k2 > 0 and k1 < self.Max1:  # tölt_2_1 operátor alkalmazási előfeltétele
            T = min(k2, self.Max1 - k1)
            lépések.append(("k2-ből tölt k2-be", (k1 +T, k2-T, k3)))

        if  k2 > 0 and k3 < self.Max3:  # tölt_2_3 operátor alkalmazási előfeltétele#
            T = min(k2, self.Max3 - k3)
            lépések.append(("k2-ből tölt k3-be", (k1, k2 - T, k3+T)))

        if  k3 > 0 and k1 < self.Max1:  # tölt_3_1 operátor alkalmazási előfeltétele#
            T = min(k3, self.Max1 - k1)
            lépések.append(("k3-ből tölt k1-be", (k1+T, k2, k3-T)))

        if  k3 > 0 and k2 < self.Max2:  # tölt_3_2 operátor alkalmazási előfeltétele#
            T = min(k3, self.Max2 - k2)
            lépések.append(("k3-ből tölt k2-be", (k1, k2+T, k3-T)))

        return lépések










if __name__ == "__main__":
    k=Kancsó((8,0,0),4)

    print('Szélességi fakeresés')
    a =szélességi_fakeresés(k)

    utam=a.út()

    utam.reverse()

    print(utam)

    print('Mélységi fakeresés')
    b = mélységi_fakeresés(k)

    utam = b.út()

    utam.reverse()

    print(utam)


