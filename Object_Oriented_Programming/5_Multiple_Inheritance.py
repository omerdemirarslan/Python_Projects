class Calisanlar():
    def __init__(self,isim,soyisim):
        self.isim    = isim
        self.soyisim = soyisim

    def islem(self):

        print("Kişi kaydedildi")


class Yonetici():
    def __init__(self,isim,soyisim,departman):
        self.isim       = isim
        self.soyisim    = soyisim
        self.departman  = departman

    def islem(self):
        print( "Departman belirlendi")


class Muhasebe():
    def __init__(self,isim,soyisim,departman,maas):
        self.isim       = isim
        self.soyisim    = soyisim
        self.departman  = departman
        self.maas       = maas

    def islem(self):
        print("Son işlem başarıyla gerçekleşti.")


class IK(Muhasebe,Calisanlar,Yonetici):
    def __init__(self,isim,soyisim,departman,maas):
        super().__init__(isim,soyisim,departman,maas)


ik_1 = IK("Ömer","Demirarslan","IT","45000")

ik_1.islem()





