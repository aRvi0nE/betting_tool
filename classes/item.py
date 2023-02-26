from classes.scraping import get_items


class Item:
    def __init__(self, name, new_patch: bool):
        self.name = name
        # get item stats
        data = get_items.get_data(self.name, new_patch)
        self.ability_haste = data["ability_haste"]
        self.hp = data["hp"]
        self.mana = data["mana"]
        self.mr = data["mr"]
        self.ap = data["ap"]
        self.mana_regen = data["mana_regen"]/100/5
        self.h_s_power = data["h_s_power"]/100
        self.ad = data["ad"]
        self.lethality = data["lethality"]
        self.gold_per10 = data["gold_per10"]
        self.attack_speed = data["attack_speed"]/100
        self.life_steal = data["life_steal"]/100
        self.crit_chance = data["crit_chance"]/100
        self.hp_regen = data["hp_regen"]/100/5
        self.move_speed = data["move_speed"]/100
        self.armor = data["armor"]
        self.armor_pen = data["armor_pen"]/100
        self.magic_pen_percent = data["magic_pen_percent"]/100
        self.magic_pen_flat = data["magic_pen_flat"]
        self.omnivamp = data["omnivamp"]/100

        # print("ability haste ", self.ability_haste)
        # print("hp ", self.hp)
        # print("mana ", self.mana)
        # print("mr ", self.mr)
        # print("ap ", self.ap)
        # print("mana regen ", self.mana_regen)
        # print("h&s power ", self.h_s_power)
        # print("ad", self.ad)
        # print("lethality ", self.lethality)
        # print("gold per 10 ", self.gold_per10)
        # print("attack speed ", self.attack_speed)
        # print("life steal ", self.life_steal)
        # print("crit chance ", self.crit_chance)
        # print("hp regen ", self.hp_regen)
        # print("move speed ", self.move_speed)
        # print("armor ", self.armor)
        # print("armor pen ", self.armor_pen)
        # print("magic pen percent ", self.magic_pen_percent)
        # print("magic pen flat ", self.magic_pen_flat)
        # print("omnivamp  ", self.omnivamp)



