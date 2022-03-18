from tkinter import *


giris_bilgileri = ("Bilge", "Ayvaz", "bilgevz11@gmail.com", "Proje123")
yanlisGirisHakki = 3


def girisYap():
    global yanlisGirisHakki
    if yanlisGirisHakki <= 0:
        return False
    kullaniciAdi = ad.get()
    kullaniciSoyadi = soyad.get()
    kullaniciMail = mail.get()
    kullaniciSifre = sifre.get()
    print(kullaniciAdi, "-", kullaniciSoyadi, "-", kullaniciMail, "-", kullaniciSifre)
    print("DOĞRULUĞU DENETLENİYOR.")

    if (kullaniciAdi == giris_bilgileri[0] and kullaniciSoyadi == giris_bilgileri[1] and kullaniciMail ==
            giris_bilgileri[2] and kullaniciSifre == giris_bilgileri[3]):
        print("BİLGİLER DOĞRU,GİRİŞİNİZ SAĞLANDI...")
        sonuc.config (text="T.C Kimlik No:12561478966,Adı:BİLGE, Soyadı:AYVAZ, Doğum Tarihi:12,07,1999,Seri No:A00B12356, Son Geçerlilik:12.01.2027, Cinsiyet:K/F, Uyruğu:T.C/TUR, Anne Adı:AYSEL,Baba Adı:SERKAN,Veren Makam:T.C İÇİŞLERİ BAKANLIĞI")
        EkranıTemizle()

    else:
        print("GİRİLEN BİLGİLER YANLIŞ !")
        yanlisGirisHakki -= 1
        sonuc.config(text="Girilen Bilgiler Yanlış! Kalan Hak:%d" % yanlisGirisHakki)


def EkranıTemizle():
    karsılama.config(text="BİLGE AYVAZ,KİMLİK BİLGİ SİSTEMİNE HOŞGELDİNİZ.")
    adsor.destroy()
    ad.destroy()
    soyadsor.destroy()
    soyad.destroy()
    sifresor.destroy()
    sifre.destroy()
    btn.destroy()


pencere = Tk()
pencere.title("GİRİŞ EKRANI")
pencere.geometry("800x400")

karsılama = Label(pencere)
karsılama.config(text="MERHABA, LÜTFEN BİLGİLERİNİZİ GİRİNİZ.",font=("Calibri",25))
karsılama.pack()

ad= Entry(pencere)
ad.pack()

soyad= Entry(pencere)
soyad.pack()

mail= Entry(pencere)
mail.pack()

sifresor= Label(pencere)
sifresor.config(text="ŞİFRE:")

sifre= Entry(pencere)
sifre.pack()

btn = Button(pencere)
btn.config(text="GİRİŞ YAP!", bg="purple",fg="black", command=girisYap)
btn.pack()

sonuc = Label(pencere)
sonuc.config(text="DAHA GİRİŞ YAPILMADI!")
sonuc.pack()

mainloop()