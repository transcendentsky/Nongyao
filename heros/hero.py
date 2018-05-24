from __future__ import print_function
import numpy as np

verbose = False


def verbose_print(*args, **kwargs):
    if verbose:
        for x in args:
            print(x, end=' ')
        for key, value in kwargs.iteritems():
            print(value, end=' ')
        print(' ')


_DEBUG = False


def ll(*args):
    if _DEBUG:
        for x in args:
            x = "[DEBUG] " + str(x)
            print(x, end='')
        print(" ")


class Hero(object):
    def __init__(self):
        self.level = 1

        self.attack = 0
        self.exattack = 0
        self.attack_1 = 0
        self.attck_15 = 0
        self.attack_inc = 0

        self.power = 0
        self.expower = 0
        self.power_inc = 0
        # attack speed
        self.attack_speed = 0
        self.attack_speed_1 = 0
        self.attack_speed_15 = 0
        self.as_inc = 0

        self.speed = 0
        # HP
        self.max_hp = 0
        self.ex_max_hp = 0
        self.max_hp_1 = 0
        self.max_hp_15 = 0
        self.hp = 0
        self.hp_inc = 0
        # MP
        self.max_mp = 0
        self.ex_max_mp = 0
        self.max_mp_1 = 0
        self.max_mp_15 = 0
        self.mp_inc = 0
        # Armor
        self.armor = 0
        self.exarmor = 0
        self.armor_1 = 0
        self.armor_15 = 0
        self.armor_inc = 0

        self.spell_resistance = 0
        self.exspell_resis = 0
        self.spell_resis_1 = 0
        self.spell_resis_15 = 0
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

        # Skills
        # self.skill_1 = Skill()
        # self.skill_2 = Skill()
        # self.skill_3 = Skill()
        # self.skill_ult = Skill()

        self.equips_funcs = {}

        self.defence_baseline = 602

        self.to_do_physical_damage = 0

        # Buffs
        self.bujiaxie_buff = False
        self.pojun_buff = False
        self.moshi_buff = False

    def print_info(self):
        verbose_print("Level: {}, \n"
                      "Attack ({} + {}),  AttackSpeed {},\n "
                      "Max HP ({} + {}),  Max MP ({} + {}),\n "
                      "Armor ({} + {}),  Spell_resis ({} + {})\n"
                      "Critical {}, {}%\n"
                      "Penetration {}, {}%".format(self.level,
                                                   self.attack, self.exattack, self.attack_speed,
                                                   self.max_hp, self.ex_max_hp, self.max_mp, self.ex_max_mp,
                                                   self.armor, self.exarmor, self.spell_resistance, self.exspell_resis,
                                                   self.critical_chance, 100 * self.critical_damage,
                                                   self.armor_penetration, self.armor_penetration_percent))

    def init_incs(self):
        self.attack_inc = self.attck_15 - self.attack_1
        self.attack_inc /= 14.0
        ll(self.attack_inc)

        self.as_inc = self.attack_speed_15 - self.attack_speed_1
        self.as_inc /= 14.0
        ll(self.as_inc)

        self.hp_inc = self.max_hp_15 - self.max_hp_1
        self.hp_inc /= 14.0
        ll(self.hp_inc)

        self.armor_inc = self.armor_15 - self.armor_1
        self.armor_inc /= 14.0
        ll(self.armor_inc)

        self.spell_resis_inc = self.spell_resis_15 - self.spell_resistance
        self.spell_resis_inc /= 14.0
        ll(self.spell_resis_inc)

    def init_state(self):
        inc_level = self.level - 1
        self.attack += self.attack_1 + inc_level * self.attack_inc
        self.attack_speed += self.attack_speed_1 + inc_level * self.as_inc

        self.armor += self.armor_1 + inc_level * self.armor_inc
        self.spell_resistance += self.spell_resis_1 + inc_level * self.spell_resis_inc

        self.max_hp += self.max_hp_1 + inc_level * self.hp_inc
        self.max_mp += self.max_mp_1 + inc_level * self.mp_inc

        self.hp += self.max_hp + self.ex_max_hp
        ll(" ### Updated ###")
        # etc.....

    def passive_skill_function(self):
        pass

    def do_damage(self):
        pass

    def receive_damage(self, damage):
        self.init_state()
        physic_defence_percent = (self.armor) / (self.armor + self.defence_baseline)
        received_damage = (1 - physic_defence_percent) * damage
        verbose_print("Received damage: {}".format(received_damage))

    def set_level(self, level):
        self.level = level

    def add_equips(self, xs):
        ll("add equips?? xs = {}".format(xs))
        for x in xs:
            self.add_equip(x)

    def add_equip(self, x):
        ll("????? ", self.__class__.__name__)
        if x == 0:  # Ping A
            verbose_print("*** Attack ***")

            def wfunc():
                def hero_attack(hero, enemy=None):
                    verbose_print("==> Hero Attack")
                    if enemy.bujiaxie_buff:
                        ll(">>> Defend by Bujiaxie..")
                        return (hero.exattack + hero.attack) * 0.85
                    return hero.attack + hero.exattack

                return hero_attack

            self.equips_funcs.update({'attack': wfunc()})

        elif x == 1:  # wujin
            ll('wujin', self.attack)
            self.exattack += 120
            self.critical_damage += 0.5
            self.critical_chance += 0.2
            verbose_print("[Equip] Wujin")
        elif x == 2:  # heiqie
            ll('heiqie', self.attack, self.max_hp)
            self.exattack += 85
            self.cd += 0.15
            self.ex_max_hp += 500
            verbose_print("[Equip] Hei Qie")
            self.armor_penetration += 50 + self.level * 10
        elif x == 3:  # zongshi
            self.exattack += 60
            self.ex_max_hp += 400
            self.ex_max_mp += 400
            verbose_print("[Equip] Zong SHI")
            self.critical_chance += 0.2

            def zongshi_f(hero, enemy=None):
                verbose_print("[Equipment func] Zongshi Power")
                return hero.attack + hero.exattack

            self.equips_funcs.update({'zongshi_f': zongshi_f})

        elif x == 4:  # pojia
            self.exattack += 80
            self.cd += 0.1
            verbose_print("[Equip] Pojia")
            self.armor_penetration_percent += 0.45
        elif x == 5:  # pojun
            self.exattack += 200
            self.pojun_buff = True
            verbose_print("[Equip] Pojun")
        elif x == 6:  # moshi
            verbose_print('[Equip] Moshi')
            self.exattack += 60
            self.attack_speed += 0.3
            # def moshi_f(enemy):
            #     return enemy.hp * 0.08
            # self.equips_funcs.update({'moshi_f':moshi_f})
            self.moshi_buff = True

        elif x == 11:  # Bujiaxie
            verbose_print("[Equip] Bujiaxie")
            self.exarmor += 110
            self.bujiaxie_buff = True


