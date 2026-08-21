from sklearn.svm import SVC
import matplotlib.pyplot as plt

# Training data 
X = [
    [2, 60],
     [3, 65],
      [4, 70],
       [5, 75],
        [6, 80],
         [7, 85],
          [8, 90],
           [9, 95],
           [10, 100]
]
#Target values
Y = [
    "FAIL",
    "FAIL",
    "FAIL",
    "PASS",
    "PASS",
    "PASS",
    "PASS",
    "PASS",
    "PASS",
]

# Create a SVM Model
model = SVC(kernel='linear')

#Train the model 
model.fit(X,Y)

# New student's data
new_student = [[2.2, 62]]

# Make prediction
prediction = model.predict(new_student)

print("Predicted Result:", prediction[0])

# Plot the training data
for i in range(len(X)):
    if Y[i] == "PASS":
        plt.scatter(X[i][0], X[i][1], color='green', label='PASS' if i == 0 else "")
    else:
        plt.scatter(X[i][0], X[i][1], color='red', label='FAIL' if i == 0 else "")   

# Plot new student
plt.scatter(
    new_student[0][0],
     new_student[0][1], 
     marker ='*',
    s = 200,
     label="New student",
     
)          
plt.xlabel("Study hours")
plt.ylabel("Attendance percentage")
plt.title("SVM Classification")
plt.legend()
plt.show()