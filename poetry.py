def get_file_lines(filename):
    franka = open(filename)
    rdy = franka.read()
    print(rdy)

    return filename

get_file_lines("poem.txt")

print('\n')

def lines_printed_backwards(filename):
    frankb = open(filename)
    lines = frankb.readlines()
    for line in reversed(lines):
        print(line)

    frankb.close()
    return filename

lines_printed_backwards("poem.txt")