class Skill(object):
    def __init__(self, level=0):
        self.trigger_times = 1
        self.skill_cd = 0

        self.skill_level = level
        self.base_damage = 0
        self.addition_by_attack = 0
        self.addition_by_power = 0
        self.addition_by_skill_level = 0
        self.addition_by_hero_level = 0

    def set_level(self, level):
        self.skill_level = level

    def function(self, hero, show_damage=True, ex=True):
        assert isinstance(hero, Hero), "args classes not right.."
        if show_damage == False:
            hero.to_do_physical_damage += self.trigger_times * (self.base_damage +
                                                                (self.skill_level - 1) * self.addition_by_skill_level +
                                                                hero.attack * self.addition_by_attack)
        else:
            if ex:
                return self.trigger_times * (self.base_damage +
                                             (self.skill_level - 1) * self.addition_by_skill_level +
                                             hero.exattack * self.addition_by_attack)
            else:
                return self.trigger_times * (self.base_damage +
                                             (self.skill_level - 1) * self.addition_by_skill_level +
                                             hero.attack * self.addition_by_attack)
                # Not implement Magic Damge


def progress_bar(x, all, length=20):
    if x < 0: x = 0
    percent = x / all
    block_num = int(round(percent * length))
    return "{:.2f} \t[{}{}] | {:.2%}".format(x, block_num * '#', (length - block_num) * '.', percent)
