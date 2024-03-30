def readFile(path):

    with open(path, "r") as file:
        return file.read().splitlines()

def writeFile(path, textArray):

    with open(path, "w") as file:
        for text in textArray:
            file.write(text + "\n")
        
def writeFileAppend(path, textArray):

    with open(path, "a") as file:
        for text in textArray:
            file.write(text + "\n")

def updateURLFiles(urls, testedURLs):

    try:
        writeFile("./inputURLs.txt", urls)
        writeFile("./testedURLs.txt", testedURLs)
    except:
        pass

def getQueries():

    # Sorguları bozan karakterleri al
    file = open("./settings/query.txt", "r")
    queries = file.read().splitlines()
    file.close()
    return queries

def checkResponses(content):

    # Dosyayı aç
    file = open("./settings/response.txt", "r")
    responses = file.read().splitlines()
    file.close()

    # Responsetakiler ile content'i karşılaştır
    for response in responses:
        if response.lower() in content.lower():
            return True

    return False