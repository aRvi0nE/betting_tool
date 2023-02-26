from classes.champion import Champion
from classes import ability_types
from classes.scraping import get_aatrox
from data.settings import *
from data.boot_stats import *
from data.item_stats import *


class Aatrox(Champion):
    def __init__(self, new_patch: bool):
        super().__init__("Aatrox", new_patch)
        ability_stats = get_aatrox.get_data(new_patch)

        # r duration
        r_duration = ability_types.AbilityDurationReset(
            original_duration=ability_stats["r"]["duration"],
            reset_extension=ability_stats["r"]["reset_extension"]).ability_duration

        # r extra ad
        self.ad = ability_types.AdEnhancer(
            cooldown=ability_stats["r"]["cooldown"],
            cast_time=ability_stats["r"]["cast_time"],
            ability_duration=r_duration,
            champion_ad=self.ad,
            ad_increase=ability_stats["r"]["ad_increase"]).ad
        self.burst = 0
        self.burst += (self.ad + NUMBER_OF_ITEMS * ITEM_AD) * (
                (NUMBER_OF_ITEMS * ITEM_CRIT_CHANCE * (1 + self.crit_damage))
                + (1 - NUMBER_OF_ITEMS * ITEM_CRIT_CHANCE))
        self.single_target_damage = 0
        self.single_target_damage += self.burst
        self.dps = 0
        self.dps += self.burst * self.attack_speed
        self.wave_clear = 0
        self.wave_clear += self.dps
        self.tower_damage = 0
        self.tower_damage += (self.ad + NUMBER_OF_ITEMS * ITEM_AD) * self.attack_speed

        # r uptime percent
        r_uptime_percent = r_duration / (
                ability_stats["r"]["cooldown"] * 100 / (100 + NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) + r_duration)

        q1_damage = ability_types.AoeDamageAbility(
            special_hit_bonus_damage=ability_stats["q"]["special_hit_bonus_damage"],
            special_hit_percent=SPECIAL_HIT_PERCENT,
            area=ability_stats["q"]["area1"],
            flat_damage=ability_stats["q"]["flat_damage"],
            scale_ad=ability_stats["q"]["scale_ad"],
            champion_ad=self.ad,
            range_=ability_stats["q"]["range1"])
        q2_damage = ability_types.AoeDamageAbility(
            special_hit_bonus_damage=ability_stats["q"]["special_hit_bonus_damage"],
            special_hit_percent=SPECIAL_HIT_PERCENT,
            area=ability_stats["q"]["area2"],
            flat_damage=ability_stats["q"]["flat_damage"] * (1 + ability_stats["q"]["damage_ramp_up"]),
            scale_ad=ability_stats["q"]["scale_ad"] * (1 + ability_stats["q"]["damage_ramp_up"]),
            champion_ad=self.ad,
            range_=ability_stats["q"]["range2"])
        q3_damage = ability_types.AoeDamageAbility(
            special_hit_bonus_damage=ability_stats["q"]["special_hit_bonus_damage"],
            special_hit_percent=SPECIAL_HIT_PERCENT,
            area=ability_stats["q"]["area3"],
            flat_damage=ability_stats["q"]["flat_damage"] * (1 + 2 * ability_stats["q"]["damage_ramp_up"]),
            scale_ad=ability_stats["q"]["scale_ad"] * (1 + 2 * ability_stats["q"]["damage_ramp_up"]),
            champion_ad=self.ad,
            range_=ability_stats["q"]["range2"])

        q1_aoe_stun = ability_types.AoeCCAbility(
            stun_duration=ability_stats["q"]["stun_duration"],
            area=ability_stats["q"]["area1"] * SPECIAL_HIT_PERCENT)
        q2_aoe_stun = ability_types.AoeCCAbility(
            stun_duration=ability_stats["q"]["stun_duration"],
            area=ability_stats["q"]["area2"] * SPECIAL_HIT_PERCENT)
        q3_aoe_stun = ability_types.AoeCCAbility(
            stun_duration=ability_stats["q"]["stun_duration"],
            area=ability_stats["q"]["area3"] * SPECIAL_HIT_PERCENT)

        q = ability_types.SteppedAbility(
            cooldown=ability_stats["q"]["cooldown"],
            cast_time=ability_stats["q"]["cast_time"],
            cooldown_between_casts=ability_stats["q"]["cooldown_between_casts"],
            burst_scores=[q1_damage.burst_score, q2_damage.burst_score, q3_damage.burst_score],
            aoe_damage_scores=[q1_damage.aoe_damage_score, q2_damage.aoe_damage_score, q3_damage.aoe_damage_score],
            aoe_cc_scores=[q1_aoe_stun.aoe_cc_score, q2_aoe_stun.aoe_cc_score, q3_aoe_stun.aoe_cc_score],
            range_scores=[q1_damage.range_score, q2_damage.range_score, q3_damage.range_score],
            minion_damage_multiplier=ability_stats["q"]["minion_damage_multiplier"],
            areas=[ability_stats["q"]["area1"], ability_stats["q"]["area2"], ability_stats["q"]["area3"]])

        self.dps += q.dps_score
        self.burst += q.burst_score
        self.aoe_damage += q.aoe_damage_score
        self.aoe_cc += q.aoe_cc_score
        self.range += q.range_score
        self.wave_clear += q.wave_clear_score

        w_damage = ability_types.SingleTargetDamageAbility(
            cooldown=ability_stats["w"]["cooldown"],
            cast_time=ability_stats["w"]["cast_time"],
            range_=ability_stats["w"]["range"],
            flat_damage=ability_stats["w"]["flat_damage"],
            scale_ad=ability_stats["w"]["scale_ad"],
            special_hit_bonus_damage=1,
            special_hit_percent=0.5,
            champion_ad=self.ad,
            minion_damage_multiplier=2)

        w_single_target_cc = ability_types.SingleTargetCCAbility(
            slow_value=ability_stats["w"]["slow_value"],
            slow_duration=ability_stats["w"]["slow_duration"],
            grab_distance=ability_stats["w"]["range"] / 2)

        w_reveal = ability_types.RevealAbility(
            reveal_duration=ability_stats["w"]["reveal_duration"])

        self.dps += w_damage.dps_score
        self.burst += w_damage.burst_score
        self.single_target_damage += w_damage.single_target_damage_score
        self.single_target_cc += w_single_target_cc.single_target_cc_score
        self.offensive_utility += w_reveal.offensive_utility_score
        self.range += w_damage.range_score
        self.wave_clear += w_damage.wave_clear_score

        hits_per_second = 1 / self.attack_speed + 1 / q.cooldown / 4 + w_damage.cooldown / 2
        special_hits_per_second = 1 / q.cooldown / 4

        passive_range = ability_types.AutoRangeEnhancer(bonus_range=ability_stats["p"]["bonus_range"])
        passive_damage = ability_types.AutoDamageEnhancer(
            static_cooldown=ability_stats["p"]["static_cooldown"],
            scale_target_max_hp=ability_stats["p"]["scale_target_max_hp"],
            cooldown_reduction_per_hit=ability_stats["p"]["cooldown_reduction_per_hit"],
            cooldown_reduction_per_special_hit=ability_stats["p"]["cooldown_reduction_per_special_hit"],
            hits_per_second=hits_per_second,
            special_hits_per_second=special_hits_per_second)
        passive_sustain = ability_types.AutoSustainEnhancer(
            dps=passive_damage.dps_score + passive_damage.wave_clear_score,
            post_mitigation_heal=ability_stats["p"]["post_mitigation_heal"],
            cooldown_reduction_per_hit=ability_stats["p"]["cooldown_reduction_per_hit"],
            cooldown_reduction_per_special_hit=ability_stats["p"]["cooldown_reduction_per_special_hit"],
            physical_damage=1,
            hits_per_second=hits_per_second,
            special_hits_per_second=special_hits_per_second)

        self.dps += passive_damage.dps_score
        self.burst += passive_damage.burt_score
        self.single_target_damage += passive_damage.single_target_damage_score
        self.sustain += passive_sustain.sustain_score
        self.range += passive_range.range_score
        self.wave_clear += passive_damage.wave_clear_score

        e_bonus_heal_passive = ability_types.HealAbility(
            dps=2 * self.aa_dps_score + q.dps_score + w_damage.dps_score + q.wave_clear_score +
                w_damage.wave_clear_score,
            healing_percent=ability_stats["e"]["healing_percent"],
            special_healing_percent=ability_stats["e"]["special_healing_percent"],
            physical_damage=1,
            special_healing_uptime_percent=r_uptime_percent)

        e_dash = ability_types.DashAbility(
            cooldown=ability_stats["e"]["cooldown"],
            distance=ability_stats["e"]["distance"])

        self.sustain += e_bonus_heal_passive.sustain_score
        self.speed += e_dash.speed_score
        self.reposition += e_dash.reposition_score
        self.range += e_dash.range_score

        r_move_speed = ability_types.MovementSpeedAbility(
            cooldown=ability_stats["r"]["cooldown"],
            cast_time=ability_stats["r"]["cast_time"],
            bonus_move_speed=ability_stats["r"]["bonus_move_speed"],
            champion_move_speed=self.base_move_speed + BOOTS_MOVE_SPEED,
            ability_duration=r_duration,
            move_speed_duration=r_duration)

        r_healing = ability_types.HealingEnhancer(
            cooldown=ability_stats["r"]["cooldown"],
            cast_time=ability_stats["r"]["cast_time"],
            healing_increase=ability_stats["r"]["healing_increase"],
            champion_healing=self.hp_regen_score + passive_sustain.sustain_score + e_bonus_heal_passive.sustain_score,
            ability_duration=r_duration)

        r_size_enhancer = ability_types.SizeEnhancer(
            cooldown=ability_stats["r"]["cooldown"],
            cast_time=ability_stats["r"]["cast_time"],
            ability_duration=r_duration,
            champion_health_score=self.health_score,
            champion_size=self.hit_box,
            size_increase_percent=ability_stats["r"]["size_increase"])

        self.tank += r_size_enhancer.tank_score
        self.sustain += r_healing.sustain_score
        self.speed += r_move_speed.speed_score
