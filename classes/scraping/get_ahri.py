from classes.scraping.get_html import get_html_champion


def get_data(new_patch: bool):
    doc = get_html_champion("Ahri", new_patch)

    # passive
    p_stack_threshold = output_handler(doc.find("span", id="Essence_Theft").
                                       parent.
                                       parent.
                                       parent.
                                       find("a", string="monster").
                                       next_element.
                                       next_element)[0]
    p_minion_flat_heal = output_handler(doc.find("span", id="Essence_Theft").
                                        parent.
                                        parent.
                                        parent.
                                        find("a", title="Healing").
                                        parent.
                                        parent.
                                        next_sibling.
                                        next_sibling)[0]
    p_minion_heal_scale_ap = output_handler(doc.find("span", id="Essence_Theft").
                                            parent.
                                            parent.
                                            parent.
                                            find("a", title="Healing").
                                            parent.
                                            parent.
                                            next_sibling.
                                            next_sibling.next_sibling.next_sibling)[0] / 100
    p_champion_flat_heal = output_handler(doc.find("span", id="Essence_Theft").
                                          parent.
                                          parent.
                                          parent.
                                          find("span", attrs={"data-tip": "Takedown"}).
                                          parent.
                                          find("span", string="heal").
                                          next_sibling.
                                          next_sibling)[0]
    p_champion_heal_scale_ap = output_handler(doc.find("span", id="Essence_Theft").
                                              parent.
                                              parent.
                                              parent.
                                              find("span", attrs={"data-tip": "Takedown"}).
                                              parent.
                                              find("span", string="heal").
                                              next_sibling.
                                              next_sibling.
                                              next_sibling.
                                              next_sibling)[0] / 200
    p = {"stack_threshold": p_stack_threshold,
         "minion_flat_heal": p_minion_flat_heal,
         "minion_heal_scale_ap": p_minion_heal_scale_ap,
         "champion_flat_heal": p_champion_flat_heal,
         "champion_heal_scale_ap": p_champion_heal_scale_ap}

    # q
    q_cooldown = output_handler(doc.find("span", id="Orb_of_Deception").
                                parent.
                                parent.
                                parent.
                                find("h3", string="COOLDOWN:").
                                next_sibling.
                                next_sibling)[0]
    q_cast_time = output_handler(doc.find("span", id="Orb_of_Deception").
                                 parent.
                                 parent.
                                 parent.
                                 find("h3", string="CAST TIME:").
                                 next_sibling.
                                 next_sibling)[0]
    q_rage = output_handler(doc.find("span", id="Orb_of_Deception").
                            parent.
                            parent.
                            parent.
                            find("h3", string="RANGE:").
                            next_sibling.
                            next_sibling)[0]
    q_width = output_handler(doc.find("span", id="Orb_of_Deception").
                             parent.
                             parent.
                             parent.
                             find("h3", string="WIDTH:").
                             next_sibling.
                             next_sibling)[0]
    q_flat_damage, \
    q_scale_ap = output_handler(doc.find("span", id="Orb_of_Deception").
                                parent.
                                parent.
                                parent.
                                find("span", string="Damage Per Pass:").
                                parent.
                                next_sibling)
    q = {"cooldown": q_cooldown,
         "cast_time": q_cast_time,
         "range": q_rage,
         "width": q_width,
         "flat_damage": q_flat_damage,
         "scale_ap": q_scale_ap / 100}

    # w
    w_cooldown = output_handler(doc.find("span", id="Fox-Fire").
                                parent.
                                parent.
                                find("h3", string="COOLDOWN:").
                                next_sibling.
                                next_sibling)[0]
    w_cast_time = output_handler(doc.find("span", id="Fox-Fire").
                                 parent.
                                 parent.
                                 find("h3", string="CAST TIME:").
                                 next_sibling.
                                 next_sibling)[0]
    w_range = float(doc.find("span", id="Fox-Fire").
                    parent.
                    parent.
                    find("h3", string="EFFECT RADIUS:").
                    next_sibling.
                    next_sibling.text.split()[-1])
    w_speed, \
    w_speed_duration, \
    w_ability_duration = output_handler(doc.find("span", id="Fox-Fire").
                                        parent.
                                        parent.
                                        parent.
                                        find("span", string="Active:").
                                        parent)
    w_minion_double_damage_threshold = output_handler(doc.find("span", id="Fox-Fire").
                                                      parent.
                                                      parent.
                                                      parent.
                                                      find("a", title="Health").
                                                      next_sibling.
                                                      next_sibling)[0] / 100
    w_damage_multiplier_per_subsequent_hit = output_handler(doc.find("span", id="Fox-Fire").
                                                            parent.
                                                            parent.
                                                            parent.
                                                            find("table").
                                                            parent.
                                                            next_sibling.
                                                            next_sibling.
                                                            next_sibling.
                                                            find("div"))[0] / 100
    w_flat_damage, \
    w_scale_ap = output_handler(doc.find("span", id="Fox-Fire").
                                parent.
                                parent.
                                parent.
                                find("span", string="Magic Damage:").
                                parent.
                                next_sibling)
    w = {"cooldown": w_cooldown,
         "cast_time": w_cast_time,
         "range": w_range,
         "bonus_move_speed": w_speed / 100,
         "move_speed_duration": w_speed_duration,
         "ability_duration": w_ability_duration,
         "minion_double_damage_threshold": w_minion_double_damage_threshold,
         "damage_multiplier_per_subsequent_hit": w_damage_multiplier_per_subsequent_hit,
         "flat_damage": w_flat_damage,
         "scale_ap": w_scale_ap / 100}

    # e
    e_cooldown = output_handler(doc.find("span", id="Charm").
                                parent.
                                parent.
                                parent.
                                find("h3", string="COOLDOWN:").
                                next_sibling.
                                next_sibling)[0]
    e_cast_time = output_handler(doc.find("span", id="Charm").
                                 parent.
                                 parent.
                                 parent.
                                 find("h3", string="CAST TIME:").
                                 next_sibling.
                                 next_sibling)[0]
    e_range = output_handler(doc.find("span", id="Charm").
                             parent.
                             parent.
                             parent.
                             find("h3", string="RANGE:").
                             next_sibling.
                             next_sibling)[0]
    e_flat_damage, \
    e_damage_scale_ap = output_handler(doc.find("span", id="Charm").
                                       parent.
                                       parent.
                                       parent.
                                       find("span", string="Magic Damage:").
                                       parent.
                                       next_sibling)
    e_stun_duration = output_handler(doc.find("span", id="Charm").
                                     parent.
                                     parent.
                                     parent.
                                     find("span", string="Disable Duration:").
                                     parent.
                                     next_sibling)[0]
    e = {"cooldown": e_cooldown,
         "cast_time": e_cast_time,
         "range": e_range,
         "flat_damage": e_flat_damage,
         "damage_scale_ap": e_damage_scale_ap / 100,
         "stun_duration": e_stun_duration}

    # R
    r_cooldown = output_handler(doc.find("span", id="Spirit_Rush").
                                parent.
                                parent.
                                parent.
                                find("h3", string="COOLDOWN:").
                                next_sibling.
                                next_sibling)[0]
    r_cast_time = output_handler(doc.find("span", id="Spirit_Rush").
                                 parent.
                                 parent.
                                 parent.
                                 find("h3", string="CAST TIME:").
                                 next_sibling.
                                 next_sibling)[0]
    r_dash_distance = output_handler(doc.find("span", id="Spirit_Rush").
                                     parent.
                                     parent.
                                     parent.
                                     find("h3", string="TARGET RANGE:").
                                     next_sibling.
                                     next_sibling)[0]
    r_range = output_handler(doc.find("span", id="Spirit_Rush").
                             parent.
                             parent.
                             parent.
                             find("h3", string="EFFECT RADIUS:").
                             next_sibling.
                             next_sibling)[0]
    r_number_of_hits = output_handler(doc.find("span", id="Spirit_Rush").
                                      parent.
                                      parent.
                                      parent.
                                      find("span", string="Active:").
                                      next_sibling.
                                      next_sibling.
                                      next_sibling.
                                      next_sibling.
                                      next_sibling)[0]
    r_duration = output_handler(doc.find("span", id="Spirit_Rush").
                                parent.
                                parent.
                                parent.
                                find("i", string="Spirit Rush").
                                next_element.
                                next_element)[0]
    r_reset_extension = output_handler(doc.find("span", id="Spirit_Rush").
                                       parent.
                                       parent.
                                       parent.
                                       find("span", string="Essence Theft").
                                       parent.
                                       parent.
                                       next_sibling.
                                       next_sibling.
                                       next_sibling)[0]
    r_flat_damage = output_handler(doc.find("span", id="Spirit_Rush").
                                   parent.
                                   parent.
                                   parent.
                                   find("span", string="Magic damage:").
                                   parent.
                                   next_sibling)[0]
    r_damage_scape_ap = output_handler(doc.find("span", id="Spirit_Rush").
                                       parent.
                                       parent.
                                       parent.
                                       find("span", string="Magic damage:").
                                       parent.
                                       next_sibling.find("span"))[0] / 100
    r = {"cooldown": r_cooldown,
         "cast_time": r_cast_time,
         "dash_distance": r_dash_distance,
         "range": r_range,
         "number_of_hits": r_number_of_hits,
         "duration": r_duration,
         "reset_extension": r_reset_extension,
         "flat_damage": r_flat_damage,
         "damage_scale_ap": r_damage_scape_ap}

    return {"p": p, "q": q, "w": w, "e": e, "r": r}


