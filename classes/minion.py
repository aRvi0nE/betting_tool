from classes.scraping import get_minions


class Minion:
    def __init__(self, name, new_patch: bool):
        self.name = name
        data = get_minions.get_data(self.name, new_patch)
        self.hp = data["hp"]
        self.ad = data["ad"]
        self.attack_speed = data["attack_speed"]
        self.rage = data["range"]
        self.armor = data["armor"]
        self.magic_resist = data["magic_resist"]
