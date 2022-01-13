import json
result = []
with open("tq/毛泽东思想和中国特色社会主义理论体系概论题库.txt", "r") as f:
    txt = f.read()
    problems = txt.split("\n\n")
    for problem in problems:
        lines = problem.split("\n")
        p = {}
        for line in lines:
            if line == "":
                pass
            elif line.startswith("A"):
                p['A'] = line
            elif line.startswith("B"):
                p['B'] = line
            elif line.startswith("C"):
                p['C'] = line
            elif line.startswith("D"):
                p['D'] = line
            elif line.startswith("正确答案"):
                p['answer'] = line.replace("正确答案: ", "")
            else:
                p['problem'] = line
        try:
            if p['answer'] == "对" or p['answer'] == "错":
                p['type'] = "判断题"
            elif len(p['answer']) > 1:
                p['type'] = "多选题"
            else:
                p['type'] = "单选题"
            result.append(p)
        except KeyError:
            print(p)
# print(result)
with open("毛泽东思想和中国特色社会主义理论体系概论题库.json", "w") as f:
    f.write(json.dumps(result, ensure_ascii=False))