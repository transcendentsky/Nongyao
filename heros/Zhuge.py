from __future__ import print_function
import numpy as np
from .hero import *


class Zhuge(Hero):
    def __init__(self, level=1, equips=[]):
        super(Zhuge, self).__init__()
        self.basic_init()
        # Skill Add points
        skills = [0, 0, 0]  # Zhu 1 Fu 2

        def addpoints():
            for _ in range(level):
                if skills[2] < (level) // 4 and skills[2] < 3:
                    skills[2] += 1
                elif skills[1] < (level + 1) // 2 and skills[1] < 6:
                    skills[1] += 1
                else:
                    skills[0] += 1
            assert sum(skills) == level, "Add points Wrong..."

        addpoints()
        self.skill_1 = Skill(skills[1])
        self.skill_2 = Skill(skills[0])
        self.skill_ult = Skill(skills[2])
        self.skill_passive = Skill(0)

        # initialization
        self.set_level(level)
        self.initilize_all()
        # Caution Maozi
        self.add_equips(equips)
        # add equips

        print(self.__class__.__name__, "Lv", self.level, ": Power", self.power, "ExAttack: ", self.expower)

        self.print_info()

    def add_runes(self):
        """Standard Zhuge Runes"""
        self.magic_penetration += 88
        self.magic_vampire += 0.1
        self.expower += 66

        """My Runes"""
        if False:
            self.magic_vampire += 0
            self.magic_penetration += 0
            self.expower += 0

    def print_info(self):
        verbose_print("Level: {}, \n"
                      "Power ({} + {}),\n "
                      "Max HP ({} + {}),  Max MP ({} + {}),\n "
                      "Armor ({} + {}),  Spell_resis ({} + {})\n"
                      "Magic Penetration {}, {}%\n".format(self.level,
                                                           self.power, self.expower,
                                                           self.max_hp, self.ex_max_hp, self.max_mp, self.ex_max_mp,
                                                           self.armor, self.exarmor, self.spell_resistance,
                                                           self.exspell_resis,
                                                           self.magic_penetration, self.magic_penetration_percent))

    def basic_init(self):
        """With Runes"""
        self.attack_1 = 156
        self.attck_15 = 287
        self.attack_inc = 0

        self.power_1 = 0
        self.power_15 = 0
        self.power_inc = 0

        self.attack_speed_1 = 0
        self.attack_speed_15 = 14
        self.as_inc = 0

        self.speed = 380
        self.max_hp_1 = 3135
        self.max_hp_15 = 5968
        self.hp_inc = 0

        self.max_mp_1 = 490
        self.max_mp_15 = 0
        self.mp_inc = 0

        # Armor and spell resistance
        self.armor_1 = 87
        self.armor_15 = 330
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
        self.critical_damage = 2.0

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

    def init_passive_skill(self, level=0):
        self.skill_passive.skill_level = 0
        self.skill_passive.base_damage = 270
        self.skill_passive.addition_by_power = 0.52

    def init_skill_1(self):
        """30% multi"""
        self.skill_1.base_damage = 500
        self.skill_1.addition_by_skill_level = 60
        self.skill_1.addition_by_power = 0.75

    def init_skill_2(self):
        """50% multi"""
        self.skill_2.base_damage = 350
        self.skill_2.addition_by_skill_level = 70
        self.skill_2.addition_by_power = 0.52

    def init_skill_ult(self):
        """1% sunshi => 2% damage"""
        self.skill_ult.base_damage = 450
        self.skill_ult.addition_by_skill_level = 150
        self.skill_ult.addition_by_power = 0.5

    def passive_skill_function(self, damage):
        magic_damage = self.skill_passive.function(self)
        verbose_print(
            "[{}] Do skill_passive: Lv {} , damage: {}".format(self.__class__.__name__, self.skill_passive.skill_level,
                                                               magic_damage))
        return magic_damage

    def skill_1_function(self, enemy):
        magic_damage = self.skill_1.function(self)
        verbose_print("[{}] Do skill_1: Lv {} , damage: {}".format(self.__class__.__name__, self.skill_1.skill_level,
                                                                   magic_damage))
        return magic_damage

    def skill_2_function(self):
        magic_damage = self.skill_2.function(self)
        verbose_print("[{}] Do skill_2: Lv{} , damage:{}".format(self.__class__.__name__, self.skill_2.skill_level,
                                                                 magic_damage))
        return magic_damage

    def skill_ult_function(self, enemy):
        magic_damage = self.skill_ult.function(self)
        verbose_print(
            "[{}] Ult Origin Dmg: Lv{} , damage:{}".format(self.__class__.__name__, self.skill_ult.skill_level,
                                                           magic_damage))
        loss_per = (enemy.ex_max_hp + enemy.max_hp - enemy.hp) / (enemy.ex_max_hp + enemy.max_hp)
        magic_damage *= (1.0 + (loss_per * 100 // 1) * 2 / 100)
        verbose_print("[{}] Do skill_ult: Lv{} , damage:{}".format(self.__class__.__name__, self.skill_ult.skill_level,
                                                                   magic_damage))
        return magic_damage

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
        damage = self.skill_ult_function(enemy)
        self.damage_combo_to_hero(enemy, damage)

        # damage = self.equips_functions(enemy)
        # self.damage_combo_to_hero(enemy, damage)
        # self.passive_skill_function()

        # print("[{}] Total damage: {}".format(self.__class__.__name__, enemy.max_hp - enemy.hp))

        return self.to_do_physical_damage

    def damage_combo_to_hero(self, enemy, damage=0):
        assert isinstance(enemy, Hero), "Oh, {} is not I wanted .".format(type(enemy))

        remain_resis = (enemy.spell_resistance + enemy.exspell_resis) * (
        1 - self.magic_penetration_percent) - self.magic_penetration
        remain_resis = max(remain_resis, 0)
        magic_defence_percent = (remain_resis) / (remain_resis + enemy.defence_baseline)
        verbose_print("{}'s Remain Resis: {}, defence_percent: {} ".format(enemy.__class__.__name__, remain_resis,
                                                                           magic_defence_percent))
        if damage > 0:
            received_damage = (1 - magic_defence_percent) * damage
        else:
            received_damage = (1 - magic_defence_percent) * self.to_do_physical_damage

        print("Did {} damage".format(received_damage, enemy.__class__.__name__))

        enemy.hp -= received_damage
        print("{}'s Remaining HP : {}".format(enemy.__class__.__name__,
                                              progress_bar(enemy.hp, enemy.ex_max_mp + enemy.max_hp)))
        self.to_do_physical_damage = 0
