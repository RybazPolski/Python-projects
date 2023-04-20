from mcpi.minecraft import *
from mcpi.block import *
from mcpi.entity import *
from mcpi.event import *
from Entities import Entities
from Blocks import Blocks

mc = Minecraft.create()
BlockOptions=[]
EntityOptions=[]
for v in Blocks:
    # print(f"Name: {v}, ID: {Blocks[v]}")
    BlockOptions.append(v)
for v in Entities:
    # print(f"Name: {v}, ID: {Entities[v]}")
    EntityOptions.append(v)

def Teleport(x=mc.player.getTilePos().x,y=mc.player.getTilePos().y,z=mc.player.getTilePos().z):
    mc.player.setPos(x,y,z)

def SpawnMob(name,x=mc.player.getTilePos().x,y=mc.player.getTilePos().y,z=mc.player.getTilePos().z):
    mc.spawnEntity(x,y,z,Entities[name])

def SetBlock(name,x=mc.player.getTilePos().x,y=mc.player.getTilePos().y,z=mc.player.getTilePos().z):
    mc.setBlock(x,y,z,Blocks[name])

def PlaceMessage(message=[],standing=True,facing="N",x=mc.player.getTilePos().x,y=mc.player.getTilePos().y,z=mc.player.getTilePos().z):
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
    mc.setSign(x,y,z,id,rot,message)
