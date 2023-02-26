import requests

from bs4 import BeautifulSoup


def check_patch():
    url = "https://leagueoflegends.fandom.com/wiki/Patch_(League_of_Legends)"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    new_patch = doc.find("a", string="LoL Patch Notes").find_previous("a").text
    try:
        with open("data/current_patch.txt", "r") as f:
            current_patch = f.read()
        if current_patch != new_patch:
            current_patch = new_patch
            with open("data/current_patch.txt", "w") as f:
                f.write(new_patch)
            return True
        else:
            return False
    except:
        with open("data/current_patch.txt", "w") as f:
            f.write(new_patch)
        return True

