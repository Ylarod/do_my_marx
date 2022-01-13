import json

only_export_error = False
problems = []
markdown_text = ""
with open("process.json", "r") as f:
    problems = json.loads(f.read())
for pid, problem in enumerate(problems):
    try:
        if only_export_error and problem['error_times'] < 1:
            continue
        markdown_text += "【" + problem['type'].replace("题", "") + "】"
        markdown_text += str(pid) + "、"
        markdown_text += problem['problem'] + "\n"
        if problem['type'] != "判断题":
            if "A" in problem['answer']:
                markdown_text += "- [X] " + problem['A'] + "\n"
            else:
                markdown_text += "- [ ] " + problem['A'] + "\n"
            if "B" in problem['answer']:
                markdown_text += "- [X] " + problem['B'] + "\n"
            else:
                markdown_text += "- [ ] " + problem['B'] + "\n"
            if "C" in problem['answer']:
                markdown_text += "- [X] " + problem['C'] + "\n"
            else:
                markdown_text += "- [ ] " + problem['C'] + "\n"
            if "D" in problem['answer']:
                markdown_text += "- [X] " + problem['D'] + "\n"
            else:
                markdown_text += "- [ ] " + problem['D'] + "\n"
        else:
            markdown_text += "正确答案: " + problem['answer'] + "\n"
        markdown_text += "错误次数: " + str(problem['error_times']) + "\n\n"
    except KeyError:
        if not only_export_error:
            markdown_text += "\n"
        continue
with open("process.md", "w") as f:
    f.write(markdown_text)