from utils.fileOperations import readFile, updateURLFiles, getQueries, checkResponses
from utils.startScreen import startScreen
from utils.log import createNewLogFile, log, vulnerableLog
from utils.find import findForms, findHrefs
from requests import *
from bs4 import *
from urllib.parse import urljoin, urlparse
import threading
import time
import re

def prepareScanner():

    # Log dosyasını oluştur
    createNewLogFile()

    # Başlangıç ayarları ekranını göster ve ayarları al
    global settings
    settings = startScreen()

    # Linkleri ve test edilenleri dosyadan çek
    global urls
    urls = readFile("./inputURLs.txt")

    if (len(urls)) == 0:
        log("[!!] inputURLs.txt Dosyasında taranacak link bulunamadı!")

    global testedURLs
    testedURLs = readFile("./testedURLs.txt")

    # Thread ile yeniOturum
    threadCount = settings["thread"]
    thread = [] * threadCount
    for _thread in range(0, threadCount):
        thread.append(threading.Thread(target = newSession, args = (getFirstURL(),)))
        thread[len(thread) - 1].start()

def newSession(url):  

    # Yeni session
    session = Session()

    # Sayfaya erişilememe durumu
    try:
        if url != "":
            content = session.get(url).content
    except:
        log("Sayfaların birine erişim sağlanamadı. (%s)" % url)
        testedURLs.append(url)
        updateURLFiles(urls, testedURLs)
        url = ""

    if url != "": # Eğer URL var ise ve erişim sağlanmışsa

        # Sayfadaki yeni URL'leri taramaya ekleme
        for href in findHrefs(content):

            newURL = urljoin(url, href)
            newURLLast = urljoin(newURL, urlparse(newURL).path)

            if (newURLLast not in testedURLs) and (newURLLast not in urls) and (bool(re.match(settings["regEx"], newURLLast))):
                if settings["urlAddScan"] == 1:
                    urls.append(newURLLast)
                elif settings["urlAddScan"] == 2 and urlparse(newURLLast).netloc == urlparse(url).netloc:
                    urls.append(newURLLast)
                    
        # URL'i dosyadan silme, test edilenlere ekleme
        testedURLs.append(url)
        updateURLFiles(urls, testedURLs)

        # Form bulma aşaması
        forms = findForms(content)

        log("Taranan Sayfa: " + url)   
        if len(urls) == 0:
            log("[!!] Taranabilecek URL kalmadı [!!]")

        # Form için Input bulma ve ayrıştırma aşaması
        for form in forms:
                    
            inputList = form.find_all("input")
            method = form.attrs.get("method", "get").lower()

            try:
                action = form.attrs.get("action").lower()
            except:
                action = None

            for input in inputList:

                type = input.attrs.get("type", "") # Türleri
                value = input.attrs.get("value", "") # Formlardaki boşluklar
                name = input.attrs.get("name") # Form adları

                #### Sorunlu karakterleri test etme ####
                for query in getQueries():

                    data = {}

                    if type == "hidden" or value:
                        data[name] = value + query

                    elif type != "submit":
                        data[name] = "aaaaaaaaaaaaa" + query

                    #### GET & POST aşaması ####
                    newURL = urljoin(url, action)

                    if method.upper() == "POST":
                        _response = session.post(newURL, data = data)

                    else:
                        _response = session.get(newURL, params = data)

                    if not _response:
                        pass

                    #### Response'ta hata var mı kontrolü ####
                    if checkResponses(str(BeautifulSoup(_response.content, "html.parser"))):
                        vulnerableLog("[++++] " + str(url) + "\n[++++] # " + str(type) + " # " + str(method) + " # {" + str(name) + ": '" + str(data[name]) + "'}")
                        break

    newSession(getFirstURL())

def getFirstURL():

    if len(urls) > 0:
        firstURL = urls[0]
        urls.remove(firstURL)
    else:
        firstURL = ""

    time.sleep(0.1)
    return firstURL

prepareScanner()
