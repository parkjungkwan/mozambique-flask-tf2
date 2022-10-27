import pandas as pd
from util.dataset import Dataset

"""
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
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

if __name__ == '__main__':
    t = TitanicModel()
    print(t)