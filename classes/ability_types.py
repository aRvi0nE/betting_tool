from data.champion_stats import *
from data.item_stats import *
from data.settings import *
from data.minion_stats import *


class AutoRangeEnhancer:
    def __init__(self, bonus_range=0):
        self.range_score = bonus_range


class AutoDamageEnhancer:
    def __init__(self,
                 static_cooldown=0,
                 cooldown=0,
                 cast_time=0,
                 scale_target_max_hp=0,
                 cooldown_reduction_per_hit=0,
                 cooldown_reduction_per_special_hit=0,
                 hits_per_second=0,
                 special_hits_per_second=0,
                 minion_damage_multiplier=1,
                 physical_damage=0,
                 magic_damage=0,
                 flat_damage=0,
                 scale_bonus_ad=0,
                 scale_ap=0):
        self.cooldown = static_cooldown + \
                        cooldown * 100 / (100 + NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) - \
                        hits_per_second * cooldown_reduction_per_hit - \
                        special_hits_per_second * cooldown_reduction_per_special_hit + \
                        cast_time
        self.burt_score = flat_damage + (CHAMPION_HP + NUMBER_OF_ITEMS * ITEM_HP) * scale_target_max_hp + \
                          (NUMBER_OF_ITEMS * ITEM_AP) * scale_ap + (NUMBER_OF_ITEMS * ITEM_AD) * scale_bonus_ad
        self.dps_score = self.burt_score / self.cooldown
        self.wave_clear_score = MINION_HP * scale_target_max_hp * minion_damage_multiplier / self.cooldown
        self.single_target_damage_score = self.burt_score


class AutoSustainEnhancer:
    def __init__(self,
                 static_cooldown=0,
                 cooldown=0,
                 cast_time=0,
                 dps=0,
                 post_mitigation_heal=0,
                 physical_damage=0,
                 magic_damage=0,
                 cooldown_reduction_per_hit=0,
                 cooldown_reduction_per_special_hit=0,
                 hits_per_second=0,
                 special_hits_per_second=0, ):
        self.cooldown = static_cooldown + \
                        cooldown * 100 / (100 + NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) - \
                        hits_per_second * cooldown_reduction_per_hit - \
                        special_hits_per_second * cooldown_reduction_per_special_hit + \
                        cast_time
        self.sustain_score = (dps *
                              (100 / (100 + CHAMPION_ARMOR + NUMBER_OF_ITEMS * ITEM_ARMOR) * physical_damage +
                               100 / (100 + CHAMPION_MR + NUMBER_OF_ITEMS * ITEM_MR) * magic_damage) *
                              post_mitigation_heal) / self.cooldown


class AoeDamageAbility:
    def __init__(self,
                 cooldown=0,
                 cast_time=0,
                 special_hit_bonus_damage=0,
                 special_hit_percent=0,
                 area=0,
                 flat_damage=0,
                 scale_ad=0,
                 minion_damage_multiplier=1,
                 physical_damage=0,
                 magic_damage=0,
                 champion_ad=0,
                 range_=0,
                 static_cooldown=0,
                 scale_bonus_ad=0,
                 scale_ap=0,
                 scale_missing_hp=0):
        self.cooldown = cooldown * 100 / (100 + NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) + cast_time + static_cooldown
        if self.cooldown == 0:
            self.cooldown = 1
        self.burst_score = (1 + special_hit_percent * special_hit_bonus_damage) * \
                           (flat_damage + scale_ad * (champion_ad + NUMBER_OF_ITEMS * ITEM_AD) +
                            scale_bonus_ad * (NUMBER_OF_ITEMS * ITEM_AD) +
                            scale_ap * (NUMBER_OF_ITEMS * ITEM_AP)) * \
                           (1 + scale_missing_hp * 50)
        self.dps_score = self.burst_score / self.cooldown
        self.wave_clear_score = self.dps_score * minion_damage_multiplier * area / MINION_SIZE / AOE_WAVE_CLEAR_BALANCER
        self.aoe_damage_score = self.burst_score * area / CHAMPION_SIZE
        self.range_score = range_


class AoeCCAbility:
    def __init__(self,
                 stun_duration=0,
                 slow_duration=0,
                 slow_value=0,
                 area=0):
        self.aoe_cc_score = (stun_duration + slow_duration * slow_value) * area / CHAMPION_SIZE


