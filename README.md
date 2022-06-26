# do_my_marx

题库json 使用parser转换 https://github.com/notnotype/xxt  的输出结果 （输出的.text文件）

Android APP版本: https://github.com/fornary4/IdeologicalExercise

复习建议：

0. 读一遍题（可选）
1. 从头到尾刷一遍题
2. 做错题 `only_do_error = True`
3. 做做错对错题 `error_threshold = 2`
4. 重复直至全对
5. 导出错题，考前看一遍


做题
```
python3 rush_b.py
```

导出错题
```
python3 extract_wrong.py
```

导出markdown
```
python3 gen_markdown.py
```

![pic](https://raw.githubusercontent.com/Ylarod/do_my_marx/main/assets/pic.png)
