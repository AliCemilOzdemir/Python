# type(1) len(1) pow(3) print(*,sep = " ",end = "\n")

# print() 

    # sep [separator (ayirici, ayrac)]  :
'print("merhaba","ben","ali","cemil",sep="--")   '

    # merhaba--ben--ali--cemil
"sep parametresi yalnizca (Str) ve (None) degerlerini alabilir . None = ' ' gibi davranir , yani on tanimli deger gibi."

    # end
"end parametresi yalnizca (Str) ve (None) degerlerini alabilir . None = ' ' gibi davranir , yani on tanimli deger gibi."

    # file
"file parametresinin degerleri : sys.stdout(standart out yerinde cikartir) ya da dosya(x = open() tarzi xler)"

    # flush
"flush parametresinin degerleri : True ya da False"
"dosyayi kapatmadan yazmak icin flush=True , ontanimli olan flush=False"

    # bu ornek bir uygulamadir... ( os.getcwd() , datetime , file = ,sep= ,end= )
"""
import os
import datetime
anlikTarih =datetime.datetime.now()
print("\nDosya dizini",os.getcwd() , sep = "  :  " , end = "\n\n")

dosyaAdi = "yazbelDeneme0.txt"

dosya = open(dosyaAdi,"w")
print("bu bir deneme yazisi ve...",

    f"{anlikTarih.ctime()} tarihinde",

    "alicemil ozdemir tarafindan yazildi...",
    
    "\ntesekkur ederim yazbel...",
    
    file = dosya,sep="\n",end = "")
dosya.close()

print("yazim basarili lutfen kontrol ediniz...",end = "\n\n")
"""

# print(*"Galatasaray") = print("G", "a", "l", "a", "t", "a", "s", "a", "r", "a", "y")

"""adres = ['C:', 'Users', 'alice', 'AppData', 'Local', 'Programs', 'Python', 'Python312']
print(*adres ,sep = "\\")"""

"""import keyword
yasakliKelimeler = keyword.kwlist
print(yasakliKelimeler)"""

"""import sys
sys.exit()""" # program biter

"""print("merhaba kankiler yeter bu comarliginiz\n\
artik buna dur demenin bir zamani geidl\n\
bence artik sacmalamayi kesin")"""

'print("merhaba\\kankiler")'
'print("\N{LATIN SMALL LETTER A}")' #"a"

# \f ile diger sayfaya gecme komutu...
"""dosya = open("yazbelDeneme0.txt","r+")
print(dosya.read())

print("deneme\fdeneme",file=dosya,flush=True)
dosya.close()"""

# \b imleci bir sola kaydirir...
"""print("alice.com\b.uk")""" # alice.co.uk

# eval() ve exec() fonksiyonlari
"bu fonksiyonlarin parametresi python komutlaridir..."
"exec in eval den farki exec de degisken tanimlama yapilabilir"

# := operator
"""if ( giris := len(input("Adin ne? ")) ) < 4:
    print("Adin kisaymis.")
elif giris < 6:
    print("Adin biraz uzunmus.")
else:
    print("Cok uzun bir adin var.")"""

#taslak = """
"""
      
                                                                                              Tarih:
        Okulunuz {} ogrencisi {} nolu {} adli ogrencinin velisiyim .
Ogrenciniz {} tarihinde hasta oldugu icin okula gelememistir .Benim velisi olarak bundan bilgim vardir .
Kendisinin devamsizliginin affini talep ediyorum.



Ogrencinin :                                                           Velisinin :

Adi : {}                                                               Adi : {}     
Soyadi : {}                                                            Soyadi : {}
Okul no : {}                                                           Okul no : {}
Sinif : {}                                                             Sinif : {}
      


"""
"del taslak"
# python ile surum denetimi ornek kodu...
"""# -*- coding: utf-8 -*-
# bu kod kodlama biciminin utf-8 oldugunu belirtir...

import sys

versiyon = sys.version_info # versiyon adli bir nesne olusturduk ve bu nesne version_info adli class in bir nesnesi
# bu nesne python un surumunu kontrol ederken kullanabilecegimiz bir takim parametreler iceriyor

if versiyon.major == 3 and versiyon.minor > 2 :
     print("programa hos geldiniz...")
else :
     if versiyon.major == 2:
          print("python un 2.x surumleri ile bu program calismaz...")
     if versiyon.minor <= 2:
          print("python un 3.3'ten onceki surumleri ile bu program calismaz...")


print("-"*30)"""

# range(ilk_sayi, son_sayi, atlama_degeri)

# dongulerde else kullanimi while icin de gecerli...break varsa islemez ,yoksa isler...
"""sifre = "124"
for x in range(3) :
    girdi = input("lutfen sifrenizi giriiniz : ")
    if girdi == sifre :
        print("hos geldiniz...")
        break
    else :
        print("yanlis sifre...")
else :
    print("3 hatali deneme yapildi lutfen 20 sn bekleyiniz...")"""

# try ve except kullanimlari 
# 1
"""ilk_sayi = input("ilk sayi: ")
ikinci_sayi = input("ikinci sayi: ")
try:
    sayi1 = int(ilk_sayi)
    sayi2 = int(ikinci_sayi)
    print(sayi1, "/", sayi2, "=", sayi1 / sayi2)
except ZeroDivisionError:
    print("Bir sayiyi 0'a bolemezsiniz!")
except ValueError:
    print("Lutfen sadece sayi girin!")"""
# 2
"""ilk_sayi = input("ilk sayi: ")
ikinci_sayi = input("ikinci sayi: ")
try:
    sayi1 = int(ilk_sayi)
    sayi2 = int(ikinci_sayi)
    print(sayi1, "/", sayi2, "=", sayi1 / sayi2)
except (ValueError, ZeroDivisionError):
    print("Bir hata olustu!")"""
# try... except... as...
"""ilk_sayi = input("ilk sayi: ")
ikinci_sayi = input("ikinci sayi: ")
try:
    sayi1 = int(ilk_sayi)
    sayi2 = int(ikinci_sayi)
    print(sayi1, "/", sayi2, "=", sayi1 / sayi2)
except (ValueError, ZeroDivisionError) as hata:
    print("Bir hata olustu!")
    print("orijinal hata mesaji: ", hata)"""

# try... except... else...
""" ilk except degilse bunlari yap anlamina gelir...Kodu daha moduler hale getirir
try:
    bolunen = int(input("bolunecek sayi: "))
    bolen = int(input("bolen sayi: "))
except ValueError:
    print("Lutfen sadece sayi girin!")
else:
    try:
        print(bolunen/bolen)
    except ZeroDivisionError:
        print("Bir sayiyi 0'a bolemezsiniz!")
"""

# try... except... finally...
"""try: # hata olussa bile finally yapilir...
    dosya = open("dosyaadi", "r")
    ...burada dosyayla bazi islemler yapiyoruz...
    ...ve ansizin bir hata olusuyor...
except IOError:
    print("bir hata olustu!")
finally:
    dosya.close()"""

# asertion ne demek - assertion error
# iddia.
# assert kalibinda yapi : assert ifade , ifadenin aksi olursa yazilacak metin(Assertion Error olarak)
"""def turkceKarakterBULUCU(girdi : str) :
    girdi = girdi.lower()
    turkceKarakterler = {"c","o","s","u","g","i"}
    varMi = False
    for imlec in girdi :
        if imlec in turkceKarakterler :
            varMi = True
            break
    return varMi

userName = input("lutfen bir kullanici adi giriniz...")

assert not turkceKarakterBULUCU(userName) , "Lutfen turkce karakter girmeyiniz..."
"""
# try ... except ValueError ... except... dene - deger hatasi - deger hatasi haric digerleri icin
"""import sys
_2x_metni = ""Python'in 2.x surumlerinden birini kullaniyorsunuz.
Programi calistirabilmek icin sisteminizde Python'in
3.x surumlerinden biri kurulu olmali.""
_3x_metni = "Programa hosgeldiniz."
try:
    if sys.version_info.major < 3:
        print(_2x_metni)
    else:
        print(_3x_metni)
except AttributeError: # 2.7 nin alti surumlerde bu hata verilir cunku .major ifadesi bulunmaz o surumlerde.
    print(_2x_metni)"""
# sorted metodu ve harf siralamasi ile bir metindeki harfleri uygun bir sekilde siralamak...
"""harfler = "abccdefgghiijklmnooprsstuuvyz"
cevrim = {i: harfler.index(i) for i in harfler}
print(sorted("afgdhkii", key=cevrim.get))"""

# immutable - mutable datatypes
"""Python’da iki tur veri tipi bulunur: degistirilemeyen veri tipleri (immutable datatypes) ve
degistirilebilen veri tipleri (mutable datatypes). Bizim simdiye kadar gordugumuz veri tipleri
(sayilar ve karakter dizileri), degistirilemeyen veri tipleridir. Henuz degistirilebilen bir veri tipi
gormedik."""

# enumarate
"""for sira, harf in enumerate("istihza", 1): # ikinci parametre numaralandirmaya nereden baslayacagimizi gosteriyor.
    print(sira, harf)"""

