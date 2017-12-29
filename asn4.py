import matplotlib.pylab as plt
import numpy as np
import csv

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
#call functions
def part2():
    loaddata()
    scatter()
    pie()
    
    srv()
    
    knn()
    kmean()
    
    
    
    

def loaddata():
#load data
    dataset = pd.read_csv('nba.csv')
    return dataset

def pie():
    with open('nba.csv','rU') as csvfile:
        reader = csv.reader(csvfile)
        po= [row[3] for row in reader]
        del po[0]
        pg=po.count('PG')
        sg=po.count('SG')
        sf=po.count('SF')
        pf=po.count('PF')
        c=po.count('C')
        
        
        labels = 'PG', 'SG', 'SF', 'PF', 'C'
        sizes = [pg, sg, sf, pf, c]
        explode = (0, 0, 0, 0, 0)  
# only "explode" the 2nd slice 

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
        ax1.axis('equal')  
# Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()

def scatter():
    
# row[27]means salary        
    with open('nba.csv','rU') as csvfile:
        reader = csv.reader(csvfile)
        sal= [row[27] for row in reader] 
        del sal[0]
        #sal2 = map(int, sal)
        sal2=np.array(sal)
# row[6]means FG
    with open('nba.csv','rU') as csvfile:    
        reader = csv.reader(csvfile)
        mp =[row[6] for row in reader]
        del mp[0]
        mp=np.array(mp)
       
    plt.scatter(mp, sal2)
    plt.title('Scatter plot')
    plt.ylabel('Salary')
    plt.xlabel(' FG ')
  
def srv():

# Importing the dataset
    b=loaddata()
    X = b.iloc[:, 5:6].values
    y = b.iloc[:, 27].values
    
# Splitting the dataset into the Training set and Test set
    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
    
    sc_X = StandardScaler()
    sc_y = StandardScaler()
    X = sc_X.fit_transform(X)
    y = sc_y.fit_transform(y)

# Fitting SVR to the dataset
    from sklearn.svm import SVR
    regressor = SVR(kernel = 'rbf')
    regressor.fit(X, y)
 
# Predicting a new result
    y_pred = regressor.predict(6.5)
    y_pred = sc_y.inverse_transform(y_pred)

# Visualising the SVR results
    plt.scatter(X, y, color = 'red')
    plt.plot(X, regressor.predict(X), color = 'blue')
    plt.title('(SVR)')
    plt.xlabel('Average Point')
    plt.ylabel('Salary')
    plt.show()

# Visualising the SVR results (for higher resolution and smoother curve)
    X_grid = np.arange(min(X), max(X), 0.01) # choice of 0.01 instead of 0.1 step because the data is feature scaled
    X_grid = X_grid.reshape((len(X_grid), 1))
    plt.scatter(X, y, color = 'red')
    plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
    plt.title('(SVR)')
    plt.xlabel('Average Point')
    plt.ylabel('Salary')
    plt.show()
    
   
def knn():
    #Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
    b=loaddata()
    
    X = b.iloc[:, 5:7].values
    y = b.iloc[:, 27].values
    
# Create KNeighbors classifier object model 

    knn = KNeighborsClassifier(n_neighbors=6) # default value for n_neighbors is 5

# Train the model using the training sets and check score
    
    knn.fit(X, y)

#Predict Output
    print knn.predict([[1.2,32333]])
    #print(knn.predict_proba([[  ]]))
   
    
def kmean():
    b=loaddata()
    #X = b.iloc[:, 5].values
    y = b.iloc[:, 20:22].values
    
#Assumed you have, X (attributes) for training data set and x_test(attributes) of test_dataset

# Create KNeighbors classifier object model 

    k_means = KMeans(n_clusters=1, random_state=0)

# Train the model using the training sets and check score

    k_means.fit(y)
    k_means.labels_
    # input test data
    k_means.predict([[4.6, 5.4]])
    print k_means.cluster_centers_
    print k_means.score(y)
    print k_means.transform(y)
