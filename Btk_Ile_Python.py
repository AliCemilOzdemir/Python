    # type fonksiyonu icine girilen degerin turunu dondurur...  output : <class 'str'>
''' print(type("Merhaba")) '''

    # operatorler
"""  

+    topla
-    cikar
*    carp
/    bol
**   us al
%    mod al
//   tam bol

"""

# degiskenler rakam ile baslamaz ancak _ ile baslayabilir ( c ile ayni  ) ...
# buyuk-kucuk harf duyarliligi vardir ...
# turkce karakter calisiyor ancak kullanmayalim ...
# degisken ismi arasinda bosluk birakilmaz ...

    #stringlerin birlestirilmesi
'''

name = "Ali Cemil"
surname = "Ozdemir"

print (name + ' ' + surname)

'''

    # toplu degisken tanimlama
'''

ad,soyad,yas,ehliyet = ("Ali Cemil","Ozdemir",18,True)

print(ad + " " + soyad , yas , ehliyet)

'''

    #string uzunlugu bulma ve stringi karakter dizisi olarak kullanma
'''

word = "abcde" + " ghij lmn oprstuvyz" + "\n0123456789" # karakter dizisi olusturuldu
length = len(word) # word un uzunlugu atandi

print(length) # uzunlugu yazdir

print(word[0]) # kelime dizisinin ilk terimini yazdir

print(word[length - 1]) # kelime dizisinin son terimini yazdir
      word[-1]    

print(word[-5]) # kelime dizisinin sondan 5. terimini yazdir

print(word[3::2]) # kelime dizisinin terimlerini 3.den sonuna kadar ikiser ikiser(1 terimi atlayarak) yazdir

print(word[3:])  # kelime dizisinin 3.teriminden(3 dahil) baslayarak son terime kadar yaz

print(word[:16]) # kelime dizisinin 0. teriminden baslayarak 15.terime(15 dahil) kadar yazdir

print(word[0:10:2]) # kelime dizisinin 0.teriminden 9.terime kadar ikiser ikiser yazdir 
      word[:10:2]

'''

    # genel ifade (string)
'''

karakter = "abcdefgh"
print(karakter[1:5]) # ilk indeks dahil ikincisi dehil degil

'''

    # string formatlama
'''

name = "Ali Cemil"
surname = "Ozdemir"

print("Merhaba benim adim {} {}".format(name,surname)) 
print("Merhaba benim adim {s} {n}".format(n=name,s=surname)) # formatin argumanlarini yerlestirdik direkt
print("Merhaba benim adim {1} {1}".format(name,surname)) # formatin 0. indeksi name 1. indeksi surname yerlestirdik

'''

    #float formatlama

"""

result = 4 / 7                                         #sayi dahil 10
print("sonuc : {r:5.3}".format(r=result)) # {r:10.3} r'yi 10 adet bosluk birakarak ilk 3 basamagini yaz...(yuvarlama yapilir) 0,5714 -> 0.571

"""


    # fstring
"""

name = "Ali Cemil"
surname = "Ozdemir"

print(f"merhaba benim adim {name} {surname}") # fstring ile kolayca yazilir ...

"""

    # stringi tersten yazdirma
"""

course = "degiskenler rakam ile baslamaz ancak _ ile baslayabilir ( c ile ayni  ) ..."

print( course[ len(course) - 1 :: -1] ) # son degiskene kadar hepsini tersten yazdirir...

"""

    # stringe mudahele edip eleman degistirme 
"""

x = "Hello world"
x = x[:6] + "W" + x[7:]

print(x)

"""

    # string fonksiyonlari
"""

message = "   Merhaba bu bir string mesajidir...   "

print(message.upper())    #   MERHABA BU BIR STRING MESAJIDIR...

print(message.lower())    #   merhaba bu bir string mesajidir...

print(message.capitalize())    #   Merhaba bu bir string mesajidir...

print(message.title())    #   Merhaba Bu Bir String Mesajidir...

print(message.strip())    #Merhaba bu bir string mesajidir...

print(message.split())    #['Merhaba', 'bu', 'bir', 'string', 'mesajidir...']

message = message.split()
print(message[2])    #bir

message = "   Merhaba bu bir string mesajidir . okudugunuz icin tesekkurler   "

message = message.split('.')    # stringi .'dan itibaren ayir
print(message)

message = ".".join(message)    # ayrilmis olan ogeleri aralarina nokta koyarak birlestir .
print(message)

message = "   Merhaba Bu bir string mesajidir . okudugunuz icin tesekkurlerr   "

print(message.find(".")) # 35 . indekste ilk nokta ile karsilasiliyor ...

print(message.endswith(".")) #FALSE

print(message.isupper()) #FALSE

print(message.replace("bir","BIR")) #   Merhaba Bu BIR string mesajidir . okudugunuz icin tesekkurlerr   

print(message.center(80)) #        Merhaba Bu bir string mesajidir . okudugunuz icin tesekkurlerr         

print(message.count("s")) #3

print(message.startswith("m")) #FALSE

print(message.replace(" ","*").replace("ç","c").replace("ö","o").replace("ı","i")) #***Merhaba*Bu*bir*string*mesajidir*.*okudugunuz*icin*tesekkurlerr***

print(message.center(80,"+")) #++++++++++++++++++++   Merhaba bu bir string mesajidir...   ++++++++++++++++++++

message = "***Merhaba bu bir string mesajidir...***"

print(message.lstrip("*")) #Merhaba bu bir string mesajidir...***
              left
print(message.rstrip("*")) #***Merhaba bu bir string mesajidir...
              right
print(message.strip("*")) #Merhaba bu bir string mesajidir...

print("www.alicemilozdemir.com".strip("w.com")) #alicemilozdemir

print("www.alicemilozdemir.com".count("i",0,11)) # 0'dan 11'e 11.indeks dahil degil , i sayisini verir

print("www.alicemilozdemir.com".find("t",0,11)) # 0'dan 11'e 11.indeks dahil degil , aralikta "t" varsa indeks numarasi yoksa EOF = -1 degeri dondurulur ...

print("www.alicemilozdemircemil.com".rfind("cemil")) #  aramaya sagdan baslar bu yuzden ikinci cemilin(c'sinin) indeks numarasi verilir...

print(message.index("i")) # 15

print(message.rindex("i")) # 32

print(message.index("ş")) # EXCEPTION - HATA

print(message.__len__()) # 40 

print(len(message)) # 40

print("Merhaba".ljust(15,"*")) # Merhaba********

print("Merhaba".rjust(15,"*")) # ********Merhaba

print("m e r h a b a".replace(" ","*",3)) # m*e*r*h a b a   yalnizca 3 tanesi degistirildi .

print("merhaba ben ali cemil ozdemir".split()[2]) #ali

"""

    # listeler(arrays) ve fonksiyonlari ...
