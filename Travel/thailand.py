class ThailandPack:
    def detail(self):
        print("[태국 패키지 여행] 방콕, 파타야, 참가비 500,000KRW")

if __name__ == "__main__":
    print("모듈이 직접 실행됨")
    trip = ThailandPack()
    trip.detail()
else:
    print("외부 호출")