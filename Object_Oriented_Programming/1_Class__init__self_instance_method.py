
#Object Oriented Programming (Nesne Yönelimli Programlama)

class Calisanlar():  #Burada Calisanlar adında bir class (sınıf) oluşturuyorum.

    # __init__ in  özelliği constructor (yapıcı) olmasıdır. Bu özelliği ile sınıfa ait nesnelerin başlatılmasını sağlar.
    #Nesnelere property (özellik) vererek nesnelere atama yapar.

    #self keyword'ü (anahtar sözcüğü) sınıf örneklerini temsil eder ve kullanıldığında nesneye ait özelliklere ulaşmamızı
    #sağlar.

    def __init__(self, isim, soyisim, maas, departman): #Calisanlar sınıfına 4 tane property (özellik) atıyorum.
        self.isim       = isim
        self.soyisim    = soyisim                      #Yaratılan her nesne için bu özellikler farklı değerler alacak.
        self.maas       = maas
        self.departman  = departman

    #Calisanlar sınıfı içinde; örneklemlere ait özellikleri ekrana yazdıran bir metot oluşturdum.

    def bilgileri_goster(self):  #Sınıfa ait özellikleri metot içinde kullanıyorum ve self anahtar sözcüğü ile ulaşıyorum.
        print(" ""İsim:", self.isim,"\n","Soyisim:", self.soyisim,"\n","Maaş:", self.maas,"\n", "Departman:", self.departman)


#Calisanlar sınıfından bir instance (örneklem/nesne) yaratttım.

personel_1 = Calisanlar("Ahmet", "Arslan", 4500, "İnsan Kaynakları")


print(personel_1.departman)  #personel_1'e ait departman bilgisine ulaşıyorum.

personel_1.bilgileri_goster()  #bilgileri_goster metodu ile personel_1'e ait bütün özellikleri ekrana yazdırıyorum.