"""

list1 = ["ali cemil".title(),18]
list2 = ["muhammet".title(),20]

lists0 = list1 + list2     # ['Ali Cemil', 18, 'Muhammet', 20]
lists00 = [ list1 , list2 ]     # [['Ali Cemil', 18], ['Muhammet', 20]]

print(f"{lists0}\n{lists00}")

print(lists00[0][0]) # ilk kullanicinin adi ... lists[0][0] 2d bir dizi .

arabalar = ["mercedes","bmw","tesla","renault"]

arabalar[1] = "opel" # atama yapildi ...

print(arabalar)

print("mercedes" in arabalar) # mercedes arabalarin icinde mi ? (bool)

print(arabalar[0:2]) # 0. ve 1. indeksler yazilir ...

arabalar[-2:] = ["ford","citroen"] # atama yapildi ...

print(arabalar)

arabalar = arabalar + ["Audi","Nissan"] # audi ve nissan ' i listeye ekle ...
print(arabalar)

del arabalar[-3:-1] # arabalarin -3. ve -2. yi sil ...
print(arabalar)

print(arabalar[::-1]) # arabalari tersten yazdirir ...


student = ["Ali Cemil","Ozdemir",18,[85,90,90]]
print("Merhaba {} {} , {} yasindasiniz ...\nnot ortalamaniz : {r:.4}...".format(student[0],student[1],student[2],r = ( student[3][0] + student[3][1] + student[3][2] ) / 3 ))

numbers = [1,3,2,5,4,8]
letters = ["s","j","u","a","q","b"]

print(max(numbers)) # 8
print(min(numbers)) # 1
print(max(letters)) # u
print(min(letters)) # a

numbers.append(0) # dizinin sonuna 0 rakami eklendi ...
print(numbers)

numbers.insert(-1,"eklenti") # -1. indekse "eklenti" eklendi ve -1. indeks -1. indeks oldu(sağa kaydi) ...
print(numbers)

numbers.pop(3) # 3. indeks kaldirildi ...
print(numbers)

numbers = [1,3,2,5,4,8]
letters = ["s","j","u","a","q","b"]

numbers.sort()    # numaralari sirala ...
print(numbers)

letters.sort()    # harfleri sirala ...
print(letters)

numbers.reverse()    # numaralari ters sirala ...
print(numbers)

letters.reverse()    # harfleri ters sirala ...
print(letters)

numbers.clear() #[]
print(numbers)

arabalar = ["mercedes","bmw","tesla","renault"]
print(arabalar.index("tesla")) #2

arabalar = ["mercedes","bmw","tesla","renault"]
print("jasjdnj" in arabalar)    #FALSE
print(arabalar.index("jasjdnj"))    # EXCEPTION

"""

    # tuple ozel bir liste bicimidir oyle ki elemanlari dogrudan degistirilemez ... ancak tuple'in yeniden tanimlanmasi lazim ...
"""

lisst = ["bu","bir","listedir"]
tupple = ("bu","bir","tupledir")
print(lisst)
print(tupple)
lisst[1] = "BIR"
tupple[2] = "TUPLEDIR"     # hata aliriz : 'tuple' object does not support item assignment
print(lisst)
print(tupple)

"""

    # DICTIONARY
"""

plakalar = {"Hatay" : 31 , "Istanbul" : 34 , "Antalya" : 7 }
plakalar["Hatay"] = "New Data"
plakalar["Mersin"] = 33

print(plakalar)


users = {
    "Ali Cemil Ozdemir" : {
        "Name" : "Ali Cemil Ozdemir" ,
        "Birthday" : False, # today is not his birthday
        "Age" : 18,
        "College" : ["BAU",2023], # college and entrance year
        "Mainland" : "Hatay" ,
        "Gender" : True ,# Man 
        "Lives" : "Istanbul"
    },
    "Fevzi Aydin" : {
        "Name" : "Fevzi Aydin" ,
        "Birthday" : True, # today is his birthday
        "Age" : 21,
        "College" : ["YTU",2020], # college and entrance year
        "Mainland" : "Trabzon" ,
        "Gender" : True , # Man
        "Lives" : "Istanbul"
    }
}

print(f"{users['Ali Cemil Ozdemir']["Name"]} got into {users['Ali Cemil Ozdemir']["College"][0]} college at {users['Ali Cemil Ozdemir']["College"][1]}")
******************************************************************************************************************
users = {}
Name = input("Lutfen ogrencinin adini soyadini giriniz...")
Number = input("Lutfen ogrencinin numarasini giriniz...")
Age = int(input("Lutfen ogrencinin yasini giriniz..."))
Gender =bool(input("Lutfen ogrencinin cinsini giriniz...(1 erkek 0 kadin)"))
Lives = input("Lutfen ogrencinin yasadigi sehri giriniz...")
users = {
    Number : {
        "Number" : Number,
        "Name" : Name ,
        "Age" : Age ,
        "Gender" : Gender ,
        "Lives" : Lives
    }
}
print("{} isimli ve {} nolu ogrencinin yasi {}, ve {}'da yasamakta...".format(users[Number]["Name"],users[Number]["Number"],users[Number]["Age"],users[Number]["Lives"]))
***************************************************************************************************************
users = {}
Name = input("Lutfen ogrencinin adini soyadini giriniz...")
Number = input("Lutfen ogrencinin numarasini giriniz...")
Age = int(input("Lutfen ogrencinin yasini giriniz..."))
Gender =bool(input("Lutfen ogrencinin cinsini giriniz...(1 erkek 0 kadin)"))
Lives = input("Lutfen ogrencinin yasadigi sehri giriniz...")
users.update({
    Number : {
        "Number" : Number,
        "Name" : Name ,
        "Age" : Age ,
        "Gender" : Gender ,
        "Lives" : Lives
    }
})
print("{} isimli ve {} nolu ogrencinin yasi {}, ve {}'da yasamakta...".format(users[Number]["Name"],users[Number]["Number"],users[Number]["Age"],users[Number]["Lives"]))

"""

    # ATAMA
"""

liste = 1,2,3,4,5
x , *y ,z = liste

print(x,y,z) # x = 1 , y = [2,3,4] , z = 5

"""

    # Identity operator : is  -  ADDRESS CONTROL
"""

x = y = [1,2,3]
z = [1,2,3]

print( x == y ) # True
print( x == z ) # True
print( y == z ) # True
print( x is y ) # True
print( x is z ) # False

print( y is z ) # False
print( y is not z ) # True

"""

    # Membership operator : in  -  CONTENT CONTROL
