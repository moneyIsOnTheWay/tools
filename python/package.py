#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('gbk')

# 打包类型
packageType = sys.argv[1]
print '类型' + packageType
file = 'xx.java'
# 多用户标志
multi = 'XXXX xxxx'
# 分割符标志
flag = ['{',';','}']


# 读文件
def getICheckInService(file):
	with open(file, 'r') as f:
		return f.read().decode('gbk')

# 写文件
def write(file,string):
	with open(file, 'w') as f:
		f.write(string)
	print 'write file done!'

# 多用户判断
def isMulti(string):
	return string.find(multi) != -1

# 单用户文件
def getSingle(string):
	content = string.split(flag[0])
	single = content[0] + flag[0]
	method = content[1].split(flag[1])
	temp = []
	for i in range(len(method)):
		if not(isMulti(method[i])):
			temp.append(method[i] + flag[1])
	for j in range(len(temp)):
		single += temp[j]
	return single[:-1]

# 多用户文件
def getMulti(string):
	content = string.split(flag[0])
	multi = content[0] + flag[0]
	method = content[1].split(flag[1])
	temp = []

	for i in range(len(method)):
		if isMulti(method[i]):
			temp.append(method[i] + flag[1])
	for j in range(len(temp)):
		multi += temp[j]
	return multi + '\n' + flag[2]

def start(string):
	if string in ['single','auto','dev']:
		write(file,getSingle(getICheckInService(file)))
	elif string == 'multi':
		write(file,getMulti(getICheckInService(file)))
	else:
		print ' 类型不存在'
		sys.exit(-1)

start(packageType)