import json
import os
import sys
import shutil
import copy
import re



def genCode(splitP,rawLine):
	en = ''
	di = ''
	total = ''

	sp =''

	for c in rawLine:
		if c == " " or c == '\t':
			print c
			sp += c
		else:
			break
			pass

		pass

	global count

	for index,wo in enumerate(splitP):
		curNameDict = nameDict
		if wo == "in":
			en = splitP[index-1]
			count = count + 1
			# if en in curNameDict.keys:
			# 	count = curNameDict[en] + 1
			# else:
			# 	curNameDict[en] = count
			# 	pass
			enn = en + "_Enum" + str(count)
			di = "(" + splitP[index+1] + ")" + '.GetEnumerator();\n'
			total = sp + "var "+ enn + " = " + di + sp + "while(" + enn + ".MoveNext())\n" + sp + "{\n" + sp + "var " + en + " = " + enn +".Current;\n" 
			return total
			pass
		
		pass

	pass


count = 0 
def replaceForeach(filename):
	print "file name is " + filename
	lines = open(filename).readlines()
	for index,curLine in enumerate(lines):
		match = re.search(r'\bforeach\b.*(.*).*{',curLine)
		if match :
			# p = re.compile()
			p = re.split(r'[;,\(\){\s]\s*',curLine)
			lines[index] = genCode(p,curLine)

			pass
		pass
	pass

	file_obj = open(filename,'w')
	
	for curLine in lines:
		file_obj.write(curLine)
		print curLine
		pass
	file_obj.close()

nameDict = {'1':2}
def main():
	yourpath = ""

	
	# print os.path.abspath(os.path.join(yourpath, os.pardir))
	parentPath = os.getcwd()# os.path.abspath(os.path.join(yourpath, os.pardir))
	# print "cur " + os.getcwd()
	# fileNames = ['skeleton','dddd']


	for root, dirs, files in os.walk(parentPath):
		for f in files:
			if f.lower().endswith('.cs') :
				filename = os.path.join(root, f)
				# print filename
				try:
					replaceForeach(filename)
				except Exception,e:
					print e
					print filename + ' error'
					continue

if __name__ == '__main__':
  	main()