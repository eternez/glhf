
import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

import random
#mc.player.setTilePos(500,115,230)

while True:
    
    x = random.randint(500,550)
    z = random.randint(230,280)
    mc.setBlock(x,114,z,41)
