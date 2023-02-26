import math

from classes.scraping.get_html import get_html_champion


def get_data(new_patch: bool):
    doc = get_html_champion("Akshan", new_patch)
    # p
    p_static_cooldown = output_handler(
        doc.
            find("span", id="Dirty_Fighting").
            parent.
            parent.
            parent.
            find("span", string="STATIC").
            parent.
            next_sibling.
            next_sibling
    )[0]
    p_damage_scale_ad = output_handler(
        doc.
        find("span", id="Dirty_Fighting").
        parent.
        parent.
        parent.
        find("a", title="Basic attack").
        next_sibling.
        next_sibling
    )[0] / 100
    p_minion_damage_multiplier = output_handler(
        doc.
        find("span", id="Dirty_Fighting").
        parent.
        parent.
        parent.
        find("span", string="physical damage").
        next_sibling.
        next_sibling
    )[0] / 100 / p_damage_scale_ad
    p_crit_damage = float(
        doc.
        find("span", id="Dirty_Fighting").
        parent.
        parent.
        parent.
        find("span", attrs={"data-item": "Infinity Edge"}).
        parent.
        text.
        replace("(", "").
        replace("%", "").
        split()[0]
    )
    print(p_crit_damage)


def output_handler(stat) -> list:
    try:
        text = stat.text
        print(text)
        if "(based on level)" in text:
            text = text.replace("(based on level)", "")
        if "−" in text:
            text = text.replace("−", "")
            text = text.replace("(based on level)", "")
            text = text.split()
            text = str((float(text[0]) + float(text[1])) / 2)
        if "%" in text:
            text = text.replace("%", "")
        if "(+" in text:
            try:
                text = text.replace("/", "")
                text = text.split()
                s = 0
                t = 0
                for i in range(5):
                    s += float(text[i])
                    try:
                        t += float(text[i + 6])
                    except:
                        t += float(text[6])
                text = str(s / 5) + " " + str(t / 5)
            except:
                text = text[1]
        if "/" in text:
            text = text.replace("/", "")
            text = text.split()
            s = 0
            for number in text:
                s += float(number)
            text = str(s / len(text))
        if "AD" in text:
            text = text.replace("AD", "")
        text = text.split()
        for i in range(len(text)):
            text[i] = float(text[i])
        return text
    except:
        return [0]


get_data(False)
