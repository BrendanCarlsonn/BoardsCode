from math import e
import pandas as pd
from sklearn import tree
import openpyxl
#Imports for pandas and sklearn and openpyxl

#Find the location of the .xlsx file
xls_data_file = r"Pokemon.xlsx"

#Set the data to df so we can use it later
df = pd.read_excel(xls_data_file)
#Need to set the features for the tree classifer
features = df[['feature_type_1', 'feature_type_2']]
#Need to set the label for the tree classifier
labels = df[['label_number']]
#Create the tree classifier
clf = tree.DecisionTreeClassifier()
#fit the features and labels
clf = clf.fit(features, labels)

#prediction_result = clf.predict([[4, 8]])
#print(df.loc[prediction_result - 1])

#System predict will take the users input and return the prediction for display_prediction
def system_predict():
    prediction_result = clf.predict([[list[0], list[1]]])
    return prediction_result

#Display prediction will display the correct pokemon to the user based on their input. Note that -1 is there because computer start counting at 0
def display_prediction():
    print("The Pokemon you are looking for is:")
    print(df.loc[prediction_result - 1])
#Change prediction takes the user string input and passes it into a int variable based on the pokemon types then returns the variables for system_predict to use
def change_prediction():
    Type1 = input(" What is the first type you would like to search for?\n")
    Type2 = input(" What is the second type you would like to search for? If there is none enter 'None'. \n")

    if Type1 == "Normal":
        type1 = 1
    elif Type1 == "Fire":
        type1 = 2
    elif Type1 == "Water":
        type1 = 3
    elif Type1 == "Grass":
        type1 = 4
    elif Type1 == "Electric":
        type1 = 5
    elif Type1 == "Ice":
        type1 = 6
    elif Type1 == "Fighting":
        type1 = 7
    elif Type1 == "Poison":
        type1 = 8
    elif Type1 == "Ground":
        type1 = 9
    elif Type1 == "Flying":
        type1 = 10
    elif Type1 == "Psychic":
        type1 = 11
    elif Type1 == "Bug":
        type1 = 12
    elif Type1 == "Rock":
        type1 = 13
    elif Type1 == "Ghost":
        type1 = 14
    elif Type1 == "Dark":
        type1 = 15
    elif Type1 == "Dragon":
        type1 = 16
    elif Type1 == "Steel":
        type1 = 17
    elif Type1 == "Fairy":
        type1 = 18
    else:
        print("There is not a matching type.")
        return

    if Type2 == "Normal":
        type2 = 1
    elif Type2 == "Fire":
        type2 = 2
    elif Type2 == "Water":
        type2 = 3
    elif Type2 == "Grass":
        type2 = 4
    elif Type2 == "Electric":
        type2 = 5
    elif Type2 == "Ice":
        type2 = 6
    elif Type2 == "Fighting":
        type2 = 7
    elif Type2 == "Poison":
        type2 = 8
    elif Type2 == "Ground":
        type2 = 9
    elif Type2 == "Flying":
        type2 = 10
    elif Type2 == "Psychic":
        type2 = 11
    elif Type2 == "Bug":
        type2 = 12
    elif Type2 == "Rock":
        type2 = 13
    elif Type2 == "Ghost":
        type2 = 14
    elif Type2 == "Dark":
        type2 = 15
    elif Type2 == "Dragon":
        type2 = 16
    elif Type2 == "Steel":
        type2 = 17
    elif Type2 == "Fairy":
        type2 = 18
    else:
        print("There is not a matching type.")
        return
    
    return type1, type2
#Asks the user if they want to look again
def ask_user():
    user_input = input("Is there another Pokemon you are looking for? Type Y or N\n")
    if user_input == "Y":
        print("Awesome! Go ahead and try as many times as you'd like!")
        x = 1
        return x
    else:
        print("Glad you got everything you needed! Come back if you are ever looking for a pokemon!")
        x = 0
        return x
#x to hold the value for the while loop
x = 1
#While loop to allow the user the choice to continue or not
while (x == 1):
    #list holds the variables in a list
    list = change_prediction()
    # predictio_result holds the data to be displayed
    prediction_result = system_predict()

    display_prediction()
    # need x to equal ask_user to change the x value from inside the function.
    x = ask_user()