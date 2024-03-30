from bs4 import *

# Form bulma
def findForms(source):

    bs = BeautifulSoup(source, "html.parser")

    return bs.find_all("form")

# href bulma(link)
def findHrefs(source):

    urls = []
    bs = BeautifulSoup(source, "html.parser")

    for url in bs.find_all("a"):
        urls.append(url.get("href"))

    return urls