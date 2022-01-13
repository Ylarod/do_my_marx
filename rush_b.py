import os
import json
import signal
import time


def check_answer(a1: str, a2: str):
    if a1 == a2:
        return True
    if a1.upper() == a2.upper():
        return True
    b1 = a1.upper().replace("1", "A").replace("2", "B").replace("2", "C").replace("4", "D")\
        .replace("对", "A").replace("错", "B").replace("T", "A").replace("F", "B")
    b2 = a2.upper().replace("1", "A").replace("2", "B").replace("2", "C").replace("4", "D")\
        .replace("对", "A").replace("错", "B").replace("T", "A").replace("F", "B")
    if b1 == b2:
        return True
    return False


do_what = "马克思主义基本原理题库.json"
problems = []


def save_exit(signum, frame):
    with open("process.json", "w") as f:
        f.write(json.dumps(problems, ensure_ascii=False))
    exit(0)


signal.signal(signal.SIGINT, save_exit)
signal.signal(signal.SIGTERM, save_exit)
if os.path.exists("process.json"):
    with open("process.json", "r") as f:
        problems = json.loads(f.read())
else:
    with open(do_what, "r", encoding='UTF-8') as f:
        problems = json.loads(f.read())

for pid, problem in enumerate(problems):
    try:
        if check_answer(problem['answer'], problem['my_answer']):
            continue
    except KeyError:
        pass
    print("[%s]第%d题：\n" % (problem['type'].replace("题", ""), pid))
    print(problem['problem'])
    if problem['type'] != "判断题":
        print(problem['A'])
        print(problem['B'])
        print(problem['C'])
        print(problem['D'])
    my_answer = input()
    if my_answer.upper() == "SAVE":
        with open("process.json", "w") as f:
            f.write(json.dumps(problems, ensure_ascii=False))
        my_answer = input()
    if my_answer.upper() == "QUIT":
        with open("process.json", "w") as f:
            f.write(json.dumps(problems, ensure_ascii=False))
        exit(0)
    problems[pid]['my_answer'] = my_answer
    if check_answer(problem['answer'], my_answer):
        print("\033[32m答对了！\033[0m\n\n\n")
    else:
        print("\033[31m答错了！\033[0m")
        print("正确答案：\033[32m" + problem['answer'] + "\033[0m")
        print("我的答案：\033[31m" + my_answer + "\033[0m")
        try:
            problems[pid]['error_times'] += 1
        except KeyError:
            problems[pid]['error_times'] = 1
        input()
        print("\n\n\n")
