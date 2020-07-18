# Basically, the main purpose of this project to check the quality of red_wine_quality i.e. is it best or not.
#Import relevant libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

def prediction(fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH	,sulphates,alcohol):
	#Load Dataset
	df = pd.read_csv(r"C:\Users\preet\Downloads\Datasets (1)\final data set\Red_Wine.csv")

	df1 =df.rename(columns={'fixed acidity':'fixed_acidity','volatile acidity':'volatile_acidity','citric acid':'citric_acid','residual sugar':'residual_sugar','free sulfur dioxide':'free_sulfur_dioxide','total sulfur dioxide':'total_sulfur_dioxide'})

	df1['quality'].unique()

	df.quality.value_counts().sort_index()

	conditions = [
	    (df1['quality'] >= 7),
	    (df1['quality'] <= 4),
	]
	rating = ['Superior','Inferior']
	df1['rating'] = np.select(conditions,rating, default = 'Fine')
	df1.rating.value_counts()


	X = df1.drop(['rating','quality'],axis = 1)


	y = df1['rating']


	# Import library for Train_Test_Split
	# Now we have to split the data into Train and Test

	from sklearn.model_selection import train_test_split

	X_train,X_test,y_train,y_test = train_test_split(X,y ,test_size=0.2)

	# First We need to import required packages

	from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
	from sklearn.svm import SVC


	svc_cl = SVC()
	svc_cl.fit(X_train,y_train)
	y_pred = svc_cl.predict(X_test)
	accuracy_score(y_test,y_pred)


	from sklearn.ensemble import RandomForestClassifier

	rf_cl = RandomForestClassifier()
	rf_cl.fit(X_train,y_train)
	y_rf = rf_cl.predict(X_test)
	accuracy_score(y_test,y_rf)

	return rf_cl.predict([[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]])
  














