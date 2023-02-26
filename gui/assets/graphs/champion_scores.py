import pandas as pd
import dataframe_image as dfi


def normalize_scores(champion_instances):
    dps_list = []
    burst_list = []
    aoe_damage_list = []
    single_target_damage_list = []
    tank_list = []
    sustain_list = []
    single_target_cc_list = []
    aoe_cc_list = []
    speed_list = []
    reposition_list = []
    offensive_utility_list = []
    defensive_utility_list = []
    tower_damage_list = []
    range_list = []
    wave_clear_list = []
    engage_list = []
    disengage_list = []
    counter_engage_list = []

    for champ in champion_instances:
        dps_list.append(champion_instances[champ].dps)
        burst_list.append(champion_instances[champ].burst)
        aoe_damage_list.append(champion_instances[champ].aoe_damage)
        single_target_damage_list.append(champion_instances[champ].single_target_damage)
        tank_list.append(champion_instances[champ].tank)
        sustain_list.append(champion_instances[champ].sustain)
        single_target_cc_list.append(champion_instances[champ].single_target_cc)
        aoe_cc_list.append(champion_instances[champ].aoe_cc)
        speed_list.append(champion_instances[champ].speed)
        reposition_list.append(champion_instances[champ].reposition)
        offensive_utility_list.append(champion_instances[champ].offensive_utility)
        defensive_utility_list.append(champion_instances[champ].defensive_utility)
        tower_damage_list.append(champion_instances[champ].tower_damage)
        range_list.append(champion_instances[champ].range)
        wave_clear_list.append(champion_instances[champ].wave_clear)
        engage_list.append(champion_instances[champ].engage)
        disengage_list.append(champion_instances[champ].disengage)
        counter_engage_list.append(champion_instances[champ].counter_engage)

    dps_min = min(dps_list)
    dps_max = max(dps_list)
    burst_min = min(burst_list)
    burst_max = max(burst_list)
    aoe_damage_min = min(aoe_damage_list)
    aoe_damage_max = max(aoe_damage_list)
    single_target_damage_min = min(single_target_damage_list)
    single_target_damage_max = max(single_target_damage_list)
    tank_min = min(tank_list)
    tank_max = max(tank_list)
    sustain_min = min(sustain_list)
    sustain_max = max(sustain_list)
    single_target_cc_min = min(single_target_cc_list)
    single_target_cc_max = max(single_target_cc_list)
    aoe_cc_min = min(aoe_cc_list)
    aoe_cc_max = max(aoe_cc_list)
    speed_min = min(speed_list)
    speed_max = max(speed_list)
    reposition_min = min(reposition_list)
    reposition_max = max(reposition_list)
    offensive_utility_min = min(offensive_utility_list)
    offensive_utility_max = max(offensive_utility_list)
    defensive_utility_min = min(defensive_utility_list)
    defensive_utility_max = max(defensive_utility_list)
    tower_damage_min = min(tower_damage_list)
    tower_damage_max = max(tower_damage_list)
    range_min = min(range_list)
    range_max = max(range_list)
    wave_clear_min = min(wave_clear_list)
    wave_clear_max = max(wave_clear_list)
    engage_min = min(engage_list)
    engage_max = max(engage_list)
    disengage_min = min(disengage_list)
    disengage_max = max(disengage_list)
    counter_engage_min = min(counter_engage_list)
    counter_engage_max = max(counter_engage_list)

    champion_scores_normalized = {}

    for champ in champion_instances:
        champion_scores_normalized[f"{champ}"] = {}
        print()
        champion_scores_normalized[f"{champ}"]["dps"] = (champion_instances[champ].dps - dps_min) / (dps_max - dps_min)
        champion_scores_normalized[f"{champ}"]["burst"] = (champion_instances[champ].burst - burst_min) / (
                    burst_max - burst_min)
        champion_scores_normalized[f"{champ}"]["aoe_damage"] = (champion_instances[
                                                                    champ].aoe_damage - aoe_damage_min) / (
                                                                           aoe_damage_max - aoe_damage_min)
        champion_scores_normalized[f"{champ}"]["single_target_damage"] = (champion_instances[
                                                                              champ].single_target_damage - single_target_damage_min) / (
                                                                                     single_target_damage_max - single_target_damage_min)
        champion_scores_normalized[f"{champ}"]["tank"] = (champion_instances[champ].tank - tank_min) / (
                    tank_max - tank_min)
        champion_scores_normalized[f"{champ}"]["sustain"] = (champion_instances[champ].sustain - sustain_min) / (
                    sustain_max - sustain_min)
        champion_scores_normalized[f"{champ}"]["single_target_cc"] = (champion_instances[
                                                                          champ].single_target_cc - single_target_cc_min) / (
                                                                                 single_target_cc_max - single_target_cc_min)
        champion_scores_normalized[f"{champ}"]["aoe_cc"] = (champion_instances[champ].aoe_cc - aoe_cc_min) / (
                    aoe_cc_max - aoe_cc_min)
        champion_scores_normalized[f"{champ}"]["speed"] = (champion_instances[champ].speed - speed_min) / (
                    speed_max - speed_min)
        champion_scores_normalized[f"{champ}"]["reposition"] = (champion_instances[
                                                                    champ].reposition - reposition_min) / (
                                                                           reposition_max - reposition_min)
        try:
            champion_scores_normalized[f"{champ}"]["offensive_utility"] = (champion_instances[
                                                                               champ].offensive_utility - offensive_utility_min) / (
                                                                                      offensive_utility_max - offensive_utility_min)
        except:
            champion_scores_normalized[f"{champ}"]["offensive_utility"] = 0
        try:
            champion_scores_normalized[f"{champ}"]["defensive_utility"] = (champion_instances[
                                                                               champ].defensive_utility - defensive_utility_min) / (
                                                                                      defensive_utility_max - defensive_utility_min)
        except:
            champion_scores_normalized[f"{champ}"]["defensive_utility"] = 0
        champion_scores_normalized[f"{champ}"]["tower_damage"] = (champion_instances[
                                                                      champ].tower_damage - tower_damage_min) / (
                                                                             tower_damage_max - tower_damage_min)
        champion_scores_normalized[f"{champ}"]["range"] = (champion_instances[champ].range - range_min) / (
                    range_max - range_min)
        champion_scores_normalized[f"{champ}"]["wave_clear"] = (champion_instances[
                                                                    champ].wave_clear - wave_clear_min) / (
                                                                           wave_clear_max - wave_clear_min)
        try:
            champion_scores_normalized[f"{champ}"]["engage"] = (champion_instances[champ].engage - engage_min) / (
                        engage_max - engage_min)
        except:
            champion_scores_normalized[f"{champ}"]["engage"] = 0
        try:
            champion_scores_normalized[f"{champ}"]["disengage"] = (champion_instances[
                                                                       champ].disengage - disengage_min) / (
                                                                              disengage_max - disengage_min)
        except:
            champion_scores_normalized[f"{champ}"]["disengage"] = 0
        try:
            champion_scores_normalized[f"{champ}"]["counter_engage"] = (champion_instances[
                                                                            champ].counter_engage - counter_engage_min) / (
                                                                                   counter_engage_max - counter_engage_min)
        except:
            champion_scores_normalized[f"{champ}"]["counter_engage"] = 0

    return champion_scores_normalized


def graph(champion_instances):
    champion_scores_normalized = normalize_scores(champion_instances)
    df = pd.DataFrame(champion_scores_normalized)
    df = df.style.background_gradient(cmap="RdYlGn")
    header_style = {'selector': 'th',
                    'props': [('background-color', '#07213a'),
                              ("color", "#c0aa73")]}
    df = df.set_table_styles([header_style])
    dfi.export(df, "gui/assets/graphs/table.png")
