import aocd

def main():
    with open("data.txt") as f:
        x, y = 0, 0
        for line in aocd.get_data(year=2021, day=2).split("\n"):
            action, unit = line.split(" ")
            unit = int(unit)

            if action == "forward":
                x += unit
            if action == "down":
                y += unit
            if action == "up":
                y -= unit

        print(x, y)
        print(x * y)

if __name__ == '__main__':
    main()