class SteppedAbility:
    def __init__(self,
                 static_cooldown=0,
                 cooldown=0,
                 cast_time=0,
                 cooldown_between_casts=0,
                 burst_scores=None,
                 aoe_damage_scores=None,
                 single_target_damage_scores=None,
                 aoe_cc_scores=None,
                 range_scores=None,
                 minion_damage_multiplier=1,
                 areas=None):

        self.burst_score = 0
        for burst in burst_scores:
            self.burst_score += burst
        self.aoe_damage_score = 0
        try:
            for aoe in aoe_damage_scores:
                self.aoe_damage_score += aoe
        except:
            pass
        self.aoe_cc_score = 0
        try:
            for aoe in aoe_cc_scores:
                self.aoe_cc_score += aoe
        except:
            pass
        self.single_target_damage_score = 0
        try:
            for damage in single_target_damage_scores:
                self.single_target_damage_score += damage
        except:
            pass
        self.range_score = 0
        for rang in range_scores:
            self.range_score += rang
        area = 0
        try:
            for ar in areas:
                area += ar
        except:
            pass
        self.cooldown = cooldown * 100 / (100 + NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) + \
                        len(burst_scores) * (cast_time + cooldown_between_casts) + static_cooldown
        self.dps_score = self.burst_score / self.cooldown
        if area != 0:
            self.wave_clear_score = self.dps_score * minion_damage_multiplier * area / MINION_SIZE / AOE_WAVE_CLEAR_BALANCER
        else:
            self.wave_clear_score = self.dps_score * minion_damage_multiplier


class SingleTargetDamageAbility:
    def __init__(self,
                 cooldown=0,
                 cast_time=0,
                 range_=0,
                 flat_damage=0,
                 scale_ad=0,
                 special_hit_bonus_damage=0,
                 special_hit_percent=0,
                 champion_ad=0,
                 minion_damage_multiplier=1,
                 number_of_hits=1,
                 damage_multiplier_per_subsequent_hit=0,
                 ability_duration=0,
                 scale_ap=0):
        self.cooldown = cooldown * 100 / (100 + NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) + cast_time + ability_duration
        if self.cooldown == 0:
            self.cooldown = 1
        self.burst_score = (1 + special_hit_percent * special_hit_bonus_damage) * \
                           (flat_damage + scale_ad * (champion_ad + NUMBER_OF_ITEMS * ITEM_AD) +
                            scale_ap * (NUMBER_OF_ITEMS * ITEM_AP)) * \
                           (1 + (number_of_hits - 1) * damage_multiplier_per_subsequent_hit)
        self.single_target_damage_score = self.burst_score
        self.range_score = range_ * number_of_hits
        self.dps_score = self.burst_score / self.cooldown
        self.wave_clear_score = self.dps_score * minion_damage_multiplier


class SingleTargetCCAbility:
    def __init__(self,
                 slow_value=0,
                 slow_duration=0,
                 grab_distance=0,
                 stun_duration=0):
        self.single_target_cc_score = slow_value * slow_duration + grab_distance / GRAB_BALANCER + stun_duration


class RevealAbility:
    def __init__(self,
                 reveal_duration=0):
        self.offensive_utility_score = reveal_duration * REVEAL_OFFENSIVE_VALUE


class HealAbility:
    def __init__(self,
                 dps=0,
                 healing_percent=0,
                 special_healing_percent=0,
                 special_healing_uptime_percent=0,
                 physical_damage=0,
                 magic_damage=0,
                 cooldown=0,
                 ability_duration=1,
                 cast_time=0,
                 flat_heal=0,
                 heal_scale_ap=0,
                 post_mitigation=True,
                 static_cooldown=0):
        self.cooldown = cooldown * 100 / (100 + NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) + cast_time + static_cooldown
        if post_mitigation:
            self.sustain_score = ((1 - special_healing_uptime_percent) * dps * healing_percent +
                                  special_healing_uptime_percent * dps * special_healing_percent) * \
                                 (physical_damage * 100 / (100 + CHAMPION_ARMOR + NUMBER_OF_ITEMS * ITEM_ARMOR)) * \
                                 ability_duration / (ability_duration + self.cooldown)
        else:
            self.sustain_score = (flat_heal + heal_scale_ap * NUMBER_OF_ITEMS * ITEM_AP) / self.cooldown


class DashAbility:
    def __init__(self,
                 cooldown=0,
                 cast_time=0,
                 distance=0,
                 ability_duration=0):
        self.reposition_score = distance
        self.range_score = distance
        self.cooldown = cooldown * 100 / (100 + NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) + cast_time + ability_duration
        self.speed_score = self.reposition_score / self.cooldown


