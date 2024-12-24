import os

def create_dir(path_name):
    if not os.path.exists(path_name):
        os.makedirs(path_name)

def create_new_file(file_path):
    #In this case you pass the 
    #file name and extension as part of the filepath
    #file_path = "folder/test.txt"
    f = open(file_path,'w')
    f.write("")
    f.close()

def write_to_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data + '\n')

def clear_file(file_path):
    f = open(file_path,'w')
    f.close()

def file_exists(file_path):
    return os.path.isfile(file_path)

def read_file(file_path):
    with open(file_path,'rt') as file:
        for line in file:
            print(line)