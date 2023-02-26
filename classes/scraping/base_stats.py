from classes.scraping.get_html import get_html_champions, get_html_champion


def get_champion_list(new_patch: bool):
    doc = get_html_champions(new_patch)
    table = doc.find("td", attrs={"data-sort-value": "Aatrox"}).parent.parent
    i = 0
    champion_list = []
    for entry in table:
        if i <= 2:
            i += 1
        if i > 2:
            try:
                champion_list.append(entry.find("td").get("data-sort-value"))
            except:
                continue
    return champion_list


def get_data(name, new_patch: bool):
    """Gets the base stats like base ad, hp, resists, etc... from html scraped from
    https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki"""
    doc = get_html_champion(name, new_patch)

    base_hp = output_handler(doc.find("span", id="Health_{}".format(name)))
    hp_growth = output_handler(doc.find("span", id="Health_{}_lvl".format(name)))

    base_resource = output_handler(doc.find("span", id="ResourceBar_{}".format(name)))
    resource_growth = output_handler(doc.find("span", id="ResourceBar_{}_lvl".format(name)))

    base_hp_regen = output_handler(doc.find("span", id="HealthRegen_{}".format(name)))
    hp_regen_growth = output_handler(doc.find("span", id="HealthRegen_{}_lvl".format(name)))

    base_resource_regen = output_handler(doc.find("span", id="ResourceRegen_{}".format(name)))
    resource_regen_growth = output_handler(doc.find("span", id="ResourceRegen_{}_lvl".format(name)))

    base_armor = output_handler(doc.find("span", id="Armor_{}".format(name)))
    armor_growth = output_handler(doc.find("span", id="Armor_{}_lvl".format(name)))

    base_ad = output_handler(doc.find("span", id="AttackDamage_{}".format(name)))
    ad_growth = output_handler(doc.find("span", id="AttackDamage_{}_lvl".format(name)))

    base_mr = output_handler(doc.find("span", id="MagicResist_{}".format(name)))
    mr_growth = output_handler(doc.find("span", id="MagicResist_{}_lvl".format(name)))

    crit_damage = output_handler(doc.find("div", attrs={'data-source': "critical damage"}))

    base_move_speed = output_handler(doc.find("span", id="MovementSpeed_{}".format(name)))

    attack_range = output_handler(doc.find("span", id="AttackRange_{}".format(name)))

    base_attack_speed = output_handler(doc.find("div", attrs={'data-source': "attack speed"}))
    attack_speed_ratio = output_handler(doc.find("div", attrs={'data-source': "as ratio"}))
    attack_speed_growth = output_handler(doc.find("span", id="AttackSpeedBonus_{}_lvl".format(name)))

    hit_box = output_handler(doc.find("div", attrs={'data-source': "gameplay radius"}))

    resource = doc.find("h3", string="Resource").parent.find("span", attrs={"data-game": "lol"}).get("data-tip")
    if resource == "Manaless":
        try:
            resource = doc.find("h3", string="Resource").parent.find("a", class_="mw-redirect").text
        except:
            resource = "Manaless"
    if resource == "Energy":
        base_resource_regen = output_handler(doc.find("a", string="Energy regen. (per 5s)").next_element.next_element)

    data_dict = {"base_hp": base_hp,
                 "hp_growth": hp_growth,
                 "base_resource": base_resource,
                 "resource_growth": resource_growth,
                 "base_hp_regen": base_hp_regen,
                 "hp_regen_growth": hp_regen_growth,
                 "base_resource_regen": base_resource_regen,
                 "resource_regen_growth": resource_regen_growth,
                 "base_armor": base_armor,
                 "armor_growth": armor_growth,
                 "base_ad": base_ad,
                 "ad_growth": ad_growth,
                 "base_mr": base_mr,
                 "mr_growth": mr_growth,
                 "crit_damage": crit_damage,
                 "base_move_speed": base_move_speed,
                 "attack_range": attack_range,
                 "base_attack_speed": base_attack_speed,
                 "attack_speed_ratio": attack_speed_ratio,
                 "attack_speed_growth": attack_speed_growth,
                 "hit_box": hit_box,
                 "resource": resource}
    return data_dict


def output_handler(stat):
    """Handles text from goofy html output"""
    try:
        if "Crit. damage" in stat.text:
            text = stat.text.replace("Crit. damage", "")
            text = text.replace("%", "")
        elif "Base AS" in stat.text:
            text = stat.text.replace("Base AS", "")
        elif "AS ratio" in stat.text:
            text = stat.text.replace("AS ratio", "")
        elif "Gameplay radius" in stat.text:
            text = stat.text.replace("Gameplay radius", "")
        else:
            text = stat.text
        return float(text)
    except:
        return 0
