from mcpi.minecraft import *
from mcpi.block import *
from mcpi.entity import *
from mcpi.event import *
from mcpi.connection import *
from Entities import Entities
from Blocks import Blocks

BlockOptions=[]
EntityOptions=[]
for v in Blocks:
    BlockOptions.append(v)
for v in Entities:
    EntityOptions.append(v)

try:
    # mc = Minecraft.create()
    
    def Teleport(x="current player x",y="current player y",z="current player z"):
        mc = Minecraft.create()
        playerPos = mc.player.getPos()
        if x=="current player x":
            x = playerPos.x
        
        if y=="current player y":
            y = playerPos.y
        
        if z=="current player z":
            z = playerPos.z
        
        mc.player.setPos(x,y,z)

    def SpawnMob(name,x="current player x",y="current player y",z="current player z"):
        mc = Minecraft.create()
        playerPos = mc.player.getPos()
        
        if x=="current player x":
            x = playerPos.x
        
        if y=="current player y":
            y = playerPos.y
        
        if z=="current player z":
            z = playerPos.z
            
        mc.spawnEntity(x,y,z,Entities[name])

    def SetBlock(name,x="current player x",y="current player y",z="current player z"):
        mc = Minecraft.create()
        playerPos = mc.player.getPos()
        
        if x=="current player x":
            x = playerPos.x
        
        if y=="current player y":
            y = playerPos.y
        
        if z=="current player z":
            z = playerPos.z
            
        mc.setBlock(x,y,z,Blocks[name])

    def PlaceMessage(message=[],standing=True,facing="N",x="current player x",y="current player y",z="current player z"):
        if(standing):
            id = 63
            if facing=="N":
                rot = 8
            elif facing=="S":
                rot = 0
            elif facing=="W":
                rot = 4
            elif facing=="E":
                rot = 12
            else:
                rot = facing
        else:
            id = 68
            if facing=="N":
                rot = 2
            elif facing=="S":
                rot = 3
            elif facing=="W":
                rot = 4
            elif facing=="E":
                rot = 5
            else:
                rot = facing
        
        mc=Minecraft.create()
        playerPos = mc.player.getPos()
        
        if x=="current player x":
            x = playerPos.x
        
        if y=="current player y":
            y = playerPos.y
        
        if z=="current player z":
            z = playerPos.z
            
        mc.setSign(x,y,z,id,rot,message)

except RequestError:
    print("Nie znaleziono serwera lub gracza. Upewnij się że wszystko gra.")
    exit()