"""
sayi = 0
for x in dir("") :
    if not "_" in x :
        print(x)
        sayi += 1
print(sayi)
"""
"""
- bir dosyaya kurum adlari alt alta girilsin...
- daha sonra bu dosyadaki kurum adlarinin bas harflerinden olusturulan kisaltmalari baska bir dosyaya yazsin...
ANCAK
    - birden fazla kurumun bas harfleri ayniysa her biri icin kisaltmalarin nasil olacagini bize sorsun ve
    ona gore dosyaya yazsin...Boylece elimizde bir kisaltmalar listesi olsun...
"""

# karakter dizisi metodlari : 

# replace(eski_harf , yeni_harf , ilk kac eski harf degistirilecek)
# split(hangi_isaretle_birlikte_bolunecek , bolme sayisi - kac defa bolunecek)
"""split() ile rsplit() arasindaki tek
fark, split() metodunun karakter dizisini soldan saga, rsplit() metodunun ise sagdan sola
dogru okumasidir."""
# splitlines(True/False)    ontanimli deger False'tur ve \n gosterilecek mi sorusunun cevabi parametredir...
# lower() ve upper()    turkce karakterlerle problemler yaratir bundan dolayi turkce karakter kullanmamaya ozen gosteriniz...
# islower() ve isupper()     metinler lower/upper uygulanmis bir metin olabilir mi sorusunu sorar
# endswith("abc")    abc ile mi bitiyor $ True / False
# startswith("abc")  abc ile mi basliyior $ True / False
# capitalize()    sadece metnin ilk kelimesinin ilk harfini buyutur
# title()    bir metnin her kelimesinin ilk harfini buyutur boylece onu bir baslik yapar
# swapcase() bir metindeki buyuk harfleri kucuge , kucukleri buyuk harflere cevirir...
# casefold() lower() ile ayni islem turkce icin ancak almancada : "ß".casefold() -> 'ss'
# strip(x) bir metnin saginda ve solunda bulunan x'leri atar x ontanimli olarak (\n,\r,\t,\f,\v," ") dir.
# rstrip(x) sadece sagdakileri atar , lstrip() sadece soldakileri atar...
# join()       str:birlestirme_karakteri.join(bolunmus : list )
# count(karakter/harf,baslama indeksi = 0 ,bitis indeksi = len(metin)-1) son iki parametre on tanimli
# index(karakter/harf,baslangic = 0 ,bitis = len(metin)-1) if harf not in metin -> ValueError
# rindex(karakter) sagdan ilk buldugun karakterin indeksini goster.Saymaya yine soldan basla
# find ve rfind , index ve rindex e denk duser sirasiyla ancak r/find metotlari hata degil -1 dondururler eger bulamazlarsa
# center(sayi) -> o sayi kadar karakterin icine metin ortalanir...
# rjust() metodu bir karakter dizisini saga yaslarken, ljust() metodu karakter dizisini sola yaslar.l/rjust(karakter,sayi) o sayi kadar yaslanir...
# zfil(sayi) = rjust(sayi,karakter) sagina sifir ekler...
# partition(karakter) o karaktere gore metni 3 e boler..bakmaya soldan baslar - bulamazsa (metin,"","") metin ssola yaslandi
# rpartition(karakter) o karaktere gore metni 3 e boler..bakmaya sagdan baslar - bulamazsa ("","",metin) metin saga yaslandi
# encode()  "cilek".encode("cp1254")
# expandtabs(sayi = 8) tab boslugunu genislet. ontanimli degeri = 8
# str.maketrans(str1,str2,silinecekler) str1 deki her karakteri sozluk olarak ste2 deki her karaktere esler .Silinecekleri de NONE degeri ile esler...
# translate() str.maketransin yaptigi eslesmeye gore metindeki harfleri degistirir ya da siler. once silme sonra degistirme yapilir...
# isalpha() icinde alfabe disinda bir simge varsa False dondurur...aksi halde True
# isdigit() metnin sayisal olup olmadigini denetler ,icinde sayi harici bir simge varsa False dondurur...
# isalnum() alfanumerik mi ? alfanumerik : sadece harf ve sayilardan olusan demek...
# isdecimal() dogal sayi mi diye bakar
# isidentifier() tanimlayici mi ? degisken / modul / fonk adi olabilir mi
# isnumeric() numerik mi ? sayi degerli mi degil mi
# isspace() sadece bosluk karaterinden mi olusuyor sorusunun cevabi..
# isprintable() basilabilen karakter mi ("\n" basilamaz "a" basilabilir...)
# removesuffix(karakter) krakterler sondaysa , metnin sondaki karakterlerini kaldirir , karakterler sonda degilse degisiklik yapmaz
# removeprefix(karakter) karakter/ler bastaysa kaldirir degilse dokunmaz...
# format() metindeki {} isaretleri yerine yazi yazdirir...
# istitle() metin == metin.title() diye bakar
# isascii() kelimeler ascii kelimeleri mi yani usd/uk harfleri mi diyek kontrol eder...
# karakter bicimlendirme
"""print("%s ve %s iyi bir ikilidir!" %("Python", "Django"))
parola = "meh"
print("Girdiginiz parola (%s) kurallara uygun bir paroladr!" %parola)"""
# print("%%%s"%5)
# print("|%15s |" %"istihza") -> |        istihza |
# print("|%s |" %"istihza".rjust(15))
'print("depoda %(miktar)s kilo %(urun)s kaldi" %{"miktar": 25,"urun": "elma"})'
# print("|{:<20}| ".format("merhabaa"), end="") -> |merhabaa            |
""" format icin
> sağa yaslama
< sola yaslama
^ ortalama
"""
"{:,} ".format(1234567890) # sayilari basamakalrina ayirir...
# fstringlerin icinde python kodu yazilabilir...
"""print(f'Sayıların toplamı { int(input("Birinci sayıyı girin: ")) + int(input("İkinci sayıyı girin: ")) } eder.')"""
# ‘liste’ (list) ve ‘demet’ (tuple).
# list() fonk. karakter dizilerini ve iter.-nesnelerin(range) her bir ogesinden listeye yazdirmak icin kullanilir. Ayrica hic bir parametre girilmezse dondurdugu deger bos dizi dir[] 
# liste = range(10)
# print(len(liste))
""""Liste öğelerini değiştirmeye çalışırken, eğer var olmayan bir sıra numarasına atıfta
bulunursanız Python size IndexError tipinde bir hata mesajı gösterecektir:
"""
"""
liste = []
a = "1762e87y2heqdjfmk5daea"
liste += a # her bir ogeyi ayri syri ekler...["1","7","6","2" ...]
print(liste == list(a))"""
# listeleri a=[1,2,3]  b=a tarzi olusturursaniz b ile a ayni nesne olur ve b deki degisiklik a yi da degistirir
# bundan kecmak icin 2 yontem :
"""
1)
a = [1,2,3]
b = a[:]
2)
a = [1,2,3]
b = list(a)
"""
# Liste Üreteçleri (List Comprehensions)
"""--------------------------------------------------------"""
# metot 1 :
"""liste = [i for i in range(1000)]"""
# alternatif =  liste = list(range(1000))
"metot 2 : "    #liste = [i for i in range(1000) if i % 2 == 0]
# coklu for kullanimi = 
"""liste = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[10, 11, 12]]
tümü = [z for i in liste for z in i]
print(tümü)"""
# metot 2 :
"""list = [f"{x}:cift" if x%2 == 0 else f"{x}:tek" for x in range(0,10)]
print(list) # ['0:cift', '1:tek', '2:cift', '3:tek', '4:cift', '5:tek', '6:cift', '7:tek', '8:cift', '9:tek']"""
# DEMETLER (TUPLE) :
"""demet = (1,"1merhbava",True,[1,2])
demet = 1,"1merhbava",True,[1,2]
demet = tuple("akjfdjwıoskoseda")""" # list() gibi
tuple(["ahmet", "mehmet", 34, 45]) # tuple ile listeyi tuple a cevirdiniz...
# tek ogeli tuple olusturmak...
"""demet = ('ahmet',)
demet = 'ahmet',
demetimsi = ("ahmet")"""
"print(type(demetimsi))" # class str
# demetler str ve int gibi immutable veri tipidir ...Dolayisiyla degistirilemez ancak yeniden tanimlanabilir...
"""demet = ('ahmet', 'mehmet')
demet = demet + ('selin',)"""
"LISTELERIN METOTLARI"
# append() 1 prmtre alır .listeye yalnizca ve yalnizca tek bir oge eklemek icin kullanilabilir...
# extend() 1 prmtre alır .iter bir parametre alir ve iter objenin her listeye ayri ayri elemanini ekler
# insert() 2 prmtre alir .Index ve eleman .Eleman verilen indexe yerlestirilir...
# remove() 1 prmtre alir .O parametre de listeden kaldirirlir...parametre kaldirilacak elemanin ta kendisidir(indeksle calismaz...)
# reverse() 0 prmtre alir .List i ters cevirir
# pop() ya 1 ya 0 prmtre alir .sildigi degeri return eder . 1 prmtre alirsa indeks ile calisir . prmtre almazsa son ogeyi siler...
# sort() key ve reverse parametreleri vardir...reverse True ise ters cevirir on tanimli degeri false tur.Key i bilmiyorum.
# index() value start ve stop degerleri alir .Bulamazsa ValueError
# count() value degeri alir int dondurur...
# copy() listeyi kopyalar(immutable/mutable) 0 prmtre alir. 
# clear() parametresiz. listeyi ([])bos listeye cevirir
"DEMETLERIN(TUPLE) METOTLARI - kullanimlari str ve list icin olanlarinkiyle ayni"
# index()
# count() 

