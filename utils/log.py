from utils.fileOperations import writeFileAppend, writeFile
import datetime
import os

def log(text):

    # Son dosyayı bul
    files = [os.getcwd() + "/logs/" + file for file in os.listdir("./logs/") if file.startswith("SQL_Log")]
    latestFile = max(files, key = os.path.getctime) # Tarihe göre son txt dosyasını buluyor

    print(text)
    writeFileAppend(latestFile, [text])

def vulnerableLog(text):

    print(text)
    writeFileAppend(os.getcwd() + "/vulnerableURLs.txt", [text]) # vulnerableURLs Dosyasına yazıyor

def createNewLogFile():
    dateTime = datetime.datetime.now().strftime("SQL_Log_%d_%m_%Y_%H-%M-%S.txt")
    writeFile("./logs/" + dateTime, [])