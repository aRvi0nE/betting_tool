from classes.scraping import get_items
from classes import item


def get_averages(new_patch: bool):
    """Gathers info from items and calculates the overall average of each stat"""
    item_list = get_items.get_item_list(new_patch)
    item_ability_haste = 0
    item_hp = 0
    item_mana = 0
    item_mr = 0
    item_ap = 0
    item_mana_regen = 0
    item_h_s_power = 0
    item_ad = 0
    item_lethality = 0
    item_gold_per10 = 0
    item_attack_speed = 0
    item_life_steal = 0
    item_crit_chance = 0
    item_hp_regen = 0
    item_move_speed = 0
    item_armor = 0
    item_armor_pen = 0
    item_magic_pen_percent = 0
    item_magic_pen_flat = 0
    item_omnivamp = 0

    if new_patch:
        for itm in item_list:
            item_instance = item.Item(itm, new_patch)
            item_ability_haste += item_instance.ability_haste
            item_hp += item_instance.hp
            item_mana += item_instance.mana
            item_mr += item_instance.armor
            item_ap += item_instance.ap
            item_mana_regen += item_instance.mana_regen
            item_h_s_power += item_instance.h_s_power
            item_ad += item_instance.ad
            item_lethality += item_instance.lethality
            item_gold_per10 += item_instance.gold_per10
            item_attack_speed += item_instance.attack_speed
            item_life_steal += item_instance.life_steal
            item_crit_chance += item_instance.crit_chance
            item_hp_regen += item_instance.hp_regen
            item_move_speed += item_instance.move_speed
            item_armor += item_instance.armor
            item_armor_pen += item_instance.armor_pen
            item_magic_pen_percent += item_instance.magic_pen_percent
            item_magic_pen_flat += item_instance.magic_pen_flat
            item_omnivamp += item_instance.omnivamp

        item_ability_haste = item_ability_haste/len(item_list)
        item_hp = item_hp/len(item_list)
        item_mana = item_mana/len(item_list)
        item_mr = item_mr/len(item_list)
        item_ap = item_ap/len(item_list)
        item_mana_regen = item_mana_regen/len(item_list)
        item_h_s_power = item_h_s_power/len(item_list)
        item_ad = item_ad/len(item_list)
        item_lethality = item_lethality/len(item_list)
        item_gold_per10 = item_gold_per10/len(item_list)
        item_attack_speed = item_attack_speed/len(item_list)
        item_life_steal = item_life_steal/len(item_list)
        item_crit_chance = item_crit_chance/len(item_list)
        item_hp_regen = item_hp_regen/len(item_list)
        item_move_speed = item_move_speed/len(item_list)
        item_armor = item_armor/len(item_list)
        item_armor_pen = item_armor_pen/len(item_list)
        item_magic_pen_percent = item_magic_pen_percent/len(item_list)
        item_magic_pen_flat = item_magic_pen_flat/len(item_list)
        item_omnivamp = item_omnivamp/len(item_list)

        code = """ITEM_ABILITY_HASTE = {}
ITEM_HP = {}
ITEM_MANA = {}
ITEM_MR = {}
ITEM_AP = {}
ITEM_MANA_REGEN = {}
ITEM_H_S_POWER = {}
ITEM_AD = {}
ITEM_LETHALITY = {}
ITEM_GOLD_PER10 = {}
ITEM_ATTACK_SPEED = {}
ITEM_LIFE_STEAL = {}
ITEM_CRIT_CHANCE = {}
ITEM_HP_REGEN = {}
ITEM_MOVE_SPEED = {}
ITEM_ARMOR = {}
ITEM_ARMOR_PEN = {}
ITEM_MAGIC_PEN_PERCENT = {}
ITEM_MAGIC_PEN_FLAT = {}
ITEM_OMNIVAMP = {}  
        """.format(item_ability_haste, item_hp, item_mana, item_mr, item_ap, item_mana_regen, item_h_s_power, item_ad,
                   item_lethality, item_gold_per10, item_attack_speed, item_life_steal, item_crit_chance, item_hp_regen,
                   item_move_speed, item_armor, item_armor_pen, item_magic_pen_percent, item_magic_pen_flat,
                   item_omnivamp)

        with open("data/item_stats.py", "w") as f:
            f.write(code)

    else:
        try:
            with open("data/item_stats.py", "r") as f:
                file = f.read()
                print(file)

        except:
            for itm in item_list:
                item_instance = item.Item(itm, new_patch)
                item_ability_haste += item_instance.ability_haste
                item_hp += item_instance.hp
                item_mana += item_instance.mana
                item_mr += item_instance.armor
                item_ap += item_instance.ap
                item_mana_regen += item_instance.mana_regen
                item_h_s_power += item_instance.h_s_power
                item_ad += item_instance.ad
                item_lethality += item_instance.lethality
                item_gold_per10 += item_instance.gold_per10
                item_attack_speed += item_instance.attack_speed
                item_life_steal += item_instance.life_steal
                item_crit_chance += item_instance.crit_chance
                item_hp_regen += item_instance.hp_regen
                item_move_speed += item_instance.move_speed
                item_armor += item_instance.armor
                item_armor_pen += item_instance.armor_pen
                item_magic_pen_percent += item_instance.magic_pen_percent
                item_magic_pen_flat += item_instance.magic_pen_flat
                item_omnivamp += item_instance.omnivamp

            item_ability_haste = item_ability_haste / len(item_list)
            item_hp = item_hp / len(item_list)
            item_mana = item_mana / len(item_list)
            item_mr = item_mr / len(item_list)
            item_ap = item_ap / len(item_list)
            item_mana_regen = item_mana_regen / len(item_list)
            item_h_s_power = item_h_s_power / len(item_list)
            item_ad = item_ad / len(item_list)
            item_lethality = item_lethality / len(item_list)
            item_gold_per10 = item_gold_per10 / len(item_list)
            item_attack_speed = item_attack_speed / len(item_list)
            item_life_steal = item_life_steal / len(item_list)
            item_crit_chance = item_crit_chance / len(item_list)
            item_hp_regen = item_hp_regen / len(item_list)
            item_move_speed = item_move_speed / len(item_list)
            item_armor = item_armor / len(item_list)
            item_armor_pen = item_armor_pen / len(item_list)
            item_magic_pen_percent = item_magic_pen_percent / len(item_list)
            item_magic_pen_flat = item_magic_pen_flat / len(item_list)
            item_omnivamp = item_omnivamp / len(item_list)

            code = """ITEM_ABILITY_HASTE = {}
ITEM_HP = {}
ITEM_MANA = {}
ITEM_MR = {}
ITEM_AP = {}
ITEM_MANA_REGEN = {}
ITEM_H_S_POWER = {}
ITEM_AD = {}
ITEM_LETHALITY = {}
ITEM_GOLD_PER10 = {}
ITEM_ATTACK_SPEED = {}
ITEM_LIFE_STEAL = {}
ITEM_CRIT_CHANCE = {}
ITEM_HP_REGEN = {}
ITEM_MOVE_SPEED = {}
ITEM_ARMOR = {}
ITEM_ARMOR_PEN = {}
ITEM_MAGIC_PEN_PERCENT = {}
ITEM_MAGIC_PEN_FLAT = {}
ITEM_OMNIVAMP = {}  
            """.format(item_ability_haste, item_hp, item_mana, item_mr, item_ap, item_mana_regen, item_h_s_power,
                       item_ad,
                       item_lethality, item_gold_per10, item_attack_speed, item_life_steal, item_crit_chance,
                       item_hp_regen,
                       item_move_speed, item_armor, item_armor_pen, item_magic_pen_percent, item_magic_pen_flat,
                       item_omnivamp)

            with open("data/item_stats.py", "w") as f:
                f.write(code)