"""

x = [ "ali" , "cemil" , "ozdemir" ]

print( "ali" in x ) # True
print( "ali" not in x ) # False

name = "alicemil"
print("a" in name) # True
print("ali" not in name) # False

"""

# import kullanimi ornegi (modul ornegi)
"""

import datetime
guncelTarih = datetime.datetime.now()

cikmaTarihi = input("aracinizin trafige cikma tarihini giriniz : (yil/ay/gun)")
cikmaTarihi = cikmaTarihi.split("/")
cikmaTarihi = datetime.datetime(int(cikmaTarihi[0]),int(cikmaTarihi[1]),int(cikmaTarihi[2]))

if (guncelTarih - cikmaTarihi).days <=365 :
    print("1.servis araligi")
elif (guncelTarih - cikmaTarihi).days > 365 and (guncelTarih - cikmaTarihi).days <= 365*2 :
    print("2.servis araligi")
elif (guncelTarih - cikmaTarihi).days > 365*2 and (guncelTarih - cikmaTarihi).days <= 365*3 :
    print("3.servis araligi")
else : 
    print("hatali veri girisi ...")

"""

    # FOR DONGULERI
"""
list0 = [1,2,3,4,5]
list1 = ["ali","ayse","baris","mert"]
list2 ={"ogrenci1":{"name":"muhammet" , "age":20 , "uni":"YTU"},"ogrenci2":{"name":"ali" , "age":18 , "uni":"BAU"}}
list3 = (1,0,9,1)
list4 = [(1,2,3),(4,5,6),(7,8,9)]
string = "merhaba"
"""

"""
for a,b,c in list4[:2] : 
    print(a,b,c)
"""
"""

for user in list2 :
    print(user.center(40,"*"))
    for info1,info2 in list2[user].items():
        print(f"{info1} : {info2} ")
print("*".center(100,"*"))

for ogrenci in list2 : 
    print(ogrenci.center(40,"*"))
    print(f"Name : {list2[ogrenci]["name"]} \nAge : {list2[ogrenci]["age"]}\nUni : {list2[ogrenci]["uni"]}")
print("*".center(40,"*"))
"""

"""
****************ogrenci1****************
name : muhammet 
age : 20 
uni : YTU 
****************ogrenci2****************
name : ali 
age : 18 
uni : BAU 
****************************************
"""
"""
urunler = [
    {"name":"samsung" , "price":5000} ,
    {"name":"apple" , "price":1000} ,
    {"name":"xiaomi" , "price":3000} ,
    {"name":"oppo" , "price":4000} ,
    {"name":"huawei" , "price":5000} ,
]
"""
    
    # urunlerin fiyatlari toplamini bulmak istiyoruz
    # urunler[0][1] + urunler[1][1] + urunler[2][1]
"""
for counter in urunler : 
    print(counter["price"])
"""
# liste
# tuple
# dictionary
"""
liste = [["ali cemil" , "ozdemir",18,"BAU"],["Baris","Calik",21,"ITU"],["Muhammet Ali","Akyuz",20,"YTU"]]
a = 0
for counter in liste :
    a+=1
    print(f"user{a}".center(40,"*"))
    print(f"name : {counter[0]}\nsurname : {counter[1]}\nage : {counter[2]}\nUni : {counter[3]}")
print("*".center(40,"*"))
"""
    
    # range() fonksiyonu ...
"""

for item in range(10,21,2) :    # range metodu liste olusturur...
    print(item) # 10 12 14 16 18 20
print(list(range(10,21,2)))    #[10, 12, 14, 16, 18, 20]

"""
    
    # enumerate() fonksiyonu ...
"""

greeting = "Hello"
for counter in enumerate(greeting) : # her bir string karakterini bir indeks ile eslestirir ...
    print(counter)
    # cikti :
    # (0, 'H')
    # (1, 'e')
    # (2, 'l')
    # (3, 'l')
    # (4, 'o')
for counter,value in enumerate(greeting) :
    print(counter,":",value)

"""

    # zip() fonksiyonu ...
"""

list1 = [120,123,124,125,126]
list2 = ["a","b","c","d","e"]
print(list(zip(list1,list2))) # [(120, 'a'), (123, 'b'), (124, 'c'), (125, 'd'), (126, 'e')]
for count in zip(list1,list2) :
    print(count)
# cikti
# (120, 'a')
# (123, 'b')
# (124, 'c')
# (125, 'd')
# (126, 'e')

"""

    # LIST COMPREHENSION
"""

list = [f"{x}:cift" if x%2 == 0 else f"{x}:tek" for x in range(0,10)]
print(list) # ['0:cift', '1:tek', '2:cift', '3:tek', '4:cift', '5:tek', '6:cift', '7:tek', '8:cift', '9:tek']

list = [f"{x}:cift" for x in range(0,10) if x%2 == 0]
print(list) # ['0:cift', '2:cift', '4:cift', '6:cift', '8:cift']

myString = "Ali Cemil"
myList = [x if(x !=" ") else "-" for x in myString]
print(myList) # ['A', 'l', 'i', '-', 'C', 'e', 'm', 'i', 'l']

wasBorn = [2005,2001,2003,2002,1975,1976,1960]
ages = [2023-year for year in wasBorn]
print(ages) # [18, 22, 20, 21, 48, 47, 63]
list = [(x,y) for x in range(2) for y in range(2) ]
print(list) # # [(0, 0), (0, 1), (1, 0), (1, 1)]

"""
"""
random sayi uret...

kullanici kac denemede bulabilecegini soylesin ...

denemelere baslasin ...

her yanlis denemede 5 puan dusur totalden ...

eger tahminini gecerse 10 puan dusur ...

"""

    # Rasgele sayiyi bulma oyunu ...
"""

import random
sayi = random.randint(1,1000000)
point = 105
print("\n")
print("SAYI BULMA OYUNUMUZA HOS GELDINIZ".center(70,"*"))
denemeSayisi = int(input("\nSayiyi kac denemede bulabileceginizi dusunuyorsunuz  ( her deneme 5 puan goturur) : "))
print("\nHer yanlis tahmin 5 dusurur ... Tahmin sayisi asilirsa her yanlis 10 puan goturur...\n")
counter = 0
while True :
    if counter >0:
        print(f"GUNCEL PUANİNİZ ... {point}")
    girdi = int(input(f"\n{counter+1}.tahmininiz :"))
    counter += 1
    if girdi == sayi :
        if counter <= denemeSayisi :
            point -= 5
        else :
            point -= 10
        print(f"\ntebrikler, sayiyi buldunuz ...Puaniniz : {point}")
        break
    else :
        if girdi < sayi :
            print("\narttir...")
        else :
            print("\nazalt...")
        if counter <= denemeSayisi :
            point -= 5
        else :
            point -= 10
    if point < 0 :
        print("\nbasarisiz oldunuz...")
        break

"""
    
    # FONKSIYONLAR
