import math

from classes.scraping.get_html import get_html_champion


def get_data(new_patch: bool):
    doc = get_html_champion("Akali", new_patch)

    # passive
    p_bonus_move_speed = output_handler(doc.find("span", id="Assassin's_Mark").
                                        parent.
                                        parent.
                                        parent.
                                        find("a", title="Movement speed").
                                        parent.
                                        previous_sibling.
                                        previous_sibling)[0] / 100
    p_speed_duration, \
    p_duration = output_handler(doc.find("span", id="Assassin's_Mark").
                                parent.
                                parent.
                                parent.
                                find("i", string="Swinging Kama").
                                parent)
    p_flat_damage = output_handler(doc.find("span", id="Assassin's_Mark").
                                   parent.
                                   parent.
                                   parent.
                                   find("a", title="Range").
                                   parent.
                                   next_sibling.
                                   next_sibling)[0]
    p_damage_scale_ad = output_handler(doc.find("span", id="Assassin's_Mark").
                                       parent.
                                       parent.
                                       parent.
                                       find("a", title="Range").
                                       parent.
                                       next_sibling.
                                       next_sibling.
                                       next_sibling.
                                       next_sibling)[0] / 100
    p_damage_scale_ap = output_handler(doc.find("span", id="Assassin's_Mark").
                                       parent.
                                       parent.
                                       parent.
                                       find("a", title="Range").
                                       parent.
                                       next_sibling.
                                       next_sibling.
                                       next_sibling.
                                       next_sibling.
                                       next_sibling.
                                       next_sibling)[0] / 100
    p = {"bonus_move_speed": p_bonus_move_speed,
         "speed_duration": p_speed_duration,
         "duration": p_duration,
         "flat_damage": p_flat_damage,
         "damage_scale_ad": p_damage_scale_ad,
         "damage_scale_ap": p_damage_scale_ap}

    # q
    q_cost = output_handler(doc.find("span", id="Five_Point_Strike").
                            parent.
                            parent.
                            parent.find("h3", string="COST:").
                            next_sibling.
                            next_sibling)[0]
    q_cooldown = output_handler(doc.find("span", id="Five_Point_Strike").
                                parent.
                                parent.
                                parent.find("h3", string="COOLDOWN:").
                                next_sibling.
                                next_sibling)[0]
    q_cast_time = output_handler(doc.find("span", id="Five_Point_Strike").
                                 parent.
                                 parent.
                                 parent.find("h3", string="CAST TIME:").
                                 next_sibling.
                                 next_sibling)[0]
    q_range, \
    q_slow_width = (doc.find("span", id="Five_Point_Strike").
                    parent.
                    parent.
                    parent.find("h3", string="TARGET RANGE:").
                    next_sibling.
                    next_sibling.
                    text.
                    replace("/", "").
                    split())
    q_angle = output_handler(doc.find("span", id="Five_Point_Strike").
                             parent.
                             parent.
                             parent.find("h3", string="ANGLE:").
                             next_sibling.
                             next_sibling)[0]
    q_slow_value, \
    q_slow_duration = output_handler(doc.find("span", id="Five_Point_Strike").
                                     parent.
                                     parent.
                                     parent.
                                     find("span", attrs={"data-tip": "Slow"}).
                                     parent)
    q_flat_damage, \
    q_scale_ad, \
    q_scale_ap = output_handler(doc.find("span", id="Five_Point_Strike").
                                parent.
                                parent.
                                parent.
                                find("span", string="Magic Damage:").
                                parent.
                                next_sibling)
    q = {"cost": q_cost,
         "cooldown": q_cooldown,
         "cast_time": q_cast_time,
         "range": float(q_range),
         "slow_width": float(q_slow_width),
         "angle": q_angle,
         "slow_value": q_slow_value / 100,
         "slow_duration": q_slow_duration,
         "flat_damage": q_flat_damage,
         "scale_ap": q_scale_ap / 100,
         "scale_ad": q_scale_ad / 100}

    # w
    w_cooldown = output_handler(doc.find("span", id="Twilight_Shroud").
                                parent.
                                parent.
                                parent.
                                find("h3", string="COOLDOWN:").
                                next_sibling.
                                next_sibling)[0]
    w_cast_time = output_handler(doc.find("span", id="Twilight_Shroud").
                                 parent.
                                 parent.
                                 parent.
                                 find("h3", string="CAST TIME:").
                                 next_sibling.
                                 next_sibling)[0]
    w_energy = output_handler(doc.find("span", id="Twilight_Shroud").
                              parent.
                              parent.
                              parent.
                              find("a", title="Energy").
                              next_sibling.
                              next_sibling)[0]
    w_speed_duration = output_handler(doc.find("span", id="Twilight_Shroud").
                                      parent.
                                      parent.
                                      parent.
                                      find("a", title="Movement speed").
                                      parent.
                                      next_sibling)[0]
    w_bonus_move_speed = output_handler(doc.find("span", id="Twilight_Shroud").
                                        parent.
                                        parent.
                                        parent.
                                        find("span", string="Bonus Movement Speed:").
                                        parent.
                                        next_sibling)[0] / 100
    w_duration = output_handler(doc.find("span", id="Twilight_Shroud").
                                parent.
                                parent.
                                parent.
                                find("span", string="Shroud Duration:").
                                parent.
                                next_sibling)[0]
    w_radius_1, \
    slash, \
    w_radius_2 = (doc.find("span", id="Twilight_Shroud").
                  parent.
                  parent.
                  parent.
                  find("h3", string="EFFECT RADIUS:").
                  next_sibling.
                  next_sibling.text.split())
    w_invisible_area = math.pi * (float(w_radius_2) ** 2 - float(w_radius_1) ** 2)

    w = {"cooldown": w_cooldown,
         "cast_time": w_cast_time,
         "energy": w_energy,
         "speed_duration": w_speed_duration,
         "bonus_move_speed": w_bonus_move_speed,
         "duration": w_duration,
         "area": w_invisible_area}

    # e
    e_cost = output_handler(doc.find("span", id="Shuriken_Flip").
                            parent.
                            parent.
                            parent.
                            find("h3", string="COST:").
                            next_sibling.
                            next_sibling)[0]
    e_cooldown = output_handler(doc.find("span", id="Shuriken_Flip").
                                parent.
                                parent.
                                parent.
                                find("h3", string="COOLDOWN:").
                                next_sibling.
                                next_sibling)[0]
    e_cast_time_1, \
    slash, \
    e_cast_time_2 = (doc.find("span", id="Shuriken_Flip").
                     parent.
                     parent.
                     parent.
                     find("h3", string="CAST TIME:").
                     next_sibling.
                     next_sibling.
                     text.
                     split())
    e_cast_time = float(e_cast_time_1) + float(e_cast_time_2)
    e_range = output_handler(doc.find("span", id="Shuriken_Flip").
                             parent.
                             parent.
                             parent.
                             find("h3", string="TARGET RANGE:").
                             next_sibling.
                             next_sibling)[0]
    e_reveal_duration = output_handler(doc.find("span", id="Shuriken_Flip").
                                       parent.
                                       parent.
                                       parent.
                                       find("i", string="Shuriken Flip").
                                       previous_element)[0]
    e_flip_length = output_handler(doc.find("div", class_="skill skill_e").
                                   next_sibling.
                                   next_sibling.
                                   next_sibling.
                                   find("b", string="Akali").
                                   parent.
                                   next_sibling.
                                   next_sibling.
                                   next_sibling.
                                   next_sibling.
                                   next_sibling.
                                   next_sibling.
                                   next_sibling.
                                   next_sibling.
                                   next_sibling.
                                   next_sibling)[0]
    e_flat_damage_1, \
    e_damage_scale_ad_1, \
    e_damage_scale_ap_1 = output_handler(doc.find("span", id="Shuriken_Flip").
                                         parent.
                                         parent.
                                         parent.find("span", string="Magic Damage:").
                                         parent.
                                         next_sibling)
    e_flat_damage_2, \
    e_damage_scale_ad_2, \
    e_damage_scale_ap_2 = output_handler(doc.find("span", id="Shuriken_Flip").
                                         parent.
                                         parent.
                                         parent.
                                         find_all("span", string="Magic Damage:")[1].
                                         parent.
                                         next_sibling)
    e = {"cost": e_cost,
         "cooldown": e_cooldown,
         "cast_time": e_cast_time,
         "range": e_range,
         "reveal_duration": e_reveal_duration,
         "flip_length": e_flip_length,
         "flat_damage_1": e_flat_damage_1,
         "damage_scale_ad_1": e_damage_scale_ad_1 / 100,
         "damage_scale_ap_1": e_damage_scale_ap_1 / 100,
         "flat_damage_2": e_flat_damage_2,
         "damage_scale_ad_2": e_damage_scale_ad_2 / 100,
         "damage_scale_ap_2": e_damage_scale_ap_2 / 100}

    # r
    r_cooldown = output_handler(doc.find("span", id="Perfect_Execution").
                                parent.
                                parent.
                                parent.
                                find("h3", string="COOLDOWN:").
                                next_sibling.
                                next_sibling)[0]
    r_cast_time = output_handler(doc.find("span", id="Perfect_Execution").
                                 parent.
                                 parent.
                                 parent.
                                 find("h3", string="CAST TIME:").
                                 next_sibling.
                                 next_sibling)[0]
    r_1_range = output_handler(doc.find("span", id="Perfect_Execution").
                               parent.
                               parent.
                               parent.
                               find("h3", string="TARGET RANGE:").
                               next_sibling.
                               next_sibling)[0]
    r_collision_radius = output_handler(doc.find("span", id="Perfect_Execution").
                                        parent.
                                        parent.
                                        parent.
                                        find("h3", string="COLLISION RADIUS:").
                                        next_sibling.
                                        next_sibling)[0]
    r_1_dash_distance = output_handler(doc.find("span", id="Perfect_Execution").
                                       parent.
                                       parent.
                                       parent.
                                       find("a", string="dashes").
                                       parent.
                                       next_sibling)[0]
    r_cooldown_between_casts, \
    r_duration = output_handler(doc.find("span", id="Perfect_Execution").
                                parent.
                                parent.
                                parent.
                                find("i", string="Perfect Execution").
                                parent)
    r_2_dash_distance = output_handler(doc.find("span", id="Perfect_Execution").
                                       parent.
                                       parent.
                                       parent.
                                       find_all("a", string="dashes")[1].
                                       parent.
                                       next_sibling.
                                       next_sibling)[0]
    r_2_missing_hp_damage_scale = (doc.find("span", id="Perfect_Execution").
                                   parent.
                                   parent.
                                   parent.
                                   find("span", attrs={"data-top_label": "target's missing health"}).
                                   get("data-displayformula").
                                   split()[0].
                                   replace("%", ""))
    r_1_flat_damage_1, \
    r_1_flat_damage_2, \
    r_1_flat_damage_3, \
    r_1_damage_scale_bonus_ad, \
    r_1_damage_scale_ap = (doc.find("span", id="Perfect_Execution").
                           parent.
                           parent.
                           parent.
                           find("span", string="Magic Damage:").
                           parent.
                           next_sibling.
                           text.replace("/", "").
                           replace("(+", "").
                           replace("%", "").
                           replace("bonus AD)", "").
                           replace("AP)", "").
                           split())
    r_1_flat_damage = (float(r_1_flat_damage_1) + float(r_1_flat_damage_2) + float(r_1_flat_damage_3)) / 3
    r_2_flat_damage_1,\
    r_2_flat_damage_2,\
    r_2_flat_damage_3,\
    r_2_damage_scale_ap= (doc.find("span", id="Perfect_Execution").
                           parent.
                           parent.
                           parent.
                           find("span", string="Minimum Magic Damage:").parent.next_sibling.text.replace("/", "").replace("(+", "").replace("% AP)", "").split())
    r_2_flat_damage = (float(r_2_flat_damage_1) + float(r_2_flat_damage_2) + float(r_2_flat_damage_3)) / 3
    r = {"cooldown": r_cooldown,
         "cast_time": r_cast_time,
         "range_1": r_1_range,
         "collision_radius": r_collision_radius,
         "dash_distance_1": r_1_dash_distance,
         "cooldown_between_casts": r_cooldown_between_casts,
         "dash_distance_2": r_2_dash_distance,
         "damage_scale_missing_health_2": float(r_2_missing_hp_damage_scale)/100,
         "flat_damage_1": r_1_flat_damage,
         "damage_scale_bonus_ad_1": float(r_1_damage_scale_bonus_ad)/100,
         "damage_scale_ap_1": float(r_1_damage_scale_ap)/100,
         "flat_damage_2": r_2_flat_damage,
         "damage_scale_ap_2": float(r_2_damage_scale_ap)/100}

    return {"p": p, "q": q, "w": w, "e": e, "r": r}


