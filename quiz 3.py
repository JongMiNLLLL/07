## 부동산 정보 입력 클래스, 부동산 정보 클래스는 위치, 평수, 건물의 종류, 가격, 건물이 지어진 년도 정보를 갖는다.
## 또한 정보 확인 함수를 사용하면 부동산 객체에 포함된 속성 정보를 화면에 출력한다.

class building:
    def __init__(self, lotate, size, category, price, year,):
        self.building_lotate = lotate
        self.building_size = size
        self.building_category = category
        self.building_price = price
        self.building_year = year

    def search(self):
        print(self.building_lotate,self.building_size,self.building_category,self.building_price ,self.building_year )

my_building = building("서울","100평","오피스텔", "97억", 1998)
my_building.search()