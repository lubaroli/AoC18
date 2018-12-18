import numpy as np

def mh_dist(p1, p2):
    return np.sum(np.abs(p1-p2))

def outer_points_ids(l_pts):
    [xmax, ymax] = np.max(l_pts, axis=0)
    [xmin, ymin] = np.min(l_pts, axis=0)
    return [idx for idx, pt in enumerate(l_pts)
            if (pt[0] in (xmin, xmax)) or (pt[1] in (ymin, ymax))]

def closest(coord, l_pts):
    min_dist = None
    for i, pt in enumerate(l_pts):
        if (min_dist == None) or (mh_dist(pt, coord) < min_dist):
            min_dist = mh_dist(pt, coord)
            idx = i
    return idx

def calculate_area(l_pts):
    [xmax, ymax] = np.max(l_pts, axis=0)
    [xmin, ymin] = np.min(l_pts, axis=0)
    border = outer_points_ids(l_pts)
    grid = {(x, y): closest([x, y], l_pts) for x in range(xmin-1, xmax+2) for
            y in range(ymin-1, ymax+2)}

    return max(list(grid.values()).count(n) for n in range(len(l_pts))
               if n not in border)

def calculate_region(l_pts):
    [xmax, ymax] = np.max(l_pts, axis=0)
    [xmin, ymin] = np.min(l_pts, axis=0)
    grid = {(x, y): sum(abs(x-i)+abs(y-j) for i, j in l_pts)
            for x in range(xmin, xmax) for y in range(ymin, ymax)}

    return sum(x < 10000 for x in grid.values())

def main():
    with open("puzzle6.txt", 'r') as f:
        l_pts = [[int(x) for x in point.split(", ")] for point in f]
        l_pts = np.array(l_pts)

    # l_pts = np.array([[1, 1], [1, 6], [8, 3], [3, 4], [5, 5], [8, 9]])
    # print(calculate_area(l_pts)
    print(calculate_region(l_pts))

if __name__ == "__main__":
    main()
