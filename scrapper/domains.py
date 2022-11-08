from dataclasses import dataclass
import pandas as pd
from bs4 import BeautifulSoup

"""
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.

class BugsMusic:
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        title={"class":"title"}
        artist = {"class":"artist"}
        titles = soup.find_all(name="p", attrs=title)
        artists = soup.find_all(name="p", attrs=artist)
        [print(f"{i}위 {j.find('a').text} : {k.find('a').text}")
         for i, j, k in zip(range(1,len(titles)), titles, artists)]


class Melon:
    pass
"""
@dataclass
class Scrap:
    html : str
    parser : str
    domain : str
    query_string : str
    headers : dict
    tag_name : str
    fname : str
    class_names : []
    artists : []
    titles : []
    diction : {}
    df : None
    soup : BeautifulSoup

    @property
    def html(self): return self._html
    @html.setter
    def html(self, html): self._html = html

    @property
    def parser(self): return self._parser

    @parser.setter
    def parser(self, parser): self._parser = parser

    @property
    def soup(self): return self._soup
    @soup.setter
    def soup(self, soup): self._soup = soup

    @property
    def domain(self): return self._domain
    @domain.setter
    def domain(self, domain): self._domain = domain

    @property
    def query_string(self): return self._query_string
    @query_string.setter
    def query_string(self, query_string): self._query_string = query_string

    @property
    def headers(self): return self._headers
    @headers.setter
    def headers(self, headers): self._headers = headers

    @property
    def tag_name(self): return self._tag_name
    @tag_name.setter
    def tag_name(self, tag_name): self._tag_name = tag_name

    @property
    def fname(self): return self._fname
    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def class_names(self): return self._class_names
    @class_names.setter
    def class_names(self, class_names): self._class_names = class_names

    @property
    def artists(self): return self._artists
    @artists.setter
    def artists(self, artists): self._artists = artists

    @property
    def titles(self): return self._titles
    @titles.setter
    def titles(self, titles): self._titles = titles

    @property
    def diction(self): return self._diction
    @diction.setter
    def diction(self, diction): self._diction = diction

    @property
    def df(self): return self._df
    @df.setter
    def df(self, df): self._df = df

    def dict_to_dataframe(self):
        print(len(self.diction))
        self.df = pd.DataFrame.from_dict(self.diction, orient='index')

    def dataframe_to_csv(self):
        path = './save/result.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN", header=None)



