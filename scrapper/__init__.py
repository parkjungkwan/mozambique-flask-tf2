from scrapper.domains import MusicRanking
from scrapper.view import ScrapController

if __name__=="__main__":
    m = MusicRanking()
    while True:
        menu = input("0번:종료,1번:벅스")
        api = ScrapController()
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print("벅스")
            m.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            m.query_string = "20221101"
            m.parser = "lxml"
            m.class_names=["title", "artist"]
            m.tag_name = "p"
            api.menu_1(m)
        else:
            print("해당메뉴 없음")