import pandas as pd
import numpy as np
import joblib 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

#------------------------------------------------------------------------------
#   Function Name : PreserveModel
#   Discription :   It is used to preserve model an secondary 
#                   traing data, testing data
#   Parameter :     df 
#   Return :        None
#   Date :          14/03/2026
#   Author :        Aryan Pandharinath Dhumal
#------------------------------------------------------------------------------

def LoadPreserveModel(filename):
    Loaded_model = joblib.load(filename)

    print("Model loaded successfully")

    return Loaded_model
#------------------------------------------------------------------------------
#   Function Name : PreserveModel
#   Discription :   It is used to preserve model an secondary 
#                   traing data, testing data
#   Parameter :     df 
#   Return :        None
#   Date :          14/03/2026
#   Author :        Aryan Pandharinath Dhumal
#------------------------------------------------------------------------------

def PreservModel(model, filename):
    joblib.dump(model, filename)

    print("Model preserve successfully with name : ", filename)
    
#------------------------------------------------------------------------------
#   Function Name : TrainTitanicModel
#   Discription :   It does split X, Y, 
#                   traing data, testing data
#   Parameter :     df 
#   Return :        None
#   Date :          14/03/2026
#   Author :        Aryan Pandharinath Dhumal
#------------------------------------------------------------------------------

def TrainTitanicModel(df):
    # Split features and labels
    X = df.drop("Survived", axis = 1)
    Y = df["Survived"]

    print("\nFeatures : ")
    print(X.head())

    print("\nLabels : ")
    print(Y.head())

    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("X_train shape : ", X_train.shape)
    print("X_test shape : ", X_test.shape)
    print("Y_train shape : ", Y_train.shape)
    print("Y_test shape : ", Y_test.shape)

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, Y_train)

    print("Model trained successfully : ")
    print("Value of C are : ", model.intercept_)

    print("\nCoefficient of model : ")
    for feature, coeficent in zip(X.columns, model.coef_[0]):
        print(feature, " : ", coeficent)

    PreservModel(model, "TitanicPreserveFile")

    loaded_model = LoadPreserveModel("TitanicPreserveFile.pkl")

    Y_pred = loaded_model.predict(X_test)

    accuracy = accuracy_score(Y_pred, Y_test)

    print("Accuracy is : ", accuracy)

    cm = confusion_matrix(Y_pred, Y_test)

    print("Confusion matrix is :", cm)

#------------------------------------------------------------------------------
#   Function Name : DisplayInfo
#   Discription :   It Displays the formated title
#   Parameter :     title(str)   
#   Return :        None
#   Date :          14/03/2026
#   Author :        Aryan Pandharinath Dhumal
#------------------------------------------------------------------------------

def DisplayInfo(title):
    print("\n"+"=" * 70)
    print(title)
    print("=" * 70)

#------------------------------------------------------------------------------
#   Function Name : ShowData
#   Discription :   It Shows basic information about dataset
#   Parameter :     df
#                   df ->       Pandas dataframe object 
#                   message
#                   message ->  Heading text display
#   Return :        None
#   Date :          14/03/2026
#   Author :        Aryan Pandharinath Dhumal
#------------------------------------------------------------------------------

def ShowData(df, message):
    DisplayInfo(message)

    print("\nFirst 5 rows of dataset : ")
    print(df.head())

    print("\nShape of dataset : ")
    print(df.shape)

    print("\nColumns names : ")
    print(df.columns.tolist())

    print("\nMissing value in each columns : ")
    print(df.isnull().sum())

#------------------------------------------------------------------------------
#   Function Name : CleanTitanicData
#   Discription :   It does preprocessing
#                   It removed unnecessary columns
#                   It handles missing values
#                   It converts text data to numeric format
#                   It does encoding to categorical columns
#   Parameter :     df
#                   df ->   Pandas dataframe   
#   Return :        df
#                   df ->   clean Pandas dataframe
#   Date :          14/03/2026
#   Author :        Aryan Pandharinath Dhumal
#------------------------------------------------------------------------------

