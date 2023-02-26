from bs4 import BeautifulSoup
import requests


def get_html_champions(new_patch: bool):
    """Scrapes html from the page wich lists all the champions at
    https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki, and saves it to a file"""
    if new_patch:
        url = "https://leagueoflegends.fandom.com/wiki/List_of_champions"
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        with open("classes/scraping/data/champions/champion_list.html", "w", encoding="utf-8") as f:
            f.write(str(doc))
    else:
        try:
            with open("classes/scraping/data/champions/champion_list.html", "r", encoding="utf-8") as f:
                doc = BeautifulSoup(f.read(), "html.parser")
        except:
            url = "https://leagueoflegends.fandom.com/wiki/List_of_champions"
            result = requests.get(url)
            doc = BeautifulSoup(result.text, "html.parser")
            with open("classes/scraping/data/champions/champion_list.html", "w", encoding="utf-8") as f:
                f.write(str(doc))
    return doc


def get_html_champion(name, new_patch: bool):
    """Scrapes champion html from https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki, and saves it to a
    file"""
    if new_patch:
        print(name)
        url = "https://leagueoflegends.fandom.com/wiki/{}/LoL".format(name)
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        with open("classes/scraping/data/champions/{}.html".format(name), "w", encoding="utf-8") as f:
            f.write(str(doc))
    else:
        try:
            with open("classes/scraping/data/champions/{}.html".format(name), "r", encoding="utf-8") as f:
                doc = BeautifulSoup(f.read(), "html.parser")
        except:
            print(name)
            url = "https://leagueoflegends.fandom.com/wiki/{}/LoL".format(name)
            result = requests.get(url)
            doc = BeautifulSoup(result.text, "html.parser")
            with open("classes/scraping/data/champions/{}.html".format(name), "w", encoding="utf-8") as f:
                f.write(str(doc))
    return doc


def get_html_items(new_patch: bool):
    """Scrapes html from the page which lists all the items at
    https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki, and saves it to a file"""
    if new_patch:
        url = "https://leagueoflegends.fandom.com/wiki/Item_(League_of_Legends)"
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        with open("classes/scraping/data/items/item_list.html", "w", encoding="utf-8") as f:
            f.write(str(doc))
    else:
        try:
            with open("classes/scraping/data/items/item_list.html", "r", encoding="utf-8") as f:
                doc = BeautifulSoup(f.read(), "html.parser")
        except:
            url = "https://leagueoflegends.fandom.com/wiki/Item_(League_of_Legends)"
            result = requests.get(url)
            doc = BeautifulSoup(result.text, "html.parser")
            with open("classes/scraping/data/items/item_list.html", "w", encoding="utf-8") as f:
                f.write(str(doc))
    return doc


def get_html_item(name, new_patch: bool):
    """Scrapes item html from https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki, and saves it to a file"""
    if new_patch:
        print(name)
        url = "https://leagueoflegends.fandom.com/wiki/{}".format(name)
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        with open("classes/scraping/data/items/{}.html".format(name), "w", encoding="utf-8") as f:
            f.write(str(doc))
    else:
        try:
            with open("classes/scraping/data/items/{}.html".format(name), "r", encoding="utf-8") as f:
                doc = BeautifulSoup(f.read(), "html.parser")
        except:
            print(name)
            url = "https://leagueoflegends.fandom.com/wiki/{}".format(name)
            result = requests.get(url)
            doc = BeautifulSoup(result.text, "html.parser")
            with open("classes/scraping/data/items/{}.html".format(name), "w", encoding="utf-8") as f:
                f.write(str(doc))
    return doc


def get_html_minion(name, new_patch: bool):
    """Scrapes minion html from https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki, and saves it to a
     file"""
    if new_patch:
        print(name)
        url = f"https://leagueoflegends.fandom.com/wiki/{name}"
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        with open(f"classes/scraping/data/minions/{name}", "w", encoding="utf-8") as f:
            f.write(str(doc))
    else:
        try:
            with open(f"classes/scraping/data/minions/{name}", "r", encoding="utf-8") as f:
                doc = BeautifulSoup(f.read(), "html.parser")
        except:
            print(name)
            url = f"https://leagueoflegends.fandom.com/wiki/{name}"
            result = requests.get(url)
            doc = BeautifulSoup(result.text, "html.parser")
            with open(f"classes/scraping/data/minions/{name}", "w", encoding="utf-8") as f:
                f.write(str(doc))
    return doc


def get_html_boot(name, newpatch: bool):
    """Scraped boot html from https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki, and saves it to a file"""
    if newpatch:
        print(name)
        url = f"https://leagueoflegends.fandom.com/wiki/{name}"
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        with open(f"classes/scraping/data/boots/{name}.html", "w", encoding="utf-8") as f:
            f.write(str(doc))
    else:
        try:
            with open(f"classes/scraping/data/boots/{name}.html", "r", encoding="utf-8") as f:
                doc = BeautifulSoup(f.read(), "html.parser")
        except:
            print(name)
            url = f"https://leagueoflegends.fandom.com/wiki/{name}"
            result = requests.get(url)
            doc = BeautifulSoup(result.text, "html.parser")
            with open(f"classes/scraping/data/boots/{name}.html", "w", encoding="utf-8") as f:
                f.write(str(doc))
    return doc
