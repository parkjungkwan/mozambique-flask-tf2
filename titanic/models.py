import numpy as np
import pandas as pd
from util.dataset import Dataset

"""
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
시각화를 통해 얻은 상관관계 변수(variable = feature= column)는
Pclass
Sex
Age
Fare
Embarked
 === null 값 ===
 Age            177
 Cabin          687
 Embarked         2
"""
class TitanicModel(object):

    dataset = Dataset()

    def __init__(self):
        pass
    def __str__(self):
        b = self.new_model(fname=self.dataset.fname)
        return f'Train type: {type(b)}\n' \
               f'Train columns: {b.columns}\n' \
               f'Train head : {b.head()}\n' \
               f'Train null의 갯수 : {b.isnull().sum()}'
    def preprocess(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this)->object:
        return this.train.drop('Survived', axis = 1)

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_features(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop(i, axis = 1)
            this.test = this.test.drop(i, axis = 1)
        return this

    @staticmethod
    def sex_norminal(this)-> object: #  female -> 1 , male -> 0
        for i in [this.train,this.test]:
            i['Gender'] = i['Sex'].map({"male" : 0, "female" : 1})
        return this

    @staticmethod
    def age_ordinal(this)-> object: # 연령대 10대, 20대, 30대
        for i in [this.train,this.test]:
            i["Age"] = i["Age"].fillna(-0.5)
        bins = [-1,0,5,12,18,24,35,68,np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                             'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        for i in [this.train,this.test]:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)
            i['AgeGroup'] = i['AgeGroup'].map(age_mapping)
        return this

    @staticmethod
    def fare_ordinal(this) -> object: # 4등분 pd.qcut() 사용
        for i in [this.train,this.test]:
            i['FareBand'] = pd.qcut(i['Fare'], 4, labels={1, 2, 3, 4})
        return this

    @staticmethod
    def embarked_norminal(this)-> object: # 승선항구 S, C, Q
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        for i in [this.train,this.test]:
            i['Embarked'] = i['Embarked'].map({"S": 1, "C": 2, "Q":3})
        return this

if __name__ == '__main__':
    t = TitanicModel()
    this = Dataset()
    this.train = t.new_model('train.csv')
    this.test = t.new_model('test.csv')
    this = TitanicModel.embarked_norminal(this)
    print(this.train.columns)
    print(f"null 갯수: {this.train['Embarked'].isnull().sum()}")
    print(this.train.head(3))