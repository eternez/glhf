import mcpi.minecraft as minecraft
mc=minecraft.Minecraft.create()
import mcpi.block as block
import time
def stemincraft():
    #лист 1низ
    mc.setBlocks(369,70,328,369,70,328,18)
    mc.setBlocks(370,70,329,370,70,329,18)
    mc.setBlocks(371,70,328,370,70,328,18)
    mc.setBlocks(370,70,327,370,70,327,18)
    #лист 2низ
    mc.setBlocks(369,71,329,371,71,331,18)
    mc.setBlocks(371,71,329,373,71,327,18)
    mc.setBlocks(369,71,329,367,71,327,18)
    mc.setBlocks(371,71,327,369,71,325,18)
    #чё-то
    mc.setBlocks(372,71,330,372,71,330,18)
    mc.setBlocks(368,71,330,368,71,330,18)
    mc.setBlocks(368,71,326,368,71,326,18)
    mc.setBlocks(372,71,326,372,71,326,18)
     #3ряд
    mc.setBlocks(370,72,329,370,72,330,18)
    mc.setBlocks(368,72,330,368,72,330,18)
    mc.setBlocks(369,72,329,369,72,330,18)
    mc.setBlocks(369,72,330,369,72,330,0)
    #чтобы не лагало
    mc.setBlocks(369,72,328,368,72,328,18)
    mc.setBlocks(369,72,327,369,72,327,18)
    mc.setBlocks(368,72,326,368,72,326,18)
    #ну вы поняли
    mc.setBlocks(370,72,327,370,72,326,18)
    #aga
    mc.setBlocks(371,72,327,371,72,327,18)
    mc.setBlocks(372,72,326,372,72,326,18)
    mc.setBlocks(371,72,328,372,72,328,18)
    #last
    mc.setBlocks(371,72,329,371,72,329,18)
    mc.setBlocks(372,72,330,372,72,330,18)
    #дальше
    mc.setBlocks(371,73,328,371,73,328,18)
    mc.setBlocks(370,73,329,370,73,329,18)
    mc.setBlocks(369,73,328,369,73,328,18)
    mc.setBlocks(370,73,327,370,73,327,18)
    #ещё
    mc.setBlocks(370,74,328,370,74,328,18)
    #ствол
    mc.setBlocks(370,71,328,370,73,328,17)
    while True:
        mc.setBlocks(370,75,328,370,75,328,41)
        time.sleep(0.5)
        mc.setBlocks(370,75,328,370,75,328,0)
        time.sleep(0.5)
        mc.setBlocks(370,75,328,370,75,328,57)
        time.sleep(0.5)
        mc.setBlocks(370,75,328,370,75,328,0)
        time.sleep(0.5)
        mc.setBlocks(370,75,328,370,75,328,89)
        time.sleep(0.5)
        mc.setBlocks(370,75,328,370,75,328,0)
        time.sleep(0.5)
        mc.setBlocks(370,75,328,370,75,328,41)
        time.sleep(0.5)
        mc.setBlocks(370,75,328,370,75,328,0)
        time.sleep(0.5)
        mc.setBlocks(370,75,328,370,75,328,89)
        time.sleep(0.5)
stemincraft()
