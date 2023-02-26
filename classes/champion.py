from classes.scraping import base_stats
from data.item_stats import *
from data.settings import *
from data.boot_stats import *


class Champion:
    def __init__(self, name, new_patch: bool):
        # get base stats
        self.name = name
        data = base_stats.get_data(self.name, new_patch)
        self.base_hp = data["base_hp"]
        self.hp_growth = data["hp_growth"]
        self.base_resource = data["base_resource"]
        self.resource_growth = data["resource_growth"]
        self.base_hp_regen = data["base_hp_regen"] / 5
        self.hp_regen_growth = data["hp_regen_growth"] / 5
        self.base_resource_regen = data["base_resource_regen"] / 5
        self.resource_regen_growth = data["resource_regen_growth"] / 5
        self.base_armor = data["base_armor"]
        self.armor_growth = data["armor_growth"]
        self.base_ad = data["base_ad"]
        self.ad_growth = data["ad_growth"]
        self.base_mr = data["base_mr"]
        self.mr_growth = data["mr_growth"]
        self.crit_damage = data["crit_damage"] / 100
        self.base_move_speed = data["base_move_speed"]
        self.attack_range = data["attack_range"]
        self.base_attack_speed = data["base_attack_speed"]
        self.attack_speed_ratio = data["attack_speed_ratio"]
        self.attack_speed_growth = data["attack_speed_growth"] / 100
        self.hit_box = data["hit_box"]
        self.resource = data["resource"]

        # calculate base average stats
        self.hp = self.average_stat_calculator(self.base_hp, self.hp_growth)
        self.resource = self.average_stat_calculator(self.base_resource, self.resource_growth)
        self.hp_regen = self.average_stat_calculator(self.base_hp_regen, self.hp_regen_growth)
        self.resource_regen = self.average_stat_calculator(self.base_resource_regen, self.resource_regen_growth)
        self.armor = self.average_stat_calculator(self.base_armor, self.armor_growth)
        self.ad = self.average_stat_calculator(self.base_ad, self.ad_growth)
        self.mr = self.average_stat_calculator(self.base_mr, self.mr_growth)
        self.bonus_attack_speed = self.average_stat_calculator(0, self.attack_speed_growth)
        self.attack_speed = self.attack_speed_formula(self.base_attack_speed,
                                                      self.bonus_attack_speed,
                                                      self.attack_speed_ratio)

        # print("hp ", self.hp)
        # print("resource ", self.resource)
        # print("resource regen ", self.resource_regen)
        # print("hp regen ", self.hp_regen)
        # print("armor ", self.armor)
        # print("ad ", self.ad)
        # print("mr ", self.mr)
        # print("attack speed ", self.attack_speed)

        # initiate champion scores
        self.dps = 0
        self.burst = 0
        self.aoe_damage = 0
        self.single_target_damage = 0
        self.tank = 0
        self.sustain = 0
        self.single_target_cc = 0
        self.aoe_cc = 0
        self.speed = 0
        self.reposition = 0
        self.offensive_utility = 0
        self.defensive_utility = 0
        self.tower_damage = 0
        self.range = 0
        self.wave_clear = 0
        self.engage = 0
        self.disengage = 0
        self.counter_engage = 0

        # calculate health score and ad it to self.tank
        self.health_score = \
            (self.hp + NUMBER_OF_ITEMS * ITEM_HP) * (100 + self.armor + NUMBER_OF_ITEMS * ITEM_ARMOR) / 100 + \
            (self.hp + NUMBER_OF_ITEMS * ITEM_HP) * (100 + self.mr + NUMBER_OF_ITEMS * ITEM_MR) / 100
        self.tank += self.health_score * self.hit_box
        # calculate health regen score and ad it to self.sustain
        self.hp_regen_score = self.hp_regen * (1 + NUMBER_OF_ITEMS * ITEM_HP_REGEN)
        self.sustain += self.hp_regen_score
        # calculate damage of each auto attack and add it to self.burst and self.single_target_damage
        self.aa_burst_score = (self.ad + NUMBER_OF_ITEMS * ITEM_AD) * (
                    (NUMBER_OF_ITEMS * ITEM_CRIT_CHANCE * (1 + self.crit_damage))
                    + (1 - NUMBER_OF_ITEMS * ITEM_CRIT_CHANCE))
        self.burst += self.aa_burst_score
        self.single_target_damage += self.aa_burst_score
        # calculate dps of auto attacks and add it to self.dps
        self.aa_dps_score = self.aa_burst_score * self.attack_speed
        self.dps += self.aa_dps_score
        self.wave_clear += self.aa_dps_score
        # calculate tower damage of autos since crits don't work on structures
        self.tower_damage += (self.ad + NUMBER_OF_ITEMS * ITEM_AD) * self.attack_speed
        # calculate move speed with boots and items
        self.speed += (self.base_move_speed + BOOTS_MOVE_SPEED) * (1 + NUMBER_OF_ITEMS * ITEM_MOVE_SPEED)
        # add range from auto attacks to range self.range
        self.range += self.attack_range

    @staticmethod
    def average_stat_calculator(base_stat, stat_growth):
        """Calculates the average value of a stat throughout the game (lvl 1 to lvl 18), using Riot's goofy formula for
        stat growth"""
        s = 0
        for i in range(1, 19):
            s += base_stat + stat_growth * (i - 1) * (0.7025 + 0.0175 * (i - 1))
        return s / 18

    @staticmethod
    def attack_speed_formula(base_attack_speed, bonus_attack_speed, attack_speed_ratio):
        """Riot's attack speed formula"""
        if attack_speed_ratio == 0:
            attack_speed_ratio = 1
        attack_speed = base_attack_speed * (1 + bonus_attack_speed * attack_speed_ratio)
        return attack_speed

    def show_stats(self):
        print("dps ", self.dps)
        print("burst ", self.burst)
        print("aoe damage ", self.aoe_damage)
        print("single target damage ", self.single_target_damage)
        print("tank ", self.tank)
        print("sustain ", self.sustain)
        print("single target cc ", self.single_target_cc)
        print("aoe cc ", self.aoe_cc)
        print("speed ", self.speed)
        print("reposition ", self.reposition)
        print("offensive utility ", self.offensive_utility)
        print("defensive utility ", self.defensive_utility)
        print("tower damage ", self.tower_damage)
        print("range ", self.range)
        print("wave clear ", self.wave_clear)
        print("engage ", self.engage)
        print("disengage ", self.disengage)
        print("counter engage ", self.counter_engage)
        print("\n")
