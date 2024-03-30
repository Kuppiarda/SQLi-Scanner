from utils.log import log
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
            log("[#] Taranan URL'de bulunan diğer URL'ler için [#]")
            log("• [1] Bulunan her URL'i taramaya ekle")
            log("• [2] Sadece aynı alan adına sahip URL'leri taramaya ekle")
            log("• [3] Taramaya ekleme yapma")
            settings["urlAddScan"] = int(input("[?] Seçiminizi yapın: "))
            if settings["urlAddScan"] >= 1 and settings["urlAddScan"] <= 3:
                break

        except:
            pass

    # RegEx
    while True:

        try:
            clearScreen()
            log("[#] Taramaya eklenecek URL'lerde düzenli ifade(RegEx) kontrolü [#]")
            log("• [1] Düzenli ifadeleri kullan")
            log("• [2] Düzenli ifadeleri kullanma")
            selection = int(input("[?] Seçiminizi yapın: "))
            
            if selection == 1:
                clearScreen()
                while True:
                    try:
                        log("[?] Taramaya ekleme yapılırken eşleşmesini istediğiniz düzenli ifadeyi(RegEx) giriniz:")
                        settings["regEx"] = input()

                        try:
                            re.compile(settings["regEx"])
                            break

                        except:
                            clearScreen()
                            log("[!] RegEx geçersiz, tekrar deneyin.\n")

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
            log("[#] Uygulama çalışmaya hazır [#]")
            log("• [1] Taranacak linkleri düzenle")
            log("• [2] Taranmış olan linkleri düzenle")
            log("• [3] Ayarları tekrar yap")
            log("• [4] Başla")
            selection = int(input("[?] Seçiminizi yapın: "))

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
    log("[SQL Enjeksiyonu Tarayıcısı / SQLi Scanner]\n")
