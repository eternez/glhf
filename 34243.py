import keyboard
import mcpi.minecraft as minecraft
import sys
import mcpi.block as block
mc=minecraft.Minecraft.create()
import time
def f():
    mc.setBlocks(100,100,100,200,100,100,5)
while True:
    if keyboard.is_pressed("r"):
       f()