def CleanTitanicData(df):
    DisplayInfo("Step 2 : Original Data")
    print(df.head())

    # Remove Unnecessary columns
    drop_columns = ["Passengerid", "zero", "Name", "cabin"]
    existing_columns = [col for col in drop_columns if col in df.columns]
    # for col in drop_columns:
    #     if col in df.columns:
    #         return col

    print("\ncolumns to be drop")
    print(existing_columns)

    # drop the unwanted columns
    df = df.drop(columns = existing_columns)
    DisplayInfo("Data After Column Removal")
    print(df.head()) 

    # Handle Age column
    if "Age" in df.columns:
        print("Age column before filling missing values")
        print(df["Age"].head(10))

        # coerce -> Invalid value gets converted as NaN
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

        age_median = df["Age"].median()
        print("\nmedian of Age column : ", age_median)


        # Replace missing values with median
        df["Age"] = df["Age"].fillna(age_median)

        print("Age column after preprocessing : ")
        print(df["Age"].head(10))

    # Handle Fare Column
    if "Fare" in df.columns:
        print("\n Fare column before preprocessing")
        print(df["Fare"].head(10))

        df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")

        fare_median = df["Fare"].median()
        print("\nmedian of Fare column : ", fare_median)

        # Replace missing values with median
        df["Fare"] = df["Fare"].fillna(fare_median)

        print("Fare column after preprocessing : ")
        print(df["Fare"].head(10))

    # Handle Embarked column
    if "Embarked" in df.columns:
        print("\n Embarked column before preprocessing")
        print(df["Embarked"].head(10))

        # Convert the data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()

        # Remove missing values
        df["Embarked"] = df["Embarked"].replace(['nan', 'None', ''], np.nan)

        # Get Most frequent value
        embarked_mode = df["Embarked"].mode()[0]
        print("\nmode of embarked column : ", embarked_mode)

        df["Embarked"] = df["Embarked"].fillna(embarked_mode)

        print("\nEmbarked column after preprocessing : ")
        print(df["Embarked"].head(10))
    
    # Handle Sex Column
    if "Sex" in df.columns:
        print("\n Sex column before preprocessing")
        print(df["Sex"].head(10))

        df["Sex"] = pd.to_numeric(df["Fare"], errors="coerce")

        print("Sex column after preprocessing : ")
        print(df["Sex"].head(10))

    DisplayInfo("Data after preprocessing : ")
    print(df.head())

    print("Missing values after preprocessing : ")
    print(df.isnull().sum())

    # Encode Enbarked column

    df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)
    print("\n Data After encoding : ")

    print(df.head())
    
    print("shape of dataset : ", df.shape)

    # convert boolean columns into integer
    for col in df.columns:
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)

    print("\n Data After encoding : ")

    print(df.head())

    return df

#------------------------------------------------------------------------------
#   Function Name : MarvellousTitanicLogistic
#   Discription :   This is main pipeline controller
#                   It loads the dataset, show raw data
#                   It preprocess the dataset & train the model
#   Parameter :     DataPath of Dataset file    
#   Return :        None
#   Date :          14/03/2026
#   Author :        Aryan Pandharinath Dhumal
#------------------------------------------------------------------------------

def TitanicLogistic(Dataset):
    DisplayInfo("Step 1 : Loading the dataset")
    df = pd.read_csv(Dataset)

    ShowData(df, "Initial Dataset")

    df = CleanTitanicData(df)

    TrainTitanicModel(df)



#------------------------------------------------------------------------------
#   Function Name : main
#   Discription :   Starting point of application
#   Parameter :     None    
#   Return :        None
#   Date :          14/03/2026
#   Author :        Aryan Pandharinath Dhumal
#------------------------------------------------------------------------------

def main():
    TitanicLogistic("TitanicDataset.csv")

if __name__ == "__main__":                    
    main()