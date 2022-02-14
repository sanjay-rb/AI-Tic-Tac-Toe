import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

class Classifier:
    le = LabelEncoder()
    def __init__(self) -> None:
        print("Loading game data....")
        dataset = pd.read_csv(r"test_v3.csv")
        X = dataset.iloc[:, [0,1,2,3,4,5,6,7,8]].values
        y = dataset.iloc[:, -1].values
        for i in range(0, 8+1):
            X[:, i] = self.le.fit_transform(X[:, i])
        
        print("Loading opponent....")
        self.classifier = LogisticRegression()
        self.classifier.fit(X, y)

    def oMove(self, board):
        # print([board])
        X = self.le.fit_transform(board)
        return self.classifier.predict([X])