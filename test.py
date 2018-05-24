from heros.ake import Ake
from heros.Houyi import Houyi
from heros.hero import *

# 3 2 1 Combo
# Wujin 1 Heiqie 2   + PingA
# Pojun = 5
ake_1 = Ake(12, [0,1,2], [3,6,3])
houyi_1 = Houyi(12)
damage = ake_1.damage_combo(houyi_1)

print("#############################################")
# Wujin Pojun  + Ping A
# 321 Combo
ake_1 = Ake(12, [0,1,5], [3,6,3])
houyi_1 = Houyi(12)
damage = ake_1.damage_combo(houyi_1)

# print("################################################")
# # moshi 6
# ake_1 = Ake(12, [0,1,6], [3,6,3])
# houyi_1 = Houyi(12)
# damage = ake_1.damage_combo(houyi_1)

print("#############################################")
# Bujiaxie
# 3 2 1 Combo
# Wujin 1 Heiqie 2   + PingA
# Pojun = 5
ake_1 = Ake(12, [0,1,2], [3,6,3])
houyi_1 = Houyi(12, [11])
damage = ake_1.damage_combo(houyi_1)

print("#############################################")
# Wujin Pojun  + Ping A
# 321 Combo
ake_1 = Ake(12, [0,1,5], [3,6,3])
houyi_1 = Houyi(12,[11])
damage = ake_1.damage_combo(houyi_1)
