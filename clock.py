#!/usr/bin/python3

import random
import time
import datetime

class Printer:
	def __init__(self):
		self.initValues()

	def initValues(self):
		self.values = []
		value = [];
# 0
		value.append('  ')
		value.append('  ')
		self.values.append(value)
		value = [];
# 1
		value.append('  ')
		value.append('¯ ')
		self.values.append(value) 
		value = [];
# 2
		value.append('  ')
		value.append('_ ')
		self.values.append(value) 
		value = [];
# 3
		value.append('  ')
		value.append('\ ')
		self.values.append(value) 
		value = [];
# 4
		value.append('  ')
		value.append('/ ')
		self.values.append(value) 
		value = [];
# 5
		value.append('_ ')
		value.append('/ ')
		self.values.append(value)
		value = [];
# 6
		value.append('  ')
		value.append(' |')
		self.values.append(value)
		value = [];
# 7
		value.append('_ ')
		value.append(' |')
		self.values.append(value)
		value = [];
# 8
		value.append('  ')
		value.append('_|')
		self.values.append(value)
		value = [];
# 9
		value.append('_ ')
		value.append('_|')
		self.values.append(value)

	def mirrorVert(self, text):
		newtext = []
		for line in text:
			newline = ""
			for letter in line:
				newletter = letter
				if letter == "\\":
					newletter = "/"
				if letter == "/":
					newletter = "\\"
				newline = newletter + newline
			line = newline
			newtext.append(line)
		return newtext

	def mirrorHorz(self, text):
		newtext = []
		for line in text:
			newline = ""
			for letter in line:
				newletter = letter
				if letter == "\\":
					newletter = "/"
				if letter == "/":
					newletter = "\\"
				if letter == "_":
					newletter = "¯"
				if letter == "¯":
					newletter = "_"
				newline = newline + newletter
			line = newline
			newtext.append(line)
		newtext.reverse()
		return newtext
		
	def generateValue(self, value):
		draw = []
		svalue = str(value)
		svalue = svalue.zfill(4)
		arts = []
		arts.append(self.values[int(svalue[3])])
		arts.append(self.values[int(svalue[2])])
		arts[1] = self.mirrorVert(arts[1])
		arts.append(self.values[int(svalue[1])])
		arts[2] = self.mirrorHorz(arts[2])
		arts.append(self.values[int(svalue[0])])
		arts[3] = self.mirrorHorz(self.mirrorVert(arts[3]))
		draw.append(arts[1][0] + " " + arts[0][0])
		draw.append(arts[1][1] + "|" + arts[0][1])
		draw.append("  |  ")
		draw.append(arts[3][0] + "|" + arts[2][0])
		draw.append(arts[3][1] + " " + arts[2][1])
		return draw

def test():
	c = Printer()

	for i in range(0, 10):
		a = c.values[i]
		print('\n'.join(a))
		print("====")
		print('\n'.join(c.mirrorHorz(a)))
		print("====")
		print('\n'.join(c.mirrorVert(a)))

def test2():
	c = Printer()
	val = random.randrange(0, 10000)
	c.generateValue(val)
	print(val)

class Clock():
	def __init__(self):
		self.printer = Printer()

	def run(self, format_, delay, verbose):
		while True:
			val = datetime.datetime.now().strftime(format_)
			sval = self.printer.generateValue(val)
			print("\n".join(sval))
			if verbose: 
				print(val)
			time.sleep(delay)

	def runClassic(self):
		self.run("%H%M", 60, False)

	def runWithMinutesAndSeconds(self):
		self.run("%M%S", 1, True)

	def runWithSecondsAndMinutes(self):
		self.run("%S%M", 1, True)


c = Clock()
#c.runWithMinutesAndSeconds()
#c.runWithSecondsAndMinutes()
c.runClassic()
