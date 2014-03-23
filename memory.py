from System import *
from System.Collections.Generic import *
from System.Linq import *
from System.Text import *

class Memory(object):
	def __init__(self):
		self._memoryBuffer = Array.CreateInstance(Byte, 4096)

	def get_Length(self):
		return 4096

	Length = property(fget=get_Length)

	def SetValue(self, address, value):
		self._memoryBuffer[address] = value

	def GetValue(self, address):
		return self._memoryBuffer[address]
