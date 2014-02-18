from System import *

class chip8(object):
		self._memory = Array.CreateInstance(Byte, 4096)
		self._V = Array.CreateInstance(Byte, 16) # 15 GP CPU registers V0-VE. 16th register is for carry flag # Index register # The program counter
		self._gfx = Array.CreateInstance(Byte, 64 * 32) # This contains every pixel to write to the screen
		self._stack = Array.CreateInstance(UInt16, 16) # The stack # The stack pointer
		self._key = Array.CreateInstance(Byte, 16) #Hex based keypad 0x0-0xF
		self._chip8_fontset =
		
		def initialize(self):
				pc = 0x200 # Program counter starts at 0x200
				opcode = 0
				I = 0
				sp = 0
				i = 0
				while i & lt:
			  		80
				i += 1
		
		def emulateCycle(self):
				opcode = memory[pc] & lt
				8 | memory[pc + 1]:
			  0xF000
			  0x000F
		elif opcode & amp == 0x000E:
			  pc = stack[sp]
			  sp -= 1
		else:
		  	self.printf(quot)
				pc = opcode & amp
		    0x0FFF
		    
#STARTED ONLY
