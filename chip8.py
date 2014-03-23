class CPU(object):
    def __init__(self, memory):
    	self._InstructionPointer = 0x200
	self._Register = Array.CreateInstance(Byte, 16)
	self._Stack = Stack[UInt16](16)
	self._InstructionSet = Dictionary[Byte, Func]()
	self._RegisterCommands = Dictionary[Byte, Action]()
	self._memory = memory
	self._InstructionSet[0x0] = SYS
	self._InstructionSet[0x1] = JP
	self._InstructionSet[0x2] = CALL
	self._InstructionSet[0x3] = SE
	self._InstructionSet[0x4] = SNE
	self._InstructionSet[0x5] = SEV
	self._InstructionSet[0x6] = LD
	self._InstructionSet[0x7] = ADD
	self._InstructionSet[0x8] = REG
	self._InstructionSet[0x9] = SNEV
	self._InstructionSet[0xA] = LDI
	self._InstructionSet[0xB] = JPV
	self._RegisterCommands[0x0] = 
	self._RegisterCommands[0x1] = 
	self._RegisterCommands[0x2] = 
	self._RegisterCommands[0x3] = 
	self._RegisterCommands[0x4] = 
	self._RegisterCommands[0x5] = 
	self._RegisterCommands[0x6] = 
	self._RegisterCommands[0x7] = 
	self._RegisterCommands[0xe] = 

    def Run(self):
	quit = False
	while not quit:
	    instruction = self.GetNextInstruction()
	    quit = self.ProcessInstruction(instruction)

    def ProcessInstruction(self, instruction):
	opcode = self.GetOpCode(instruction)
	func = self._InstructionSet[opcode]
	return self.func(instruction)

    def SYS(self, instruction):
        if self.GetAddress(instruction) == 0xee:
            return self.RET()
	return False

    def LDI(self, instruction):
	self._AddressRegister = self.GetAddress(instruction)
	return False

    def LD(self, instruction):
        x = self.GetX(instruction)
        self._Register[x] = self.GetValue(instruction)
        return False

    def SEV(self, instruction):
        x = self.GetX(instruction)
        regValueX = self._Register[x]
        y = self.GetY(instruction)
        regValueY = self._Register[y]
        if regValueX == regValueY:
	    self._InstructionPointer += 2
        return False

    def SNE(self, instruction):
        x = self.GetX(instruction)
        regValue = self._Register[x]
        opValue = self.GetValue(instruction)
		
    def CALL(self, instruction):
        self._Stack.Push(self._InstructionPointer)
        self._InstructionPointer = self.GetAddress(instruction)
        return False

    def RET(self):
        if self._Stack.Count == 0:
            return True
	    self._InstructionPointer = self._Stack.Pop()
	    return False

    def JP(self, instruction):
        self._InstructionPointer = self.GetAddress(instruction)
        return False

    def ADD(self, instruction):
        register = self.GetX(instruction)
        value = self.GetValue(instruction)
        self._Register[register] += value
        return False

    def REG(self, instruction):
        subcommand = self.GetSubCommand(instruction)
        command = self._RegisterCommands[subcommand]
        regX = self.GetX(instruction)
        regY = self.GetY(instruction)
        self.command(regX, regY)
        return False

    def SNEV(self, instruction):
        regX = self.GetX(instruction)
        regY = self.GetY(instruction)
        regValueX = self._Register[regX]
        regValueY = self._Register[regY]
        if regValueX != regValueY:
            self._InstructionPointer += 2
	    return True

    def JPV(self, instruction):
        offset = self._Register[0]
        address = self.GetAddress(instruction)
        a = offset + address

    def GetY(self, instruction):
        return (instruction >> 4 & 0x0f)

    def GetX(self, instruction):
        return (instruction >> 8 & 0x0f)

    def GetValue(self, instruction):
        return (instruction & 0xff)

    def GetSubCommand(self, instruction):
        return (instruction & 0x0f)

    def GetOpCode(self, instruction):
        return (instruction >> 12)

    def GetAddress(self, instruction):
        return (instruction & 0x7ff)

    def GetNextInstruction(self):
        operation_hi = self._memory.GetValue(self._InstructionPointer += 1)
        operation_lo = self._memory.GetValue(self._InstructionPointer += 1)
        return (((operation_hi << 8)) | operation_lo)
