# 学生总分元组
print("\t\t\t班级学生考试成绩统计")
students = (
    ("S001", "王林",   85, 92, 78),
    ("S002", "李慕晚", 92, 88, 95),
    ("S003", "十三",   78, 85, 82),
    ("S004", "曾牛",   88, 79, 91),
    ("S005", "离铁",   95, 96, 89),
    ("S006", "王卓",   76, 82, 77),
    ("S007", "红蝶",   89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木",   86, 89, 98),
    ("S010", "遁天",   66, 59, 72),
)
# 1.计算每个学生的总分,各科平均分,然后一并输出出来
print("学号\t\t姓名\t\t语文成绩\t数学成绩\t英语成绩\t 总分\t 平均分")
for i in students :
    total = i[2]+i[3]+i[4]
    avg = total / 3
    print(f"{i[0]} \t {i[1]} \t {i[2]} \t {i[3]} \t {i[4]} \t {total} \t {avg:.1f}")
# avg后：.1f是注释浮点数只保留一位小数
# i也是一个小元组
print("")
#2.统计各科成绩的最低分、最高分、平均分，并输出
chinese_scores = [i[2] for i in students]
math_scores = [i[3] for i in students]
english_scores = [i[4] for i in students]
print(f"语文成绩的最低分为：{min(chinese_scores)}\n语文成绩的最高分为：{max(chinese_scores)}\n语文成绩的平均分为：{sum(chinese_scores)/len(chinese_scores):.1f}")
print()
print(f"数学成绩的最低分为：{min(math_scores)}\n数学成绩的最高分为：{max(math_scores)}\n数学成绩的平均分为：{sum(math_scores)/len(math_scores):.1f}")
print()
print(f"英语成绩的最低分为：{min(english_scores)}\n英语成绩的最高分为：{max(english_scores)}\n英语成绩的平均分为：{sum(english_scores)/len(english_scores):.1f}")

print()
#3.查找成绩优秀（平均分大于90）的学生print("成绩优秀的学生（平均分 > 90）：")
print("优秀学生名单如下：")
for i in students:
    total = i[2] + i[3] + i[4]
    avg = total / 3
    if avg > 90:
        print(f"学号：{i[0]} 姓名：{i[1]} 平均分：{avg:.1f}")
