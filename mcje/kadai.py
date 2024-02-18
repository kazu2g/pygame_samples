from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('kadai #1  the first golden block')

mc.setBlock(0, 5, 0,  param.GOLD_BLOCK)