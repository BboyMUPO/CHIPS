class ChipEmu(object):
	def __init__(self):
		self._V = Array.CreateInstance(Byte, 16) # general purpose registers & VF carry flag # adress register # program counter # stack pointer
		self._stack = Array.CreateInstance(UInt16, 16)
		self._memory = Array.CreateInstance(Byte, 4096)
		#		void drawSprite(byte X, byte Y, byte N);
		self._hp48_flags = Array.CreateInstance(Byte, 8)
