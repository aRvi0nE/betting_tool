from classes.scraping.get_html import get_html_items, get_html_item


def get_item_list(new_patch: bool):
    doc = get_html_items(new_patch)
    divs = doc.find("dt", string="Legendary items").\
        previous_element.\
        next_sibling.\
        find_all("div", attrs={"style": "padding:1px;"})
    item_list = []
    for item in divs:
        item_list.append(item.get("data-item"))

    divs = doc.find("dt", string="Mythic items").\
        previous_element.\
        next_sibling.\
        find_all("div", attrs={"style": "padding:1px;"})
    for item in divs:
        item_list.append(item.get("data-item"))
    return item_list


def get_data(name, new_patch: bool):
    doc = get_html_item(name, new_patch)

    ability_haste = output_handler(doc.find("a", string="ability haste"))
    hp = output_handler(doc.find("a", string="health"))
    mana = output_handler(doc.find("a", string="mana"))
    mr = output_handler(doc.find("a", string="magic resistance"))
    ap = output_handler(doc.find("a", string="ability power"))
    mana_regen = output_handler(doc.find("a", string="base mana regeneration"))
    h_s_power = output_handler(doc.find("a", string="heal and shield power"))
    ad = output_handler(doc.find("a", string="attack damage"))
    lethality = output_handler(doc.find("a", string="Lethality"))
    gold_per10 = output_handler(doc.find("a", string="per 10 seconds"))
    attack_speed = output_handler(doc.find("a", string="attack speed"))
    life_steal = output_handler(doc.find("a", string="life steal"))
    crit_chance = output_handler(doc.find("a", string="critical strike chance"))
    hp_regen = output_handler(doc.find("a", string="base health regeneration"))
    move_speed = output_handler(doc.find("a", string="movement speed"))
    armor = output_handler(doc.find("a", string="armor"))
    armor_pen = output_handler(doc.find("a", string="armor penetration"))
    if name == "Void Staff":
        magic_pen_percent = output_handler(doc.find("a", string="magic penetration"))
        magic_pen_flat = 0
    else:
        magic_pen_percent = 0
        magic_pen_flat = output_handler(doc.find("a", string="magic penetration"))
    omnivamp = output_handler(doc.find("a", string="omnivamp"))

    data_dict = {"ability_haste": ability_haste,
                 "hp": hp,
                 "mana": mana,
                 "mr": mr,
                 "ap": ap,
                 "mana_regen": mana_regen,
                 "h_s_power": h_s_power,
                 "ad": ad,
                 "lethality": lethality,
                 "gold_per10": gold_per10,
                 "attack_speed": attack_speed,
                 "life_steal": life_steal,
                 "crit_chance": crit_chance,
                 "hp_regen": hp_regen,
                 "move_speed": move_speed,
                 "armor": armor,
                 "armor_pen": armor_pen,
                 "magic_pen_percent": magic_pen_percent,
                 "magic_pen_flat": magic_pen_flat,
                 "omnivamp": omnivamp}
    return data_dict


def output_handler(stat):
    try:
        if "%" in stat.previous_element:
            text = stat.previous_element.replace("%", "")
        else:
            text = stat.previous_element
        return float(text)
    except:
        return 0
