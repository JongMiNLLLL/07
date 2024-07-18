## 문자 메세지 길이 판별 클래스 문자메시지 길이에 따라 문자요금이 결정되는 프로그램을 작성하시오
## 문자 메세지 길이에 따라 부과되는 요금은 클래스를 생성할 때 속성 정보로 갖게 된다.
## 또한, 요금이 부과될 문자 메시지의 길이를 정할 수 있도록 설정하시오(속성정보)
## 이때, 사용자로부터 문자메시지를 입력 받아서 문자요금을 환산하는 코드를 작성하시오.

class MMS:
    def __init__(self, l,p1,p2):
        self.len_message = l
        self.price_1 = p1
        self.price_2 = p2
    def price(self,text):
        if len(text) <= self.len_message:
            print(self.price_1)
        elif len(text) > self.len_message:
            print(self.price_2)

mms = MMS(5,50,1000)
mms.price("임의의 텍스트를 입력하ㅔ요. :")
