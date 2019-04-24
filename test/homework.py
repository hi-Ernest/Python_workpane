import os

from collections import Counter
from random import randint, choice
from string import letters

filename = 'text.txt'
dirname = os.getcwd()
fname = os.path.join(dirname, filename)

lines = []

for i in range(20):
    line = []
    for j in range(randint(1,20)):
        line.append(''.join([choice(letters) for c in range(randint(1, 10))]))
        lines.append(' '.join(line))
    with open(fname, 'w') as f:
        f.write('\n'.join(lines))
    # '''
    with open(fname) as f:
        s = f.read()

    counter = Counter(s.replace('\n', ' ').split(' '))


def geshi(a, b, c):
    return alignment(str(a)) + alignment(str(b), 18) + alignment(str(c)) + '\n'


def alignment(str1, space=8, align='left'):
    length = len(str1.encode('gbk'))
    space = space - length if space >= length else 0
    if align in ['left', 'l', 'L', 'Left', 'LEFT']:
        return str1 + ' ' * space
    elif align in ['right', 'r', 'R', 'Right', 'RIGHT']:
        return ' ' * space + str1
    elif align in ['center', 'c', 'C', 'Center', 'CENTER', 'centre']:
        return ' ' * (space // 2) + str1 + ' ' * (space - space // 2)
    return 'Unknow align format'


title = geshi('xunhao', 'ci', 'pinglv')
results = []
for i, (w, c) in enumerate(counter.most_common(), 1):
    results.append(geshi(i, w, c))

writefile = 'text_out.txt'
wpath = os.path.join(dirname, writefile)
with open(wpath, 'w') as f:
    f.write(''.join([title] + results))