"""

def sayHello(name = "user") : # eger herhangi bir deger girilmediyse name = "user" al
    return("Welcome "+name.title())

print(sayHello("ALI CEMIL")) # Welcome Ali Cemil
def x() :
    print(10)
print(print(print(10))) # print return donduren bir fonksiyon degildir ... OUTPUT : 10 None None


def sayHello() :
    ""
    DOCSTRING:this function returns 'hello' str.
    INPUT : NONE
    OUTPUT : HELLO
    ""
    return "hello"
help(sayHello)    # OUTPUT : 
#Help on function sayHello in module __main__:

# sayHello()
#     this function returns 'hello' str.

def change0(w0) :
    w0 = "degisti"
    return w0
word = "degismedi"
print(change0(word))
print(word) # word ve w0 birbirinden etkilenmedi , veriler kopyalandi adresler farkli ...

def change1(w1) :
    w1[0] = "degisti"
    return w1
words = ["ali","cemil"]
print(change1(words))
print(words) # words ve w1 birbirinden etkilendi , veriler kopyalanmadi adresler ayni ...

# OUTPUTS:
#   degisti
#   degismedi
#   ['degisti', 'cemil']
#   ['degisti', 'cemil']
words = ["ali","cemil"]
change1(words[0:2]) # (slicing)words un elemanlarini teker teker w1'e kaydeder , adres esitlemesi yapmaz , words ve w1 birbirinden bagimsiz ...
print(words) # ['ali', 'cemil'] degisiklik yok ...

def add(a=0,b=0,c=0) : # max 3 sayiyi toplayan program ...
    return sum((a,b,c))
print(add(10,5))

def topla(*elemanlar) : # elemanlar bir listedir ...
    return sum(elemanlar) # sum ' in girdileri de bir listedir dolayisiyla dogrudan yazilabilir...
print(topla(10,7,8,92,85)) # 202

def selamla(ad,soyad,**digerBilgiler) :
    print(f"merhaba {ad} {soyad}:\nBilgilerin...\n")
    for x,y in digerBilgiler.items() :
        print(f"{x} : {y}\n")
selamla("Ali Cemil","Ozdemir", Okul = "BAU" , Memleket = "Hatay", Yas = 18)

def func(ad,soyad,*args,**kwargs) :
    print(ad) # ali
    print(soyad) # ozdemir
    print(yasMemleket) # (18, 'Hatay')
    print(sozluk) # {'Okul': ' BAU', 'Gozluk': True}
func("ali","ozdemir",18,"Hatay",Okul = " BAU",Gozluk = True )
"""
# def kelimeYazdir( kelime , sayi ) :
    # 1. cozum ...
#     for x in range(0,sayi) :
#         print(kelime)
    # 2. cozum ...
#    return ( ( kelime + "\n" ) * sayi )
# kelimeYazdir("nothing can stop me i'm all the way up...\n",6)

# liste = []
# while True :
#     girdi = input("parametre : ")
#     if(girdi != "EOF") :
#         liste.append(girdi)
#     else :
#         break
# print(liste)

# girdi1 = int(input("ilk sayiyi giriniz..."))
# girdi2 = int(input("ikinci sayiyi giriniz..."))

# def asalmi(sayi0) :
#     checkAsalmi = True
#     for x in range(2,sayi0) :
#         if(sayi0 % x == 0) :
#             checkAsalmi = False
#             break
#     return checkAsalmi

# checkAsalVarmi = False
# if girdi1 < girdi2 :
#     min = girdi1
#     max = girdi2
# elif girdi1 > girdi2 :
#     min = girdi2
#     max = girdi1
# else :
#     print("ayni sayilari girdiniz...")
#     quit()
# counter = min
# while(counter < max-1) :
#     counter += 1
#     if asalmi(counter) :
#         print(counter)
#         checkAsalVarmi = True
# if not(checkAsalVarmi) :
#     print("Asal sayi bulunamadi...")
"""
def bolenler(sayi) :
    liste = []
    counter = 0
    for x in range(1,sayi+1):
        if sayi % x == 0:
            liste.append(x)
            liste.append(-x)
            counter += 2
    liste.sort()
    return liste,"bolen sayisi:" + str(counter)
print(bolenler(27))
"""
    
    # map() function

"""def square(num) : return num**2 # tek satirda yanyana yazilabilir ..."""
"""bir listedeki her elemanin karesini almak istiyoruz..."""
"""
liste = [2,5,10,13,7]
result = map(square,liste) # # result un adresiyle map in adresi farkli o yuzden ...

print(f"result : {result}") # result : <map object at 0x0000022585256140>
print(liste,"**2 = ",list(result)) # [2, 5, 10, 13, 7] **2 =  [4, 25, 100, 169, 49]
print(map(square,liste))  # <map object at 0x0000022585256230>
print(type(result)) # <class 'map'>
"""
"""
for item in result : # # result tan okuma yapilamiyor ...
    print(item)
"""
"""
for item in map(square,liste) : # # bu sekilde yapilabiliyor ...
    print(item) 
"""
# 4
# 25
# 100
# 169
# 49

    # lambda expressions
"""
numbers = [4,10,23,5,8]
result = map(lambda num : num**2 , numbers) # lambda fonk. tanimlamadan fonk islemi gorur ...
print(list(result)) # [16, 100, 529, 25, 64]
# kolay yoldan fonk olusturma ...
sq = lambda num : num**2
print(sq(5)) # 25
result = map(sq , numbers)
print(list(result)) # [16, 100, 529, 25, 64]
"""

    # filter() function
"""
array = [12,8,4,6,9] # indeks numarasi tek olanlarin karesini alip ekrana yazdiracagiz ...
def indeksKontrol(num):
    return array.index(num) % 2 != 0 # eger indeks tekse TRUE return yapar ...
""print(list(map(lambda num : num**2,list(filter(indeksKontrol,array)))))""
print(filter(lambda num : array.index(num) != 0 ,array)) # <filter object at 0x00000192AB915F00>
print(list(filter(lambda num : array.index(num) % 2 != 0 ,array))) # [8, 6] tek indexliler...
"""
"""
liste = ["bu","buyulu","bir","mesajdir"]
#listenin her bir elemanini center metoduyla duzenlicem ...
liste = list(map(lambda word : word.center(11,"*") , liste))
for ayrim in liste :
    print(ayrim)
"""

    # global on eki
