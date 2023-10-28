import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, recall_score, f1_score

data = pd.read_csv('netflow_label.csv')

# Displaying the data
print(data.info())
print(data.columns)


label_encoder = LabelEncoder()
for column in data.columns:
    data[column] = label_encoder.fit_transform(data[column])

# 显示转换后的结果
print(data.info())
print(data.columns)


# Taking care of missing data, Removing duplicates
data.replace([np.inf, -np.inf], np.nan, inplace=True)
# drop missing values
data.dropna(inplace=True)
print(data.duplicated().sum())

data.drop_duplicates(inplace = True)
print(data.duplicated().sum())

# Implementing binary classification
print(data["malicious"].value_counts())

old_value = 'yes'
new_value = 1
data['malicious'] = data['malicious'].replace(old_value, new_value)

old_value = 'no'
new_value = 0
data['malicious'] = data['malicious'].replace(old_value, new_value)

df=data
train, test = train_test_split(df, test_size=0.2)

print(train.info())
print(test.info())

print("---------------")
print("Full dataset:")
print("---------------")
print("Malicious: " + str(df['malicious'].value_counts()[[1]].sum()))
print("Normal: " + str(df['malicious'].value_counts()[[0]].sum()))
print("")


print("---------------")
print("Training set:")
print("---------------")
print("Malicious: " + str(train['malicious'].value_counts()[[1]].sum()))
print("Normal: " + str(train['malicious'].value_counts()[[0]].sum()))
print("")


print("---------------")
print("Test set:")
print("---------------")
print("Malicious: " + str(test['malicious'].value_counts()[[1]].sum()))
print("Normal: " + str(test['malicious'].value_counts()[[0]].sum()))
print("")


y_train = np.array(train.pop('malicious'))# pop removes "Label" from the dataframe
X_train = train.values

y_test = np.array(test.pop('malicious')) # pop removes "Label" from the dataframe
X_test = test.values

# Building the model
forest = RandomForestClassifier(n_estimators=100, random_state=42)

# Train model
forest.fit(X_train, y_train)

# Predict on test set
y_pred = forest.predict(X_test)

# Caclulate accuracy
print("---------------")
print("Result")
print("---------------")
accuracy = accuracy_score(y_test, y_pred)

# Predict on test set
y_pred = forest.predict(X_test)

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Calculate recall
recall = recall_score(y_test, y_pred)

# Calculate F1 score
f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(conf_matrix)
print("Recall:", recall)
print("F1 Score:", f1)
