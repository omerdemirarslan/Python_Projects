
#class (sınıf) oluşturmanın birinci metodu class Calisanlar: ikinci metodu ise class Calisanlar(): dır.
#class Calisanlar(): şeklinde oluşturulan sınıfa ait bütün özellikler başka bir sınıfta da kullanılabilir. Bu işleme inheritance denir.
#() kullanmamız bizim inheritance (kalıtım) yapabilmemizi sağlar.

class Calisanlar():

    def __init__(self, isim, soyisim, maas, departman):
        self.isim       = isim
        self.soyisim    = soyisim
        self.maas       = maas
        self.departman  = departman

    def bilgileri_goster(self):
        print(" ""İsim:", self.isim,"\n","Soyisim:", self.soyisim,"\n","Maaş:", self.maas,"\n", "Departman:", self.departman)


personel_1 = Calisanlar("Ahmet", "Arslan", 4500, "İnsan Kaynakları")

#inheritance (Kalıtım) bir sınıfa ait bütün özellikleri başka bir sınıfta kullanmamızı sağlayan OOP özelliğidir.


class Yonetici(Calisanlar):  #Yonetici adında bir sınıf oluşturuyorum ve Calisanlar sınıfını kalıtım yolu ile bu sınıfa
                             #dahil ediyorum.


    #Yonetici sınıfına ek bir özellikler ekleyerek Calisanlar sınıfının __init__ metodunu overriding (Geçersiz Kılma)
    #ediyorum.

    def __init__(self, isim, soyisim, maas, departman, sicil_puani):
        super().__init__(isim, soyisim, maas, departman)  #super fonksiyonu Calisanlar sınıfının özelliklerine ulaşmamı sağlıyor.

        self.__sicil_puani = sicil_puani   #Yoneticiler sınıfının beşinci özelliği.

    def departman_degistir(self, yeni_departman):  #Yonetici sınıfı içinde metot oluşturuyorum ve bu metoda depertman değiştirme
                                                   #görevi veriyorum.
        print("Departman Değiştiriliyor...")
        self.departman = yeni_departman

    #Calisanlar sınıfında da bulunan aynı isimde bir metodu Yonetici sınıfında da oluşturuyorum.
    def bilgileri_goster(self):
        print("","İsim:", self.isim,"\n","Soyisim:", self.soyisim,"\n","Maaş:", self.maas,"\n",
              "Departman:", self.departman,"\n","Sicil Puanı:",self.__sicil_puani)


yonetici_1 = Yonetici("Ömer", "Demirarslan", 4500, "Bilgi İşlem",100)  #Yonetici sınıfından yonetici_1 adında örneklem yaratıyorum.

personel_1.bilgileri_goster()  #Calisanlar sınıfının bir örneklemi olan personel_1'e ait özellikleri bilgileri_goster metodu ile ekrana yazdırıyorum.


yonetici_1.bilgileri_goster()  #Yonetici sınıfının bir örneklemi olan yonetici_1'e ait özellikleri bilgileri_goster metodu ile ekrana yazdırıyorum.

#Aynı isimli metodu iki farklı örneklemde çağırıp farklı çıktılar elde etmeye, OOP'ta Polymorphisim (Çok Biçimlilik) denir.