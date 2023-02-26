import math

from classes.scraping.get_html import get_html_champion


def get_data(new_patch: bool):
    """Gets stats of aatrox's abilities"""
    doc = get_html_champion("Aatrox", new_patch)

    # passive
    passive_static_cooldown = output_handler(doc.find("span", string="Deathbringer Stance").
                                             parent.
                                             parent.
                                             parent.
                                             find("span", string="STATIC").
                                             parent.
                                             parent.
                                             find("div", attrs={"class": "pi-data-value pi-font"}))[0]
    passive_bonus_range = output_handler(doc.find("span", string="Deathbringer Stance").
                                         parent.
                                         parent.
                                         parent.
                                         find("a", attrs={"title": "Range"}).
                                         parent)[0]
    passive_scale_target_max_hp = output_handler(doc.find("span", string="Deathbringer Stance").
                                                 parent.
                                                 parent.
                                                 parent.
                                                 find("b", string="maximum").
                                                 parent)[0] / 100
    passive_post_mitigation_heal = output_handler(doc.find("span", string="Deathbringer Stance").
                                                  parent.
                                                  parent.
                                                  parent.
                                                  find("a", string="heals").
                                                  next_element.
                                                  next_element)[0] / 100
    passive_cooldown_reduction_per_hit, \
    passive_cooldown_reduction_per_special_hit = output_handler(doc.find("span", string="Deathbringer Stance").
                                                                parent.
                                                                parent.
                                                                parent.
                                                                find("i", string="Deathbringer Stance").
                                                                next_element.
                                                                next_element)
    passive = {"static_cooldown": passive_static_cooldown,
               "bonus_range": passive_bonus_range,
               "scale_target_max_hp": passive_scale_target_max_hp,
               "post_mitigation_heal": passive_post_mitigation_heal,
               "cooldown_reduction_per_hit": passive_cooldown_reduction_per_hit,
               "cooldown_reduction_per_special_hit": passive_cooldown_reduction_per_special_hit}

    # Q
    q_cooldown = output_handler(doc.find("span", id="The_Darkin_Blade").
                                parent.
                                parent.
                                parent.
                                find("h3", string="COOLDOWN:").
                                next_sibling.
                                next_sibling)[0]
    q_cast_time = output_handler(doc.find("span", id="The_Darkin_Blade").
                                 parent.
                                 parent.
                                 parent.
                                 find("h3", string="CAST TIME:").
                                 next_sibling.
                                 next_sibling)[0]
    q_cooldown_between_casts = output_handler(doc.find("span", id="The_Darkin_Blade").
                                              parent.
                                              parent.
                                              parent.
                                              find("i", string="The Darkin Blade").
                                              next_sibling)[0]
    q_special_hit_bonus_damage, \
    q_stun_duration, \
    q_damage_ramp_up = output_handler(doc.find("span", id="The_Darkin_Blade").
                                      parent.
                                      parent.
                                      parent.
                                      find("a", string="knocked up").
                                      parent.
                                      parent)
    q1_area, \
    q1_range = output_handler(doc.find("span", id="The_Darkin_Blade").
                              parent.
                              parent.
                              parent.
                              find("b", string="First Cast:").
                              parent.
                              next_sibling.
                              next_sibling.
                              next_sibling)
    q1_flat_damage, \
    q1_scale_ad = output_handler(doc.find("span", id="The_Darkin_Blade").
                                 parent.
                                 parent.
                                 parent.
                                 find("span", string="First Cast Damage:").
                                 parent.
                                 next_sibling)
    q2_area, \
    q2_range = output_handler(doc.find("span", id="The_Darkin_Blade").
                              parent.
                              parent.
                              parent.
                              find("span", string="Second Cast:").
                              parent)
    q3_area, \
    q3_range = output_handler(doc.find("span", id="The_Darkin_Blade").
                              parent.
                              parent.
                              parent.
                              find("span", string="Third Cast:").
                              parent)
    q_minion_damage_multiplier = output_handler(doc.find("span", id="The_Darkin_Blade").
                                                parent.
                                                parent.
                                                parent.
                                                find("a", string="minions").
                                                parent.
                                                parent)[0] / 100
    q = {"cooldown": q_cooldown,
         "cast_time": q_cast_time,
         "cooldown_between_casts": q_cooldown_between_casts,
         "special_hit_bonus_damage": q_special_hit_bonus_damage / 100,
         "damage_ramp_up": q_damage_ramp_up / 100,
         "stun_duration": q_stun_duration,
         "area1": q1_area,
         "area2": q2_area,
         "area3": q3_area,
         "range1": q1_range,
         "range2": q2_range,
         "range3": q3_range,
         "flat_damage": q1_flat_damage,
         "scale_ad": q1_scale_ad / 100,
         "minion_damage_multiplier": q_minion_damage_multiplier}

    # W
    w_cooldown = output_handler(doc.find("span", id="Infernal_Chains").
                                parent.
                                parent.
                                parent.
                                find("h3", string="COOLDOWN:").
                                next_sibling.
                                next_sibling)[0]
    w_cast_time = output_handler(doc.find("span", id="Infernal_Chains").
                                 parent.
                                 parent.
                                 parent.
                                 find("h3", string="CAST TIME:").
                                 next_sibling.
                                 next_sibling)[0]
    w_range = output_handler(doc.find("span", id="Infernal_Chains").
                             parent.
                             parent.
                             parent.
                             find("h3", string="RANGE:").
                             next_sibling.
                             next_sibling)[0]
    w_slow_value, \
    w_slow_duration = output_handler(doc.find("span", id="Infernal_Chains").
                                     parent.
                                     parent.
                                     parent.
                                     find("span", string="Active:").
                                     parent)
    w_reveal_duration = output_handler(doc.find("span", id="Infernal_Chains").
                                       parent.
                                       parent.
                                       parent.
                                       find("span", attrs={"data-tip": "True sight"}).
                                       parent)[0]
    w_flat_damage, \
    w_scale_ad = output_handler(doc.find("span", id="Infernal_Chains").
                                parent.
                                parent.
                                parent.
                                find("span", string="Physical Damage:").
                                parent.
                                next_sibling)
    w = {"cooldown": w_cooldown,
         "cast_time": w_cast_time,
         "range": w_range,
         "slow_value": w_slow_value / 100,
         "slow_duration": w_slow_duration,
         "reveal_duration": w_reveal_duration,
         "flat_damage": w_flat_damage,
         "scale_ad": w_scale_ad / 100}

    # E
    e_cooldown = output_handler(doc.find("span", id="Umbral_Dash").
                                parent.
                                parent.
                                parent.
                                find("h3", string="COOLDOWN:").
                                next_sibling.
                                next_sibling)[0]
    e_distance = output_handler(doc.find("span", id="Umbral_Dash").
                                parent.
                                parent.
                                parent.
                                find("h3", string="TARGET RANGE:").
                                next_sibling.
                                next_sibling.
                                find("span", title="Maximum dash distance"))[0]
    e_healing_percent = output_handler(doc.find("span", id="Umbral_Dash").
                                       parent.
                                       parent.
                                       parent.find("span", string="Healing:").parent.next_sibling)[0] / 100
    e_special_healing_percent = output_handler(doc.find("span", id="Umbral_Dash").
                                               parent.
                                               parent.
                                               parent.find("span", string="Healing:").
                                               parent.
                                               next_sibling.
                                               next_sibling.
                                               next_sibling)[0] / 100
    e = {"cooldown": e_cooldown,
         "distance": e_distance,
         "healing_percent": e_healing_percent,
         "special_healing_percent": e_special_healing_percent}

    # R
    r_cooldown = output_handler(doc.find("span", id="World_Ender").
                                parent.
                                parent.
                                parent.
                                find("h3", string="COOLDOWN:").
                                next_sibling.
                                next_sibling)[0]
    r_cast_time = output_handler(doc.find("span", id="World_Ender").
                                 parent.
                                 parent.
                                 parent.
                                 find("h3", string="CAST TIME:").
                                 next_sibling.
                                 next_sibling)[0]
    r_duration = output_handler(doc.find("span", id="World_Ender").
                                parent.
                                parent.
                                parent.
                                find("b", string="Aatrox").
                                parent)[0]
    r_reset_extension = output_handler(doc.find("span", id="World_Ender").
                                       parent.
                                       parent.
                                       parent.
                                       find("a", string="takedown").
                                       parent.
                                       parent)[0]
    r_size_increase = output_handler(doc.find("span", id="World_Ender").
                                     parent.
                                     parent.
                                     parent.
                                     find("a", string="self-healing").
                                     parent.
                                     parent)[0] / 100
    r_bonus_move_speed = output_handler(doc.find("span", id="World_Ender").
                                        parent.
                                        parent.
                                        parent.
                                        find("span", string="Bonus Movement Speed:").
                                        parent.
                                        next_sibling)[0] / 100
    r_ad_increase = output_handler(doc.find("span", id="World_Ender").
                                        parent.
                                        parent.
                                        parent.
                                        find("span", string="Bonus Attack Damage:").
                                        parent.
                                        next_sibling)[0] / 100
    r_healing_increase = output_handler(doc.find("span", id="World_Ender").
                                        parent.
                                        parent.
                                        parent.
                                        find("span", string="Increased Healing:").
                                        parent.
                                        next_sibling)[0] / 100
    r = {"cooldown": r_cooldown,
         "cast_time": r_cast_time,
         "duration": r_duration,
         "reset_extension": r_reset_extension,
         "size_increase": r_size_increase,
         "bonus_move_speed": r_bonus_move_speed,
         "ad_increase": r_ad_increase,
         "healing_increase": r_healing_increase}

    return {"p": passive, "q": q, "w": w, "e": e, "r": r}


