import random
import time

def main():
    random.seed(time.time())
    while True:
        x = random.randint(0x0, 0x10)
        y = random.randint(0x0, 0x10)
        ans = x + y
        print("0x{:x} + 0x{:x}".format(x, y))
        usr_ans = int(input(), base=16)
        if usr_ans == ans:
            print("correct")
        else:
            print("incorrect, answer was 0x{:x}".format(ans))

if __name__ == "__main__":
    main()