def output_handler(stat) -> list:
    try:
        text = stat.text
        if "Perfect Execution can be recast after a" in text:
            text = text.replace("Perfect Execution can be recast after a", "")
            text = text.replace("-second static cooldown within", "")
            text = text.replace("seconds of the first activation.", "")
        if " units in the direction of the target enemy" in text:
            text = text.replace(" units in the direction of the target enemy", "")
        if "None (" in text:
            text = text.replace("None (", "")
            text = text.replace(") / None", "")
        if "Akali will dash backwards up-to" in text:
            text = text.replace("Akali will dash backwards up-to", "")
            text = text.replace("units in a straight line. This dash can cross terrain if the end point is beyond it. "
                                "If she would end the dash inside terrain, she will instead look for a location  in "
                                "either direction left or right that is outside of terrain and dash there. If there "
                                "is no such location, she will dash only up to the wall at her normal speed, "
                                "ending the dash early.", "")
        if "section hit for" in text:
            text = text.replace("section hit for", "")
            text = text.replace("seconds, during which", "")
        if "that decays over" in text:
            text = text.replace("that decays over", "")
            text = text.replace("seconds. She also detonates a smoke bomb a fixed distance away in the target "
                                "direction, creating a circular shroud that expands over the next 5 seconds into a "
                                "ring. The shroud does not permeate terrain, and will expand toward nearby enemy "
                                "champions. While the shroud is active,", "")
        if "Active: Akali unleashes kunais in a cone" in text:
            text = text.replace(
                "Active: Akali unleashes kunais in a cone in the target direction, dealing magic damage to enemies hit. Targets at maximum range are also  slowed by",
                "")
            text = text.replace("for", "")
            text = text.replace("seconds.", "")
        if "When Akali exits the ring, for" in text:
            text = text.replace("When Akali exits the ring, for", "")
            text = text.replace(
                "seconds, she regains the bonus movement speed while facing nearby enemy champions and becomes "
                "empowered with Swinging Kama for",
                "")
            text = text.replace("seconds, during which she cannot create another ring.", "")
        if "(based on level)" in text:
            text = text.replace("(based on level)", "")
        if "energy" in text:
            text = text.replace("energy", "")
        if "−" in text:
            text = text.replace("−", "")
            text = text.replace("(based on level)", "")
            text = text.split()
            text = str((float(text[0]) + float(text[1])) / 2)
        if "%" in text:
            text = text.replace("%", "")
        if "°" in text:
            text = text.replace("°", "")
        if "(+" in text:
            try:
                text = text.replace("/", "")
                text = text.split()
                s = 0
                t = 0
                u = 0
                for i in range(5):
                    s += float(text[i])
                    try:
                        t += float(text[i + 6])
                        u += float(text[i + 11])
                    except:
                        t = float(text[6]) * 5
                        u = float(text[9]) * 5
                text = str(s / 5) + " " + str(t / 5) + " " + str(u / 5)
            except:
                text = text[1]
        if "/" in text:
            text = text.replace("/", "")
            text = text.split()
            s = 0
            for number in text:
                s += float(number)
            text = str(s / len(text))
        text = text.split()
        for i in range(len(text)):
            text[i] = float(text[i])
        return text
    except:
        return [0]


#get_data(False)
