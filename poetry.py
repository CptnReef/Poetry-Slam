import random

def get_file_lines(filename):
    franka = open(filename)
    rdy = franka.read()
    print(rdy)
    franka.close
    return filename

def lines_printed_backwards(lines_list):
    frankb = open(lines_list)
    lines = frankb.readlines()
    for line in reversed(lines):
        print(line)

    frankb.close()
    return lines_list

def lines_printed_random(lines_list):
    beef = open(lines_list)
    lines = beef.readlines()
    linelen = 21
    for line in range(linelen):
        line
        print(lines[random.randint(1,len(lines)-1)])

    beef.close()
    return lines_list

def lines_printed_custom(lines_list):
    custom = open(lines_list)
    line = custom.readlines()
    for i in range(len(line)):
        print(line[-i])
    custom.close
    return lines_list

