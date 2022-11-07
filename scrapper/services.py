from urllib.request import urlopen

from bs4 import BeautifulSoup

from scrapper import MusicRanking


def BugsMusic(arg):
    soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), 'lxml')
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    # 디버깅
    [print(f"{i}위 {j.find('a').text} : {k.find('a').text}")
     for i, j, k in zip(range(1, len(titles)), titles, artists)]
    # dict 로 변환
    diction = {}
    print("#" * 10)
    print(len(titles))
    for i, j in zip(titles, artists):
        diction[j.find('a').text] = i.find('a').text
    print(diction)
    arg.diction = diction

    # csv 파일로 저장
    arg.dict_to_dataframe()
    arg.dataframe_to_csv()

    