"""
x = 10

def plus1():
    global x
    x += 1
    return x

print("plus1:",plus1()) #plus1: 11
print("x:",x) #x: 11
"""
    # pass keyword'u
if 5<10 : pass # bos ifadeyi gecmeyi saglar ...

    # OBJECT-ORIENTED PROGRAMMING
# class
"""
class Lesson :
    # class attributes 
    # - bunlar sabir degerlerdir ve her obje icin gecerlidir...aksi belirtilmedigi surece...
    city = "Istanbul"
    education = "Bachelor"
    # constructor (yapici metof)
    def __init__(self,name,surname,university,age,dormOrHouse) :
    # object attributes
        self.name = name
        self.surname = surname
        self.university = university
        self.age = age
        self.dormOrHouse = dormOrHouse
    # methods -- su an eklenmedi
#object (instance)
alicemil = Lesson("Ali Cemil","Ozdemir","BAU",18,"Dorm")
print(alicemil) # <__main__.Lesson object at 0x00000298F92F6150>
"""
#methods
"""
class Circle :
    PI = 3.141519
    def __init__(self,yaricap) :
        self.r = yaricap
    def cevreHesapla(self) : # self eklenmezse o fonk , obje tarafindan cagrilamaz ...
        return 2 * self.r * self.PI
    def alanHesapla(self) :
        return self.PI * self.r**2
c1 = Circle(10)
print(c1.cevreHesapla())# 62.830380000000005
print(c1.alanHesapla()) # 314.1519
c1.__init__(5) # bu metodla degiskenlerin icerikleri tekrardan ayarlanabilir ...
print(c1.cevreHesapla()) # 31.415190000000003
print(c1.alanHesapla()) # 78.537975
"""

    # Inheritance ( Miras Alma )
"""

class Person :

    country = "Turkiye"

    def __init__(self,name,surname,city,birthyear):
        self.name = name
        self.surname = surname
        self.city = city
        self.birthyear = birthyear
    
    def findAge(self) :
        return 2023 - self.birthyear
    
    def greeting(self) :
        print(f"Merhaba {self.name} {self.surname} bu metod , person class'indan seni selamlamak icin cagirilmistir...")


class Student(Person) :
    def __init__(self, name, surname, city, birthyear,uni,stayIn,rentalFee):
        # 1. ulasma sekli ...
        super().__init__(name, surname, city, birthyear)
        
        # 2. ulasma sekli ...
        # Person.__init__(self,name,surname,city,birthyear)
        
        self.uni = uni
        self.stayIn = stayIn
        self.rentalFee =rentalFee
    
    def annuallyRF(self) :
        return 9 * self.rentalFee
    # ayni isimli bir metod persondakini ezer . buna OVERRIDE denir...
    def greeting(self):
        print(f"Merhaba {self.name} {self.surname} bu metod , student class'indan seni selamlamak icin cagirilmistir(overriding yapildi...)")
alicemil = Student ("Ali Cemil" , "Ozdemir" , "Istanbul" , 2005 , "BAU" , "Bagcilar" , 1300)
print(alicemil.annuallyRF())
alicemil.greeting()

"""

    # OOP : SPECIAL METHODS - Standart Kutuphane Fonksiyonlarinin Class'ta hangi degeri dondurecegine karar veriyoruz ...
# python special method list yazip intte arastir ali cemil ...
"""

class Telefon :
    def __init__(self,marka,fiyat,uzunluk) :
        self.marka = marka
        self.fiyat = fiyat
        self.uzunluk = uzunluk
    def __len__(self) :
        return self.uzunluk
    def __str__(self) :
        return f"Telefon class...{self.marka} telefonunuzun fiyati {self.fiyat}'tir..."
    def __del__(self) : # kod sonlandiginda obje otomatik olarak bellekten silinir ( bu metod calistirilarak )
        print("obje silindi...")
A20 = Telefon("Samsung A20",13500,20)
print(len(A20))

"""

    # Modules
# 1. import etme metodu
"""
import math as islem # math kutuphanesi kullaniminda math on eki yerine islem on ekini kullanacaz

functions = dir(islem) # list tipinde fonk isimleri
# for x in functions :
#     print(x)

# print(help(math.cos))
# print(islem.cos(islem.pi*2))

"""
# 2. import etme metodu
"""
from math import * # butun math fonklari import edilir , dolayisiyla islem on eki kullanilmaz ...
print(ceil(8.9)) # 9
from math import ceil,floor,sqrt,sin,pow # sadece yanda belirtilen fonksiyonlar import edildi ...
print(pow(3,5)) # 243.0

"""

# sqrt fonksiyonu hem import edilsin hem de biz sqrt isimli fonk yazalim ... hangisi kullanilir ? asagida import varsa dahil edilen fonk kullanilir , asagida def'li sqrt fonk ifademiz varsa o kullanilir ... hangisi daha sonra tanimlanmissa o ...
"""
def sqrt() :
    print("ezemediniz")
"""
"""
from math import sqrt
def sqrt(x) :
    return "ezdiniz math.sqrt()'yi ..."

print(sqrt(9)) # ezdiniz math.sqrt()'yi ...

"""
    # random modulu
"""
import random as rand

print(rand.random()) # 0 ile 1 arasinda rasgele float uretir ...
print(rand.uniform(0,2)) # 0 ile 100 arasinda float uretir ...
print(rand.randint(0,1)) # 1 de dahil...

liste = [1,2,3,4,5] # range(1,5)
print(rand.choice(liste)) # listeden(stringte olabilir) rasgele bir eleman secer ...

liste = list(range(20)) # 0,1,2,3,4,5,6,7,8,9,10 ...
rand.shuffle(liste) # listedeki elemanlari karistirir saglar ...
print(liste) # [6, 14, 10, 11, 8, 1, 12, 7, 16, 5, 9, 15, 18, 0, 19, 2, 17, 3, 4, 13]

result = [True,False,0]
print(rand.sample(result,2))
"""

#       Error
##################################################
# print(a) NameError - a henuz tanimlanmadi ...
# int("12a") ValueError - 12a bir tamsayiyi temsil etmez ...
# print(19/0) ZeroDivisionError - 0 ' a bolme hatasi ...
# print("denem"e) SyntaxError - sozdizimi hatasi , python da boyle bir kullanim yok ...

