"""
Day 5 of Advent of Code
"""
def file():
    with open("day5_data.txt") as file:
        lines = file.read().split("\n")
        data = []
        for line in lines:
            temp = line.split(" -> ")
            data.append(temp)
        coords = []
        for dline in data:
            coords.append([list(map(int, dline[0].split(","))), list(map(int, dline[1].split(",")))])

        return coords

def overlaps_of_points(diagonal):
    coords = file()

    board = {}
    for coord in coords:
        dx = coord[0][0] - coord[1][0]
        dy = coord[0][1] - coord[1][1]

        if dx == 0:
            start = f"{coord[0][0], min(coord[0][1], coord[1][1])}"
            board[start] = board.get(start, 0) + 1

            for y_point in range(min(coord[0][1], coord[1][1])+1, max(coord[0][1], coord[1][1])+1):
                str_point = f"{coord[0][0], y_point}"
                board[str_point] = board.get(str_point, 0) + 1

        if dy == 0:
            start = f"{min(coord[0][0], coord[1][0]), coord[0][1]}"
            board[start] = board.get(start, 0) + 1

            for x_point in range(min(coord[0][0], coord[1][0])+1, max(coord[0][0], coord[1][0])+1):
                str_point = f"{x_point, coord[0][1]}"
                board[str_point] = board.get(str_point, 0) + 1

        elif diagonal and abs(dx) == abs(dy):
            start = f"{coord[0][0], coord[0][1]}"
            board[start] = board.get(start, 0) + 1

            sign = lambda x: (x<0) - (x>0)
            xm = sign(dx)
            ym = sign(dy)

            for diag in range(1, abs(coord[0][0]-coord[1][0])+1):
                str_point = f"{coord[0][0]+xm*diag, coord[0][1]+ym*diag}"
                board[str_point] = board.get(str_point, 0) + 1
    return board


if __name__ == "__main__":
    no_diag = overlaps_of_points(False)
    diag = overlaps_of_points(True)

    no_diag_overlaps = 0
    for key in no_diag.keys():
        if no_diag[key] > 1:
            no_diag_overlaps += 1

    diag_overlaps = 0
    for key in diag.keys():
        if diag[key] > 1:
            diag_overlaps += 1

    print(f"Overlaps without diagonal: {no_diag_overlaps}")
    print(f"Overlaps with diagonal: {diag_overlaps}")



