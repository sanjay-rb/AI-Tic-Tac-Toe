# %%
import pandas as pd 

# %%
dataset = pd.read_csv(r"tic-tac-toe.csv")
X = dataset.iloc[:, [0,1,2,3,4,5,6,7,8]].values
y = dataset.iloc[:, -1].values

# %%
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for i in range(0, 8+1):
    X[:, i] = le.fit_transform(X[:, i])
print(X)
print(set(y))

# %%
from sklearn.tree import DecisionTreeClassifier
decision_tree_calssifier = DecisionTreeClassifier(criterion='entropy')
decision_tree_calssifier.fit(X, y)

# %%
y_pred = decision_tree_calssifier.predict(X)

# %%
from sklearn.metrics import confusion_matrix
matrix = confusion_matrix(y_true=y, y_pred=y_pred)
print("Confusion Matrix : ")
print(matrix)

# Detail view of matrix
print("Detail view of matrix : ")
NO_OF_CATEGORY = len(set(y))
for i in range(NO_OF_CATEGORY):
    for j in range(NO_OF_CATEGORY):
        print(f"Expect {j}", f"Predict {i}", ":", matrix[i][j])

# %%
from sklearn.metrics import accuracy_score
print(accuracy_score(y_true=y, y_pred=y_pred))


