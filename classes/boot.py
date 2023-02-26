from classes.scraping import get_boot


class Boot:
    def __init__(self, name, new_patch: bool):
        self.name = name
        data = get_boot.get_data(self.name, new_patch)
        self.move_speed = data
