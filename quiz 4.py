# 사용자의 이름, 나이, 연락처를 입력 받아서 화면에 '입력하신 이름은 ### 이며, 나이는 ###, 그리고 연락처는
# ###-####-####입니다. 를 출력하는 클래스를 작성하시오.

class user:
    def __init__(self,name,age,adress):
        self.user_name = name
        self.user_age = age
        self.user_adress = adress
    def print(self):
        print('입력하신 이름은',self.user_name,'이며, 나이는', self.user_age,' 그리고 연락처는',self.user_adress )

my_user = user("이종민", 26,"010-0000-0000")
my_user.print()
