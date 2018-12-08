from collections import defaultdict

def adjust_frequency(start_f, sequence):
    for f in sequence:
        start_f += f
    return start_f

def find_repeated_frequency(start_f, sequence, max_iter=150):
    freqs = defaultdict(int)
    freqs[start_f] = True
    while max_iter:
        for f in sequence:
            start_f += f
            if not freqs[start_f]:
                freqs[start_f] = True
            else:
                return start_f
        max_iter -= 1


def main():
    with open("puzzle1.txt", 'r', newline='\n') as f:
        lines = f.readlines()

    sequence = [int(s) for s in lines]
    frequency = adjust_frequency(0, sequence)
    print("Final frequency is {}".format(frequency))
    rep_freq = find_repeated_frequency(0, sequence)
    print("First repeated frequency is {}".format(rep_freq))

if __name__ == "__main__":
    main()
