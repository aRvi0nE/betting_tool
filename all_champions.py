import importlib

from classes.scraping import base_stats
from classes import champion
from data.item_stats import *
from classes.scraping import base_stats


def get_averages(new_patch: bool):
    """Gathers info from all champions and calculates averages of each base stat"""
    champion_list = base_stats.get_champion_list(new_patch)
    champion_hp = 0
    champion_hp_regen = 0
    champion_armor = 0
    champion_mr = 0
    champion_ad = 0
    champion_attack_speed = 0
    champion_size = 0

    if new_patch:
        for champ in champion_list:
            champion_instance = champion.Champion(champ, new_patch)
            champion_hp += champion_instance.hp
            champion_hp_regen += champion_instance.hp_regen
            champion_armor += champion_instance.armor
            champion_mr += champion_instance.mr
            champion_ad += champion_instance.ad
            champion_attack_speed += champion_instance.attack_speed
            champion_size += champion_instance.hit_box

        champion_hp = champion_hp / len(champion_list)
        champion_hp_regen = champion_hp_regen / len(champion_list)
        champion_armor = champion_armor / len(champion_list)
        champion_mr = champion_mr / len(champion_list)
        champion_ad = champion_ad / len(champion_list)
        champion_attack_speed = champion_attack_speed / len(champion_list)
        champion_size = champion_size / len(champion_list)

        code = """CHAMPION_HP = {}
CHAMPION_HP_REGEN = {}
CHAMPION_ARMOR = {}
CHAMPION_MR = {}
CHAMPION_AD = {}
CHAMPION_ATTACK_SPEED = {}
CHAMPION_SIZE = {}
        """.format(champion_hp, champion_hp_regen, champion_armor, champion_mr, champion_ad, champion_attack_speed, champion_size)

        with open("data/champion_stats.py", "w") as f:
            f.write(code)

    else:
        try:
            with open("data/champion_stats.py", "r") as f:
                file = f.read()
                print(file)

        except:
            for champ in champion_list:
                champion_instance = champion.Champion(champ, new_patch)
                champion_hp += champion_instance.hp
                champion_hp_regen += champion_instance.hp_regen
                champion_armor += champion_instance.armor
                champion_mr += champion_instance.mr
                champion_ad += champion_instance.ad
                champion_attack_speed += champion_instance.attack_speed
                champion_size += champion_instance.hit_box

            champion_hp = champion_hp / len(champion_list)
            champion_hp_regen = champion_hp_regen / len(champion_list)
            champion_armor = champion_armor / len(champion_list)
            champion_mr = champion_mr / len(champion_list)
            champion_ad = champion_ad / len(champion_list)
            champion_attack_speed = champion_attack_speed / len(champion_list)
            champion_size = champion_size / len(champion_list)

            code = """CHAMPION_HP = {}
            CHAMPION_HP_REGEN = {}
            CHAMPION_ARMOR = {}
            CHAMPION_MR = {}
            CHAMPION_AD = {}
            CHAMPION_ATTACK_SPEED = {}
            CHAMPION_SIZE = {}
                    """.format(champion_hp, champion_hp_regen, champion_armor, champion_mr, champion_ad,
                               champion_attack_speed, champion_size)

            with open("data/champion_stats.py", "w") as f:
                f.write(code)


def get_champion_instances():
    champion_list = base_stats.get_champion_list(False)
    champion_instances = {}
    for champ in champion_list:
        try:
            champ_module = importlib.import_module("classes." + champ.lower())
            champ_class = getattr(champ_module, champ)
            obj = champ_class(False)
            champion_instances[champ.lower()] = obj
            print(obj.show_stats())
        except ImportError:
            pass
    return champion_instances
