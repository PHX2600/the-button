import bcrypt
import io
import random as rnd

words = []
with file('/usr/share/dict/words', 'r') as f:
    for word in f.readlines():
        if len(word) == 6:
            words.append(word.strip())

pws = file('passwords.txt', 'w')

num_words = len(words)

def get_word():
    return words[rnd.randint(0, num_words - 1)]

for i in range(20):
    team = get_word()
    password = get_word() + str(rnd.randint(10,99)) + get_word()
    hash = bcrypt.hashpw(password, bcrypt.gensalt())

    pws.write(team + "\t -- " + password + '\n')
    print "INSERT into teams (name, score, hash, last_click, spamming) VALUES ('%s', 0, '%s', 10000, 0); -- %s " % (team, hash, password)

pws.close()