# Error handling
"""
try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(f"sonuc : {x/y}")
except ZeroDivisionError:
    print("Bolen sayi 0 olamaz..")
except ValueError :
    print("Uygunsuz karakter girisi...")
except KeyboardInterrupt:
    print("Hatali klavye tuslamasi...")
else :
    print("dogru giris ...")
"""
##################################################
"""
try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(f"sonuc : {x/y}")
except (ZeroDivisionError,ValueError,KeyboardInterrupt) as hata :
    print("Hatali tuslama ...",hata)
"""
##################################################
"""
while True :
    try: # baslangicta dogrudan calistirilir ...
        x = int(input("x : "))
        y = int(input("y : "))
        print(f"sonuc : {x/y}")
    except Exception as hataKodu: # Hata var ise calistirilir ...
        print("Hatali giris...","Hata kodunuz :",hataKodu,"\n")
    except KeyboardInterrupt : # KeyboardInterrupt var ise calistirilir ...
        print("Klavye tuslama hatasi...")

    else : # except calismamissa calistirilir ...
        print("dogru giris ... dongu sonlandirildi...")
        break
    finally : # try except'ten cikildigi gibi calistirilir ... ister hatali giris olsun ister basarili giris , mutlaka calistirilir ...
        print("Finally blogu calistirildi ...")
"""
####################################################
"""
def checkPassword(psw) :
    import re
    # en az 8 karakter
    # icinde buyuk, kucuk harfler , sayilar , semboller olacak ...
    if len(psw) < 8 :
        raise Exception("Parola en az 8 sayidan olusmalidir...")
    elif not re.search("[a-z]",psw) :
        raise Exception("Lutfen sifrenizde kucuk harf bulunsun...")
    elif not re.search("[0-9]",psw) :
        raise Exception("Lutfen sifrenizde rakam bulunsun...")
    elif not re.search("[A-Z]",psw) :
        raise Exception("Lutfen sifrenizde buyuk harf bulunsun...")
    elif not re.search("[!_'+%&/(=?)>£#$½{}|]",psw) :
        raise Exception("Lutfen sifrenizde sembol bulunsun...")
    elif re.search(" ",psw) :
        raise Exception("Lutfen sifrenizde bosluk bulunmasin...")
        #hata kodunun altinda yazilan kodlar islevsizdir...
    else :
        print("Sifreniz basariyla olusturulmustur...")

while True:
    # password = input("sifre giriniz...")
    try :
        password = input("sifre giriniz...")    
        checkPassword(password)
    except Exception as ex:
        # 1.yol :
        # checkPassword(password)
        # 2. yol :
        print(ex)
    else : 
        print("Hata yok(else blogu...)")
        break
    finally:
        print("finally blogu calistirildi...")
"""
"""
class Applicant:
    def __init__(self,city,age) :
        if city.lower() != "istanbul" :
            raise Exception("Istanbul disindan basvuru alinmamaktadir...")
        elif 18>age or 25<age :
            raise Exception("Basvuru icin 18 ile 25 yaslari arasinda olmaniz gerekiyor...")
        else : 
            self.city = city
            self.age = age
            print("Basvurunuz icin bir engel bulunmamaktadir...")
            name = input("Adinizi giriniz...")
            surname = input("soyadinizi giriniz...")
            uni = input("okulunuzu giriniz...")
            print("Basvurunuz basariyla olusturulmustur...")
AliCemil =Applicant("ISTANBUL",25)
"""

    # Bir listedeki tamsayilari bulma...
"""

liste = ["1","2","5a","10b","abc"]
tamsayilar = []
for eleman in liste :
    try :
        tamsayiMi = int(eleman)
        tamsayilar.append(tamsayiMi)
    except :
        pass
print(tamsayilar)

"""

    # kullanici q degerini girene kadar input al ... Tamsayi girmezse hata mesaji ver ...
"""

while True :
    try :
        girdi = input("Lutfen bir sayi giriniz...Durmak icin q'ya basin...")
        if girdi != "q" :
            girdi = int(girdi)
        else:
            print("Tebrikler basariyla kod durduruldu...")
            break
    except ValueError :
        raise Exception("amin evladi sayi gir...")
    else :
        print("Tebrikler tamsayi girdiniz...")

"""

    # bir parola buradan girilecek ve icinde turkce karakter varsa turkce karakter hatasi verilecek ...
"""

psw = input("Lutfen parola olusturunuz : ")
def parolaKontrol(psw) :
    import re
    if re.search("[ığüşöç]",psw) :
        raise Exception("Lutfen parolada turkce karakter kullanmayiniz...")
    else :
        print("Tebrikler sifreniz basariyla olusturuldu...")
try :
    parolaKontrol(psw)
except Exception as yazdir:
    print(yazdir)

"""

    # bir tamsayinin faktoriyelini bulan ve hata uyarilari bulan fonksiyon...
"""
def faktoriyel(sayi) :
    carpim = 1
    if type(sayi) == type(1) :
        if sayi >= 0 :
            if not(sayi == 0 or sayi ==1) :
                for sayac in range(1,sayi+1) :
                    carpim *= sayac
        else :
            raise Exception("Negatif tamsayilarin faktoriyeli bulunamaz...")
    else :
        raise Exception("Lutfen bir tamsayi giriniz...")
    return carpim

try :
    print(faktoriyel(a))
except Exception as hata :
    print(hata)
"""
# import ex1
# def personelEkle() :
#     ad,soyad,yas,pozisyon,maas,girisYili
#     ad = input("Lutfen Personelinizin adini giriniz ...")
#     soyad = input("Lutfen Personelinizin soyadini giriniz ...")
#     yas = input("Lutfen Personelinizin yasini giriniz ...")
#     pozisyon = input("Lutfen Personelinizin pozisyonunu giriniz ...")
#     maas = input("Lutfen Personelinizin maasini giriniz ...")
#     girisYili = input("Lutfen Personelinizin giris yilini giriniz ...")
#     personel = ex1.Personel(ad,soyad,yas,pozisyon,maas,girisYili)
#     return personel
# uyeler = []
# while True :
#     a =int(input("Personellerle ilgili bilgilere ulasmak icin 1'i\nYeni personel eklemek icin 2'yi tuslayiniz..."))
#     if a == 2:
#         uyeler.append(personelEkle())
#     if a == 1 :
#         print(str(uyeler))

    # DOSYA ISLEMLERI ...
"""
dosya acmak ve olusturmak icin open(dosya_adi , dosya_erisme_modu) fonksiyonu kullanilir...

"w" : (Write) yazma modu . yazi varsa siler , kendi write metodundakini ekler... Dosya konumda yoksa olusturur...
"a" : (Append) ekleme modu . var olan yaziyi silmez, write metodundakini yaziyi ekler... Dosya konumda yoksa olusturur...
"x" : (Create) olusturma modu . Dosya varsa hata verir...
"r" : (Read) okuma modu . dosya konumda yoksa hata verir

"""         

