import math

from classes.champion import Champion
from classes import ability_types
from classes.scraping import get_akali
from data.settings import *
from data.boot_stats import *
from data.item_stats import *


class Akali(Champion):
    def __init__(self, new_patch):
        super().__init__("Akali", new_patch)
        ability_stats = get_akali.get_data(new_patch)

        w_energy_regen = ability_types.EnergyRegenAbility(
            cooldown=ability_stats["w"]["cooldown"],
            cast_time=ability_stats["w"]["cast_time"],
            ability_duration=ability_stats["w"]["duration"],
            total_regen_amount=ability_stats["w"]["energy"]
        )

        w_invisibility = ability_types.InvisibleAbility(
            cooldown=ability_stats["w"]["cooldown"],
            cast_time=ability_stats["w"]["cast_time"],
            ability_duration=ability_stats["w"]["duration"],
            area=ability_stats["w"]["area"],
            champion_size=self.hit_box
        )

        w_speed = ability_types.MovementSpeedAbility(
            cooldown=ability_stats["w"]["cooldown"],
            cast_time=ability_stats["w"]["cast_time"],
            bonus_move_speed=ability_stats["w"]["bonus_move_speed"],
            champion_move_speed=self.base_move_speed + BOOTS_MOVE_SPEED,
            ability_duration=ability_stats["w"]["duration"],
            move_speed_duration=ability_stats["w"]["speed_duration"]
        )

        self.tank += w_invisibility.tank_score
        self.speed += w_speed.speed_score

        q_cooldown = ability_types.EnergyAbilityCooldown(
            cooldown=ability_stats["q"]["cooldown"],
            energy_cost=ability_stats["q"]["cost"],
            energy_per_sec=self.resource_regen + w_energy_regen.energy_regen,
            energy_bank=self.resource,
            cast_time=ability_stats["q"]["cast_time"]
        )

        q_damage = ability_types.AoeDamageAbility(
            static_cooldown=q_cooldown.cooldown,
            area=ability_stats["q"]["range"] ** 2 * math.pi * ability_stats["q"]["angle"] / 360,
            flat_damage=ability_stats["q"]["flat_damage"],
            scale_ad=ability_stats["q"]["scale_ad"],
            champion_ad=self.ad,
            range_=ability_stats["q"]["range"]
        )

        q_cc = ability_types.AoeCCAbility(
            slow_duration=ability_stats["q"]["slow_duration"],
            slow_value=ability_stats["q"]["slow_value"],
            area=(ability_stats["q"]["range"] ** 2 - (
                    ability_stats["q"]["range"] - ability_stats["q"]["slow_width"]) ** 2) *
                 math.pi * ability_stats["q"]["angle"] / 360
        )

        self.dps += q_damage.dps_score
        self.burst += q_damage.burst_score
        self.aoe_damage += q_damage.aoe_damage_score
        self.aoe_cc += q_cc.aoe_cc_score
        self.range += q_damage.range_score
        self.wave_clear += q_damage.wave_clear_score

        e_damage_1 = ability_types.SingleTargetDamageAbility(
            range_=ability_stats["e"]["range"],
            flat_damage=ability_stats["e"]["flat_damage_1"],
            scale_ad=ability_stats["e"]["damage_scale_ad_1"],
            champion_ad=self.ad,
            scale_ap=ability_stats["e"]["damage_scale_ap_1"]
        )

        e_damage_2 = ability_types.SingleTargetDamageAbility(
            range_=ability_stats["e"]["range"],
            flat_damage=ability_stats["e"]["flat_damage_2"],
            scale_ad=ability_stats["e"]["damage_scale_ad_2"],
            champion_ad=self.ad,
            scale_ap=ability_stats["e"]["damage_scale_ap_2"]
        )

        e_cooldown = ability_types.EnergyAbilityCooldown(
            cooldown=ability_stats["e"]["cooldown"],
            energy_cost=ability_stats["e"]["cost"],
            energy_per_sec=self.resource_regen + w_energy_regen.energy_regen,
            energy_bank=self.resource,
            cast_time=ability_stats["e"]["cast_time"]
        )

        e_dash_1 = ability_types.DashAbility(
            cooldown=e_cooldown.cooldown,
            cast_time=ability_stats["e"]["cast_time"],
            distance=ability_stats["e"]["flip_length"]
        )

        e_dash_2 = ability_types.DashAbility(
            cooldown=e_cooldown.cooldown,
            cast_time=ability_stats["e"]["cast_time"],
            distance=ability_stats["e"]["range"]
        )

        e_damage = ability_types.SteppedAbility(
            static_cooldown=e_cooldown.cooldown,
            burst_scores=[e_damage_1.burst_score, e_damage_2.burst_score],
            single_target_damage_scores=[e_damage_1.single_target_damage_score, e_damage_2.single_target_damage_score],
            range_scores=[e_damage_1.range_score, e_damage_2.range_score]
        )

        e_reveal = ability_types.RevealAbility(
            reveal_duration=ability_stats["e"]["reveal_duration"])

        self.dps += e_damage.dps_score
        self.burst += e_damage.burst_score
        self.single_target_damage += e_damage.single_target_damage_score
        self.speed += e_dash_1.speed_score
        self.reposition += e_dash_1.reposition_score + e_dash_2.reposition_score
        self.offensive_utility += e_reveal.offensive_utility_score
        self.range += e_damage.range_score
        self.wave_clear += e_damage.wave_clear_score

        r_1_damage = ability_types.AoeDamageAbility(
            area=ability_stats["r"]["collision_radius"] ** 2 * math.pi +
                 ability_stats["r"]["collision_radius"] * ability_stats["r"]["dash_distance_1"],
            flat_damage=ability_stats["r"]["flat_damage_1"],
            scale_bonus_ad=ability_stats["r"]["damage_scale_bonus_ad_1"],
            range_=ability_stats["r"]["range_1"],
            scale_ap=ability_stats["r"]["damage_scale_ap_1"]
        )

        r_2_damage = ability_types.AoeDamageAbility(
            area=ability_stats["r"]["collision_radius"] ** 2 * math.pi +
                 ability_stats["r"]["collision_radius"] * ability_stats["r"]["dash_distance_2"],
            flat_damage=ability_stats["r"]["flat_damage_2"],
            scale_ap=ability_stats["r"]["damage_scale_ap_2"],
            range_=ability_stats["r"]["dash_distance_2"],
            scale_missing_hp=ability_stats["r"]["damage_scale_missing_health_2"]
        )

        r_1_dash = ability_types.DashAbility(
            cooldown=ability_stats["r"]["cooldown"],
            cast_time=ability_stats["r"]["cast_time"] + ability_stats["r"]["cooldown_between_casts"],
            distance=ability_stats["r"]["dash_distance_1"]
        )

        r_2_dash = ability_types.DashAbility(
            cooldown=ability_stats["r"]["cooldown"],
            cast_time=ability_stats["r"]["cast_time"] + ability_stats["r"]["cooldown_between_casts"],
            distance=ability_stats["r"]["dash_distance_2"]
        )

        r_damage = ability_types.SteppedAbility(
            cooldown=ability_stats["r"]["cooldown"],
            cast_time=ability_stats["r"]["cast_time"],
            cooldown_between_casts=ability_stats["r"]["cooldown_between_casts"],
            burst_scores=[r_1_damage.burst_score, r_2_damage.burst_score],
            aoe_damage_scores=[r_1_damage.aoe_damage_score, r_2_damage.aoe_damage_score],
            range_scores=[r_1_damage.range_score, r_2_damage.range_score],
            areas=[ability_stats["r"]["collision_radius"] ** 2 * math.pi +
                   ability_stats["r"]["collision_radius"] * ability_stats["r"]["dash_distance_1"],
                   ability_stats["r"]["collision_radius"] ** 2 * math.pi +
                   ability_stats["r"]["collision_radius"] * ability_stats["r"]["dash_distance_2"]]
        )

        self.dps += r_damage.dps_score
        self.burst += r_damage.burst_score
        self.aoe_damage += r_damage.aoe_damage_score
        self.speed += r_2_dash.speed_score
        self.reposition += r_1_dash.reposition_score + r_2_dash.reposition_score
        self.range += r_damage.range_score
        self.wave_clear += r_damage.wave_clear_score

        abilities_hit_per_second = 1 / q_cooldown.cooldown / 2 + 1 / e_cooldown.cooldown + 1 / r_damage.cooldown

        p_range = ability_types.AutoRangeEnhancer(
            bonus_range=self.attack_range)

        p_damage = ability_types.AutoDamageEnhancer(
            static_cooldown=1 / abilities_hit_per_second + ability_stats["p"]["duration"],
            minion_damage_multiplier=0,
            flat_damage=ability_stats["p"]["flat_damage"],
            scale_bonus_ad=ability_stats["p"]["damage_scale_ad"],
            scale_ap=ability_stats["p"]["damage_scale_ap"])

        p_speed = ability_types.MovementSpeedAbility(
            static_cooldown=1 / abilities_hit_per_second,
            bonus_move_speed=ability_stats["p"]["bonus_move_speed"],
            champion_move_speed=self.base_move_speed + BOOTS_MOVE_SPEED,
            ability_duration=ability_stats["p"]["duration"],
            move_speed_duration=ability_stats["p"]["speed_duration"]
        )

        self.dps += p_damage.dps_score
        self.burst += p_damage.burt_score
        self.single_target_damage += p_damage.single_target_damage_score
        self.speed += p_speed.speed_score
        self.range += p_range.range_score
