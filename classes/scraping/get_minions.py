from classes.scraping.get_html import get_html_minion


def get_data(name, new_patch: bool):
    """Gets minion base stats from scraped html from https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki"""
    doc = get_html_minion(name, new_patch)

    hp = output_handler(doc.find("a", string="Health").parent.parent.find("span"))

    ad = output_handler(doc.find("a", string="Attack damage").parent.parent.find("span"))
    if name == "Siege_Minion":
        ad = ad/90

    attack_speed = output_handler(doc.find("a", string="Attack speed").parent.parent.find("div"))

    range_ = output_handler(doc.find("a", string="Range").parent.parent.find("div"))

    armor = output_handler(doc.find("a", string="Armor").parent.parent.find("span"))

    magic_resist = output_handler(doc.find("a", string="Magic res.").parent.parent.find("div"))

    data_dict = {"hp": hp,
                 "ad": ad,
                 "attack_speed": attack_speed,
                 "range": range_,
                 "armor": armor,
                 "magic_resist": magic_resist}

    return data_dict


def output_handler(stat):
    """Handles text from goofy html output"""
    try:

        if "(based on upgrades)" in stat.text:
            text = stat.text.replace("(based on upgrades)", "")
            text = text.split()
            text = (float(text[0]) + float(text[2]))/2
        else:
            text = stat.text
        return float(text)
    except:
        return 0
