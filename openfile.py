# encoding: utf-8
import os

def open_file(filename):

    if(os.path.isfile(filename + ".txt")):
        return open(filename + ".txt", 'w', encoding = 'UTF-8' )
    else:
        return open(filename + ".txt", 'w+', encoding = 'UTF-8')

def read_file(filename):

    if(os.path.isfile(filename + ".txt")):
        return open(filename + ".txt", 'r', encoding = 'UTF-8' )
    else:
        return open(filename + ".txt", 'w+', encoding = 'UTF-8')

def readp_file(filename):

    if(os.path.isfile(filename + ".txt")):
        return open(filename + ".txt", 'r+', encoding = 'UTF-8' )
    else:
        return open(filename + ".txt", 'w+', encoding = 'UTF-8')

def dirs_check_dir(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)

def dirs_clear_file(dir, filename):
    dirs_check_dir(dir)

    dir_file = dir + filename
    if (os.path.isfile(dir_file + ".txt")):
        return open(dir_file + ".txt", 'w+', encoding='UTF-8')
    else:
        return open(dir_file + ".txt", 'w+', encoding='UTF-8')

def dirs_open_file(dir, filename):
    dirs_check_dir(dir)

    dir_file = dir + filename
    if (os.path.isfile(dir_file + ".txt")):
        return open(dir_file + ".txt", 'a', encoding='UTF-8')
    else:
        return open(dir_file + ".txt", 'w+', encoding='UTF-8')

def dirs_read_file(dir, filename):
    dirs_check_dir(dir)

    dir_file = dir + filename
    if (os.path.isfile(dir_file + ".txt")):
        return open(dir_file + ".txt", 'r', encoding='UTF-8')
    else:
        return open(dir_file + ".txt", 'w+', encoding='UTF-8')


def dirs_readp_file(dir, filename):
    dirs_check_dir(dir)

    dir_file = dir + filename
    if (os.path.isfile(dir_file + ".txt")):
        return open(dir_file + ".txt", 'r+', encoding='UTF-8')
    else:
        return open(dir_file + ".txt", 'w+', encoding='UTF-8')

def dirs_clear_file_html(dir, filename):
    dirs_check_dir(dir)

    dir_file = dir + filename
    if (os.path.isfile(dir_file + ".html")):
        print(dir_file + ".html is not exist")
        return open(dir_file + ".html", 'w+', encoding='UTF-8')
    else:
        return open(dir_file + ".html", 'w+', encoding='UTF-8')

def close_file():
    return close_file()