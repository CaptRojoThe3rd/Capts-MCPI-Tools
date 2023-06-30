# Import modules
import sys
from mcpi.minecraft import Minecraft

# Python 3.10 check
python_version_data = sys.version.split(".")
if int(python_version_data[0]) < 3 or int(python_version_data[1]) < 10:
	print("This program requires Python 3.10.")
	input()
	quit()

mc = Minecraft.create()
mc.postToChat("Hello, world!")

# Assign block IDs and damage values for commands
# True/False determines whether the player is allowed to modify the damage value
# Split into 10s for organization
BLOCK_IDS = {
	"air": 						[0, 0, True],
	"stone": 					[1, 0, True],
	"grass_block":				[2, 0, True],
	"dirt":						[3, 0, True],
	"cobblestone":				[4, 0, True],
	"wood_planks":				[5, 0, True],
	"oak_planks":				[5, 0, False],
	"sapling":					[6, 0, True],
	"oak_sapling":				[6, 0, False],
	"spruce_sapling":			[6, 1, False],
	"birch_sapling":			[6, 2, False],
	"bedrock":					[7, 0, True],
	"water":					[8, 0, True],
	"stationary_water":			[9, 0, True],

	"lava":						[10, 0, True],
	"stationary_lava":			[11, 0, True],
	"sand":						[12, 0, True],
	"gravel":					[13, 0, True],
	"gold_ore":					[14, 0, True],
	"iron_ore":					[15, 0, True],
	"coal_ore":					[16, 0, True],
	"log":						[17, 0, True],
	"oak_log":					[17, 0, False],
	"spruce_log":				[17, 1, False],
	"birch_log":				[17, 2, False],
	"leaves":					[18, 0, True],
	"oak_leaves":				[18, 0, False],
	"spruce_leaves":			[18, 1, False],
	"birch_leaves":				[18, 2, False],

	"glass":					[20, 0, True],
	"lapis_lazuli_ore":			[21, 0, True],
	"lapis_lazuli_block":		[22, 0, True],
	"sandstone":				[24, 0, True],
	"chiseled_sandstone":		[24, 1, False],
	"cut_sandstone":			[24, 2, False],
	"bed":						[26, 0, True],

	"cobweb":					[30, 0, True],
	"tall_grass":				[31, 0, True],
	"dead_bush":				[31, 0, False],
	"grass":					[31, 1, False],
	"fern":						[31, 3, False],
	"wool":						[35, 0, True],
	"white_wool":				[35, 0, False],
	"orange_wool":				[35, 1, False],
	"magenta_wool":				[35, 2, False],
	"light_blue_wool":			[35, 3, False],
	"yellow_wool":				[35, 4, False],
	"lime_wool":				[35, 5, False],
	"pink_wool":				[35, 6, False],
	"gray_wool":				[35, 7, False],
	"light_gray_wool":			[35, 8, False],
	"cyan_wool":				[35, 9, False],
	"purple_wool":				[35, 10, False],
	"blue_wool":				[35, 11, False],
	"brown_wool":				[35, 12, False],
	"green_wool":				[35, 13, False],
	"red_wool":					[35, 14, False],
	"black_wool":				[35, 15, False],
	"dandelion":				[37, 0, True],
	"cyan_rose":				[38, 0, True],
	"brown_mushroom":			[39, 0, True],

	"red_mushroom":				[40, 0, True],
	"gold_block":				[41, 0, True],
	"iron_block":				[42, 0, True],
	"smooth_stone_double_slab":	[43, 0, False],
	"sandstone_double_slab":	[43, 1, False],
	"wood_double_slab":			[43, 2, False],
	"cobblestone_double_slab":	[43, 3, False],
	"brick_double_slab":		[43, 4, False],
	"stone_brick_double_slab":	[43, 5, False],
	"nether_brick_double_slab":	[43, 6, False],
	"quartz_double_slab":		[43, 7, False],
	"smooth_stone_slab":		[44, 0, False],
	"sandstone_slab":			[44, 1, False],
	"wood_slab":				[44, 2, False],
	"cobblestone_slab":			[44, 3, False],
	"brick_slab":				[44, 4, False],
	"stone_brick_slab":			[44, 5, False],
	"nether_brick_slab":		[44, 6, False],
	"quartz_slab":				[44, 7, False],
	"bricks":					[45, 0, True],
	"tnt":						[46, 0, True],
	"bookshelf":				[47, 0, True],
	"mossy_cobblestone":		[48, 0, True],
	"obsidian":					[49, 0, True],

	"torch":					[50, 0, True],
	"fire":						[51, 0, True],
	"wood_stairs":				[53, 0, True],
	"oak_stairs":				[53, 0, False],
	"chest":					[54, 0, True],
	"diamond_ore":				[56, 0, True],
	"diamond_block":			[57, 0, True],
	"crafting_table":			[58, 0, True],
	"wheat":					[59, 0, True],

	"farmland":					[60, 0, True],
	"furnace":					[61, 0, True],
	"active_furnace":			[62, 0, True],
	"wood_door":				[64, 0, True],
	"oak_door":					[64, 0, False],
	"ladder":					[65, 0, True],
	"cobblestone_stairs":		[67, 0, True],

	"iron_door":				[71, 0, True],
	"redstone_ore":				[73, 0, True],
	"snow_layer":				[78, 0, True],
	"ice":						[79, 0, True],

	"snow_block":				[80, 0, True],
	"cactus":					[81, 0, True],
	"clay":						[82, 0, True],
	"sugar_cane":				[83, 0, True],
	"fence":					[85, 0, True],
	"oak_fence":				[85, 0, False],
	"netherrack":				[87, 0, True],
	"glowstone":				[89, 0, True],

	"invisible_bedrock":		[95, 0, True],
	"trapdoor":					[96, 0, True],
	"stone_bricks":				[98, 0, True],

	"glass_pane":				[102, 0, True],
	"melon":					[103, 0, True],
	"melon_stem":				[105, 0, True],
	"fence_gate":				[107, 0, True],
	"oak_fence_gate":			[107, 0, False],
	"brick_stairs":				[108, 0, True],
	"stone_brick_stairs":		[109, 0, True],

	"nether_bricks":			[112, 0, True],
	"nether_brick_stairs":		[114, 0, True],

	"sandstone_stairs":			[128, 0, True],

	"quartz":					[155, 0, False],
	"chiseled_quartz":			[155, 1, False],
	"quartz_pillar":			[155, 2, False],
	"quartz_stairs":			[156, 0, True],

	"stonecutter":				[245, 0, True],
	"glowing_obsidian":			[246, 0, True],
	"nether_reactor_core":		[247, 0, True],

	"painting":					[321, 0, True],
	
	"bone_meal":				[351, 0, True]
}

