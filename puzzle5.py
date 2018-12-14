import re
from string import ascii_lowercase

def chain_reaction(s):
    while True:
        i_len = len(s)
        for char in ascii_lowercase:
            p = re.compile(char+char.upper()+"|"+char.upper()+char)
            s = p.sub("", s)
        if i_len == len(s):
            return s

def shortest_polymer(s):
    l = 1e10
    for char in ascii_lowercase:
        s_candidate = re.sub(char+"|"+char.upper(), "", s)
        l_new = len(chain_reaction(s_candidate))
        if l_new < l:
            l = l_new
    return l

def main():
    with open("puzzle5.txt", 'r', newline='\n') as f:
        s = f.readlines()[0]

    # s = "dabAcCaCBAcCcaDA"
    s = chain_reaction(s)
    print("After reacting, there are {} units remaining.".format(len(s)))
    l = shortest_polymer(s)
    print("The most optimal polymer has {} units.".format(l))

if __name__ == "__main__":
    main()