def output_handler(stat) -> list:
    try:
        text = stat.text
        if "During World Ender, Aatrox gains  bonus attack damage and " in text:
            text = text.replace("During World Ender, Aatrox gains  bonus attack damage and ", "")
            text = text.replace("increased size, and receives increased  self-healing from all sources.", "")
        if "Whenever Aatrox scores a champion  takedown, he extends the duration by " in text:
            text = text.replace("Whenever Aatrox scores a champion  takedown, he extends the duration by ", "")
            text = text.replace("seconds and becomes unleashed again.", "")
        if "Active: Aatrox unleashes his true form for " in text:
            text = text.replace("Active: Aatrox unleashes his true form for ", "")
            text = text.replace("seconds,  fearing nearby enemy  minions and  monsters for 3 seconds, during which "
                                "they are gradually  slowed by up to 99% over the duration. He also gains  ghosting "
                                "and  bonus movement speed that decays by 10% of the current bonus every 0.25 "
                                "seconds, lasting until World Ender has ended.", "")
        if "during which they are  revealed." in text:
            text = text.replace("If this hits an enemy  champion or large  monster, a  tether is formed between the "
                                "target and the ground beneath them for ", "")
            text = text.replace("seconds, during which they are  revealed.", "")
        if "Aatrox sends a chain" in text:
            text = text.replace("Active: Aatrox sends a chain in the target direction that deals physical damage to "
                                "the first enemy hit, doubled against  minions, and  slowing them by", "")
            text = text.replace("for", "")
            text = text.replace("seconds.", "")
        if "damage against  minions, and the" in text:
            text = text.replace("The Darkin Blade deals ", "")
            text = text.replace("damage against  minions, and the  knock up duration from hitting the Sweetspot is "
                                "doubled to 0.5 seconds against  monsters.", "")
        if "Third Cast: Aatrox's third strike affects a" in text:
            text = text.replace("Third Cast: Aatrox's third strike affects a ", "")
            text = text.replace("-radius circular area centered on a target location that is 200 units in front of "
                                "him, with a 180-radius Sweetspot within.", "")
            text = str(float(text) ** 2 * math.pi) + " " + text
        if "Second Cast: Aatrox's second strike affects a trapezoidal area in the target direction, with the " \
           "Sweetspot at the farthest edge. The hitbox begins" in text:
            text = text.replace("Second Cast: Aatrox's second strike affects a trapezoidal area in the target "
                                "direction, with the Sweetspot at the farthest edge. The hitbox begins", "")
            text = text.replace("-units behind Aatrox and extends", "")
            text = text.replace("-units in front of him, measuring between", "")
            text = text.replace("and", "")
            text = text.replace("-units wide from behind to in front.", "")
            text = text.split()
            text = str((float(text[2]) + float(text[3])) * (float(text[0]) + float(text[1])) / 2) + " " + text[1]
        if "first strike affects a" in text:
            text = text.replace("first strike affects a", "")
            text = text.replace(
                "-unit rectangular area in the target direction, with him centered on the back line and the", "")
            text = text.split()
            text = str(float(text[0]) * float(text[2])) + " " + text[0]
        if "Aatrox performs a strike with his greatsword for each of the three casts, dealing physical damage to " \
           "enemies hit within an area. Enemies hit within a Sweetspot of the area take" in text:
            text = text.replace("Aatrox performs a strike with his greatsword for each of the three casts, dealing "
                                "physical damage to enemies hit within an area. Enemies hit within a Sweetspot of the"
                                " area take", "")
            text = text.replace("bonus damage and also  knocked up for", "")
            text = text.replace("seconds. Each subsequent cast increases The Darkin Blade's damage by", "")
        if "%" in text:
            text = text.replace("%", "")
        if "is reduced by" in text:
            text = text.replace("is reduced by", "")
        if "seconds, modified to" in text:
            text = text.replace("seconds, modified to", "")
        if "if he hits with the" in text:
            text = text.replace("if he hits with the", "")
        if "of the" in text:
            text = text.replace("of the", "")
        if "−" in text:
            text = text.split()
            text = str((float(text[0]) + float(text[2])) / 2)
        if "bonus range" in text:
            text = text.replace("bonus range", "")
        if "bonus damage" in text:
            text = text.replace("bonus damage", "")
        if "(+" in text:
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
        if "AD" in text:
            text = text.replace("AD", "")
        if "/" in text:
            text = text.replace("/", "")
            text = text.split()
            s = 0
            for number in text:
                s += float(number)
            text = str(s / len(text))
        if " three times before the ability goes on cooldown, with a" in text:
            text = text.replace("three times before the ability goes on cooldown, with a", "")
        if "second" in text:
            text = text.replace("second", "")
        if "for" in text:
            text = text.replace("for", "")
        text = text.split()
        for i in range(len(text)):
            text[i] = float(text[i])
        return text

    except:
        return [0]


get_data(False)
