class House:
    def __init__ (self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print("{} {} {} {} {}년".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

house = []
numOfHouse = 3

house.append(House("강남", "아파트", "매매", "10억", 2010))
house.append(House("미포", "오피스텔", "전세", "5억", 2007))
house.append(House("송파", "빌라", "월세", "500/50", 2000))

print("총 {}대의 매물이 있습니다.".format(numOfHouse))
for home in house:
    home.show_detail()


