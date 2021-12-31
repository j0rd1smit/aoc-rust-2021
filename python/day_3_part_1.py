import aocd


def main():
    data = aocd.get_data(year=2021, day=3).split("\n")

    counts = [0 for _ in range(len(data[0]))]
    for line in data:
        for i, v in enumerate(line):
            counts[i] += int(v)

    gamma = []
    epsilon = []
    for i in counts:
        if i > len(data) // 2:
            gamma.append("1")
            epsilon.append("0")
        else:
            gamma.append("0")
            epsilon.append("1")
    gamma = "".join(gamma)
    epsilon = "".join(epsilon)
    print(gamma, int(gamma, 2))
    print(epsilon, int(epsilon, 2))
    print(int(epsilon, 2) * int(gamma, 2))



if __name__ == '__main__':
    main()