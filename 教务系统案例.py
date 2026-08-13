#Day One
#学生
class Students :
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
#对于显示形式
    def __str__(self) -> str:
        return f"姓名:{self.name}|语文:{self.chinese}|数学:{self.math}|英语:{self.english}"

    def update_score(self,chinese =None ,math = None ,english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

#测试
if __name__ == "__main__":
    num01 = Students("蔡徐坤",78,91,13)
    print(num01)
    num01.update_score(chinese=91)
    print(num01)


#Day Two