# w modu ile yazi yaziliyor... yazi varsa siler , kendi write metodundakini ekler...
# adres yazilmazsa bu py dosyasi ile ayni dizinde olusturulur...
"""
file = open("C:/Users/alice/desktop/Deneme.txt" , "w" , encoding="utf-8")
file.write("Ali Cemil Özdemir2")
file.close()
"""

# a modu ile yazi yazalim ... dosyaya yazi ekler...
"""
file = open("C:/Users/alice/desktop/Deneme.txt" , "a" , encoding="utf-8")
file.write(" Merhaba")
file.write(" benim")
file.write(" adim")
file.write(" Ali")
file.write(" Cemil.")
file.close()
"""

# a modu ile dosya okuma ...
""" try :"""
    # kod
"""
    file = open("C:/Users/alice/desktop/Deneme.txt","r",encoding="utf-8")
    """
    # kod
"""
    for x in file : # her bir harfi degil her bir satiri tarar
        print(x,end = "") # end print'in bos satir ekleme ozelligini onler ...
    file.close()
    """
    # kod
"""
    okuma1=file.read()
    print("okuma1:\n",okuma1) # dosyayi okur ...
    okuma2 =file.read()
    print("okuma2:\n",okuma2)
    """
    # output
"""
    okuma1:
    Merhaba Bu bir metin dosyasidir...
    okuma2:
    """
    # okuma yapilmamasinin sebebi 1. okumayla imlec sona geldi ... okuma yap dedigimizde(okuma2) imlec sonda oldugu icin okuyacak bir sey bulamiyor...
    # cozum : imleci tekrar basa almak (dosyayi tekrar acmak...)
"""
    file = open("C:/Users/alice/desktop/Deneme.txt","r",encoding="utf-8")
    okuma1=file.read()
    print("okuma1:\n",okuma1) # dosyayi okur ...
    file = open("C:/Users/alice/desktop/Deneme.txt","r",encoding="utf-8")
    okuma2 =file.read()
    print("okuma2:\n",okuma2)
    """
    # output
"""
    okuma1:
    Merhaba Bu bir metin dosyasidir...
    okuma2:
    Merhaba Bu bir metin dosyasidir...
    """
""" except :
    print("Dosya Bulunamadi...")"""
# read fonk ozellik :
"""
file = open("C:/Users/alice/desktop/Deneme.txt","r",encoding="utf-8")
content = file.read(5) #merha
content = file.read(3) #ba
content = file.read(4) #bu b
print(content) #bu b
"""
#readline() fonk
"""
file = open("C:/Users/alice/desktop/Deneme.txt","r",encoding="utf-8")
print(file.readline(),end = "")
print(file.readline(),end = "")
print(file.readline(),end = "")
print(file.readline(),end = "")
print(file.readline(),end = "")
print(file.readline(),end = "")
print(file.readline(),end = "")
print(file.readline(),end = "")
print(file.readline(),end = "")# okunacak sey olmadiginda okumaz...
"""
#output
"""
Merhaba Bu bir metin dosyasidir... satir = 1
Merhaba Bu bir metin dosyasidir... satir = 2
Merhaba Bu bir metin dosyasidir... satir = 3
Merhaba Bu bir metin dosyasidir... satir = 4
Merhaba Bu bir metin dosyasidir... satir = 5
"""
# readlines() fonk
"""
file = open("C:/Users/alice/desktop/Deneme.txt","r",encoding="utf-8")
print(file.readlines()) # readlines fonk bir liste dondurur
# imlec mantigi burda da gecerli bu satirin ustundeki ve altindaki kodu birlikte calistirmaya kalkarsak hata aliriz...
oku = file.readlines()
print(oku[0]) #Merhaba Bu bir metin dosyasidir... satir = 1
file.close()
"""
#output : imlec mantigi yorumunun ustu icin...
"""
['Merhaba Bu bir metin dosyasidir... satir = 1\n', 'Merhaba Bu bir metin dosyasidir... satir = 2\n', 'Merhaba Bu bir metin dosyasidir... satir = 3\n', 'Merhaba Bu bir metin dosyasidir... satir = 4\n', 'Merhaba Bu bir metin dosyasidir... satir = 5'] 
"""
# alternatif dosya acma kapama ifadesi :
    # standart olan :
"""
file = open("C:/Users/alice/desktop/deneme.txt","r",encoding="utf-8")
file.close()
"""
    # alternatif :
