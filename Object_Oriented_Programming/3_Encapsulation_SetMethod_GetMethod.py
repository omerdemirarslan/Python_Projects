class Calisanlar():         #Calisanlar adında bir class (sınıf) oluşturuyorum.

    def __init__(self,isim,soyisim,tckn,eposta):  #Sınıfın yapıcı metodu olan __init__ (Initializer/Başlatıcı) metodumu kullanıyorum.
                                                  #Sınıfa 4 tane property(özellik) atıyorum.
        self.isim       = isim
        self.soyisim    = soyisim
        self.tckn       = tckn
        self.eposta     = eposta

                                #Calisanlar sınıfından calisan_1 adında instance(örneklem) yaratıyorum.


calisan_1 = Calisanlar("Ömer","Demirarslan","01234567890","omerdemirarsln@gmail.com")

                                #calisan_1'e ait özellikleri ekrana bastırıyorum.
print(f'İsim: {calisan_1.isim}, Soyisim: {calisan_1.soyisim}, TCKN: {calisan_1.tckn}, E-posta: {calisan_1.eposta}')

calisan_1.isim = "Hakan"
                                #calisan_1'in ismini ve tckn'sini değiştiriyorum.
calisan_1.tckn = "12125121259"

                                #calisan_1'e ait özellikleri tekrar ekrana bastırıyorum. Bu sefer isim ve tckn değişmiş olacak.
print(f'İsim: {calisan_1.isim}, Soyisim: {calisan_1.soyisim}, TCKN: {calisan_1.tckn}, E-posta: {calisan_1.eposta}')


class Calisanlar():

    #Yukarıda isim ve tckn'yi rahatlıkla değiştirebilmiştik. Bu işlemi herkesin yapmasını engellemek için Encapsulation (Kapsülleme)...
    #özelliğini kullanabiliriz. Bu özellikle sabit veya değişken tipi verilerimizi sınıf dışı müdahalelere karşı koruma altına alırız.

    def __init__(self,isim,soyisim,tckn,eposta):
        self.__isim     = isim
        self.__soyisim  = soyisim   #Burada, isim, soyisim ve tckn değişkenlerini Private(Özel) koruma sağlıyorum...
        self.__tckn     = tckn      #bu şekilde bu değişkenlere dışardan erişmek ve değiştirmek kısıtlanmış oluyor.
        self.eposta     = eposta    #Private koruma sağlamak içim "double underscore" (çift altçizgi) kullanıyorum.

    #Private olan değişkenlerime ulaşmak için get metotlarımı oluşturuyorum.
    def get_isim(self):
        return self.__isim

    def get_soyisim(self):
        return self.__soyisim

    def get_tckn(self):
        return self.__tckn

    #Private olan değişkenlerimde olabilecek hataları düzeltmek için set metotlarımı oluşturuyorum.

    def set_isim(self,isim):
        self.__isim = isim

    def set_soyisim(self,soyisim):
        self.__soyisim = soyisim

    def set_tckn(self,tckn):
        self.__tckn = tckn

#Calisanlar sınıfımdan calisan_2 adında bir örneklem yaratıyorum.


calisan_2 = Calisanlar("Mert","Kaya","35735735735","mertkaya@gmail.com")

#calisan_2 örneklemime ait bilgileri ekrana bastırıyorum. Burada self.isim, self.soyisim ve self.tckn yazmadığıma dikkat çekiyorum...
#değişkenlere ulaşmak ve görüntülemek için get metotlarımı kullanıyorum.

print(f'İsim: {calisan_2.get_isim()}, Soyisim: {calisan_2.get_soyisim()}, TCKN: {calisan_2.get_tckn()}, E-posta: {calisan_2.eposta}')

#calisan_2 örneklemimde isim,soyisim ve tckn'de hata yaptığımı fark ediyorum ve bu 3 özelliği güncellemek için set metotlarımı kullanıyorum.
calisan_2.set_isim("Ahmet")
calisan_2.set_soyisim("Kaya")
calisan_2.set_tckn("35735700000")

#calisan_2 örneklemimi tekrar ekrana bastırdığımda artık güncellenmiş bilgiler ekrana gelecektir.
print(f'İsim: {calisan_2.get_isim()}, Soyisim: {calisan_2.get_soyisim()}, TCKN: {calisan_2.get_tckn()}, E-posta: {calisan_2.eposta}')









