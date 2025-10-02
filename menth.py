import random
import time
import argparse
import math
from reportlab.pdfgen import canvas
from reportlab import platypus


def get_parser():
    parser = argparse.ArgumentParser(description="practice math")
    parser.add_argument("--seed")
    parser.add_argument("-l", "--length", type=int, default=None)
    parser.add_argument("pattern", type=str)
    parser.add_argument("-b", "--answer_base", type=int, default=10)
    parser.add_argument("-t", "--tries", type=int, default=1)
    return parser


BASE = {2: "b", 8: "o", 10: "d", 16: "x"}
PREFIX = {2: "0b", 8: "0o", 10: "", 16: "0x"}
OPERATORS = "+-*/^|&%"


class Test:
    def __init__(self, pattern, answer_base, length=None):
        self.operands = []
        self.operators = []
        assert answer_base in BASE.keys()
        self.answer_base = answer_base
        self.length = length
        self.curr = 0
        p = pattern.split(",")
        for i, o in enumerate(p):
            if i != 0:
                opr = o[0]
                assert opr in OPERATORS
                o = o[1:]
                self.operators.append(opr)
            rnge = o.split(":")
            if len(rnge) == 1:
                remain = rnge[0]
            else:
                remain = rnge[1]
            bas = remain.split("#")
            if len(bas) == 1:
                base = 10
            else:
                base = int(bas[1])
                assert base in BASE.keys()
            mn = int(rnge[0], base)
            mx = int(bas[0], base)
            self.operands.append((mn, mx, base))
        assert len(self.operands) - 1 == len(self.operators)
        return

    def get_question(self):
        if self.curr == self.length:
            return None
        self.curr += 1
        question = ""
        answer = 0
        for i, op in enumerate(self.operands):
            if i == 0:
                val = random.randint(op[0], op[1])
                question += (PREFIX[op[2]] + "{:" + BASE[op[2]] + "}").format(val)
                answer = val
            else:
                opr = self.operators[i - 1]
                val = random.randint(op[0], op[1])
                question += " "
                question += opr
                question += " "
                question += (PREFIX[op[2]] + "{:" + BASE[op[2]] + "}").format(val)
                if opr == "+":
                    answer += val
                elif opr == "-":
                    answer -= val
                elif opr == "*":
                    answer *= val
                elif opr == "/":
                    # we don't care about float div
                    answer //= val
                elif opr == "^":
                    answer = int(math.pow(answer, val))
                elif opr == "%":
                    answer %= val
                elif opr == "&":
                    answer &= val
                elif opr == "|":
                    answer |= val
        self.curr_answer = answer
        return question

    def check_answer(self, answer):
        val = int(answer, base=self.answer_base)
        return val == self.curr_answer

    def get_answer(self):
        return (PREFIX[self.answer_base] + "{:" + BASE[self.answer_base] + "}").format(self.curr_answer)

    # def generate_pdf(self):
    #     story = []
    #     doc = platypus.SimpleDocTemplate("hello.pdf")
    #     table = platypus.Table([["hello"], ["how are you"])


def generate_pdf():
    story = []
    doc = platypus.SimpleDocTemplate("hello.pdf")
    data = 
    table = platypus.Table(data, colWidths=)
    story.append(table)
    doc.build(story)


def main():
    args = get_parser().parse_args()
    random.seed(time.time())
    test = Test(args.pattern, args.answer_base, length=args.length)
    while True:
        q = test.get_question()
        if q is None:
            return
        tries = 0
        correct = False
        while tries < args.tries or args.tries == 0:
            print(q)
            try: 
                usr_ans = input()
            except KeyboardInterrupt:
                return
            try:
                if test.check_answer(usr_ans):
                    print("correct")
                    correct = True
                    break
                else:
                    print("incorrect")
                    tries += 1
                    continue
            except:
                print("incorrect")
                tries += 1
                continue
        if not correct:
            print("answer was " + test.get_answer())


if __name__ == "__main__":
    # main()
    generate_pdf()
