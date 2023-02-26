from classes.champion import Champion
from classes import ability_types
from classes.scraping import get_akshan
from data.settings import *
from data.boot_stats import *
from data.item_stats import *


class Akshan(Champion):
    def __init__(self, new_patch: bool):
        super().__init__("Akshan", new_patch)
        ability_stats = get_akshan.get_data(new_patch)
