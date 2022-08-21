
# answers
# Who designed both RC5 and MD5?
# What organization designed SHA-1?
# Who co-developed both AES and SHA-3?


import hashlib

# puzzle path
p_path = 'puzzle/puzzle.txt'

hash_list = open(p_path, 'r')

h_list = hash_list.readlines()

hash_list.close()

# show that the list of hashes has been put in array
print("read done")


def create_hash(hash_type, string):
    if hash_type == 'md5':
        hash_ = hashlib.md5(string.encode()).hexdigest()
        return hash_
    elif hash_type == 'sha1':
        hash_ = hashlib.sha1(string.encode()).hexdigest()
        return hash_
    else:
        hash_ = hashlib.sha3_256(string.encode()).hexdigest()
        return hash_


def decode(hash_type):
    global h_list
    current_str = ""
    percentage_tracker = 0

    for h in h_list:
        new_hash = str(h)
        new_hash = new_hash[:-1]

        # percent_done = (percentage_tracker / len(h_list)) * 100
        # print(round(percent_done, 2), "%")  # show percent complete on each decode

        for i in range(200):

            current_str = current_str + chr(i)

            compare = create_hash(hash_type, current_str)

            if new_hash == compare:
                # print(current_str)
                break

            current_str = current_str[:-1]

        percentage_tracker = percentage_tracker + 1

    new_str = ""
    h_list.clear()

    for i in current_str:
        new_str = new_str + i
        if i == "\n":
            h_list.append(new_str)
            new_str = ""

    h_list.append(new_str)


answers = []

decode('md5')
answers.append(h_list[0])

decode('sha1')
answers.append(h_list[0])

decode('sha3')
answers.append(h_list[0])

print(answers)
