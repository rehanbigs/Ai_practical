from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from math import sqrt
import numpy as np
iris = load_iris() 
X = iris.data # Features
y = iris.target # Labels
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2)
def euclideandist(point1,point2):
  dist=0
  for i in range(len (point1)):
    dist=dist+((point1[i]-point2[i])**2)
  print(sqrt(dist))
  return sqrt(dist)



def get_k_neighbors(X_train, y_train, test_sample, k):
    nearest = [(float('inf'), None)] * k

    for i in range(len(X_train)):
        dist = euclideandist(X_train[i], test_sample)
        for j in range(len(nearest)):
            if dist < nearest[j][0]:
                nearest[j]=(dist, y_train[i])
                break

        nearest.sort()

    return nearest


def predict_classification(X_train, y_train, test_sample, k):
  votes=[0,0]
  nearest=get_k_neighbors(X_train,y_train,test_sample,k)
  for i in range(len(nearest)):
    if(nearest[i][1]==0):
      votes[0]+=1
    elif(nearest[i][1]==1):
        votes[1]+=1
    
  return 0 if votes[0] > votes[1] else 1



def calculate_accuracy(X_train, y_train, X_test, y_test, k_values):
    accuracies = {}

    for k in k_values:
        correct_predictions=0

        for i in range(len(X_test)):
            predicted_label = predict_classification(X_train, y_train, X_test[i], k)
            if predicted_label==y_test[i]:
                correct_predictions+=1

        accuracy = correct_predictions / len(y_test)
        accuracies[k] = accuracy

    return accuracies

kvalues = [1,5,7,9]
accuracies = calculate_accuracy(X_train, Y_train, X_test, Y_test, kvalues)\

for i in range(len(kvalues)):
    print(f"Accuracy for k={kvalues[i]}: {accuracies[kvalues[i]]:.2f}")

print(X_train.shape)


