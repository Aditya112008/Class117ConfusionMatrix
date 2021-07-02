from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

actual_data = ["Not Sick", "Sick", "Not Sick", "Not Sick", "Sick", "Sick", "Not Sick", "Not Sick", "Not Sick", "Not Sick", "Not Sick", "Not Sick"]
predicted_data = ["Not Sick", "Sick", "Not Sick", "Not Sick", "Not Sick", "Sick", "Not Sick", "Sick", "Not Sick", "Not Sick", "Sick", "Not Sick"]
labels = ["Not Sick", "Sick"]   

cm = confusion_matrix(actual_data, predicted_data, labels)

ax= plt.subplot()
sns.heatmap(cm, annot=True, ax = ax)

ax.set_xlabel('Predicted')
ax.set_ylabel('Actual') 
ax.set_title('Confusion Matrix')
ax.xaxis.set_ticklabels(labels); ax.yaxis.set_ticklabels(labels)

plt.show()
# Correct Predictions = Actual (Not Sick) , Predicted (Not Sick) = 7 
# Correct Predictions = Actual (Sick) , Predicted (Sick) = 2
# Accuracy = 2 + 7 / 2 + 7 + 1 + 2
accuracy = (2 + 7 )/ (2 + 7 + 2 + 1 )
print(accuracy)

# accuracy = 9 / 12
# accuracy = 0.75
