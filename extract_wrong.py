import json


problems = []
wrong_problems = []
wrong_txt = ""
with open("process.json", "r") as f:
    problems = json.loads(f.read())
for problem in problems:
    try:
        if problem['error_times'] > 1:
            wrong_problem = {}
            wrong_problem['problem'] = problem['problem']
            wrong_problem['type'] = problem['type']
            if problem['type'] != "判断题":
                wrong_problem['A'] = problem['A']
                wrong_problem['B'] = problem['B']
                wrong_problem['C'] = problem['C']
                wrong_problem['D'] = problem['D']
            wrong_problem['answer'] = problem['answer']
            wrong_problem['error_times'] = problem['error_times']
            wrong_problems.append(wrong_problem)
            wrong_txt += "[" + problem['type'].replace("题", "") + "]"
            wrong_txt += problem['problem'] + "\n"
            if problem['type'] != "判断题":
                wrong_txt += problem['A'] + "\n"
                wrong_txt += problem['B'] + "\n"
                wrong_txt += problem['C'] + "\n"
                wrong_txt += problem['D'] + "\n"
            wrong_txt += "正确答案: " + problem['answer'] + "\n"
            wrong_txt += "错误次数: " + str(problem['error_times']) + "\n\n"
    except KeyError:
        continue
with open("wrong.json", "w") as f:
    f.write(json.dumps(wrong_problems, ensure_ascii=False))
with open("wrong.txt", "w") as f:
    f.write(wrong_txt)