" Sayi sistemleri donusturme fonksiyonlari :"
# bin() - binary -> str  bin(2) = '0b10'
# hex() - hexadecimal -> str  hex(10) = '0xa'
# oct() - octadecimal -> str oct(8) ="0o10"
# int() - int("100",4) = 16
"sayi sistemlerini donusturme karakterleri : "
# sayı_sistemleri = ["onlu", "sekizli", "on altılı", "ikili"]
# print(("{:^9} "*len(sayı_sistemleri)).format(*sayı_sistemleri))
# for i in range(17):
#     print("{0:^9} {0:^9o} {0:^9x} {0:^9b} ".format(i))
# int i donusturmek icin int() disinda alternatifimiz yok

"Tamsayi metotlari :"
# (sayi).bit_length() tamsayinin kac bitlik yer kapladigini gosterir : len(bin(int[2:]))
"sayi. koymamamizin sebebi 10. yazdigimiz anda python bunun bir float oldugunu dusunuyor ve boylece bir tam sayi metodunu uygulayamayip hata veriyro"
"Float metotlari : "
# as_integer_ratio() kesire cevir ve tuple olarak sun
# is_integer() . dan sonrasi sifir mi diye bakar
"Complex nitelikleri : "
# c = 12+4j
# c.imag  4.0
# c.real  12.0
"Aritmetik Fonksiyonlari :"
# divmod() bir sayının bir sayıya bölünmesi işleminde bölümü ve kalanı verir:
# divmod(10,6) -> (1,4)
# max/min() bir dizideki max/min i bulurlar . Key = len dedigimizde metinleri uzunluklarına gore sıralarlar...
# sum() girilen bir kumedeki butun elemanları toplar ayrıyeten eklenen sayılar da toplama eklenir...

"DOSYALAR"
# Eğer bir dosyayı okuma kipinde açacaksanız, bu “r” harfini hiç belirtmeseniz de olur.
"""dosya = open("yazbelDeneme0.txt")"""
#-----------------------
"dosya.close()"
# with deyimi ile dosyayi acmak... Bu sayede dosya python tarafindan otomatik kapanacaktir
"""with open("yazbelDeneme0.txt") as dosya:
    print(dosya.read())"""
# hata alabilecegimiz programlarda try...except...finally blogunu kullanmaliyiz ki finally altinda dosya her durumda kapansin
"seek() ve tell()"
# seek(int) -> girdigimiz byte'i dondurur ayrica girilen byte'a imleci goturur
# tell() -> imlecin hangi byte uzerinde oldugunu soyler
# KIPLER ---------------------------------------/
# r
""" "r" Bu öntanımlı kiptir. Bu kip dosyayı okuma yetkisiyle açar. Ancak bu kipi
kullanabilmemiz için, ilgili dosyanın disk üzerinde halihazırda var olması gerekir.
Eğer bu kipte açılmak istenen dosya mevcut değilse Python bize bir hata
mesajı gösterecektir. Dediğimiz gibi, bu öntanımlı kiptir. Dolayısıyla dosyayı
açarken herhangi bir kip belirtmezsek Python dosyayı bu kipte açmak istediğimizi
varsayacaktır."""
# w
""" "w" Bu kip dosyayı yazma yetkisiyle açar. Eğer belirttiğiniz adda bir dosya zaten disk
üzerinde varsa, Python hiçbir şey sormadan dosya içeriğini silecektir. Eğer belirttiğiniz
adda bir dosya diskte yoksa, Python o adda bir dosyayı otomatik olarak oluşturur."""
# a
""" "a" Bu kip dosyayı yazma yetkisiyle açar. Eğer dosya zaten disk üzerinde mevcutsa
içeriğinde herhangi bir değişiklik yapılmaz. Bu kipte açtığınız bir dosyaya eklediğiniz
veriler varolan verilere ilave edilir. Eğer belirttiğiniz adda bir dosya yoksa Python
otomatik olarak o adda bir dosyayı sizin için oluşturacaktır."""
# x
""" "x" Bu kip dosyayı yazma yetkisiyle açar. Eğer belirttiğiniz adda bir dosya zaten disk
üzerinde varsa, Python varolan dosyayı silmek yerine size bir hata mesajı gösterir.
Zaten bu kipin “w” kipinden farkı, varolan dosyaları silmemesidir. Eğer belirttiğiniz
adda bir dosya diskte yoksa, bu kip yardımıyla o ada sahip bir dosya oluşturabilirsiniz."""
# r+
""" "r+" Bu kip, bir dosyayı hem yazma hem de okuma yetkisiyle açar. Bu kipi kullanabilmeniz
için, belirttiğiniz dosyanın disk üzerinde mevcut olması gerekir."""
# w+
""" "w+" Bu kip bir dosyayı hem yazma hem de okuma yetkisiyle açar. Eğer dosya mevcutsa
içerik silinir, eğer dosya mevcut değilse oluşturulur."""
# a+
""" "a+" Bu kip bir dosyayı hem yazma hem de okuma yetkisiyle açar. Eğer dosya zaten disk
üzerinde mevcutsa içeriğinde herhangi bir değişiklik yapılmaz. Bu kipte açtığınız bir
dosyaya eklediğiniz veriler varolan verilere ilave edilir. Eğer belirttiğiniz adda bir
dosya yoksa Python otomatik olarak o adda bir dosyayı sizin için oluşturacaktır."""
# x+
""" "x+" Bu kip dosyayı hem okuma hem de yazma yetkisiyle açar. Eğer belirttiğiniz adda bir
dosya zaten disk üzerinde varsa, Python varolan dosyayı silmek yerine size bir hata
mesajı gösterir. Zaten bu kipin “w+” kipinden farkı, varolan dosyaları silmemesidir.
Eğer belirttiğiniz adda bir dosya diskte yoksa, bu kip yardımıyla o ada sahip bir dosya
oluşturup bu dosyayı hem okuma hem de yazma yetkisiyle açabilirsiniz"""
# Dosya metotlari :
# closed niteligi -> dosya kapaliysa True aciksa False dondurur.
# readable() -> bir dosya okunabilir mi sorusunun cevabi.
# writable() -> bir dosyaya yazi yazabilir miyiz sorusunun cevabi.
# truncate(x = 0 : int) -> ilk x byte haric diger butun byte lar budanir/kirpilir.Truncate budamak/kırpmak anlamlarına gelir..Truncate ile imlecin bulundugu yerden sonraki her karakter kirpilir.x metodu imlecin yerini ayarlar.Eger x metindeki karakter sayisindan fazlaysa gei kalan kisim 0larla doldurulur.
# mode ,name ,encoding nitelikleri .Dosyaya ait niteliklere ulasmamizi saglar...

# IKILI DOSYALAR :
"""
Creator Belgeyi oluşturan yazilim
/Producer Belgeyi PDF'e çeviren yazilim
/Title Belgenin başliği
/Author Belgenin yazari
/Subject Belgenin konusu
/Keywords Belgenin anahtar kelimeleri
/CreationDate Belgenin oluşturulma zamani
/ModDate Belgenin değiştirilme zamani
"""
# ikili dosyalar...
"""
for f in dosyalar:
okunan = open(f, 'rb').read(10)
if okunan[6:11] in [b'JFIF', b'Exif']:
print("{} adlı dosya bir JPEG!".format(f))
elif okunan[:8] == b"\211PNG\r\n\032\n":
print("{} adlı dosya bir PNG!".format(f))
elif okunan[:3] == b'GIF':
print("{} adlı dosya bir GIF!".format(f))
elif okunan[:2] in [b'II', b'MM']:
print("{} adlı dosya bir TIFF!".format(f))
elif okunan[:2] in [b'BM']:
print("{} adlı dosya bir BMP!".format(f))
else:
print("Türü bilinmeyen dosya: {} ".format(f))
"""
# !s string disi demek
"""print("{:<5} {!s:<15} {:<15} ".format(s,
s.encode("utf-8"),
len(s.encode("utf-8"))))"""
# encode - Parametre Anlamı
"""
'strict' Karakter temsil edilemiyorsa hata verilir
'ignore' Temsil edilemeyen karakter görmezden gelinir
'replace' Temsil edilemeyen karakterin yerine bir '?' işareti koyulur
'xmlcharrefreplace' Temsil edilemeyen karakter yerine XML karşiligi koyulur. Bu değer, programınızdan alacağınız çıktıyı bir
XML dosyasında kullanacağınız durumlarda işinize yarayabilir."""

