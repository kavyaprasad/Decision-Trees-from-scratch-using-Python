import decision_tree as dtree
import random
import os.path
import matplotlib.pyplot as plt

Accuracy_list=[]
Depth_list = []

# we are trying to input the Train, test file and the delimiter 
while True:
    file_name = input('Enter the train file name: ')
    train_file_path = 'datasets/' + file_name.strip()
    if os.path.exists(train_file_path):
        break
    else:
        print("Specified file doesn't exist in the 'datasets' directory.\n"
              "Please ensure that 'datasets' directory exists in the same\n"
              "directory as this script is and the file is present in the \n"
              "'datasets' directory")
while True:
    file_name = input('Enter the test file name: ')
    test_file_path = 'datasets/' + file_name.strip()
    if os.path.exists(train_file_path):
        break
    else:
        print("Specified file doesn't exist in the 'datasets' directory.\n"
              "Please ensure that 'datasets' directory exists in the same\n"
              "directory as this script is and the file is present in the \n"
              "'datasets' directory")

delim = input('Enter the delimiter to be used for reading the file:: ')
if not delim:
    delim = ','
    print('Nothing has been entered, defaulted to ","')

def plot_graph():
 plt.title("Learning curve")
 plt.xlabel("depth")
 plt.ylabel("accuracy")
 plt.plot( Depth_list ,  Accuracy_list ) 
 plt.show()
#This method parses the file and returns the dataset
def parse_file(file_path): 
    f = open(file_path, 'r')
    file_data = []
    for line in f.readlines():
        line_strip = line.strip('\n').split(delim)
        rowData = []
        for value in line_strip:
            try:
                rowData.append(float(value))
            except:
                rowData.append(value)
        file_data.append(rowData)
    f.close()
    return file_data

tot_count = 0
tot_correct = 0

train_data = parse_file(train_file_path)
test_data = parse_file(test_file_path)

#Calculating the Accuracy at every level 
correct = 0
total =0
TP = 0
TN = 0
FP = 0
FN = 0
depth = 0
for i in range (1,7):
    tree = dtree.buildtree(train_data,0,i)
    for data in test_data:
        predicted = list(dtree.decision(tree,data).keys())[0]
        actual = data[-1]
        total = total +1 
        if predicted == 1.0 and actual == 1.0:
            correct = correct + 1
            TP = TP + 1
        if predicted == 0.0 and actual == 0.0:
            correct = correct + 1
            TN = TN + 1
        if predicted == 1.0 and actual == 0.0:
            FP = FP+ 1
        if predicted == 0.0 and actual == 1.0:
            FN = FN + 1
    tot_correct += correct
    tot_count += total
    Accuracy = round(100*correct/total,2)
    Depth_list.append(depth)
    depth=depth+1
    print (Accuracy_list)
    print (Depth_list)
    #printing the confusion matrix
    print("Accuracy::",str(Accuracy)+'%')
    print("False Negatives ", str(FN))
    print("False positives ", str(FP))
    print("True Negatives ", str(TN))
    print("True Positives ", str(TP))
    print("Confusion Matrix")
    print("------")
    print("| ", TP , "|", FN, "|")
    print("------")
    print("| ", FP , "|", TN, "|")
    print("------")
plot_graph()      
