import os
import sys

#Создание директорие
def create_file(file):
	os.mkdir(file)
	return

#Удаление директории
def remove_dir(file):
	os.rmdir(file)
	return

#Открытие файла для читания
def look_file(file):
	os.listdir(file)
	print(os.listdir)
