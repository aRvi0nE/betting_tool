from classes import boot


def get_averages(new_patch: bool):
    """Gatthers info from boos and calculates their average move speed"""
    boots_list = ["Berserker%27s_Greaves",
                  "Boots_of_Swiftness",
                  "Ionian_Boots_of_Lucidity",
                  "Mercury%27s_Treads",
                  "Mobility_Boots",
                  "Plated_Steelcaps",
                  "Sorcerer%27s_Shoes"]
    boots_move_speed = 0

    if new_patch:
        for boots in boots_list:
            boots_move_speed += boot.Boot(boots, new_patch).move_speed
        boots_move_speed = boots_move_speed / len(boots_list)

        code = f"BOOTS_MOVE_SPEED = {boots_move_speed}"
        with open("data/boot_stats.py", "w") as f:
            f.write(code)

    else:
        try:
            with open("data/boot_stats.py", "r") as f:
                file = f.read()
                print(file)

        except:
            for boots in boots_list:
                boots_move_speed += boot.Boot(boots, new_patch)
            boots_move_speed = boots_move_speed / len(boots_list)

            code = f"BOOTS_MOVE_SPEED = {boots_move_speed}"
            with open("data/boot_stats.py", "w") as f:
                f.write(code)
