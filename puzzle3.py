import numpy as np

def best_claim(claims_dict, fabric):

    for id in claims_dict.keys():
        x1 = claims_dict[id][0]
        x2 = claims_dict[id][2] + x1
        y1 = claims_dict[id][1]
        y2 = claims_dict[id][3] + y1
        if np.sum(fabric[x1:x2, y1:y2] == 1) == ((x2-x1)*(y2-y1)):
            return id

    return None

def allocate_claims(claims_dict, fabric_width=1000, fabric_height=1000):
    fabric = np.zeros((fabric_width, fabric_height), dtype="int32")

    for id in claims_dict.keys():
        x1 = claims_dict[id][0]
        x2 = claims_dict[id][2] + x1
        y1 = claims_dict[id][1]
        y2 = claims_dict[id][3] + y1
        fabric[x1:x2, y1:y2] += 1

    # Subtracts 1 from resulting "fabric" to ignore single claimed inches,
    # then replaces negative numbers by zero (unclaimed inches). Finally,
    # turns each resulting inch claimes multiple times (i.e. > 1) into 1 and
    # sums the flattened array.
    overlap = np.sum(np.maximum(fabric-1, 0) >= 1)
    return fabric, overlap

def process_claims(lines):
    claims_dict = {}
    for line in lines:
        id = line[0:line.index("@")-1]
        x = int(line[line.index("@")+1:line.index(",")])
        y = int(line[line.index(",")+1:line.index(":")])
        w = int(line[line.index(":")+1:line.index("x")])
        h = int(line[line.index("x")+1:line.index("\n")])
        claims_dict[id] = [x, y, w, h]

    return claims_dict

def main():
    with open("puzzle3.txt", 'r', newline='\n') as f:
        lines = f.readlines()

    claims = process_claims(lines)
    fabric, overlap = allocate_claims(claims)
    print(overlap)
    id = best_claim(claims, fabric)
    print(id)

if __name__ == "__main__":
    main()
