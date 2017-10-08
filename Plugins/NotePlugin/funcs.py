import json
import os
from datetime import datetime

def main(usrCommand):
	command = usrCommand.split(" ")
	try:
		return getNote(command)
	except Exception:
		return "Master, type 'Darya help note'"

def create(data): #Esta ya quedo
	if(len(data) > 0):
		#Conseguir el y updated_at
		hour = datetime.now()
		updated_at = (str(hour.day) + "/" + str(hour.month) + "/" + str(hour.year) + " " + str(hour.hour).zfill(2) + ":" + str(hour.minute).zfill(2) + ":" + str(hour.second).zfill(2))
		#Conseguir la base de datos
		db = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteDB.txt", "r")
		lines = db.readlines()
		db.close()
		registros = []
		for line in lines:
			registro = line.split("\t")
			registros.append(registro)
		#Conseguir las clases
		file = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteClasses.txt", "r")
		lineas = file.readlines()
		file.close()
		clases = []
		for linea in lineas:
			element = linea.split("\t")
			clases.append(element[1].strip("\n"))
		clases.pop(0)
		#Si el usuario ingresa una clase...
		for i in reversed(data):
			if("--" in i):
				indice = data.index(i)
				break
		if "indice" in locals():
			clase = ((" ".join(data[indice:])).lstrip("--")).capitalize()
			note = " ".join(data[:indice])
			if (not(clase in clases)):
				return "The class doesn't exist"
		else:
			clase = "Default"
			note = " ".join(data)			
		#Aqui ya tengo la clase, la nota, el created_at y el updated_at / Faltan los ID's
		new_note = ["0", clase, updated_at, note+"\n"]
		#registros[-1][-1] += "\n"
		registros.append(new_note)
		for i in range(len(registros) - 1):
			registros[i+1][0] = str(i+1)
		new_db = ""
		for j in registros:
			new_db += str("\t".join(j))
		#Modificamos la base de datos
		outDB = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteDB.txt", "w")
		outDB.write(new_db)
		outDB.close()
		#Imprimimos
		response = "\n"
		for i in registros:
			if (registros.index(i) == 0):
				response += ("{0:3} |  {1:20} |  {2:20} |  {3}\n".format(i[0].upper(), i[1].upper(), i[2].upper(), i[3].upper()))
			else:
				response += ("{0:3} |  {1:20} |  {2:20} |  {3}\n".format(i[0], i[1], i[2], i[3]))
		return response
	else:
		return "I need at least the content of the note"

def list(data): #Esta ya quedo
	#Conseguir la base de datos
	response = "\n"
	db = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteDB.txt", "r")
	lines = db.readlines()
	db.close()
	registros = []
	for line in lines:
		registro = line.split("\t")
		registros.append(registro)
	#Conseguir las clases
	file = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteClasses.txt", "r")
	lineas = file.readlines()
	file.close()
	clases = []
	for linea in lineas:
		element = linea.split("\t")
		clases.append(element[1].strip("\n"))
	clases.pop(0)
	if(len(data) >= 1):
		clase_buscada = " ".join(data[:]).capitalize()
		if not(clase_buscada in clases):
			return "The class you're looking for doesn't exist"
		for i in registros:
			if (registros.index(i) == 0):
				response += ("{0:3} |  {1:20} |  {2:20} |  {3}\n".format(i[0].upper(), i[1].upper(), i[2].upper(), i[3].upper()))
			else:
				if(i[1] == clase_buscada):
					response += ("{0:3} |  {1:20} |  {2:20} |  {3}\n".format(i[0], i[1], i[2], i[3]))
		return response
	else:
		for i in registros:
			if (registros.index(i) == 0):
				response += ("{0:3} |  {1:20} |  {2:20} |  {3}\n".format(i[0].upper(), i[1].upper(), i[2].upper(), i[3].upper()))
			else:
				response += ("{0:3} |  {1:20} |  {2:20} |  {3}\n".format(i[0], i[1], i[2], i[3]))
		return response

