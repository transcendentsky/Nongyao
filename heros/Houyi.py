from __future__ import print_function
import numpy as np
from .hero import Hero


class Houyi(Hero):
    def __init__(self, level=1, equips=[]):
        super(Houyi, self).__init__()
        self.attack_1 = 161
        self.attck_15 = 396
        self.attack_inc = 0

        self.spell_power = 0
        self.power_inc = 0

        self.attack_speed_1 = 0
        self.attack_speed_15 = 28
        self.as_inc = 0

        self.speed = 360

        self.max_hp_1 = 3182
        self.max_hp_15 = 5986
        self.hp_inc = 0

        self.max_mp_1 = 1784
        self.max_mp_15 = 0
        self.mp_inc = 0

        self.armor_1 = 86
        self.armor_15 = 336
        self.armor_inc = 0

        self.spell_resis_1 = 50
        self.spell_resis_15 = 169
        self.spell_resis_inc = 0

        self.armor_penetration = 0
        self.armor_penetration_percent = 0
        self.magic_penetration = 0
        self.magic_penetration_percent = 0


        self.critical_chance = 0
        self.critical_damage = 2.0

        self.cd = 0
        # Blood sucking
        self.physical_vampire = 0
        self.magic_vampire = 0

        self.set_level(level)
        self.init_incs()
        self.init_state()

        self.add_equips(equips)

        print(self.__class__.__name__, "Lv" ,self.level, ": HP", self.hp)

        self.print_info()

    # def receive_damage(self, damage):


    