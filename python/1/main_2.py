
def main():
    with open("data.txt") as f:
        lines = [int(line.strip()) for line in f.readlines()]

        prev_line = sum(lines[0:3])
        count = 0

        for i in range(1, len(lines)):
            line = sum(lines[i:i+3])
            if line > prev_line:
                count += 1
            prev_line = line

        print(count)




if __name__ == '__main__':
    main()