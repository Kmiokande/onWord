import os
from sys import argv, exit
from getopt import getopt
from itertools import product


R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white
version = '1.0.0'


def banner():
    os.system('clear')
    text = r'''
         \ \        / /          | |
  ___  _ _\ \  /\  / /__  _ __ __| |
 / _ \| '_ \ \/  \/ / _ \| '__/ _` |
| (_) | | | \  /\  / (_) | | | (_| |
 \___/|_| |_|\/  \/ \___/|_|  \__,_|'''

    print(G + text + W + '\n')
    print(G + '[>]' + C + ' Created By : ' + W + 'Kmiokande')
    print(G + '[>]' + C + ' Version    : ' + W + version + '\n')
    print(G + '[*]' + C + ' Wordlist generator')
    print(G + '[+]' + C + ' Options:')
    print('\t' + G + '-c' + W + ' <charset string>')
    print('\t' + G + '-m' + W + ' <min-len>')
    print('\t' + G + '-x' + W + ' <max-len>')
    print('\t' + G + '-o' + W + ' <file name>')
    print('\n' + G +
          'Exemplo: python3 %s -c abcde1234 -m 2 -x 5 -o wordlist.txt' % argv[0])


try:
    minimo = 0
    maximo = 0
    caracteres = None
    file = None
    optList, args = getopt(argv[1:], 'c: m: x: o:')

    for opt, i in optList:
        if opt == '-c':
            caracteres = i
        if opt == '-m':
            minimo = i
        if opt == '-x':
            maximo = i
        if opt == '-o':
            file = i

    if int(minimo) > int(maximo) or caracteres is None or file is None:
        banner()
        exit()

    with open(file, 'w') as arquivo:
        caracteres = list(str(caracteres))

        os.system('clear')
        print(G + '[*]' + C + ' Generating wordlist...')

        for i in range(int(minimo), int(maximo)+1):
            for j in product(caracteres, repeat=i):
                word = ''.join(j)
                print(W + '%s' % word)
                arquivo.write('%s\n' % word)

        print(G + '[*]' + C + ' Generated wordlist!')
        print(G + '[*]' + C + ' File: %s' % (file) + W)

except KeyboardInterrupt:
    print('\n' + R + '[-]' + C + ' Keyboard interrupt.' + W)
