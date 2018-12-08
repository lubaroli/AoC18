from collections import defaultdict

def count_x_repeated(string, x=1):
    cnt = defaultdict(int)
    for c in string:
        cnt[c] += 1
    if x in cnt.values():
        return True
    else:
        return False

def checksum(tags):
    cnt_two = cnt_three = 0
    for tag in tags:
        if count_x_repeated(tag, 2):
            cnt_two += 1
        if count_x_repeated(tag, 3):
            cnt_three += 1
    return cnt_two*cnt_three

def similar_tags(tag1, tag2):
    cnt = 0
    rem = ""
    for c1, c2 in zip(tag1, tag2):
        if c1 != c2:
            cnt += 1
        else:
            rem += c1

    if cnt == 1:
        return rem
    else:
        return False

def find_close_tags(tags):
    for tag1 in tags:
        for tag2 in tags[tags.index(tag1):]:
            if similar_tags(tag1, tag2):
                string = similar_tags(tag1, tag2)
                return string
def main():
    with open("puzzle2.txt", 'r', newline='\n') as f:
        lines = f.readlines()

    count = checksum(lines)
    print("The checksum for all box IDs is {}".format(count))
    result = find_close_tags(lines)
    print("The resulting tag ID is {}".format(result))

if __name__ == "__main__":
    main()