"""
with open("C:/Users/alice/desktop/deneme.txt","r",encoding="utf-8") as file :
    content = file.read() # with blogu okunduktan sonra dosya otomatik olarak kapatilir...
    print(content)
"""
# Dosya Islem Fonksiyonlari ...
"""
with open("C:/Users/alice/desktop/deneme.txt","r",encoding="utf-8") as file :
    content = file.read(10)
    print(content) #0123456789
    file.seek(2) # imleci baslangictan 2 adim saga kaydirir...
    print(file.tell()) # imlecin yerini soyler(ustte 2 ol demistik) output:2
    content2 = file.read(10) # imlecin kaldigi yerden 10 byte(karakter) okur...
    print(content2)#23456789ab
"""
"""

    # github ' a hazirla ...

# python ile siparis uygulamasi yapacagiz...
# degiskenler : musteriAdi , siparisAdi , siparisUcreti , siparis teslimEdildi_Mi , siparisNo
# ilk once dosyada siparis numarasini yazdiriyoruz ... aksi takdirde kod calismaz ... kodun kaburgasi siparis no
with open("C:/Users/alice/desktop/siparis.txt","r",encoding="utf-8") as file :
    kontrol_siparisNo =file.read()
    kontrol_siparisNo.lower()
    if kontrol_siparisNo.find("siparis no:") == -1 and kontrol_siparisNo.find("siparis no :") == -1 :
        with open("C:/Users/alice/desktop/siparis.txt","w",encoding="utf-8") as file :
            file.write("siparis no : 0")
ilkIslem = int(input("0 ) Siparis ekle \n1 ) Teslim edilen siparis gir\n2 ) Siparisleri goruntule\n..."))
# siparisleri goruntule guncel olanlari ve teslim edilenleri seklinde 2'ye ayrilacak ...
if ilkIslem == 0 :
    # siparis eklenecek...
    musteriAdi = input("musteri adi bilgisi : ")
    siparisAdi = input("siparis bilgisi : ")
    siparisUcreti = input("ucret bilgisi : ")
    teslimEdildi_Mi = False
    with open("C:/Users/alice/desktop/siparis.txt","r",encoding="utf-8") as file :
        siparisNo = file.readlines() # her satiri kopyalar
        siparisNo = siparisNo[0]

        if siparisNo.find("siparis no:") != -1 :siparisNo = siparisNo.split()[2]
        else : siparisNo = siparisNo.split()[3]
        
        siparisNo = int(siparisNo)
    siparisNo += 1
    # tum veriler alindi simdi kaydetme islemi basliyor ...
    with open("C:/Users/alice/desktop/siparis.txt","r+",encoding="utf-8") as file :
        file.seek(0)
        file.write("siparis no : "+str(siparisNo)+"\n")
    with open("C:/Users/alice/desktop/siparis.txt","a",encoding="utf-8") as file :
        musteriAdi = musteriAdi.center(20)
        siparisAdi = siparisAdi.center(30)
        siparisUcreti = siparisUcreti.center(5)
        teslimEdildi_Mi = "Teslim edilmedi"
        file.write("\n"+str(siparisNo) + " | ")
        file.write(musteriAdi + " | ")
        file.write(siparisAdi + " | ")
        file.write(siparisUcreti + " | ")
        file.write(teslimEdildi_Mi + " | ")
elif ilkIslem == 1:
    with open("C:/Users/alice/desktop/siparis.txt","r",encoding="utf-8") as file : # siparisleri goruntule
        print(file.read())
    teslimEdilenSiparis = int(input("teslim edilen siparisin siparis numarasini giriniz : "))
    with open("C:/Users/alice/desktop/siparis.txt","r",encoding="utf-8") as file :
        duzenleme = file.readlines()
        duzenleme0 = duzenleme[teslimEdilenSiparis+1]
        TeslimIndeksi = int(duzenleme0.index("Teslim"))
        duzenleme0 = duzenleme0[:TeslimIndeksi-1]+" Teslim edildi " + duzenleme0[TeslimIndeksi+15:]
        duzenleme[teslimEdilenSiparis+1] = duzenleme0
        duzenleme = map(lambda girdi : girdi.strip() , duzenleme)
        duzenleme="\n".join(duzenleme)
    with open("C:/Users/alice/desktop/siparis.txt","w",encoding="utf-8") as file :
        file.write(duzenleme)
elif ilkIslem == 2: # detaylandiracagiz...
    with open("C:/Users/alice/desktop/siparis.txt","r",encoding="utf-8") as file :
        print(file.read())

"""
    # ic ice fonksiyonlar :
#1
"""
def faktoriyel(sayi) :
    if not isinstance(sayi , int) :
        raise TypeError("Lutfen integer 1 deger giriniz...")
    elif sayi < 0 :
        raise ValueError("Sayi yalnizca pozitif ya da sifir olabilir...")
    else :
        def faktoriyel_inner(sayi) :
            if sayi <= 1 :
                return 1
            else :
                return sayi * faktoriyel_inner(sayi - 1)
        return faktoriyel_inner(sayi)
try :
    print(faktoriyel(2))
except Exception as hata :
    print(hata)
"""
#2
"""
def usalma(number) :
    def inner(power):
        return number ** power
    return inner
print(usalma(3)(2)) # 3 ** 2 = 9
"""
# 3
"""
def hesapla(islem) :
    def topla(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carp(*args) :
        carpim = 1
        for i in args :
            carpim *= i
        return carpim
    if islem =="topla" :return topla

    if islem =="carp" :return carp

print(hesapla("topla")(1,4,5,46,84))
print(hesapla("carp")(3,8,9,5))
"""
#decorator fonksiyonlar
"""
def my_decorator(func) :
    def wrapper(name) :
        print("fonktan onceki islemler")
        func(name)
        print("fonksiyondan sonraki islemler")
    return wrapper

@my_decorator  # @operatoru fonksiyonu islemlere sokuyor...
def sayHello(namse) :
    print("hello",namse)
sayHello("wlii")
"""
"""
import math
import time

def zamanHesapla(fonk):
    def inner(*args) :
        basla = time.time()
        time.sleep(1)
        fonk(*args)
        bitir = time.time()
        print("fonksiyon",(bitir-basla),"saniyede calisti")
    return inner

@zamanHesapla
def toplama(*args) :
    toplam = 0
    for x in args :
        toplam +=x
    print(toplam)
toplama(5,7,17,8547,5)
"""
"""
import time

def Baslangic(funk) :
    def inner(*args) :
        print("merhaba alicemil ozdemir...")
        print("isleminizin sonucu : ")
        baslangicSaniyesi = time.time()
        funk(*args)
        time.sleep(1)
        bitisSaniyesi = time.time()
        print("isleminiz " + str(-baslangicSaniyesi+bitisSaniyesi-1) + " saniye surdu...\n")
    return inner

@Baslangic
def toplama(*args) :
    toplam = 0
    for x in args :
        toplam += x
    print(toplam)

@Baslangic
def carpma(*args) :
    carpim = 1
    for x in args :
        carpim *= x
    print(carpim)

@Baslangic
def faktoriyel(parametre) :
    carpim = 1
    for x in range(1,parametre+1) :
        carpim *= x
    print(carpim)

toplama(5,-7,8,9,14,-85)
faktoriyel(1357)
carpma(5,8,95,4,75,798)
"""
# iterators ...
"""liste = [1,2,3,4,5]
iterator = iter(liste)"""

"""print(iterator) #<list_iterator object at 0x000001E4130A59C0>"""
"""print(next(iterator)) #1
print(next(iterator)) #2
print(next(iterator)) #3
print(next(iterator)) #4
print(next(iterator)) #5
print(next(iterator)) #StopIteration - exception"""

"""print(next(liste)) # TypeError: 'list' object is not an iterator"""
"""class myNumbers:
    def __init__(self,start,stop) :
        self.start=start
        self.stop=stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<=self.stop :
            x = self.start
            self.start+=1
            return x
        else :
            raise StopIteration
list = myNumbers(2,14)
iterator1 = iter(list)
print(next(iterator1))"""
# generators
"""
def cube() :
    for i in range(5) : #4 e kadar...
        yield i**3
generator = cube()
print(generator) # <generator object cube at 0x0000022326954A00>
print(next(generator)) #0
print(next(generator)) #1
print(next(generator)) #8
print(next(generator)) #27
print(next(generator)) #64
print(next(generator)) # StopIteration
"""
"""
generator = (i**3 for i in range(5)) # basit generator olusturma yolu...
print(generator) # <generator object <genexpr> at 0x0000018E912D3780>
for x in generator :
    print(x)
"""
###################################################################################################################
