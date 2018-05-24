from __future__ import print_function
import numpy as np
from .hero import *


class Ake(Hero):
    def __init__(self, level=1, equips=[]):
        super(Ake, self).__init__()
        self.basic_init_ake()
        # Skill Add points
        skills = [0,0,0]
        def addpoints():
            for _ in range(level):
                if skills[2] < (level)//4 and skills[2] < 3:
                    skills[2] += 1
                elif skills[1] < (level+1)//2 and skills[1] < 6:
                    skills[1] += 1
                else:
                    skills[0] += 1
            assert sum(skills) == level, "Add points Wrong..."
        addpoints()
        self.skill_1 = Skill(skills[0])
        self.skill_2 = Skill(skills[1])
        self.skill_ult = Skill(skills[2])

        # initialization
        self.set_level(level)
        self.add_equips(equips)
        self.initilize_all()
        # add equips

        print(self.__class__.__name__, "Lv", self.level, ": Attack", self.attack, "ExAttack: ", self.exattack)

        self.print_info()

    def add_runes(self):
        """Standard AKe Runes"""
        self.exattack += 9
        self.attack_speed += 10
        self.critical_damage += 0.36
        self.armor_penetration += 66
        self.critical_chance += 0.07


    def basic_init_ake(self):
        """With Runes"""
        self.attack_1 = 177
        self.attck_15 = 427
        self.attack_inc = 0

        self.spell_power = 0
        self.power_inc = 0


        self.attack_speed_1 = 0
        self.attack_speed_15 = 28
        self.as_inc = 0

        self.speed = 380
        self.max_hp_1 = 3269
        self.max_hp_15 = 5968
        self.hp_inc = 0

        self.max_mp_1 = 0
        self.max_mp_15 = 0
        self.mp_inc = 0

        # Armor and spell resistance
        self.armor_1 = 89
        self.armor_15 = 349
        self.armor_inc = 0

        self.spell_resis_1 = 50
        self.spell_resis_15 = 169
        self.spell_resis_inc = 0
        # penetration
        self.armor_penetration = 0
        self.armor_penetration_percent = 0
        self.magic_penetration = 0
        self.magic_penetration_percent = 0

        # critical
        self.critical_chance = 0
        self.critical_damage = 1.25

        self.cd = 0
        # Blood sucking
        self.physical_vampire = 0
        self.magic_vampire = 0
        # Add Runes
        self.add_runes()

    def initilize_all(self):
        self.init_skill_1()
        self.init_skill_2()
        self.init_skill_ult()
        self.init_incs()
        self.init_state()

    def init_skill_1(self):
        ## Convenient to Calc Pojun
        self.skill_1.trigger_times = 1

        self.skill_1.base_damage = 175
        self.skill_1.addition_by_skill_level = 25
        self.skill_1.addition_by_attack = 0.65

    def init_skill_2(self):
        self.skill_2.base_damage = 350
        self.skill_2.addition_by_skill_level = 40
        self.skill_2.addition_by_attack = 1.0

    def init_skill_ult(self):
        self.skill_ult.base_damage = 150
        self.skill_ult.addition_by_skill_level = 25


    def init_state(self):
        """passive skill"""
        super(Ake, self).init_state()
        self.critical_damage += 0.5 * self.critical_chance

    def passive_skill_function(self, damage):
        # self.extra_critical_damage = 0.5 * self.critical_chance
        # self.to_do_physical_damage *= (self.critical_damage + self.extra_critical_damage)
        # if self.pojun_buff > 1.0:
        #     verbose_print("Higher Damage with Pojun...")
        #     damage = damage * 1.3
        return damage * self.critical_damage

    def skill_1_function(self, enemy):
        physical_damage = self.passive_skill_function(self.skill_1.function(self))
        if enemy.bujiaxie_buff:
            verbose_print(">>> Defend by Bujiaxie...")
            physical_damage *= 0.85
        verbose_print("[{}] Do skill_1: Lv {} , damage: {}".format(self.__class__.__name__, self.skill_1.skill_level,
                                                              physical_damage))
        if self.moshi_buff:
            print(">>> Moshi damage: {}".format(enemy.hp * 0.08))
            physical_damage += enemy.hp * 0.08 / self.critical_damage

        return physical_damage

    def skill_2_function(self):
        physical_damage = self.passive_skill_function(self.skill_2.function(self))
        verbose_print("[{}] Do skill_2: Lv{} , damage:{}".format(self.__class__.__name__, self.skill_2.skill_level,
                                                              physical_damage))
        return physical_damage

    def skill_ult_function(self):
        inc_attack = self.skill_ult.base_damage + (
                                                      self.skill_ult.skill_level - 1) * self.skill_ult.addition_by_skill_level
        self.exattack += inc_attack
        verbose_print("[{}] Do skill_ult Lv{} , increased attack: {}, "
              "inc range: {}".format(self.__class__.__name__, self.skill_ult.skill_level, self.exattack+self.attack, inc_attack))

    def equips_functions(self, enemy):
        if len(self.equips_funcs) > 0:
            ll("Using Equips")
            for key, func in self.equips_funcs.iteritems():
                if key == 'hero_attack' or 'zongshi_f':
                    self.to_do_physical_damage += self.passive_skill_function(func(self, enemy))
                # elif key == 'zongshi_f':
                    # pass
                    # self.to_do_physical_damage += func(self, enemy)
                else:
                    raise ValueError("Not Implement")
        else:
            pass

    def damage_combo(self, enemy):
        # if self.calc_damage:
        self.skill_ult_function()

        damage = self.skill_2_function()
        self.damage_combo_to_hero(enemy, damage)
        ll(damage)

        # Skill 1 Damage Twice
        damage = self.skill_1_function(enemy)
        self.damage_combo_to_hero(enemy, damage)
        damage = self.skill_1_function(enemy)
        self.damage_combo_to_hero(enemy, damage)

        damage = self.equips_functions(enemy)
        self.damage_combo_to_hero(enemy, damage)
        # self.passive_skill_function()

        print("[{}] Total damage: {}".format(self.__class__.__name__, enemy.max_hp - enemy.hp))

        return self.to_do_physical_damage

    def damage_combo_to_hero(self, enemy, damage=0):
        assert isinstance(enemy, Hero), "Oh, {} is not I wanted .".format(type(enemy))

        remain_armor = (enemy.armor + enemy.exarmor) * (1 - self.armor_penetration_percent) - self.armor_penetration
        remain_armor = max(remain_armor,0)
        physic_defence_percent = (remain_armor) / (remain_armor + enemy.defence_baseline)
        verbose_print("{}'s Remain Armor: {}, defence_percent: {} ".format(enemy.__class__.__name__, remain_armor,
                                                                   physic_defence_percent))
        if damage > 0:
            received_damage = (1 - physic_defence_percent) * damage
        else:
            received_damage = (1 - physic_defence_percent) * self.to_do_physical_damage

        # Pojun Buff
        if enemy.hp / enemy.max_hp < 0.5 and self.pojun_buff:
            received_damage *= 1.3
            verbose_print(">>>> Po Jun <<<<")
        print("Did {} damage".format(received_damage, enemy.__class__.__name__))

        enemy.hp -= received_damage
        print("{}'s Remaining HP : {}".format(enemy.__class__.__name__, progress_bar(enemy.hp, enemy.ex_max_mp+enemy.max_hp)))
        self.to_do_physical_damage = 0