def edit(data): #Esta ya quedo
	if(len(data) > 1 and (data[0].isdigit())):
		#Conseguir el y updated_at
		hour = datetime.now()
		updated_at = (str(hour.day) + "/" + str(hour.month) + "/" + str(hour.year) + " " + str(hour.hour).zfill(2) + ":" + str(hour.minute).zfill(2) + ":" + str(hour.second).zfill(2))
		#Conseguir la base de datos
		db = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteDB.txt", "r")
		lines = db.readlines()
		db.close()
		registros = []
		for line in lines:
			registro = line.split("\t")
			registros.append(registro)
		#Conseguir las clases
		file = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteClasses.txt", "r")
		lineas = file.readlines()
		file.close()
		clases = []
		for linea in lineas:
			element = linea.split("\t")
			clases.append(element[1].strip("\n"))
		clases.pop(0)
		#Si el usuario ingresa una clase...
		for i in reversed(data):
			if("--" in i):
				indice = data.index(i)
				break
		if "indice" in locals():
			clase = ((" ".join(data[indice:])).lstrip("--")).capitalize()
			note = " ".join(data[1:indice])
			if (not(clase in clases)):
				return "The class doesn't exist"
		else:
			clase = registros[int(data[0])][1]
			note = " ".join(data[1:])			
		#Cambiamos los valores
		registros[int(data[0])][1] = clase
		registros[int(data[0])][2] = updated_at
		registros[int(data[0])][3] = note + "\n"
		#registros[-1][-1] += "\n"
		#if(int(data[0]) != (len(registros) - 1)):
		for i in range(len(registros) - 1):
			registros[i+1][0] = str(i+1)
		new_db = ""
		for j in registros:
			new_db += str("\t".join(j))
		#Modificamos la base de datos
		outDB = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteDB.txt", "w")
		outDB.write(new_db)
		outDB.close()
		#Imprimimos
		response = "\n"
		for i in registros:
			if (registros.index(i) == 0):
				response += ("{0:3} |  {1:20} |  {2:20} |  {3}\n".format(i[0].upper(), i[1].upper(), i[2].upper(), i[3].upper()))
			else:
				response += ("{0:3} |  {1:20} |  {2:20} |  {3}\n".format(i[0], i[1], i[2], i[3]))
		return response
	else:
		return "I need at least 2 parameters, the ID of the note and its content"

def delete(data): #Esta ya quedo
	if((len(data) == 2) and (data[0].isdigit()) and (data[1] == "sure")):
		#Conseguir la base de datos
		response = "\n"
		db = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteDB.txt", "r")
		lines = db.readlines()
		db.close()
		registros = []
		for line in lines:
			registro = line.split("\t")
			registros.append(registro)
		if(int(data[0]) <= (len(registros) - 1) and (int(data[0]) > 0)):
			registros.pop(int(data[0]))
			for i in range(len(registros) - 1):
				registros[i+1][0] = str(i+1)
			registros[-1][-1].replace("\n", "")
			new_db = ""
			for j in registros:
				new_db += str("\t".join(j))
			#Modificamos la base de datos
			outDB = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteDB.txt", "w")
			outDB.write(new_db)
			outDB.close()
			#Imprimimos
			for i in registros:
				if (registros.index(i) == 0):
					response += ("{0:3} |  {1:20} |  {2:20} |  {3}\n".format(i[0].upper(), i[1].upper(), i[2].upper(), i[3].upper()))
				else:
					response += ("{0:3} |  {1:20} |  {2:20} |  {3}\n".format(i[0], i[1], i[2], i[3]))
			return response
		else:
			return "The ID doesn't exist"
	else:
		return "I need 2 parameters, the ID of the note and the word 'sure'"

def classCreate(data): #esta ya quedo
	if(len(data) > 0):
		response = ""
		file = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteClasses.txt", "r")
		lines = file.readlines()
		file.close()
		elements = []
		for line in lines:
			element = line.split("\t")
			elements.append(element)
		class_name = " ".join(data).capitalize()
		#Verificar si ya existe
		clases_existentes = []
		for k in elements:
			clases_existentes.append(k[1])
		#return clases_existentes
		if((class_name + "\n") in clases_existentes):
			return "This class alreasy exists"
		#Hasta aqui
		else:
			new_class = []
			new_class += ("0", str(class_name) + "\n")
			#elements[-1][1] += "\n"
			elements.append(new_class)
			for i in range(len(elements) - 2):
				elements[i+2][0] = i+1
			for j in elements:
				response += (str(j[0]) + "\t" + str(j[1]))
			outfile = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteClasses.txt", "w")
			outfile.write(response)
			outfile.close()
			return response + "\n"
	else:
		return "I need the name of the class"

