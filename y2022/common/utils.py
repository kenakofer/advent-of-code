import os

INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output.txt"

filename = "filename not set"
input_file = "input_file not set"
output_file = "output_file not set"

def init_file_paths(name):
    global filename, input_file, output_file
    filename = name
    input_file = get_input_path(filename)
    output_file = get_output_path(filename)

def open_input():
    return open(input_file)

def get_input_path(file_path):
    dir_path = os.path.dirname(os.path.realpath(file_path))
    for i in range(3):
        path = os.path.join(dir_path, INPUT_FILENAME)
        if os.path.exists(path):
            return path

        else:
            dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
    raise Exception(f"Couldn't find {INPUT_FILENAME}")

def get_output_path(file_path):
    dir_path = os.path.dirname(os.path.realpath(file_path))
    return os.path.join(dir_path, OUTPUT_FILENAME)

def output(object):
    print(object)
    with open(output_file, "a") as out:
        out.write(str(object) + "\n")
