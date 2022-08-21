import hashlib


def create_hash(string):
    hash_ = hashlib.md5(string.encode()).hexdigest()
    return hash_


# word list path
# path = 'realuniq.txt'
path = 'rockyou.txt'
# path = 'test.txt'

# puzzle path
p_path = 'puzzle.txt'

word_list = open(path, encoding="Latin-1")
hash_list = open(p_path, 'r')

w_list = word_list.readlines()
h_list = hash_list.readlines()

print("read done")

answers = []

percentage_tracker = 0

for h in h_list:
    new_hash = str(h)
    new_hash = new_hash[:-1]

    percent_done = (percentage_tracker / len(h_list)) * 100
    print(percent_done, " of hashes checked against ", path, ", ", len(answers), " found")

    for word in w_list:

        next_test = str(word)
        next_test = next_test[:-1]

        compare = create_hash(next_test)

        if new_hash == compare:
            row = [new_hash, next_test]
            answers.append(row)
            print(answers)
            break

    percentage_tracker = percentage_tracker + 1

if len(answers) > 0:
    for row in answers:
        print(row)
else:
    print("no keys found")
