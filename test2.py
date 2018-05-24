from heros.Houyi import Houyi
from heros.hero import *
from heros.ake import Ake

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
# Bujiaxie
# 3 2 1 Combo
# Wujin 1 Heiqie 2  Zongshi 3 // + PingA
# Pojun = 5
ake_1 = Ake(12, [0,1,2], [2,3,1])
houyi_1 = Houyi(12, [11])
# print(houyi_1.hp)
damage = ake_1.damage_combo(houyi_1)


print("#############################################")
# Bujiaxie
# Wujin 1 Heiqie 2 Pojiagong 4  //+ PingA
# Pojun = 5
ake_2 = Ake(14, [0,1,2,4], [3,6,3])
houyi_2 = Houyi(14, [])
# print(houyi_2.attack)
damage = ake_2.damage_combo(houyi_2)

print("#############################################")
# Bujiaxie
# Wujin 1 Heiqie 2 //Pojiagong 4 Pojun 5  //+ PingA
# Pojun = 5
ake_2 = Ake(14, [0,1,2,5], [3,6,3])
houyi_2 = Houyi(14, [])
# print(houyi_2.attack)
damage = ake_2.damage_combo(houyi_2)

print("#############################################")
# Bujiaxie
# Wujin 1 Heiqie 2 //Pojiagong 4 Pojun 5  //+ PingA
# Pojun = 5
ake_2 = Ake(14, [1,2,3], [3,6,3])
houyi_2 = Houyi(14, [11])
# print(houyi_2.attack)
damage = ake_2.damage_combo(houyi_2)