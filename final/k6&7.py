
# answer 06
# 1071
# answer 07
# 7048

triangle = []

max_number = []

# f_path = 'triangles/triangle_L.txt'
f_path = 'triangles/triangle_S.txt'


def line_count():
    f = open(f_path, 'r')
    lines = len(f.readlines())
    f.close()
    return lines


def organize(str):
    num = ''
    row = []

    counter = 1
    for i in str:
        if i != ' ':
            num = num + i

        if i == ' ' or counter == len(str):
            row.append(num)
            num = ''
        counter = counter + 1

    triangle.append(row)


def read_file():
    lines = line_count()

    f = open(f_path, 'r')

    for i in range(lines):
        organize(f.readline())


def calc_max():
    max = 0
    for i in max_number:
        max = max + int(i)

    return max


def find_max():
    index = 0

    for i in triangle:

        if len(i) == 1:
            max_number.append(i[0])
            continue

        if index == 0:
            middle = int(i[0])
            right = int(i[1])
            if middle > right:
                max_number.append(middle)
                index = 0
            else:
                max_number.append(right)
                index = 1
        else:
            left = int(i[index - 1])
            middle = int(i[index])
            right = int(i[index + 1])

            if left > middle and left > right:
                max_number.append(left)
                index = index - 1
            elif middle > left and middle > right:
                max_number.append(middle)
                index = index
            elif right > left and right > middle:
                max_number.append(right)
                index = index + 1


if __name__ == '__main__':
    read_file()
    find_max()
    print(calc_max())
