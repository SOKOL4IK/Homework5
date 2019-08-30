import os

from easy4 import create_file, remove_dir, look_file

choice = input('Выберите пункт:\n'
               '1. Просмотреть содержимое текущей папки\n'
               '2. Удалить папку\n'
               '3. Создать папку\n'
               'Ваш выбор: ')

if choice == "1":
	look_file(input("Введите папку: "))
elif choice == "2":
	remove_dir("Введите папку: ")
elif choice == "3":
	create_file("Введите папку: ")
else:
	print("Не правильный ответ!")			