"KARAKTER KODLAMA ILE ILGILI FONKSIYONLAR"
# repr() bir objeyi tanimlayan bir string dondurur...
# ascii() bir stringin ascii karsiligi varsa onu yoksa , bu karakterlerin UNICODE kod konumlarını (code points) gosterir.
# ord() Bu fonksiyon, bir karakterin sayı karşılığını verir:
# chr() Bu fonksiyon, bir sayının karakter karşılığını verir:

"BYTE LARIN FONKSIYONLARI :"
# decode()  --- > b"\xc4\xb0".decode("utf-8")  $ utf-8 e gore  byte i karaktere ceviriyor...
#   fromhex() --> 16 lik duzenden byte a cevirir . $ bytes.fromhex("c4b0")
"""bytes adlı veri tipi ile elde ettiğimiz veri tıpkı karakter dizileri gibi, üzerinde değişiklik
yapılamayan bir veridir. Dolayısıyla bir bytes nesnesi üzerinde değişiklik yapabilmek için o
nesneyi tekrar tanımlamamız gerekir:"""
# bytearray
"""Ama Python programlama dilinde bytes veri tipi dışında, baytlara ilişkin ikinci veri tipi daha
bulunur. bytearray adlı bu veri tipi, bytes veri tipinin aksine, üzerinde değişiklik yapılabilen bir
veri tipidir.
Python’da bytearray veri tipini şu şekilde tanımlıyoruz:
>>> pdf = bytearray(b'PDF-1.7')"""

# Eğer bir sözlük içinde bulunmayan bir öğeye erişmeye çalışırsak Python bize KeyError tipinde bir hata mesajı verecektir. 
"""bir sözlüğe anahtar(key) olarak ancak şu veri tiplerini ekleyebiliriz: - degistirilemeyen veri tiplerini:
1. Demetler
2. Sayılar
3. Karakter Dizileri
deger(Value) olarak her turlu veriyi ekleyebiliriz..."""
# Sözlükler değiştirilebilir veri tipleridir. Dolayısıyla sözlükler üzerinde rahatlıkla istediğimiz değişikliği yapabiliriz.                                                                                                                                                                

# sozluk uretecleri(Dict Comprehensions) - > sözlük = {i: harfler.index(i) for i in harfler}

# sozluk = {'b': 1, 'c': 2, 'a': 0, 'd': 3}
"SOZLUKLERIN METOTLARI"
# keys() dict_keys objesi dondurur .Bu objeyi list(obje),tuple(obje) ve "".join(obje) sekillerinde veriye donusturebiliriz...Str'e cevirmek istiyorsdaniz join i kullanmadan once objenin verilerinin str e cevrildiginden emin olun
"STR CEVIRME METODU : "  " ''.join([str(i) for i in sözlük.values()]) "
# values() dict_values objesi dondurur .Bu objeyi list(obje),tuple(obje) ve "".join(obje) sekillerinde veriye donusturebiliriz...Str'e cevirmek istiyorsdaniz join i kullanmadan once objenin verilerinin str e cevrildiginden emin olun
# items() dict_items nesnesi dondurur . list ve tuple ile kullanilabilir .Uzerinde donguler kurulur genelde.
# get(sorgu , sorgu yoksa yerine dondurulecek deger) ile sozlukte bir sorgulama yapilir .
# clear() bos sozluge cevirir .
#MUTABLE DATATYPES ILE ILGILI BIR ACIKLAMA
"""Varolan bir sözlüğü veya listeyi başka bir değişkene atadığımızda aslında
yaptığımız şey bir kopyalama işleminden ziyade bellekteki aynı nesneye gönderme yapan iki
farklı isim belirlemekten ibaret."""
# copy() metodu ile mutable veri tipleri kopyalanır ve immutable gibi davranırlar.
# dict.fromkeys(iterable,value) her iterable elemanina ayni value'yu ata...
# sozluk.pop("tatlılar", "Silinecek öğe yok!") ilk ogeyi siler ,yoksa ikinci argumani yazar ,o da yoksa hata mesaji basar
# sozluk.popitem() son eklenen ogeyi siler .Eger sozluk bos sozlukse hata mesaji verir
# setdefault(key,value) o key aranir .Varsa ekrana sozlukteki degeri basilir(value dan bagimsiz olarak) yoksa o key ve value sozluge eklenir...
# dict1.update(dict0) dict1 = dict0

"KUMELER VE DONDURULMUS KUMELER"
# set(prmtr) fonk ile kumeler olusturlur prmtr yok ise bos kume olusturulur .Prmtr bir iterable object olmalidir(dict,tuple,list,str)
# küme = {'Python', 'C++', 'Ruby', 'PHP'} ifadesi de bir kume belirtir.
"""bir sözlüğü kümeye çevirdiğinizde, elbette sözlüğün yalnizca anahtarlari kümeye
eklenecektir. Sözlüğün değerleri ise böyle bir işlemin sonucunda ortadan kaybolur."""
# kümeler aynı öğeyi birden fazla tekrar etmez
# set comprehensions
"""import random
liste = [random.randint(0, 10000) for i in range(1000)]
küme = {i for i in liste if i < 100}
print(küme)"""

"KUMELERIN METOTLARI :"
# clear()
# copy()
# add(x) x i kumeye ekle .
"""Bir kümeye
herhangi bir öğe ekleyebilmemiz için, o öğenin değiştirilemeyen (immutable) bir veri tipi
olmasi gerekiyor.""" # (immutable)
"""mutable :  1. Listeler  2. Sözlükler  3. Kümeler
immutable :  1. Demetler  2. Sayılar  3. Karakter Dizileri"""
# difference(k2) k1 ile k2 nin farkini al - kumeler ... k1.difference(k2) = k1 - k2
# difference_update(k2) k1 = k1-k2
# discard(x) x ogesini sil .Eger x diye bir eleman yoksa HATA VERMEZ.
# remove(x) x ogesini sil .Eger x diye bir eleman yoksa HATA VERIR.
# intersection(k2) k1 ile k2 nin kesisimi = k1 & k2
# intersection_update(k2) k1 = k2 & k1
# isdisjoint(k2) ayrik kumeler mi diye sorar ? True -> kesisimleri bos kume.
# issubset(k2) k1 k2'in alt kumesi mi diye sorar ?True -> k1 k2nin alt kumesi
# issuberset(k2) k1 k2 nin ust kumesi mi ?
# union() metodu iki kümenin birleşimini almamızı sağlar. k1 | k2 birlesim demek .
# update(x) update metodu normal yollarla kumeye ekleyemedigimiz veri tipleri olan mutable tipleri kumeye ekler.
# symetric_difference(k2) iki kumenin simetrik farki...
# symmetric_difference_update(k2) gunceller.
# pop() rastgele bir elemani siler.

"Dondurulmus kumeler normal kumelerin immutable halidir .Bu iliski liste ve demet arasi iliskiye benzer .Bir dondurulmus kume set metodundan farkli olarak frozenset() metodu ile set() metoduna benzer sekilde tanımlanır."

# python da fonksiyonlar gomulu fonksiyonlar - builtin functions ve ozel fonksiyonlar - custom functions olarak ikiye ayrilir .Ozel fonksiyonlar bizim yaptıklarımız .
# isimli arguman kullanacaksak isimsiz argumandan sonra kullanmalıyız ya da hepsini isimli yapmalıyız :print("merrhba",sep="\n") gibi ya da işBul(yer="ant",iş="IT") vb
# *parametre gibi parametre ifadeleri teknik olarak en fazla 256 karaktrer alabilir .
# def fonksiyon(*parametreler): - seklinde tanimlanmis bir fonksiyonda parametreler demet(tuple) tipindedir .
"""* işareti herhangi bir öğeyi alıp, bunu parçalarına ayırıyor. İşte bu * işaretini
fonksiyon tanımlarken kullandığımızda ise bu işlemin tam tersi gerçekleşiyor. Yani fonksiyon
tanımında parametrenin soluna * getirdiğimizde, bu fonksiyon çağrılırken verilen argümanlar
tek bir değişken içinde bir demet olarak toplanıyor. """
# def kayıt_oluştur(**kwargs): --- yapisiyla sinirsiz sayida isimsiz parametre girilmesi saglanir... Bu sekilde alinan kwargs parametresi bir sozluk tipindedir ...**kwargs da isimli parametre döndürür.
"""def bas(*args, start='', **kwargs):
    for öğe in args:
        print(start+öğe, **kwargs)
bas('öğe1', 'öğe2', 'öğe3', start="#.",end=" -- ")"""

"""Eğer tanımladığımız bir fonksiyonda return deyimini kullanarak herhangi bir değer
döndürmezsek, Python fonksiyondan hususi bir değerin döndürülmediğini göstermek için
‘None’ adlı bir değer döndürür..."""

