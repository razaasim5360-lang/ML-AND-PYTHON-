import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,plot_tree

# features:
# column 1 = hours studied
# column 2 = attendence percentage
X = np.array([[1, 50], [2, 60], [3, 70], [4, 80], [5, 90], [6, 100]])
y = np.array([0, 0, 1, 1, 1, 1])  # labels: 0 = fail, 1 = pass
model = DecisionTreeClassifier(
    criterion="gini", max_depth=3, random_state=42
)
model.fit(X, y)
# student studied for 9 hours and has 88% attendance
new_student = np.array([[9, 88]])
prediction = model.predict(new_student)
if prediction[0] == 1:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")
plt.figure(figsize=(14,8))
plot_tree(
    model, feature_names=["Hours Studied", "Attendance Percentage"],
     class_names=["Fail", "Pass"], 
     filled=True,
     rounded=True,
)
plt.title("Decision Tree Classification")
plt.savefig("decision_tree.png", dpi = 300, bbox_inches='tight')
plt.show()    