def menu():
    print("\33[1;34;40m ")
    print("╔═════════════════════════════════════╗")
    print("║\33[36m    REHBER UYGULAMASI               \33[0m\33[1;34;40m ║")
    print("║═════════════════════════════════════║")
    print("║\33[36m   1-)  Rehbere Ekle              \33[0m\33[1;34;40m   ║")
    print("║\33[36m   2-)  Numaraları Listele          \33[0m\33[1;34;40m ║")
    print("║\33[36m   3-)  Numaraları Sil             \33[0m\33[1;34;40m  ║")
    print("║\33[36m   4-)  Numaraları Değiştir         \33[0m\33[1;34;40m ║")
    print("║\33[36m   5-)  Okuma             \33[0m\33[1;34;40m           ║")
    print("║\33[36m   Seçiminizi Giriniz          \33[0m\33[1;34;40m      ║")
    print("╚═════════════════════════════════════╝")
    secim=input("Lütfen seçiminizi giriniz: ")
    if secim == "1":
        try:
            rehbereEkle()
        except:
            print("dosya bulunamadı")
    if secim== "2":
        listele()

    if secim== "3":
        numaraSil()

    if secim=="5":
        oku()
    
def rehbereEkle():
    dosya = open("rehber.txt","a")
    
    ad =    input("Ad    : ")
    soyad = input("Soyad : ")
    telefon= input("Numara: ")
    yazilacak = {"ad":ad,"soyad":soyad,"numara":telefon}
    dosya.write(str(yazilacak)+"\n")

    menu()
    dosya.close()

def listele():
    try:
        dosya = open("rehber.txt","r")
        print("   Rehber Kayıt Listesi ")        
        print("═════════════════════════════")
        a = 1        
        kayit = {}
        for k in dosya.readlines():
            kayit = k
            print(k)
          
            a += 1
    except:
        print("Dosya bulunamadı.")
        print("Devam etmek için Enter'a basın.")
        input()


def numaraSil():
    isim = input("Numarasını silmek istediğiniz kişinin ismini giriniz: ")
    dosya=open("rehber.txt","a+")
    dosya.seek(0)
    satirlar=dosya.readlines()
    rehber=[]
    rehber_yeni = [] # yeni bir liste tanımla
    for satir in satirlar:
        kisi=satir.split("\n") # split fonksiyonuna ayırıcı parametresi ver
        rehber.append(kisi)
    for kisi in rehber:
        if kisi[0] == isim:
            # rehber.remove(kisi) # rehber listesini değiştirme
            print("Numara başarıyla silindi.")
        else:
            rehber_yeni.append(kisi) # silmek istemediğin kişileri yeni listeye ekle
    dosya.close() # dosyayı kapat
    menu() # menüye geri dön
    return # fonksiyondan çık







def oku():
    print("\nPozisyon Bilgisi")
    dosya=open("rehber.txt","r")
    parca= dosya.read(5)
    print("1.okunan:",parca)
    pozisyon=dosya.tell()
    print("şu anki pozisyon :", pozisyon)



menu()