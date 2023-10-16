import os
import random
from pathlib import Path


def get_user_directory():
    user_home = str(Path.home())
    return user_home

def config_directory(user_home):
    '''Create a configuration directory if non exists.'''
    directory_path = user_home + "/.iid"
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    return directory_path

def read_file():
    '''Read the a file filled with quotes into a list.'''
    file_path = "quotes.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    return lines

def create_file(lines, directory_path):
    '''Write a list of quotes into a file.'''
    file_path = directory_path + "/quotes.txt"
    with open(file_path, 'w') as file:
        for item in lines:
            file.write(item + "\n")
    return True

def get_quote(directory_path):
    '''Get a quote and display it.'''
    file_path = directory_path + "/quotes.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    fortune = random.choice(lines)
    return fortune

def main():
    '''Main Function.'''
    directory_path = config_directory(get_user_directory())
    lines = read_file()
    create_file(lines, directory_path)
    quote = get_quote(directory_path)
    print(quote)
    return True


if __name__ == "__main__":
   main()