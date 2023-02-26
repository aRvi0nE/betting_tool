from classes.champion import Champion
from classes import ability_types
from classes.scraping import get_ahri
from data.settings import *
from data.boot_stats import *
from data.item_stats import *


class Ahri(Champion):
    def __init__(self, new_patch: bool):
        super().__init__("Ahri", new_patch)
        ability_stats = get_ahri.get_data(new_patch)

        # passive
        p_minion_cooldown = ability_types.StackChargeAbility(
            stacks_per_second=MINIONS_PER_SECOND,
            stack_threshold=ability_stats["p"]["stack_threshold"]
        ).cooldown

        p_minion_heal = ability_types.HealAbility(
            post_mitigation=False,
            static_cooldown=p_minion_cooldown,
            flat_heal=ability_stats["p"]["minion_flat_heal"],
            heal_scale_ap=ability_stats["p"]["minion_heal_scale_ap"]
        )

        p_champion_heal = ability_types.HealAbility(
            post_mitigation=False,
            static_cooldown=1 / TAKE_DOWNS_PER_SECOND,
            flat_heal=ability_stats["p"]["champion_flat_heal"],
            heal_scale_ap=ability_stats["p"]["champion_heal_scale_ap"]
        )

        self.sustain += p_minion_heal.sustain_score + p_champion_heal.sustain_score

        # q
        q = ability_types.BoomerangAbility(
            cooldown=ability_stats["q"]["cooldown"],
            cast_time=ability_stats["q"]["cast_time"],
            range_=ability_stats["q"]["range"],
            width=ability_stats["q"]["width"],
            number_of_passes=2,
            true_damage_hits=1,
            flat_damage=ability_stats["q"]["flat_damage"],
            damage_scale_ap=ability_stats["q"]["scale_ap"]
        )

        self.dps += q.dps_score
        self.burst += q.burst_score
        self.aoe_damage += q.aoe_damage_score
        self.range += q.range_score
        self.wave_clear += q.wave_clear_score
        print(q.wave_clear_score)

        # w
        w_speed = ability_types.MovementSpeedAbility(
            cooldown=ability_stats["w"]["cooldown"],
            cast_time=ability_stats["w"]["cast_time"],
            bonus_move_speed=ability_stats["w"]["bonus_move_speed"],
            champion_move_speed=self.base_move_speed + BOOTS_MOVE_SPEED,
            ability_duration=ability_stats["w"]["ability_duration"],
            move_speed_duration=ability_stats["w"]["move_speed_duration"]
        )

        w_damage = ability_types.SingleTargetDamageAbility(
            cooldown=ability_stats["w"]["cooldown"],
            cast_time=ability_stats["w"]["cast_time"],
            range_=ability_stats["w"]["range"],
            flat_damage=ability_stats["w"]["flat_damage"],
            scale_ap=ability_stats["w"]["scale_ap"],
            minion_damage_multiplier=(1 - ability_stats["w"]["minion_double_damage_threshold"]) +
                                     2 * ability_stats["w"]["minion_double_damage_threshold"],
            number_of_hits=3,
            damage_multiplier_per_subsequent_hit=ability_stats["w"]["damage_multiplier_per_subsequent_hit"],
            ability_duration=ability_stats["w"]["ability_duration"]
        )
        print(w_damage.wave_clear_score)

        self.dps += w_damage.dps_score
        self.burst += w_damage.burst_score
        self.single_target_damage += w_damage.single_target_damage_score
        self.speed += w_speed.speed_score
        self.range += w_damage.range_score
        self.wave_clear += w_damage.wave_clear_score

        # e
        e_damage = ability_types.SingleTargetDamageAbility(
            cooldown=ability_stats["e"]["cooldown"],
            cast_time=ability_stats["e"]["cast_time"],
            range_=ability_stats["e"]["range"],
            flat_damage=ability_stats["e"]["flat_damage"],
            scale_ap=ability_stats["e"]["damage_scale_ap"]
        )

        e_cc = ability_types.SingleTargetCCAbility(
            stun_duration=ability_stats["e"]["stun_duration"]
        )

        self.dps += e_damage.dps_score
        self.burst += e_damage.burst_score
        self.single_target_damage += e_damage.single_target_damage_score
        self.single_target_cc += e_cc.single_target_cc_score
        self.wave_clear += e_damage.wave_clear_score
        print(e_damage.wave_clear_score)

        # r
        r_duration = ability_types.AbilityDurationReset(
            original_duration=ability_stats["r"]["duration"],
            reset_extension=ability_stats["r"]["reset_extension"]
        ).ability_duration

        r_number_of_uses = ability_types.AbilityUseReset(
            ability_duration=r_duration,
            extra_uses_per_reset=1
        )

        r_damage = ability_types.SingleTargetDamageAbility(
            cooldown=ability_stats["r"]["cooldown"],
            cast_time=ability_stats["r"]["cast_time"],
            range_=ability_stats["r"]["dash_distance"] + ability_stats["r"]["range"],
            flat_damage=ability_stats["r"]["flat_damage"],
            number_of_hits=3+r_number_of_uses.extra_uses,
            damage_multiplier_per_subsequent_hit=1,
            ability_duration=r_duration,
            scale_ap=ability_stats["r"]["damage_scale_ap"]
        )

        r_dash = ability_types.DashAbility(
            cooldown=ability_stats["r"]["cooldown"],
            cast_time=ability_stats["r"]["cast_time"],
            distance=ability_stats["r"]["dash_distance"] * (3+r_number_of_uses.extra_uses),
            ability_duration=r_duration
        )

        print(r_damage.wave_clear_score)

        self.dps += r_damage.dps_score
        self.burst += r_damage.burst_score
        self.single_target_damage += r_damage.single_target_damage_score
        self.speed += r_dash.speed_score
        self.reposition += r_dash.reposition_score
        self.range += r_damage.range_score
        self.wave_clear += r_damage.wave_clear_score