def classList(data): #Esta ya quedo
	if(len(data) > 0):
		return "This action doesn't wait parameters"
	else:
		response = ""
		file = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteClasses.txt", "r")
		lines = file.readlines()
		file.close()
		elements = []
		for line in lines:
			element = line.split("\t")
			elements.append(element)
		for i in elements:
			response += (str(i[0]) + "\t" + str(i[1]))
		return response + "\n"
		#return elements

def classEdit(data): #Esta ya quedo
	if((len(data) >= 2) and (data[0].isdigit())):
		if(data[0] != "0"):
			file = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteClasses.txt", "r")
			lines = file.readlines()
			file.close()
			elements = []
			for line in lines:
				element = line.split("\t")
				elements.append(element)
			if(int(data[0]) <= (len(elements) - 2) and (int(data[0]) > 0)):
				new_class = " ".join(data[1:]).capitalize()
				#Verificar si ya existe
				clases_existentes = []
				for k in elements:
					clases_existentes.append(k[1])
				if((new_class + "\n") in clases_existentes):
					return "This class alreasy exists"
				#Hasta aqui
				else:
					#if(int(data[0]) != (len(elements) - 2)):
					old_class = elements[int(data[0]) + 1][1]
					db = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteDB.txt", "r")
					lineas = db.readlines()
					db.close()
					registros = []
					for linea in lineas:
						registro = linea.split("\t")
						registros.append(registro)
					for m in registros:
						if((m[1] + "\n") == old_class):
							m[1] = new_class
					new_db = ""
					for j in registros:
						new_db += str("\t".join(j))
					#Modificamos la base de datos
					outDB = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteDB.txt", "w")
					outDB.write(new_db)
					outDB.close()


					new_class += "\n"
					elements[int(data[0]) + 1][1] = new_class
					response = ""
					for i in elements:
						response += (str(i[0]) + "\t" + str(i[1]))
					outfile = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteClasses.txt", "w")
					outfile.write(response)
					outfile.close()
					return response + "\n"
			else:
				return "The ID doesn't exist"
		else:
			return "You can't edit the default class"
	else:
		return "I need 2 parameters, the ID of the class and its new name"

def classDelete(data): #Esta ya quedo
	if((len(data) == 2) and (data[0].isdigit()) and (data[1] == "sure")):
		if(data[0] != "0"):
			file = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteClasses.txt", "r")
			lines = file.readlines()
			file.close()
			elements = []
			for line in lines:
				element = line.split("\t")
				elements.append(element)
			if(int(data[0]) <= (len(elements) - 2) and (int(data[0]) > 0)):
				response = ""
				old_class = elements[int(data[0]) + 1][1]
				db = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteDB.txt", "r")
				lineas = db.readlines()
				db.close()
				registros = []
				for linea in lineas:
					registro = linea.split("\t")
					registros.append(registro)
				for m in registros:
					if((m[1] + "\n") == old_class):
						m[1] = "Default"
				new_db = ""
				for j in registros:
					new_db += str("\t".join(j))
				#Modificamos la base de datos
				outDB = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteDB.txt", "w")
				outDB.write(new_db)
				outDB.close()

				elements.pop(int(data[0]) + 1)
				for i in range(len(elements) - 2):
					elements[i+2][0] = i+1
				for i in elements:
					response += (str(i[0]) + "\t" + str(i[1]))
				response[-1][-1].rstrip("\n")
				outfile = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/noteClasses.txt", "w")
				outfile.write(response)
				outfile.close()
				return response + "\n"
			else:
				return "The ID doesn't exist"
		else:
			return "You can't delete the default class"
	else:
		return "I need 2 parameters, the ID of the class and the word 'sure'"

def getNote(command):
	if(len(command) == 1):
		response = ""
		file = open("/usr/local/bin/dlib/Plugins/NotePlugin/docs/help.txt", "r")
		for line in file:
			response += (line)
	else:
		action = command[1]
		if (action == "create"):
			response = create(command[2:])
		elif(action == "list"):
			response = list(command[2:])
		elif(action == "edit"):
			response = edit(command[2:])
		elif(action == "delete"):
			response = delete(command[2:])
		elif (action == "class:create"):
			response = classCreate(command[2:])
		elif(action == "class:list"):
			response = classList(command[2:])
		elif(action == "class:edit"):
			response = classEdit(command[2:])
		elif(action == "class:delete"):
			response = classDelete(command[2:])
		else:
			response = "The action you want doesn't exist"
	return response