# random.sample(list,2) listten 2 tane rastgele eleman secer
# random.shuffle(list) listeyi rastgele karistirir...
# random.randrange(x,y) girilen aralikta tamsayi uretir

"""Python’da değişkenlerin, fonksiyonların ve daha sonra göreceğiniz gibi sınıfların bir kapsamı
vardır. Bu kapsama Python’da ‘isim alanı’ adı verilir. Dolayısıyla Python’da her nesnenin,
geçerli ve etkin olduğu bir isim alanı bulunur. Örneğin yukarıdaki kodlarda fonksiyon dışındaki
x değişkeni ana isim alanında yer alan ‘global’ bir değişkendir. Fonksiyon içindeki x değişkeni
ise fonk() değişkeninin isim alanı içinde yer alan ‘lokal’ bir değişkendir. Bu iki değişken, adları
aynı da olsa, birbirlerinden farklı iki nesnedir.

Python herhangi bir nesneye göndermede bulunduğumuzda, yani o nesnenin değerini talep
ettiğimizde aradığımız nesneyi ilk önce mevcut isim alanı içinde arar. Eğer aranan nesneyi
mevcut isim alanı içinde bulamazsa yukarıya doğru bütün isim alanlarını tek tek kontrol eder.

Python’da bir nesnenin değerini değiştirmekle, o nesneyi yeniden tanımlamak farklı
kavramlardır :
    degistirilebilir veri tipleri - list ,dict ,set
    degistirilemez veri tipler - str ,int/float/complex ,tuple

Eğer bir nesne değiştirilebilir bir nesne ise, o nesnenin değerini, lokal isim alanlarından
değiştirebilirsiniz ANCAK bunu yaparken bir "yeniden tamamlama islemi YAPAMAZSINIZ"

LOKAL ALANLARDA YENIDEN TANIMLAMA YAPILAMAZ .ANCAK O DEGISKENLE AYNI ADA SAHIP BIR DEGISKEN OLUSTURULABILIR BOYLECE GLOBAL ALANDAKI DEGISMEDEN VARLIGINI SURDURUR.

global deyimi  kullanılırsa global alandaki degisken lokal alana da tasinir ve orada butun degisiklikler kullanilabilir hale gelir .
kullanım :
yas = 10

def yeniSene() :
    global yas
    yas += 1
    return yas

yeniSene()
print(yas) # 11
"""

"""---------------------GOMULU FONKSIYONLAR---------------------"""
# abs(sayi) tek bir parametre alır ve onun mutlak degerini dondurur .
# round(sayi, yuvarlama hassasiyeti= 0 (float dondurur) - None(int dondurur)) yuvarlama hassasiyeti kac olursa noktadan sonra o kadar sayi olur. 
"""kayan noktalı bir sayının üst ve alt tam sayılara olan uzaklığının
birbirine eşit olduğu durumlarda Python çift sayıya doğru yuvarlama yapmayı tercih eder. """
# all(iterable) eger all un icindeki iterable ın içindeki butun degerlerin BOOL degeri True ise True dondur aksi halde False .BOOL degeri false olan tipler list(),int(),str() tarzi tanimlaninca olusan bos kumeler yahut 0 dır.
# any(iterable) "herhangi bir = any" en az bir tane True varsa True dondurur yoksa false .
"['', 0, [], (), set(), {},frozenset()] --bos veri tipleri-- [str(),int(),list(),tuple(),set(),dict(),frozenset()]"
# ascii() ASCII kodlarını normal olarak dondurur .Non-ASCII kodlarının UNICODE karsılıklarını dondurur(16lık duzen) ,a = ascii(list) type(a) = str olur .
# repr() non-ascii ile karsilastimi karakter karsiligini dondurur .Onun harici ascii ile aynidir...For many object types, including most builtins, eval(repr(obj)) == obj.
# bool() bool degerini verir bir nesnenin
# bin() bir nesnenin ikili karsiligini str olarak verir . bin(12) = '0b1100'
# bytes(x) x: int ise x degerince 0 byte yerlestirir.x : str ise ayrica bir y parametresi ile kod çözücü belirtmeliyiz ki byte lar ona gore belirlensin.eger kod cozucu bu metni cozemezse hata verir .Bu hatayla bas etmek icin errors diye bir parametremiz de var/errors(replace,ignore,xml..)
# bytearray() byte veri tipi degistirilemez(immutable) bir veri tipidir .bytearray() ile bu veriyle ayni olan ancak degistirilebilen bir veri tipi elde etmis oluyoruz
# chr(sayi) unicode sistemine gore girilen sayinin karakter karsiligini bulur.
# list() ya liste olusturur ya da basak veri tipini listeye cevirir.
# set() ya set olusturur ya da basak veri tipini set e cevirir.
# tuple() ya tuple olusturur ya da basak veri tipini tuple a cevirir.
# frozenset() ya frozenset olusturur ya da basak veri tipini frozenset a cevirir.
# complex(sayi,sanal) = sayi +(sanal)j
# float()  sayıları veya karakter dizilerini kayan noktalı sayıya dönüştürür .
# int() float ve str yi int yapar ayrica sayi sistemleri arasinda donusumler saglar : int("12",8) = 10
# str() int float ve byte i str ye cevirir. byte kullanirken ayrica bir encoding= ve errors= parametrelerini de kullanmalıyız .
# dict() boş bir sözlük oluşturabiliriz: >>> s = dict() /  değişkenlerden sözlükler oluşturabilirlz : >>> s = dict(a=1, b=2, c=3) / ikişer elemanlı kumelerden sozlukler olusturabiliriz : sozluk =dict([[1,2],["aynen","sensin"]]) .1 PARAMETRE ALIR.
# callable() bir nesne ÇAĞIRILABILIR MI(fonksiyonlar gibi) diye bakar.
# ord() bir karakterin karşılık geldiği ondalık sayıyı verir.
# oct() bir sayıyı sekizli düzendeki karşılığına çevirmemizi sağlar:
# hex() bir sayıyı onaltılı düzendeki karşılığına çevirmemizi sağlar:
"""Yalniz oct,hex,bin fonksiyonlarinda dikkat etmemiz gereken şey, bu
fonksiyonlarin parametre olarak bir sayi alip, çikti olarak bir karakter dizisi veriyor olmasidir."""
# eval,exec,globals,locals,compile()
"""pythonda expressionlar(ifade) ve statementlar(deyim) vardir.
'ifadeler', bir değer üretmek için kullanilan kod parçalaridir.
Karakter dizileri, sayilar, işleçler, öteki veri tipleri, liste üreteçleri, sözlük üreteçleri, küme
üreteçleri, fonksiyonlar hep birer ifadedir. Örneğin:
>>> 5
>>> 23 + 4
>>> [i for i in range(10)]
>>> len([1, 2, 3])

ifadelerin
bir araya gelmesi ile deyimler oluşturulabilir.
Deyimlere birkaç örnek verelim:
>>> a = 5
>>> if a:
...     print(a)
>>> for i in range(10):
...     print(i)

"""
# eval() yalnizca ifadeler ile calisir.
# exec() ise yalnizca deyimler ile.
#-------------------------------------------------------------------------------------------------------------------
# copyright() ile python un telif hakları gösterilir .
# credits() katkida bulunanlara bir tesekkur.
# license() lisans
# dir() Eğer parametresiz olarak kullanırsak, mevcut isim alanındaki öğeleri bir liste halinde elde ederiz .Ayrıca dir() fonksiyonunu kullanarak nesnelerin metot ve niteliklerini içeren bir listeye ulaşabiliriz.
# divmod(a,b) -> (a//b :int ,a % b : int)
# enumerate(iterable,baslama_sayisi) iterable ın her elemanina baslama_sayisi ndan baslayarak numaralandırır ve bir (iterablenin_ogesi,numara) tuple a cevirir her elemanini .
# exit() o anki programdan cikar .Etkilesimli kabuktaysa onu kapatir .
# help()
# id() Python’daki her nesnenin kimliği eşşiz, tek ve benzersizdir.
# format()
# filter(fonksiyon,iterable1) iterable bir filter nesnesi yaratır .Oyle ki bu nesnenin elemanlari iterable1 in fonksiyona prmtr olarak deger girilince True donduren degerleridir.
# Bu fonksiyon, belirli türdeki nesnelere bir karma değeri vermemizi sağlar.
# isinstance(ifade , veri tipi=int,str vs) ifade o veri tipinde mi diye bakar. 
# len() 
# map(fonksiyon,iterable) iterablenin her ogesine fonksiyon uygulanır.
# max() karmasik bir fonksiyondur .En buyuk degerin istendigi orneklerde akla ilk gelmesi gereken fonksiyondur .
"""def en_yüksek_rütbe(rütbe):
    rütbeler = {'er' : 0,
                'onbaşı' : 1,
                'çavuş' : 2,
                'asteğmen' : 3,
                'teğmen' : 4,
                'üsteğmen' : 5,
                'yüzbaşı' : 6,
                'binbaşı' : 7,
                'yarbay' : 8,
                'albay' : 9}
    return rütbeler[rütbe]

askerler = {'ahmet': 'onbaşı',
'mehmet': 'teğmen',
'ali': 'yüzbaşı',
'cevat': 'albay',
'berkay': 'üsteğmen',
'mahmut': 'binbaşı'}

print(max(askerler.values(), key=en_yüksek_rütbe))"""
# min() max ile benzer islevi yapar yalnizca buyugu degil kucugu bulur .

