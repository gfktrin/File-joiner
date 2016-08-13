#!/usr/bin/env python
# -*- coding: utf-8 -*-
import binascii
import os
#It won't work with more than two files united
#exe files don't work with image files, but can be joined with mp3 files(I don't know why, yet)
filename = ''
hex_data = ''
type = ''

def hex_to_file(novo_hex):
	global type, filename
	char_data = binascii.a2b_hex(novo_hex)#transforms hexadecimal code into characters
	file = open(filename,'wb')
	file.write(char_data)
	file.close()
	os.rename(filename, filename[0:len(filename)-4]+'.'+type)#changes extension of file

def to_jpg():
	global hex_data, filename
	hex_jpg = hex_data[hex_data.find('ffd8ffe0'):hex_data.find('6f6365616e6f')+12] #ffd8ffe0 marks the beginning of any jpg file, 6f6365616e6f = oceano and marks the end
	hex_restante = hex_data.replace(hex_jpg, '')#creates a new variable without the data stored in hex_jpg variable
	novo_hex = hex_jpg + hex_restante #joins the two variables into a new one
	hex_to_file(novo_hex)
	
def to_mp3():
	global hex_data, filename
	hex_mp3 = hex_data[hex_data.find('49443304'):hex_data.find('6d61726d6f7461')+14] #6d61726d6f7461 = marmota
	hex_restante = hex_data.replace(hex_mp3, '')
	novo_hex = hex_mp3 + hex_restante
	hex_to_file(novo_hex)
	
def to_exe():
	global hex_data, filename
	hex_exe = hex_data[hex_data.find('4d5a900003'):hex_data.find('6c656d757265')+12] #6c656d757265 = lemure
	hex_restante = hex_data.replace(hex_exe, '')
	novo_hex = hex_exe + hex_restante
	hex_to_file(novo_hex)

def to_png():
	global hex_data, filename
	hex_png = hex_data[hex_data.find('89504e47'):hex_data.find('6d616361636f')+12] #6d616361636f = macaco
	hex_restante = hex_data.replace(hex_png, '')
	novo_hex = hex_png + hex_restante
	hex_to_file(novo_hex)

def to_rar():
	global hex_data, filename
	hex_rar = hex_data[hex_data.find('526172211a07'):hex_data.find('6c6f6e747261')+12] #6c6f6e747261 = lontra
	hex_restante = hex_data.replace(hex_rar, '')
	novo_hex = hex_rar + hex_restante
	hex_to_file(novo_hex)

def to_gif():
	global hex_data, filename
	hex_gif = hex_data[hex_data.find('474946383961'):hex_data.find('63616d656c6f')+18] #63616d656c6f = camelo
	hex_restante = hex_data.replace(hex_gif, '')
	novo_hex = hex_gif + hex_restante
	hex_to_file(novo_hex)
	
def type():#checks the new extension for the file
	global filename, type
	check = filename[len(filename)-3:len(filename)]
	type = raw_input("Insert file's new extension:")
	if (type == 'jpg') and (type != check):
		to_jpg()
	elif (type == 'mp3') and (type != check):
		to_mp3()
	elif (type == 'exe') and (type != check):
		to_exe()
	elif (type == 'png') and (type != check):
		to_png()
	elif (type == 'rar') and (type != check):
		to_rar()
	elif (type == 'gif') and (type != check):
		to_gif()
	else:
		print("Extension not supported")
		
def change_extension():
	global filename, hex_data
	filename = raw_input("Insert file's name or path:")
	file =  open(filename,'rb')
	data = file.read()
	file.close()
	hex_data = binascii.b2a_hex(data)
	type()

def change_data(data, archive):#Inserts a word in the end of any file code, that is necessary for searching the code after the files are joined
	if archive[len(archive)-3:len(archive)] == 'jpg':
		new_data = data + "oceano"
	elif archive[len(archive)-3:len(archive)] == 'mp3':
		new_data = data + "marmota"
	elif archive[len(archive)-3:len(archive)] == 'exe':
		new_data = data + "lemure"
	elif archive[len(archive)-3:len(archive)] == 'png':
		new_data = data + "macaco"
	elif archive[len(archive)-3:len(archive)] == 'rar':
		new_data = data + "lontra"
	elif archive[len(archive)-3:len(archive)] == 'gif':
		new_data = data + "camelo"
	else:
		print("Extension not supported")
	return new_data
	
def join_files():#joins files
	archive1 = raw_input("Insert first file's name or path:")
	file1 = open(archive1,'rb')
	data1 = file1.read()
	file1.close()
	new_data1 = change_data(data1, archive1)
	archive2 = raw_input("Insert second file's name or path:")
	file2 = open(archive2,'rb')
	data2 = file2.read()
	file2.close()
	new_data2 = change_data(data2, archive2)
	extension = archive1[len(archive1)-4:len(archive1)]
	new_file = open("newfile" + extension,'wb')
	new_file.write(new_data1)
	new_file.write(new_data2)
	new_file.close()
	print("File created")
	
def initial_screen():
	print("You want to join files or change the extension?")
	print("1 - Join files")
	print("2 - Change extension")
	print("3 - Exit")
	choice = raw_input("")
	if choice == '1':
		join_files()
	elif choice == '2':
		change_extension()
	elif choice == '3':
		quit()
	else:
		print("Invalid choice")
	
initial_screen()