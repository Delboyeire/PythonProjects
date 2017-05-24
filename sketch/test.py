def array_left_rotation(a, n, k):
    #n number of elements
    #k number of lefts
    #a list of ints
    answer = []

    for element in a:
        answer.append(element)
    return answer

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
