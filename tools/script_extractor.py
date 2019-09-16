#!/usr/bin/env python3

import argparse

#TODO:
# - Add arguments to all functions (have fun lol)
# - implement text
# - (Possibly) add new type of word that looks for matches in the sym file
# - enter to continually generate more lines of the script
# - full script mode?
# - Make pretty!!

def decodeLine(scriptList, game_data, loc, ignore_broken):
	currLine = scriptList[game_data[loc]]
	ret = "\trun_script " + currLine[0] + "\n"
	loc+=1
	quit = currLine[2]
	for c in currLine[1]:
		if c == "b":
			ret += "\tdb $" + format(game_data[loc],"02x") + "\n"
			loc += 1
		elif c == "w":
			ret += "\tdb $" + format((game_data[loc] + (game_data[loc+1]<<8)),"04x") + "\n"
			loc += 2
		elif c == "t":
			ret += "\ttx Text" + format((game_data[loc] + (game_data[loc+1]<<8)),"04x") + "\n"
			loc += 2
		elif c == "q":
			print("haven't updated data for this yet")
			if not ignore_broken:
				quit = True
	return (loc, ret, quit)
			

def main():
	scriptList = createList()

	with open("tcg.gbc", "rb") as file:
	    game_data = file.read()
	loc = 0xd52e
	auto = True
	end = False
	ignore_broken = True
	script = ""
	if game_data[loc] != 0xe7:
		print("Error: first byte was not start_script")
	else:
 		
		# TODO this is hacky please don't do this 
		ls = format(loc,"04x")
		lsa = format(loc-0x8000,"04x")
		print("OWSequence_" + ls + ": ; " + ls + " (3:" + lsa + ")" )
		loc += 1
		print("\tstart_script")
	while not end:
		loc, outstr, end = decodeLine(scriptList,game_data,loc,ignore_broken)
		outstr = outstr[:-1] # [:-1] strips the newline at the end
		if auto:
			print(outstr)
		else:
			input(outstr)
	print("; " + hex(loc))
		

def createList(): # this is a func just so all this can go at the bottom
	# name, arg list, is an ender
	return [
	("OWScript_EndScriptLoop1", "", True),
	("OWScript_CloseTextBox", "", False),
	("OWScript_PrintTextString", "t", False),
	("Func_ccdc", "bb", False),
	("OWScript_AskQuestionJump", "bbbb", False), # more complex behavior too (jumping)
	("OWScript_StartBattle", "bbb", False),
	("Func_cd83", "bbbb", False),
	("Func_cda8", "bbbb", False),
	("OWScript_PrintTextCloseBox", "t", False),
	("Func_cdcb", "bb", False),
	("Func_ce26", "bb", False),
	("Func_ce84", "", False),
	("OWScript_GiveBoosterPacks", "bbb", False),
	("Func_cf0c", "bbb", False), # more complex behavior too (jumping)
	("Func_cf12", "bbb", False),
	("Func_cf3f", "b", False),
	("Func_cf4c", "b", False),
	("Func_cf53", "d", False), # more complex behavior too (jumping)
	("Func_cf7b", "", False),
	("Func_cf2d", "bbbb", False), # more complex behavior too (jumping + ??)
	("Func_cf96", "d", False), # only jumps? still needs args to do that though
	("Func_cfc6", "b", False),
	("Func_cfd4", "", False),
	("Func_d00b", "", False), # includes something with random and extra data
	("Func_d025", "d", False), # possibly only jumps, still needs args
	("Func_d032", "d", False), # see above
	("Func_d03f", "", False),
	("OWScript_ScriptJump", "d", False), # jumps to d
	("Func_d04f", "", False),
	("Func_d055", "b", False),
	("OWScript_MovePlayer", "bb", False),
	("Func_cee2", "b", False),
	("OWScript_SetDialogName", "b", False),
	("Func_d088", "bbb", False),
	("Func_d095", "bbb", False),
	("Func_d0be", "bb", False),
	("OWScript_DoFrames", "b", False),
	("Func_d0d9", "bbb", False), # jumps but still needs args
	("Func_d0f2", "bbb", False), # jumps but still needs args
	("Func_ce4a", "bb", False),
	("Func_ceba", "q", False),
	("Func_d103", "q", False),
	("Func_d125", "q", False),
	("Func_d135", "q", False),
	("Func_d16b", "q", False),
	("Func_cd4f", "q", False),
	("Func_cd94", "q", False),
	("Func_ce52", "q", False),
	("Func_cdd8", "q", False),
	("Func_cdf5", "q", False),
	("Func_d195", "q", False),
	("Func_d1ad", "q", False),
	("Func_d1b3", "q", False),
	("OWScript_EndScriptCloseText", "", True), # it calls inc twice but it ends anyway?
	("Func_d244", "q", False),
	("Func_d24c", "q", False),
	("OWScript_OpenDeckMachine", "q", False),
	("Func_d271", "q", False),
	("Func_d36d", "bbbbb", False),
	("Func_ce6f", "q", False),
	("Func_d209", "q", False),
	("Func_d38f", "q", False),
	("Func_d396", "q", False),
	("Func_cd76", "q", False),
	("Func_d39d", "q", False),
	("Func_d3b9", "q", False),
	("Func_d3c9", "q", False),
	("Func_d3d1", "q", False),
	("Func_d3d4", "q", False),
	("Func_d3e0", "", False),
	("Func_d3fe", "q", False),
	("Func_d408", "q", False),
	("Func_d40f", "q", False),
	("Func_d416", "q", False),
	("Func_d423", "q", False),
	("Func_d429", "q", False),
	("Func_d41d", "q", False),
	("Func_d42f", "q", False),
	("Func_d435", "q", False),
	("Func_cce4", "q", False),
	("Func_d2f6", "q", False),
	("Func_d317", "q", False),
	("Func_d43d", "q", False),
	("OWScript_EndScriptLoop2", "q", True),
	("OWScript_EndScriptLoop3", "q", True),
	("OWScript_EndScriptLoop4", "q", True),
	("OWScript_EndScriptLoop5", "q", True),
	("OWScript_EndScriptLoop6", "q", True),
	("OWScript_CustomModifyEventFlags", "q", False),
	("Func_d460", "q", False),
	("OWScript_JumpIfFlagSet", "q", False),
	("Func_d484", "q", False),
	("Func_d49e", "q", False),
	("Func_d4a6", "q", False),
	("Func_d4ae", "q", False),
	("OWScript_SetEventFlags", "q", False),
	("Func_d4c3", "q", False),
	("Func_d4ca", "q", False),
	("OWScript_JumpIfFlagNotSet", "q", False),
	("Func_d452", "q", False),
	("OWScript_EndScriptLoop7", "q", True),
	("OWScript_EndScriptLoop8", "q", True),
	("OWScript_EndScriptLoop9", "q", True),
	("OWScript_EndScriptLoop10", "q", True)
	]

main()