# 게임 캐릭터 만들기. 게임 캐릭터 생성 클래스는 아이디, 성별, 직업wjd보를 갖으며
# 기본 공격 함수를 갖는다. 기본 공격 함수는 사용시 '공격!' 문자열을 화면에 출력한다.

class Character:
    def __init__(self, ID, sex, job):
        self.Character_ID = ID
        self.Character_sex = sex
        self.Character_job = job

    def attack(self, 상대방_ID):
        print(self.Character_ID,"(이)가", 상대방_ID,'를 조온나 강한 공격!!!!!!!!!!!!')



my_Character = Character('흑룡기사이종민', '남', '용기사')
my_Character.attack("리자몽")
