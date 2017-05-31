def extract_player_data(file):
    with open(file) as fle:
        data = fle.readline()
        data = data.strip().split(',')
        return data


def sanitise(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


def sanitise_and_sort_list_top_3(list):
    clean_list = [sanitise(x) for x in list]
    sorted_list = sorted(set(clean_list))
    return sorted_list[0:3]

print(extract_player_data('james.txt'))
print(sanitise_and_sort_list(extract_player_data('james.txt')))

