import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

'''
Data columns (total 12 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Unnamed: 0    234 non-null    int64  
 1   manufacturer : 회사  234 non-null    object 
 2   model : 모델        234 non-null    object 
 3   displ : 배기량         234 non-null    float64
 4   year : 연식         234 non-null    int64  
 5   cyl : 실린더          234 non-null    int64  
 6   trans : 차축        234 non-null    object 
 7   drv : 오토          234 non-null    object 
 8   cty : 시내연비          234 non-null    int64  
 9   hwy : 시외연비          234 non-null    int64  
 10  fl : 연료            234 non-null    object 
 11  class : 차종         234 non-null    object 
dtypes: float64(1), int64(5), object(6)

'''
my_meta = {
    "manufacturer": "회사",
    "model": "모델",
    "displ": "배기량",
    "year": "연식",
    "cyl": "실린더",
    "trans": "차축",
    "drv": "오토",
    "cty": "시내연비",
    "hwy": "시외연비",
    "fl": "연료",
    "class": "차종"
}
def my_menu(ls):
    print(f'type is {type(ls)}')
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

MENUS = ["종료","mpg 앞부분 확인",
         "mpg 뒷부분 확인",
         "행,열 출력",
         "데이터 속성 확인",
         "요약 통계량 출력",
         "문자 변수 요약 통계량 함께 출력",
         # mpg 129페이지
         "manufacturer 를 company 로 변경",
         "test 변수 생성" 
         # cty 와 hwy 변수를 머지(merge)하여 total 
         # 변수 생성하고 20이상이면 pass 미만이면 fail 저장
         "test 빈도표 만들기",
         "test 빈도 막대 그래프 그리기",
         # mpg 144페이지 문제
         "displ(배기량)이 4이하와 5이상 자동차의 hwy(고속도로 연비) 비교",
         "아우디와 토요타 중 도시연비(cty) 평균이 높은 회사 검색",
         "쉐보레, 포드, 혼다 데이터 출력과 hwy 전체 평균",
         # mpg 150페이지 문제
         # 메타데이터가 category, cty 데이터는 해당 raw 데이터인 객체생성
         # 후 다음 문제 풀이
         "suv / 컴팩 자동차 중 어떤 자동차의 도시연비 평균이 더 높은가?",
         # mpg 153페이지 문제
         "아우디차에서 고속도로 연비 1~5위 출력하시오",
         # mpg 158페이지 문제
         "평균연비가 가장 높은 자동차 1~3위 출력하시오"
         ]
class Mpg:

    def __init__(self):
        self.mpg = pd.read_csv('./data/mpg.csv')
        self.my_mpg = None
        self.count_test = None

    def head(self):
        print(self.mpg.head(3))

    def tail(self):
        print(self.mpg.tail(3))

    def shape(self):
        print(self.mpg.shape)

    def info(self):
        print(self.mpg.info())

    def describe(self):
        print(self.mpg.describe())

    def describe_include(self):
        print(self.mpg.describe(include ='all'))
    # "","manufacturer","model","displ","year",
    # "cyl","trans","drv","cty","hwy","fl","class"
    def change_meta(self):
        self.my_mpg = self.mpg.rename(columns=my_meta)
    def create_test_variable(self): # No.8
        self.change_meta()
        t = self.my_mpg
        t['총연비'] = (t['시내연비'] + t['시외연비'])/2
        t['연비테스트'] = np.where(t['총연비']>=20, 'pass', 'fail')
        self.my_mpg = t
        print(self.my_mpg.columns)
        print(self.my_mpg.head())

    def create_test_frequency(self): # No.9
        self.create_test_variable()
        t = self.my_mpg
        self.count_test = t['연비테스트'].value_counts()
        print(self.count_test)


    def draw_freq_bar_graph(self): # No.10
        self.create_test_frequency()
        self.count_test.plot.bar(rot=0)
        plt.savefig('./save/draw_freq_bar_graph.png')

    def compare_displ_and_hwy(self):
        pass

    def search_higher_cty(self):
        pass

    def find_hwy_average(self):
        pass

    def which_higher_between_suv_compact(self):
        pass

    def search_hwy_in_audi_top5(self):
        pass

    def search_average_mileage_top3(self):
        pass


if __name__ == '__main__':
    t = Mpg()
    while True:
        menu = my_menu(MENUS)
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("mpg 앞부분 확인")
            t.head()
        elif menu == '2':
            print("mpg 뒷부분 확인")
            t.tail()
        elif menu == '3':
            print("행,열 출력")
            t.shape()
        elif menu == '4':
            print("데이터 속성 확인")
            t.info()
        elif menu == '5':
            print("요약 통계량 출력")
            t.describe()
        elif menu == '6':
            print("문자 변수 요약 통계량 함께 출력")
            t.describe_include()
        elif menu == '7':
            print("manufacturer 를 company 로 변경")
            t.change_manufacturer_to_company()
        elif menu == '8':
            print("test 변수 생성")
            # cty 와 hwy 변수를 머지(merge)하여 total
            # 변수 생성하고 20이상이면 pass 미만이면 fail 저장
            t.create_test_variable()
        elif menu == '9':
            print("test 빈도표 만들기")
            t.create_test_frequency()
        elif menu == '10':
            print("test 빈도 막대 그래프 그리기")
            t.draw_freq_bar_graph()
        elif menu == '11':
            # mpg 144페이지 문제
            print("displ(배기량)이 4이하와 5이상 자동차의 hwy(고속도로 연비) 비교")
            t.compare_displ_and_hwy()
        elif menu == '12':
            print("아우디와 토요타 중 도시연비(cty) 평균이 높은 회사 검색")
            t.search_higher_cty()
        elif menu == '13':
            print("쉐보레, 포드, 혼다 데이터 출력과 hwy 전체 평균")
            t.find_hwy_average()
        elif menu == '14':
            # mpg 150페이지 문제
            # 메타데이터가 category, cty 데이터는 해당 raw 데이터인 객체생성
            # 후 다음 문제 풀이
            print("suv / 컴팩 자동차 중 어떤 자동차의 도시연비 평균이 더 높은가?")
            t.which_higher_between_suv_compact()
        elif menu == '15':
            print("아우디차에서 고속도로 연비 1~5위 출력하시오")
            t.search_hwy_in_audi_top5()
        elif menu == '16':
            print("평균연비가 가장 높은 자동차 1~3위 출력하시오")
            t.search_average_mileage_top3()
        else:
            print("잘못된 번호입니다")