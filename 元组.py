students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李婷婷", 92, 88, 95),
    ("S003", "刘三", 78, 85, 82),
    ("S004", "张华", 88, 79, 91),
    ("S005", "周欢", 95, 96, 89),
    ("S006", "陈明", 76, 82, 77),
    ("S007", "红梅", 89, 91, 94),
    ("S008", "赵立国", 75, 69, 82),
    ("S009", "许杰", 86, 89, 98),
    ("S010", "谢天", 66, 59, 72)
)
#每个同学总分
print("学号  姓名  总分 各科平均分")
for i in students:
    total = i[2] + i[3] + i[4]
    avg = total / 3
    print(i[0], i[1], total ,f"{avg:.1f}")



chimese_score2 = [i[2] for i in students]
math_score2 = [i[3] for i in students]
english_score2 = [i[4] for i in students]

print(      )
print(      )
print(      )
print(      )

print("语文最低分:",min(chimese_score2),"语文最高分",max(chimese_score2),"语文平均分",sum(chimese_score2)/len(chimese_score2))
print("数学最低分:",min(math_score2),"数学最高分",max(math_score2),"数学平均分",sum(math_score2)/len(math_score2))
print("英语最低分:",min(english_score2),"语文最高分",max(english_score2),"语文平均分",sum(english_score2)/len(english_score2))



print(      )
print(      )
print(      )
print(      )

for i in students:
    total = i[2] + i[3] + i[4]
    avg = total / 3
    if avg > 90:
        print(i[0], i[1])