import requests

def main():
    with open("data.txt") as f:
        lines = [int(line.strip()) for line in f.readlines()]

        prev_line = lines[0]
        count = 0

        for line in lines[1:]:
            if line > prev_line:
                count += 1
            prev_line = line

        print(count)




if __name__ == '__main__':
    main()