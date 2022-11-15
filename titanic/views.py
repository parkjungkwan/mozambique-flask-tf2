from titanic.models import TitanicModel
from util.dataset import Dataset


class TitanicController(object):
    def __init__(self):
        pass

    def __str__(self):
        return f""
    
    dataset = Dataset()
    model = TitanicModel()

    def preprocess(self,train, test) -> object: # 전처리
        model = self.model
        this = self.dataset
        this.train = model.new_model(train) # Data Partition
        this.test = model.new_model(test)
        this.id = this.test['PassengerId']
        this = model.sex_norminal(this)
        this = model.age_ordinal(this)
        this = model.fare_ordinal(this)
        this = model.embarked_norminal(this)
        this = model.title_norminal(this)
        this = model.drop_features(this,
                                   'PassengerId','Name','Sex','Age',
                                   'SibSp','Parch','Ticket','Fare','Cabin')
        return this

    def modeling(self,train, test) -> object: # 모델생성
        model = self.model
        this = self.preprocess(train, test)
        this.label = model.create_label(this)
        this.train = model.create_train(this)
        return this
    
    def learning(self, train, test, algo): # 기계학습
        this = self.modeling(train, test)
        accuracy = self.model.get_accuracy(this, algo)
        print(f"랜덤포레스트분류기 정확도: {accuracy} %")
    
    def submit(self): # 배포
        pass


if __name__=="__main__":
    t = TitanicController()
    this = Dataset()
    this = t.modeling('train.csv', 'test.csv')
    print(this.train.head())
    print(this.train.columns)
