# pip install matplotlib
# pip install joblib
import pandas
from sklearn.utils import shuffle
import matplotlib
import matplotlib.pyplot as plot
import cv2
from sklearn.model_selection import train_test_split
import joblib
from sklearn.svm import SVC

# Set the backend to Agg
matplotlib.use('Agg')

data = pandas.read_csv('dataset.csv')
data = shuffle(data)

# Seperation of dependent and independent variable
X = data.drop(["label"], axis=1)
Y = data["label"]

# preview of image using matplotlib
index = 188
image = X.loc[index].values.reshape(28, 28)
print(Y[index])
plot.imshow(image)
plot.savefig('output.png')

# Train test split
# test_size=0.2 => 20% used for testing and 80% used for training part
train_x, test_x, train_y, test_y = train_test_split(X,Y, test_size=0.2)

# Fit the model using svc and also save the model using joblib
classifier=SVC(kernel="linear", random_state=6)
classifier.fit(train_x,train_y)
joblib.dump(classifier, "model/digit_recognizer")

# calculate accuracy
from sklearn import metrics
prediction = classifier.predict(test_x)
print("Accuracy= ",metrics.accuracy_score(prediction, test_y))