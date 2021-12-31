
def main():
    with open("data.txt") as f:
        x, y, aim = 0, 0, 0
        for line in f.readlines():
            action, unit = line.split(" ")
            unit = int(unit)

            if action == "forward":
                x += unit
                y += aim * unit
            if action == "down":
                aim += unit
            if action == "up":
                aim -= unit

        print(x, y)
        print(x * y)

if __name__ == '__main__':
    main()