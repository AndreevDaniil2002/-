import os
import sys
import shutil
import settings as sett


path = "D:\ВУЗ\Практикум по программированию\File Manager"
sett.start()


def helpp():
    print('''Показать все команды [команда] - help
    Узнать текущее местонахождение [команда] - pwd
    Создание папки [команда, имя] - makeDir
    Удаление папки по имени [команда, имя] - delDir
    Создание пустого текстового файла [команда, имя] - makeFile
    Записать текст в файл [команда, имя] - addFile
    Посмотреть содержимое файла [команда, имя] - seeFile
    Удаление файла по имени [команда, имя] - delFile
    Скопировать файл [команда, имя_файла, путь] - copyFile
    Переместить файл [команда, имя_файла, путь] - moveFile
    Переимновать файл [команда, имя1, имя2] - renameFile
    Спустить в директории на один уровень ниже [команда, имя] - chpwd
    Подняться в директории на один уровень выше [команда] - chpwdUp
    Выход из программы [команда] - exit''')


def pwd():
    print(os.getcwd())


def makeDir(dirName):
    try:
        os.mkdir(dirName)
    except FileExistsError:
        print('file already exists')


def delDir(dirName):
    try:
        os.rmdir(dirName)
    except FileNotFoundError:
        print('directory does not exist')


def makeFile(fileName):
    file = open(fileName, "w+")
    file.close()


def addFile(filename, w):
    try:
        f = open(filename, "a")
        f.write(w)
        f.close()
    except FileExistsError:
        print('file does not exist')


def seeFile(fileName):
    try:
        file = open(fileName, "r")
        print(file.read())
        file.close()
    except FileExistsError:
        print('file does not exists')


def delFile(fileName):
    try:
        os.remove(fileName)
    except FileExistsError:
        print('file does not exist')


def copyFile(fileName, newFilename):
    try:
        shutil.copy(fileName, newFilename)
    except FileExistsError:
        print('file does not exist')


def moveFile(fileName, newFilename):
    try:
        shutil.move(fileName, newFilename)
    except FileExistsError:
        print('file does not exist')


def renameFile(fileName, newFilename):
    try:
        os.rename(fileName, newFilename)
    except FileExistsError:
        print('file does not exist')


def chpwd(dirName):
    try:
        OS = sys.platform
        if OS == 'darwin':
            a = os.getcwd()
            os.chdir(a + '/' + dirName)
            print(os.getcwd())

        elif OS == 'cygwin' or OS == 'win32':
            a = os.getcwd()
            os.chdir(a + '\\' + dirName)
            print(os.getcwd())
    except FileNotFoundError:
        print('directory do not exist')


def chpwdUp():
    try:
        z = os.getcwd()
        if len(os.path.split(os.getcwd())[0]) < len(path):
            print('Выход за пределы рабочей папки')
        elif len(os.path.split(os.getcwd())[0]) <= len(z) or len(os.path.split(os.getcwd())[0]) + 1 <= len(z):
            OS = sys.platform
            # print(OS)
            if OS == 'darwin':
                a = os.getcwd()
                b = a.split('/')
                del b[-1]
                a = '/'.join([str(item) for item in b])
                os.chdir(a)
                print(os.getcwd())

            elif OS == 'cygwin' or OS == 'win32':
                a = os.getcwd()
                b = a.split('\\')
                del b[-1]
                a = '\\'.join([str(item) for item in b])
                os.chdir(a)
                print(os.getcwd())
        else:
            print("cant go further")
            print(os.getcwd())
    except:
        print('cant go up')



while True:
    try:
        command = input('Введите команду (help - список всех команд): ')
        command = command.split(' ')
        if command[0] == 'exit':
            sys.exit()
        elif command[0] == 'help':
            helpp()
        elif command[0] == 'makeDir':
            makeDir(command[1])
        elif command[0] == 'delDir':
            delDir(command[1])
        elif command[0] == 'makeFile':
            makeFile(command[1])
        elif command[0] == 'seeFile':
            seeFile(command[1])
        elif command[0] == 'addFile':
            contentWrap = input("Текст: ")
            addFile(command[1], contentWrap)
        elif command[0] == 'pwd':
            pwd()
        elif command[0] == 'delFile':
            delFile(command[1])
        elif command[0] == 'copyFile':
            copyFile(command[1], command[2])
        elif command[0] == 'moveFile':
            moveFile(command[1], command[2])
        elif command[0] == 'renameFile':
            renameFile(command[1], command[2])
        elif command[0] == 'chpwd':
            chpwd(command[1])
        elif command[0] == 'chpwdUp':
            chpwdUp()
        else:
            print('команды не существует')
    except:
        print('Команда введена неправильно')
