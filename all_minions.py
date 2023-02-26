from classes import minion


def get_averages(new_patch: bool):
    """Gathers info from minions and calculates their average stats"""
    minion_list = [["Melee_Minion", 6/13], ["Caster_Minion", 6/13], ["Siege_Minion", 1/13]]
    minion_hp = 0
    minion_ad = 0
    minion_attack_speed = 0
    minion_range = 0
    minion_armor = 0
    minion_magic_resist = 0
    minion_size = 12/13 * 48 + 1/13 * 65

    if new_patch:
        for item in minion_list:
            minion_instance = minion.Minion(item[0], new_patch)
            minion_hp += item[1] * minion_instance.hp
            minion_ad += item[1] * minion_instance.ad
            minion_attack_speed += item[1] * minion_instance.attack_speed
            minion_range += item[1] * minion_instance.rage
            minion_armor += item[1] * minion_instance.armor
            minion_magic_resist += item[1] * minion_instance.magic_resist

        code = f"""MINION_HP = {minion_hp}
MINION_AD = {minion_ad}
MINION_ATTACK_SPEED = {minion_attack_speed}
MINION_RANGE = {minion_range}
MINION_ARMOR = {minion_armor}
MINION_MAGIC_RESIST = {minion_magic_resist}
MINION_SIZE = {minion_size}"""

        with open("data/minion_stats.py", "w") as f:
            f.write(code)

    else:
        try:
            with open("data/minion_stats.py", "r") as f:
                file = f.read()
                print(file)

        except:
            for item in minion_list:

                minion_instance = minion.Minion(item[0], new_patch)
                minion_hp += item[1] * minion_instance.hp
                minion_ad += item[1] * minion_instance.ad
                minion_attack_speed += item[1] * minion_instance.attack_speed
                minion_range += item[1] * minion_instance.rage
                minion_armor += item[1] * minion_instance.armor
                minion_magic_resist += item[1] * minion_instance.magic_resist

            code = f"""MINION_HP = {minion_hp}
MINION_AD = {minion_ad}
MINION_ATTACK_SPEED = {minion_attack_speed}
MINION_RANGE = {minion_range}
MINION_ARMOR = {minion_armor}
MINION_MAGIC_RESIST = {minion_magic_resist}
MINION_SIZE = {minion_size}"""

            with open("data/minion_stats.py", "w") as f:
                f.write(code)
