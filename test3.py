from heros.Houyi import Houyi
from heros.hero import *
from heros.ake import Ake
from heros.Zhuge import Zhuge
import numpy as np

"""
1:30    Jungle lv4  700  top lv2~3  600  
        No Attack Equips
2:30                   top lv4    800~ 
        1~2 Iron Sword
4:00    Jungle lv6  2000+

6:00    Jungle lv8  3000~4000
        Wujin
9~10:00 Jungle lv12 6000+
        Wujin Heiqie
12:00   Jungle lv14 8000~
        Wujin Heiqie + Pojia/Zongshi
"""

print("#############################################")
# Mianju 33  Xueshu 34 ==> 37.7%
# Mianju 33  Xueshu 34  Huiyue 35 ==> 39.8%
# Mianju 33  Xueshu 34  Maozi  32 ==> 44%

zhuge_1 = Zhuge(12, [33,34,32])
houyi_1 = Houyi(10, [11])
# print(houyi_1.hp)
# print("\n>>>>>>   Set Hp : {}".format(houyi_1.set_hp(percent=0.3)))
# damage = zhuge_1.damage_combo(houyi_1)

def search_deadline():
    print("???")
    for x in np.linspace(0.6,0.0,200):
        print(">>>>>>   Set Hp : {}".format(houyi_1.set_hp(percent=x)))
        damage = zhuge_1.damage_combo(houyi_1)
        if houyi_1.hp <=0.0:
            print("........................")
            print("The Dead line is {}".format(x))
            print("........................")
            break

search_deadline()