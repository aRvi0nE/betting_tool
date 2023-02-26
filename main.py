from check_patch import check_patch
import all_boots
import all_champions
import all_items
import all_minions
from gui.assets.graphs import champion_scores
from gui import gui_main

# check if patch has changed
new_patch = check_patch()

# get average stats from champs boots items and minions
all_boots.get_averages(new_patch)
all_champions.get_averages(new_patch)
all_items.get_averages(new_patch)
all_minions.get_averages(new_patch)

# get individual champion instances dictionary
champion_instances = all_champions.get_champion_instances()

champion_scores.graph(champion_instances)

gui_main.run()