YES_INPUTS = ["Y", "y"]


# User input variables
user_input = ""
user_input_list = []

# Player variables
player_x = 0
player_y = 0
player_z = 0

# Command error handling
UNKNOWN_COMMAND 	= 0
TOO_FEW_ARGS 		= 1
ARG_NOT_INT			= 2
TOO_MANY_ARGS		= 3
UNKNOWN_BLOCK		= 4
CANT_MODIFY_DAMAGE	= 5
ARG_NOT_INT_OR_WORD	= 6
def displayError(error, details = 0):
	match error:
		case 0:
			print(f"Unknown command: {user_input_list[0]}")
		case 1:
			print(f"Too few arguments in command: {user_input}")
		case 2:
			print(f"Argument not integer: {user_input_list[details]}")
		case 3:
			print(f"Too many arguments in command: {user_input}")
		case 4:
			print(f"Unknown block: {user_input_list[details]}")
		case 5:
			print(f"Can't modify damage value of block: {user_input_list[details]}")
		case 6:
			print(f"Argument not integer or valid word: {user_input_list[details]}")

# Convert ~ to player position
def convertTilda(text, position_value):
	if "~" in text:
		text_modified = text.replace("~", "")
		if text_modified == "":
			return position_value
		return position_value + int(text_modified)
	return int(text)

# Teleport
# Teleports the player to the specified coordinates.
def teleport():
	if len(user_input_list) == 4:
		for i in range(1, 4):
			try:
				user_input_list[i] = int(convertTilda(user_input_list[i] [player_x, player_y, player_z][i]))
			except:
				displayError(ARG_NOT_INT, i)
				return
		mc.player.setPos(user_input_list[1], user_input_list[2], user_input_list[3])
	else:
		if len(user_input_list) < 4:
			displayError(TOO_FEW_ARGS)
		else:
			displayError(TOO_MANY_ARGS)
		return