def output_handler(stat) -> list:
    try:
        text = stat.text
        if "is active extends the recast duration by and up to" in text:
            text = text.replace("is active extends the recast duration by and up to", "")
            text = text.replace(" seconds, and grants an additional recast, storing up to 3 recasts at a time.", "")
        if "can be recast twice more within" in text:
            text = text.replace("can be recast twice more within", "")
            text = text.replace("seconds of the activation at no additional cost, with a 1 second", "")
        if " to the target location and then fires essence bolts to up to" in text:
            text = text.replace(" to the target location and then fires essence bolts to up to", "")
            text = text.replace("nearby", "")
        if "Subsequent flames on a single target deal" in text:
            text = text.replace("Subsequent flames on a single target deal", "")
            text = text.replace("damage.", "")
        if "Active: Ahri gains" in text:
            text = text.replace("Active: Ahri gains", "")
            text = text.replace("% bonus movement speed that decays over", "")
            text = text.replace("seconds and conjures three flames which orbit her clockwise for up to", "")
            text = text.replace("seconds.", "")
        if ". At" in text:
            text = text.replace(". At", "")
            text = text.replace(" stacks, she consumes them to", "")
        if "maximum health" in text:
            text = text.replace("maximum health", "")
        if "−" in text:
            text = text.replace("−", "")
            text = text.replace("(based on level)", "")
            text = text.split()
            text = str((float(text[0]) + float(text[1])) / 2)
        if "%" in text:
            text = text.replace("%", "")
        if "(+" in text:
            try:
                text = text.replace("/", "")
                text = text.split()
                s = 0
                t = 0
                for i in range(5):
                    s += float(text[i])
                    try:
                        t += float(text[i + 6])
                    except:
                        t += float(text[6])
                text = str(s / 5) + " " + str(t / 5)
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
