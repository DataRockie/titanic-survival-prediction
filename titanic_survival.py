import numpy as np
import pandas as pd

from titanic_visualizations import survival_stats

titanic_data = pd.read_csv('titanic_data.csv')
print titanic_data.head()

##storing the survived feature
survived_real = titanic_data['Survived']
data_left = titanic_data.drop('Survived', axis = 1)
##data after survived feature removed
print data_left.head()

##accuracy score
def accuracy_score(true, prediction):
    if len(true) == len(prediction):
           return "accuracy of prediction is {:.2f}%.".format((true == prediction).mean()*100)
    else:
           print "Number of prediction does not match the number of outcomes"
##Out of the first five passengers, if we predict that all of them survived, what would you expect the accuracy of our predictions to be?
predictions = pd.Series(np.ones(5, dtype=int))
print"accuracy that out of first 5 all passangers survived:", accuracy_score(survived_real[:5], predictions)

##how accurate would a prediction be that none of the passengers survived?
def predictions_0(data):
   

    predictions = []
    for _, passenger in data.iterrows():
        
        # Predict the survival of 'passenger'
        predictions.append(0)
    
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions|
predictions = predictions_0(data_left)

print "accuracy if no passanger survived:", accuracy_score(survived_real, predictions)

##passanger survival statistics with 'sex' feature
survival_stats(data_left, survived_real, 'sex')

##prediction that the female survive
def predictions_1(data):
    """ Model with one feature: 
            - Predict a passenger survived if they are female. """
    
    predictions = []
    for _, passenger in data.iterrows():
        
        # Remove the 'pass' statement below 
        # and write your prediction conditions here
        if (passenger['Sex'] == 'female'):
            predictions.append(1)
        else:
            predictions.append(0)
    
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_1(data_left)
print "accuracy score that female survived and all others passangers not", accuracy_score(survived_real, predictions)

##Passanger survival statictics with 'Fare' Feature
survival_stats(data_left, survived_real, 'Fare', ["Sex == 'female'"])

## Making prediction with multiple features
def predictions_3(data):
    """ Model with multiple features. Makes a prediction with an accuracy of at least 80%. """
    
    predictions = []
    for _, passenger in data.iterrows():
        
        # Remove the 'pass' statement below 
        # and write your prediction conditions here
        if passenger['Age'] < 12:
            predictions.append(1)
        else:
            if passenger['Sex'] == 'male':
                predictions.append(0)
            else:
                predictions.append(1 if passenger['Pclass'] < 3 or passenger['Fare'] < 20 else 0)
    
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_3(data_left)

print accuracy_score(survived_real, predictions)