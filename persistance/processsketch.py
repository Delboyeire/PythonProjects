man = []
other = []
data = open('sketch.txt')
try:
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(":", 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print("An error occurred with the file, does the file exist?")
try:
    man_out = open('man_data.txt', 'w')
    other_out = open('other_data.txt', 'w')
    print(man, file=man_out)
    print(other, file=other_out)
except IOError:
    print('an error occured writing files')
finally:
    man_out.close()
    other_out.close()
