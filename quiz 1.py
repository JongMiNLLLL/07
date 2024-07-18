# 두 수의 덧셈, 뺄셈, 나눗셈, 곱셈 함수를 포함하는 클래스를 만들고, 해당 클래스틀 통해 객체를 생성하시오.
class 사칙연산계산기 :

    def add (slef, a, b):
        result = a + b
        return result
    def mul (self, a, b):
        result = a * b
        return result

    def sub (self, a,b):
        result = a - b
        return result

app = 사칙연산계산기()
print(app.add(7,9))
print(app.mul(7,9))
print(app.sub(7,9))
class 사칙연산계산기 :
    def __init__(self, name):
        self.app_name = name

app_name = 사칙연산계산기("이종민계산기")
print(app_name)
