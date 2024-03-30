import os
import subprocess
import re

def startScreen():   
    
    settings = {}
    settings["regEx"] = "." # Başlangıçta regexsiz olacağı için her şeyi alsın

    clearScreen()

    # Thread belirleme
    while True:

        try:
            clearScreen()
            settings["thread"] = int(input("[?] Uygulama kaç thread ile çalışsın: "))
            if settings["thread"] > 0:
                break

        except:
            pass

    # Sayfa bulma
    while True:

        try:
            clearScreen()
            print("[#] Taranan URL'de bulunan diğer URL'ler için [#]")
            print("• [1] Bulunan her URL'i taramaya ekle")
            print("• [2] Sadece aynı alan adına sahip URL'leri taramaya ekle")
            print("• [3] Taramaya ekleme yapma")
            settings["urlAddScan"] = int(input("\n[?] Seçiminizi yapın: "))
            if settings["urlAddScan"] >= 1 and settings["urlAddScan"] <= 3:
                break

        except:
            pass

    # RegEx
    while True:

        try:
            clearScreen()
            print("[#] Taramaya eklenecek URL'lerde düzenli ifade(RegEx) kontrolü [#]")
            print("• [1] Düzenli ifadeleri kullan")
            print("• [2] Düzenli ifadeleri kullanma")
            selection = int(input("\n[?] Seçiminizi yapın: "))
            
            if selection == 1:
                clearScreen()
                while True:
                    try:
                        print("\n[?] Taramaya ekleme yapılırken eşleşmesini istediğiniz düzenli ifadeyi(RegEx) giriniz:")
                        settings["regEx"] = input()

                        try:
                            re.compile(settings["regEx"])
                            break

                        except:
                            clearScreen()
                            print("[!] RegEx geçersiz, tekrar deneyin.\n")

                    except:
                        pass

                break

            elif selection == 2:
                break

        except:
            pass

    # Başlangıç aşaması
    while True:

        selection = 0
        try:
            clearScreen()
            print("[#] Uygulama çalışmaya hazır [#]")
            print("• [1] Taranacak linkleri düzenle")
            print("• [2] Taranmış olan linkleri düzenle")
            print("• [3] Ayarları tekrar yap")
            print("• [4] Başla")
            selection = int(input("\n[?] Seçiminizi yapın: "))

            if selection == 1:
                subprocess.Popen([r"C:\Windows\System32\notepad.exe", os.getcwd() + "/inputURLs.txt"])

            elif selection == 2:
                subprocess.Popen([r"C:\Windows\System32\notepad.exe", os.getcwd() + "/testedURLs.txt"])

            elif selection == 3:
                return startScreen()

            elif selection == 4:
                clearScreen()
                break

        except:
            pass

    return settings

def clearScreen():
    os.system("cls")
    print("[SQL Enjeksiyonu Tarayıcısı / SQLi Scanner]\n")
