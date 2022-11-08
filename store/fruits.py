import pandas as pd


def new_fruits_df():
    ls1 = ['제품','가격','판매량'] # 스키마
    ls2 = ['사과', '딸기', '수박'] # 제품
    ls3 = [1800, 1500, 3000] # 가격
    ls4 = [30, 40, 50] # 판매량
    ls5 = [ls2, ls3, ls4]
    df = pd.DataFrame(
        {j : ls5[i] for i, j in enumerate(ls1)})
    print(df)
    print('가격평균: '+str(df['가격'].mean()))
    print('판매량평균: '+str(df['판매량'].mean()))

if __name__ == '__main__':
    new_fruits_df()