# open(dosya_adi, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
"""Bu fonksiyon herhangi bir dosyayi açmak veya oluşturmak için kullanilir. Eğer dosyanin
açilmasi veya oluşturulmasi esnasinda bir hata ortaya çikarsa IOError türünde bir hata mesaji
verilir"""
# f = open("C:\\Users\\alice\\Desktop\\ALICEMIL\\PythonCodeFiles\\yazbelDeneme0.txt",mode="w",buffering=1 , encoding="ascii",errors="replace")
# f.write("merhaba\n")
# f.write("nasislsin lanki")
# f.write("?her sey yolunda mi\n")
# f.write("hayir her sey yolunda degil salak misin")
# f.write("bilmiyorum aptalm isin")
# f.write("yeş aptalşın")
"""buffering = 1  oldugu zaman \n olmadan dosyaya veri islenmiyor .Tamponda tutuluyor."""
"""Eğer dosyaya işlenecek verilerin tampona alınmadan doğrudan dosyaya işlenmesini isterseniz
buffering değerini 0 olarak belirlersiniz.YALNIZ BU SADECE IKILI DOSYALARDA VAR.METINDE YOK"""
# fileno() 0,1,2 sırasıyla standart girdi,standart cikti,standart hata dosyalarıdır .Sizin olusturdugunuz dosyaların numaraları 2'den buyuk,essiz ve benzerdsizdir.
# dosyayı dosya numarası ile acabiliriz .Ornek : g.fileno() = 4 -> n=open(4)/n=open(g.fileno())
""". Normalde dosyayı
kapattığımızda dosyanın tanımlayıcısı serbest kalır ve başka bir dosya açıldığında bu
tanımlayıcı yeni dosyaya atanır. Ama closefd parametresine False değeri verdiğimizde dosya
kapansa bile, o dosyaya ait dosya tanımlayıcısı varolmaya devam edecektir."""
# pow(sayi,us,modulus) = (sayi**us) % modulus
# print(deg1, deg2, deg3, ...,deg256, sep=' ', end='\n', file=sys.stdout, flush=False)
# quit() = exit()
# range(başlangıç_değer, bitiş_değeri, atlama_değeri) iterable bir range nesnesi dondurur daha sonra biz bu nesnenin iterable olması sayesinde istedigğimiz forma ceviririz
# reversed(iterator) Sırali bir nesneyi ters ceviren reverseiterator - nesnesi .Iterator oldugu icin Evir cevir kullan.
# sorted(iterator,key=fonksiyon) fonksiyon sayılardan olusan bir deger dondururse kelimedeki her harfi o fonksiyona gore sayiya cevirir. Ona gore sıralamasını yapar. MUHTEŞEM BIR FONKSIYON
# slice(başlangıç, bitiş, atlama) iterable verileri dilimler.
# sum(iterable,int) iterable ogelerini ve int'i,hepsini topla
# type(x) xin tipini soyler.
# zip(iter1,iter2) iter1 ile iter2 nin her elemanini tuple olarak birlestirir ve iterable bir zip nesnesi dondurur.
# vars() parametresiz locals() ile ayni parametre vererek nesnelerin metotları ve niteliklerini ogrenebiliriz
"""import tkinter
import tkinter.ttk as ttk
pen = tkinter.Tk()
btn = ttk.Button(text='merhaba', command=lambda: print('merhaba'))
btn.pack(padx=20, pady=20)
pen.mainloop()"""

# RECURSIVE FUNCTIONS ...
"""
DIP NOKTA BULMA :
>>> import sys
>>> sys.getrecursionlimit()
bu komutları girersek ,sistemimizin max yineleme miktarını goruruz .Eger bir fonksiyhon bundan fazla yineleme yapmaya calisirsa
RuntimeError: maximum recursion depth exceeded --------HATASINI ALIR

"""

# def topla(liste:list):
#     if len(liste) == 1 :
#         return int(liste[0])
#     else :
#         return liste[0] + topla(liste[1:])
    
"""def fonk1():
def fonk2():
...
Burada fonk1 kapsayıcı (enclosing) veya dış fonksiyonumuz, fonk2 ise içerideki (nested) yani
iç fonksiyonumuz oluyor"""
# kapsayıcı fonksiyona ait değişkenleri, iç fonksiyonumuzda değiştirebilmek için nonlocal ifadesine ihtiyacımız vardır. nonlocal kullanimi global kullanşmi ile aynidir.
""" İç fonksiyonun, çağırılan
kapsayıcı fonksiyonun yerel değişkenlerinden biri olduğunu ve her seferinde yeniden
tanımlandığını, bu yüzden de aynı işi yapsalar da aslında farklı olan fonksiyonlar elde ettiğimizi bilin. """
# Ancak her seferinde yeniden tanımlanan tek şey iç fonksiyon değildir. Kapsayıcı fonksiyonun içindeki her değişken, dış fonksiyonun her çağırılışında baştan tanımlanır.
"""def sayıcı():
    sayı = 0
    def say():
        nonlocal sayı
        sayı += 1
        return sayı
    return say"""
# return
"""Bir fonksiyonun
içinde return deyimine ulaşıldığında fonksiyon sonlanır ve fonksiyona ait yerel değişkenler
silinir. """
# yield
"""yield deyiminde böyle bir şey söz konusu değildir. Aynı iç içe fonksiyonlarda iç
fonksiyonunun dış fonksiyondaki değişkeni kullanması gibi üreteçlerin de yerel değişkenleri
Python tarafından saklanır.Ancak üreteçlerde belli değişkenler değil, yerel değişkenlerin
tamamı saklanır. """
"""
yield from bir_üreteç
ifadesi bu ifade eş değerdir:
for i in bir_üreteç:
yield i
"""
# os.name = "nt" for win , os.name="posix" for linuX and Mac
# os.getcwd() GET Current Working Directory
# os.makedirs(adress or name , make it on current directory if there is no address but just name) MAKE DİRectorieS

# from os import * seklindeki modul tanımlama islemi yalnızca global isim alanında gerceklestirilebilir .Bir fonksiyonun icinde boyle bir sey yapamayız.

"""import sys
>>> sys.path
python bir modulu dahil etmek icin ararken kendisinin calistirildigi dizine(os.getcwd())
ve sys.path komutunun verdigi listedeki adreslere bakar ."""
# from import modul *  ile ice aktarma yaparsak "_" ile baslayanlar ice aktarilmayacaktir .Sadece bu dahil etme yonteminde gecerli olmak uzere,
# __all__ = ["fonk1","fonk2"...] tarzı bir ifadeyi modulun en basina eklersek ,o dahil etme yonteminde , from import modul * dahil etme yonteminde yalnizca __all__ listesinde adlari belirtilmis fonk ve ozellikler dahil edilecektir .

# set.intersection(*kumeler) kumeleri iceren iterable kumeler nesnesindeki kumelerin kesisimi boyle alinir.

# os.__file__ os un bulundugu dizini dondurur.

# ORTAK 5 NITELIK - BUTUN MODULLERDE :{'__doc__', '__name__', '__loader__', '__spec__', '__package__'}
# __doc__ > Modüllerin __doc__ niteliğini kullanarak, bir modül dosyasının en başında bulunan belgelendirme dizilerine erişebiliriz.documentation string
# __name__ > bu ozellik sayesinde programımızın dogrudan calistirildiginda ve iceri aktarildiginda farkli davranmasini saglayabiliriz .Cunku __name__ niteligi yalnizca asil programda calisirken "__main__" dondurur.Aksi halde dahil edildigi modulun adini dondurur.
# __loader__ > Bu nitelik, ilgili modülü içe aktaran mekanizma hakkında bize çeşitli bilgiler veren birtakım araçlar sunar
# __spec__ > __spec__ niteliği de bize modüller hakkında çeşitli bilgiler sunan birtakım araçları içinde barındırır. Mesela bir modülün ad ve konum bilgilerine ulaşmak için bu niteliği kullanabiliriz
# __package__ > paketler konusunda ele alınacak ...

#---------------------------- BABALARIN BABASI OOP -----------------------------------
# Bos bir sınıf tanımlamak(sınıf adından sonra tercihe baglı olarak () konabilir ) :
"""   class Çalişan:          class Çalişan() :       
          pass                    pass                   """

# instantiation (ornekleme / orneklendirme)
"""class Çalışan():
    kabiliyetleri = []  #class attribute
    unvanı = 'işçi'     #class attribute
    maaşı = 1500        #class attribute
    memleketi = ''      #class attribute
    doğum_tarihi = ''   #class attribute
(instance) ahmet = Çalışan()""" # instantiation