# Setblock
# Sets the block at the given coordinates.
def setblock():
	for i in range(1, 4):
		try:
			user_input_list[i] = convertTilda(user_input_list[i], [0, player_x, player_y, player_z][i])
			user_input_list[i] = int(user_input_list[i])
		except:
			displayError(ARG_NOT_INT, i)
			return
	try:
		i = BLOCK_IDS[user_input_list[4]]
	except:
		displayError(UNKNOWN_BLOCK, 4)
		return
	if len(user_input_list) == 6:
		if i[2]:
			try:
				i[1] = int(user_input_list[5])
			except:
				displayError(ARG_NOT_INT, 5)
				return
		else:
			displayError(CANT_MODIFY_DAMAGE, 4)
	mc.setBlock(user_input_list[1], user_input_list[2], user_input_list[3], i[0], i[1])

# Fill
# Fills a specified region with blocks, and can replace only certain blocks if specified.
def fill():
	if len(user_input_list) < 8:
		displayError(TOO_FEW_ARGS)
		return
	if len(user_input_list) > 12:
		displayError(TOO_MANY_ARGS)
		return

	positions = [0, 0, 0, 0, 0, 0, 0]
	for i in range(1, 7):
		try:
			positions[i] = int(convertTilda(user_input_list[i], [0, player_x, player_y, player_z, player_x, player_y, player_z][i]))
		except:
			displayError(ARG_NOT_INT, i)
			return

	try:
		fill_block = BLOCK_IDS[user_input_list[7]]
	except:
		displayError(UNKNOWN_BLOCK)
		return

	replace_block = None
	replace_block_damage = 0
	fill_block_damage = 0
	if len(user_input_list) > 8:
		if user_input_list[8] == "replace":
			if len(user_input_list) < 10:
				displayError(TOO_FEW_ARGS)
				return
			try:
				replace_block = BLOCK_IDS[user_input_list[9]]
			except:
				displayError(UNKNOWN_BLOCK, 9)
				return
		else:
			if not fill_block[2]:
				displayError(CANT_MODIFY_DAMAGE, user_input_list[7])
				return
			try:
				fill_block_damage = int(user_input_list[8])
			except:
				displayError(ARG_NOT_INT_OR_WORD, 8)
				return
			if not fill_block[2]:
				fill_block_damage = fill_block[1]
			if len(user_input_list) > 10:
				if user_input_list[9] == "replace":
					try:
						replace_block = BLOCK_IDS[user_input_list[10]]
					except:
						displayError(UNKNOWN_BLOCK, 10)
					
	if replace_block == None:
		mc.setBlocks(positions[1], positions[2], positions[3], positions[4], positions[5], positions[6], fill_block, fill_block_damage)
	else:
		x_inc = int((positions[4] - positions[1]) / (positions[4] - positions[1]))
		y_inc = int((positions[5] - positions[2]) / (positions[5] - positions[2]))
		z_inc = int((positions[6] - positions[3]) / (positions[6] - positions[3]))
		for x in range(positions[1], positions[4] + x_inc, x_inc):
			for y in range(positions[2], positions[5] + y_inc, y_inc):
				for z in range(positions[3], positions[6] + z_inc, z_inc):
					if replace_block[0] == mc.getBlock(x, y, z):
						mc.setBlock(x, y, z, fill_block[0], fill_block_damage)

# Kill
# Kills the player.
def kill():
	mc.player.setPos(player_x, -256, player_z)

# Void
# Deletes all blocks in a world.
def void():
	if input("Are you sure you want to delete all blocks in this world? [Y/n] ") in YES_INPUTS:
		mc.setBlocks(-128, -64, -128, 128, 64, 128, 0)


# Main loop
while True:
	user_input = str(input("> "))

	player_x, player_y, player_z = mc.player.getPos()

	user_input_list = user_input.split(" ")
	if user_input_list[0] == "":
		continue
	
	if user_input_list[0][0] != "/":
		mc.postToChat(user_input)
		continue
	else:
		match user_input_list[0]:
			# /tp and /teleport
			case "/tp":
				teleport()
			case "/teleport":
				teleport()

			# /setblock
			case "/setblock":
				setblock()

			# /fill
			case "/fill":
				fill()

			# /kill
			case "/kill":
				kill()

			# /void
			case "/void":
				void()

			case _:
				displayError(UNKNOWN_COMMAND)