class MovementSpeedAbility:
    def __init__(self,
                 static_cooldown=0,
                 cooldown=0,
                 cast_time=0,
                 bonus_move_speed=0,
                 champion_move_speed=0,
                 ability_duration=1,
                 move_speed_duration=0):
        self.cooldown = cooldown * 100 / (100 * NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) + cast_time + static_cooldown
        self.speed_score = champion_move_speed * bonus_move_speed * \
                           move_speed_duration / (ability_duration + self.cooldown)


class HealingEnhancer:
    def __init__(self,
                 cooldown=0,
                 cast_time=0,
                 healing_increase=0,
                 champion_healing=0,
                 ability_duration=1):
        self.cooldown = cooldown * 100 / (100 * NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) + cast_time
        self.sustain_score = champion_healing * healing_increase * \
                             ability_duration / (ability_duration + self.cooldown)


class AdEnhancer:
    def __init__(self,
                 cooldown=0,
                 cast_time=0,
                 ability_duration=1,
                 champion_ad=0,
                 ad_increase=0):
        self.cooldown = cooldown * 100 / (100 * NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) + cast_time
        self.ad = (self.cooldown / (self.cooldown + ability_duration) * (champion_ad + NUMBER_OF_ITEMS * ITEM_AD)) + \
                  (ability_duration / (self.cooldown + ability_duration) * (champion_ad + NUMBER_OF_ITEMS * ITEM_AD) *
                   (1 + ad_increase)) - NUMBER_OF_ITEMS * ITEM_AD


class SizeEnhancer:
    def __init__(self,
                 cooldown=0,
                 cast_time=0,
                 ability_duration=1,
                 champion_health_score=0,
                 champion_size=0,
                 size_increase_percent=0):
        self.cooldown = cooldown * 100 / (100 * NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) + cast_time
        self.tank_score = champion_health_score * champion_size * size_increase_percent * \
                          ability_duration / (ability_duration + self.cooldown)


class AbilityDurationReset:
    def __init__(self,
                 original_duration=0,
                 reset_extension=0):
        self.ability_duration = original_duration + reset_extension * \
                                (original_duration + reset_extension) * TAKE_DOWNS_PER_SECOND


class AbilityUseReset:
    def __init__(self,
                 ability_duration=0,
                 extra_uses_per_reset=0):
        self.extra_uses = ability_duration * TAKE_DOWNS_PER_SECOND * extra_uses_per_reset


class StackChargeAbility:
    def __init__(self,
                 stacks_per_second=0,
                 stack_threshold=0):
        self.cooldown = stack_threshold / stacks_per_second


class BoomerangAbility:
    def __init__(self,
                 cooldown=0,
                 cast_time=0,
                 range_=0,
                 width=0,
                 number_of_passes=0,
                 true_damage_hits=0,
                 flat_damage=0,
                 damage_scale_ap=0):
        self.cooldown = cooldown * 100 / (100 + NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) + cast_time
        area = range_ * width
        self.burst_score = (flat_damage + damage_scale_ap * NUMBER_OF_ITEMS * ITEM_AP) * \
                           (number_of_passes + true_damage_hits * TRUE_DAMAGE_VALUE)
        self.dps_score = self.burst_score / self.cooldown
        self.aoe_damage_score = self.burst_score * area / CHAMPION_SIZE
        self.wave_clear_score = self.dps_score * area / MINION_SIZE / AOE_WAVE_CLEAR_BALANCER
        self.range_score = range_


class EnergyAbilityCooldown:
    def __init__(self,
                 cooldown=0,
                 energy_cost=0,
                 energy_per_sec=0,
                 energy_bank=0,
                 cast_time=0):
        number_of_bank_abilities = energy_bank / energy_cost
        cooldown = cooldown * 100 / (100 + NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) + cast_time
        self.cooldown = (cooldown * number_of_bank_abilities * ENERGY_VS_BANK_BALANCER) + \
                        max(energy_cost / energy_per_sec, cooldown) * (1 - number_of_bank_abilities * ENERGY_VS_BANK_BALANCER)


class EnergyRegenAbility:
    def __init__(self,
                 cooldown=0,
                 cast_time=0,
                 ability_duration=0,
                 total_regen_amount=0):
        self.cooldown = cooldown * 100 / (100 + NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) + cast_time + ability_duration
        self.energy_regen = total_regen_amount / self.cooldown


class InvisibleAbility:
    def __init__(self,
                 cooldown=0,
                 cast_time=0,
                 ability_duration=0,
                 area=0,
                 champion_size=0):
        self.cooldown = cooldown * 100 / (100 + NUMBER_OF_ITEMS * ITEM_ABILITY_HASTE) + cast_time + ability_duration
        self.tank_score = area / champion_size * ability_duration / self.cooldown / INVISIBLE_BALANCER