# class attiributes ile ilgili onemli bir aciklama...Degistirilebilir veri tipleri ile calısırken dikkatli olun :
"""Hatırlarsanız, sınıf niteliklerinden bahsederken, bu niteliklerin önemli bir özelliğinin, sınıf
çağrılmadan çalışmaya başlamaları olduğunu söylemiştik. Sınıf niteliklerinin bir başka önemli
özelliği de, bu niteliklere atanan değerlerin ve eğer yapılabiliyorsa bu değerler üzerinde
sonradan yapılan değişikliklerin o sınıfın bütün örneklerini etkiliyor olmasıdır. Eğer ilgili sınıf
niteliği; karakter dizisi, demet ve sayı gibi değiştirilemeyen (immutable) bir veri tipi ise bu sınıf niteliği üzerinde zaten değişiklik yapamazsınız. Yaptığınız şey ancak ilgili sınıf niteliğini
yeniden tanımlamak olacaktır. Ancak eğer sınıf niteliği, liste, sözlük ve küme gibi değiştirilebilir
(mutable) bir veri tipi ise bu nitelik üzerinde yapacağınız değişiklikler bütün sınıf örneklerine
yansıyacaktır."""


# kabiliyetlerine append() ile yaptigimiz eklemeler listelerin mutable olmasından dolayı Çalışan'ın bizzat kendi özelligi olacaktır... sebebi yukarda.

# instant attiributes - örnek nitelikleri
"""__init__(), alelade bir fonksiyondan başka bir şey değildir. Bu fonksiyonun öteki
fonksiyonlardan tek farkı, sınıflar açısından biraz özel bir anlam taşıyor olmasıdır. Bu özel
fonksiyonun görevi, sınıfımızı örneklediğimiz sırada, yani mesela ahmet = Çalışan() gibi bir
komut verdiğimiz anda oluşturulacak nitelikleri ve gerçekleştirilecek işlemleri tanımlamaktır."""

# instance methods - ornek metotları
"ornekler icin yapilmis olan metotlar self parametreleri ile kullanılır."

"""her ne kadar Python’da sınıf niteliklerine hem örnekler hem
de doğrudan sınıf adları üzerinden erişebilsek de örnek niteliklerine ve örnek metotlarına
yalnızca örnekler üzerinden erişebiliriz."""

# class methods - cls parametresi ile kullanilir , baslarina @classmethod bezeyicisi(decorator)'u atanir.

"""eğer bir sınıf içindeki herhangi bir fonksiyonda örnek(erişmek için self) veya sınıf niteliklerinin(erişmek için cls ve @classmethod)
hiçbirine erişmeniz gerekmiyorsa, statik metotları kullanabilirsiniz."""
"""class Sorgu():
    def __init__(self, değer=None, sıra=None):
        Sorgu.hosgeldiniz()
        self.liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
        ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim','İthaki'),
        ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt','Cem')]
        if not değer and not sıra:
            l = self.liste
        else:
            l = [li for li in self.liste if değer == li[sıra]]
        for i in l:
            print(*i, sep=', ')
    @classmethod
    def isbnden(cls, isbn): # alternatif insa... bu fonk ile nesneyi farklı bir yontemle inşa ediyoruz...
        cls(isbn, 0)
    @classmethod
    def yazardan(cls, yazar):
        cls(yazar, 1)
    @classmethod
    def eserden(cls, eser):
        cls(eser, 2)
    @classmethod
    def yayınevinden(cls, yayınevi):
        cls(yayınevi, 3)
    @staticmethod
    def hosgeldiniz() :
        print("KUTUPHANEMIZDEKI KITAPLARI BULMANIZI SAGLAYACAK DIJITAL ARSIVE HOS GELDINIZ")
"""

"""import time
import random
import sys
class Oyuncu():
    def __init__(self, isim, can=5, enerji=100):
        self.isim = isim
        self.darbe = 0
        self.can = can
        self.enerji = enerji
    def mevcut_durumu_görüntüle(self):
        print('darbe: ', self.darbe)
        print('can: ', self.can)
        print('enerji: ', self.enerji)
    def saldır(self, rakip):
        print('Bir saldırı gerçekleştirdiniz.')
        print('Saldırı sürüyor. Bekleyiniz.')
        for i in range(10):
            time.sleep(.3)
            print('.', end='', flush=True)
        sonuç = self.saldırı_sonucunu_hesapla()
        
        if sonuç == 0:
            print('\nSONUÇ: kazanan taraf yok')
        if sonuç == 1:
            print('\nSONUÇ: rakibinizi darbelediniz')
            self.darbele(rakip)
        if sonuç == 2:
            print('\nSONUÇ: rakibinizden darbe aldınız')
            rakip.darbele(self)
    def saldırı_sonucunu_hesapla(self):
        return random.randint(0, 2)
    def kaç(self):
        print('Kaçılıyor...')
        for i in range(10):
            time.sleep(.3)
            print('\n', flush=True)
        print('Rakibiniz sizi yakaladı')
    def darbele(self, darbelenen):
        darbelenen.darbe += 1
        darbelenen.enerji -= 1
        if (darbelenen.darbe % 5) == 0:
            darbelenen.can -= 1
        if darbelenen.can < 1:
            darbelenen.enerji = 0
            print('Oyunu {} kazandı!'.format(self.isim))
            self.oyundan_çık()
    def oyundan_çık(self):
        print('Çıkılıyor...')
        sys.exit()"""

"""Bir nesnenin hangi
niteliklere sahip olacağını belirleyen veri tipine sınıf (class) derken, o sınıfın ortaya çıkardığı
ürüne ise nesne (object) adını veriyoruz. """

# OOP yapmak her biri kendi verilerine sahip nesneler tanimlamak demektir .
#Dolayisiyla bu metot ile bir program yazilirken farkli fonksiyonlari bir araya getirerek anlamli bir iş ortaya cikarmaliyiz .
# Işte bunun icin fonksiyonlarimizi tanimlarken o fonksiyon bir/birkaç nesnenin özelligini mi degistirecek(ornek metotları) yoksa butun nesneleri mi etkileyecek(sınıf metodları) diye karar vermeliyiz.

""": Python'da her şey bir nesnedir. Gerçekten de (if,
def, and, or gibi deyim ve işleçler hariç) Python'da her şey bir nesnedir."""

# Pythonda nesneler birinci sınıf ögelerdir .First Class items
"""1. Başka bir fonksiyona veya sinifa parametre olarak verilebilirler
2. Bir fonksiyondan döndürülebilirler
3. Bir değişkene atanabilirler
Yani, bir öğenin 'birinci sinif' olmasi demek, dil içindeki başka öğelerle yapabildiğiniz her şeyi
o öğeyle de yapabilmeniz demektir."""

# class members : public members,private members,semi-private members
# private members : 
"""Dilerseniz gizli üye oluşturma kurallarını şöyle bir netleştirelim:
Bir üyenin gizli olabilmesi için başında en az iki adet, ucunda da en fazla bir adet alt çizgi
bulunmalıdır. """
"""Gizli üyeler yalnızca sınıf dışına
kapalıdır. Bu üyelere sınıf içinden rahatlıkla erişebiliriz. Mesela : __gizli adlı değişkene örnek_metodu() içinden normal bir şekilde
erişebiliyoruz:
"""
# dogrudan erisemesek de bu o fonksiyonun gizli oldugu anlamina gelmez cunku python isim bulandırma(name mangling)
# ozelligi ile bu nesnenin adini degistirir ve metodun adini = _sinif__metot() olarak degistirir.

# semi-private members :
""" _yarıgizli adlı niteliğe sınıf içinden veya dışından erişmemizi engelleyen veya
zorlaştıran hiçbir mekanizma bulunmaz. Ama biz bir sınıf içinde tek alt çizgi ile başlayan bir
öğe gördüğümüzde, bunun sınıfın iç işleyişine ilişkin bir ayrıntı olduğunu, sınıf dışından bu
öğeyi değiştirmeye kalkışmamamız gerektiğini anlarız."""

"""class Çalışan():
    _personel = []
    def __init__(self, isim):
        self._isim = isim
        self.personele_ekle()
    def personele_ekle(self):
        self._personel.append(self._isim)
        print('{} adlı kişi personele eklendi'.format(self._isim))
    @classmethod
    def personeli_görüntüle(cls):
        print('Personel listesi:')
        for kişi in cls._personel:
            print(kişi)
    @property
    def isim(self):
        return self._isim
    @isim.setter
    def isim(self, yeni_isim):
        kişi = self._personel.index(self.isim)
        self._personel[kişi] = yeni_isim
        print('yeni isim: ', yeni_isim)"""

