from classes.scraping.get_html import get_html_boot


def get_data(name, new_patch: bool):
    """Gets boot stats from scraped html"""
    doc = get_html_boot(name, new_patch)
    movement_speed = output_handler(doc.find("a", string="movement speed").parent)
    try:
        reduction = float(doc.find("span", string="movement speed").next_sibling.next_sibling.text)
        movement_speed = (movement_speed + movement_speed - reduction)/2
    except:
        pass
    return movement_speed


def output_handler(stat):
    text = stat.text
    if "movement speed" in text:
        text = text.replace("movement speed", "")
    return float(text)