# property bezeyicisi - @property
"""Property kelimesi (attribute kelimesine benzer bir şekilde) İngilizcede 'özellik, nitelik' gibi
anlamlara gelir. Kelime anlamina uygun olarak, @property bezeyicisinin yaptigi en temel iş,
bir metodu, nitelik gibi kullanilabilecek hale getirmektir."""
""""""
# @property bezeyicisinin bir başka kabiliyeti de salt okunur nitelikler oluşturabilmesidir .cunku metotlarin degerleri degistirilemez .PROPERTY ILE DEGISKENE CEVIRSEK BILE.
"""class Program():
    def __init__(self):
        self._sayı = 0
    @property
    def sayı(self):
        return self._sayı
    @sayı.setter
    def sayı(self, yeni_değer):
        if yeni_değer % 2 == 0:
            self._sayı = yeni_değer
        else:
            print('çift değil!')
        return self.sayı
    @sayı.deleter
    def sayı(self):
        print("basariyla silindi")
        del self._sayı"""

# Taban sınıf , birkaç farklı sınıfta ortak olan nitelik ve metotları barındıran bir sınıf türüdür.(base class/super class/parent class)
# Bir taban sınıftan türeyen bütün sınıflar, o taban sınıfın alt sınıflarıdır. (subclass).
"Alt siniflar, kendilerinden türedikleri taban siniflarin metot ve niteliklerini miras yoluyla devralir."
# INHERITANCE(MIRAS ALMA...) Asker class ı Oyuncu class ının butun metot ve niteliklerine sahip.
# Oyuncu = (base class/super class/parent class) ------ Asker = (subclass).
"""class Oyuncu():
    def __init__(self, isim, rütbe):
        self.isim = isim
        self.rütbe = rütbe
        self.güç = 0
    def hareket_et(self):
        print('hareket ediliyor...')
    def puan_kazan(self):
        print('puan kazanildi')
    def puan_kaybet(self):
        print('puan kaybedildi')

class Asker(Oyuncu):
    pass"""

# super()
"""Miras alınan üst sınıfa
atıfta bulunan super() fonksiyonu, miras aldığımız bir üst sınıfın nitelik ve metotları üzerinde
değişiklik yaparken, mevcut özellikleri de muhafaza edebilmemizi sağlar."""
# class Asker(Oyuncu):
#     def __init__(self, isim, rütbe):
#         super().__init__(isim, rütbe)
#         self.güç = 100
    # super().__init__(isim, rütbe)
"""bu satirda super() fonksiyonu, tam da adinin anlamina uygun olarak, miras alinan üst
sinifin __init__() metodu içindeki kodlarin, miras alan alt sinifin __init__() metodu içine
aktarilmasini sağliyor. Böylece hem taban sinifin __init__() metodu içindeki self.isim ve
self.rütbe niteliklerini korumuş, hem de self.güç adli yeni bir nitelik ekleme imkani elde etmiş
oluyoruz"""
# super().__init__(isim,rutbe) fonksiyonunda parametreleri tek tek yazmak istemiyorsak,
# konumlu parametreler(positional args) icin *args ,
# isimli parametreler(keyword args) icin **kwargs ifadeleri kullanilabilir .
'Böylece konumlu argümanlari bir demet içinde, isimli argümanlari ise bir sözlük içinde toplamiş oluyoruz.'
"""super() fonksiyonu gelmeden önce taban sınıfa atıfta
bulunabilmek için doğrudan o sınıfın adını kullanıyorduk:"""
# class Asker(Oyuncu):
#     def __init__(self, isim, rütbe):
#         Oyuncu.__init__(self, isim, rütbe)
#         self.güç = 100
# veya:
# class Asker(Oyuncu):
#     def __init__(self, *args):
#         Oyuncu.__init__(self, *args)
#         self.güç = 100

"""Gördüğünüz gibi, eski yöntemde taban sinifin adini iki kez kullanmamiz gerekiyor. Ayrica
__init__() fonksiyonunun parametre listesinde ilk siraya yine self kelimesini de eklemek
zorunda kaliyoruz."""# super().fonk() 'ta self yok .Ancak eski yontemde var.

"""class Oyuncu():
    def __init__(self, isim, rütbe):
        self.isim = isim
        self.rütbe = rütbe
        self.güç = 0
    def hareket_et(self):
        print('hareket ediliyor...')
    def puan_kazan(self):
        print('puan kazanildi')
    def puan_kaybet(self):
        print('puan kaybedildi')

class Asker(Oyuncu):
    def __init__(self, isim, rütbe):
        super().__init__(isim, rütbe)
        self.güç = 100
    def hareket_et(self):
        super().hareket_et()
        print('hedefe ulaşıldı.')"""

# Burada super().hareket_et() satırıyla taban sınıfın hareket_et() adlı metodunu alt sınıfta
# tanımladığımız yeni hareket_et() metodu içinde çalıştırarak, bu metodun kabiliyetlerini yeni
# hareket_et() metoduna aktarıyoruz.

""" OBJECT SINIFI
Python un 2 surumlerinde sininflar yeni tip ve eski tip olamk uzere ikiye ayriliyordu.
eski tip siniflarda bir takim ozellikler yoktu(property bezeyicisi gibi) yeni tip siniflarda yeni ozellikler vardi
ve yeni tip siniflarin da object class'indan miras almasi gerekiyordu .
GUNUMUZDE BUTUN CLASS LAR YENI Tiptir .Dolayisilya
class a = class a() = class a(object)
bu uc tanimlama da da on tanimli olarak object class i miras alinacaktir...
"""

"import tkinter"
"pencere = tkinter.Tk()" # 200x200 boyutunda bir pencere uretir.
"pencere.mainloop()" # uretilmis pencereyi gosterir.
"""Yukaridaki kodlari yazdiğimizda, yani tkinter modülünün Tk() sinifini örneklediğimiz anda
aslinda penceremiz oluştu. Ancak bu pencere örnekleme ile birlikte oluşmuş olsa da,
Tkinter'in iç işleyişi gereği, 'ana döngü' adli bir mekanizma çalişmaya başlamadan görünür
hale gelmez. İşte bu özel ana döngü mekanizmasini çaliştirmak ve böylece oluşturduğumuz
pencereyi görünür hale getirmek için, Tk() sinif örneklerinin mainloop() adli bir metodunu
çaliştiracağiz:"""
# Tk() sınıfını pencere adıyla örnekledikten sonra Tk() sınıfının mainloop() adlı metoduna pencere örneği üzerinden eriştik.

# coklu miras almada coklu_sinif(c1,c2,c3) seklinde yazarsak ucu de miras alinmis olur .
# ancak ayni isimli metodlarda super yazpilacaginda c1 e gore metot insa edilir.
# bunu onlemek icin c3.ortak_metot(self) yazarsak c3 un metodu miras alinir (multiple inheritance)

"""
Miras alma ve dahil etme yöntemleri arasinda tercih yaparken genel yaklaşimimiz şu olacak:
Eğer yazdiğimiz uygulama, bir başka sinifin türevi ise, o sinifi miras alacağiz. Ama eğer bir sinif,
yazdiğimiz uygulamanin bir parçasi ise o sinifi uygulamamiza dahil edeceğiz.
"""

"""Yani mesela yukaridaki örnekte temel olarak yaptiğimiz şey bir uygulama penceresi
tasarlamaktir. Dolayisiyla uygulama penceremiz, tk.Tk() sinifinin doğrudan bir türevidir. O
yüzden bu sinifi miras almayi tercih ediyoruz.

Pencere üzerine etiket ve düğme yerleştirmemizi sağlayan Label() ve Button() siniflari ise,
uygulama penceresinin birer parçasidir. Dolayisiyla bu siniflari uygulamamizin içine dahil
ediyoruz."""

# path paketlerin nerede oldugunu soyler .
# https://pypi.org/ moduller buradan bulunur.


# import paket            ----->             urllib.request.urlopen('https://yazbel.com/')
# import paket.modül                  ----->                                request.urlopen('https://yazbel.com/')
# from paket.modül import nitelik_veya_metot         ----->              urlopen('https://yazbel.com/')
# from paket.modül import *             ----->                urlopen('https://yazbel.com/')

# eger import edilen nwsne bir paketse __package__ niteligi paket adi dondurecektir .Eger degilse '' bos karakter dizisi

"""import tkinter as tk
class Pencere(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol('WM_DELETE_WINDOW', self.çıkış)
        self.etiket = tk.Label(text='Merhaba Zalim Dünya')
        self.etiket.pack()
        self.düğme = tk.Button(text='Çık', command=self.çıkış)
        self.düğme.pack()
    def çıkış(self):
        self.etiket['text'] = 'Elveda zalim dünya...'
        self.düğme['text'] = 'Bekleyin...'
        self.düğme['state'] = 'disabled'
        self.after(2000, self.destroy)


pencere = Pencere()
pencere.mainloop()"""

# from . import altmodul1 ---------- bağıl aktarma .Iyi bir yoldur. ---- mevcut dizinden aktarma yap
# from .. import altmodul1 ---------- bir üst dizinden aktarma yap
# from ... import falanca ----------- iki üst dizinden aktar .

"""import os, sys
kullanıcı = os.environ['HOME'] #Windows'ta os.environ['HOMEPATH']
masaüstü = os.path.join(kullanıcı, 'Desktop')
sys.path.append(masaüstü)"""


