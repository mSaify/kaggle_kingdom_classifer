# kaggle_kingdom_classifer

Identify the evolutionary origins (Kingdom) of these organisms. 
https://www.kaggle.com/c/iith-aml-hackathon-2020/overview

### Attempt_Hackathon.ipynb
contains feature engineering and different trained models and their classification reports.


### utils_processing
creates new_train.csv from Train.csv by adding kingdom_float columns.



## Models
```
Extra Tree Classifier
Random Forest Classifier
XG_BOOST Classifier
Logistic Regression Classifier
SVM Classifier
```

##  Result

Best result on validation set was obtained using **SVM classifier**
 
training parameters


```
{
    'kernel':['rbf'],
     'tol': [0.00001,0.000001,0.000001],
     'C': [1,10,100],
     'max_iter': [3000],
     'decision_function_shape': ['ovo'],
     'gamma':['auto'],
     'class_weight': [ {
         0:5,
         1:0.25,
         2:0.25,
         3:0.25,
         4:0.25,
         5:0.5,
         6:0.5,
         7:5,
         8:5,
         9:5} ]
     }
```

classification report

```
              precision    recall  f1-score   support

         0.0       0.57      0.33      0.42        12
         1.0       0.93      0.95      0.94       104
         2.0       0.89      0.91      0.90       155
         3.0       0.91      0.93      0.92       174
         4.0       0.87      0.88      0.87       129
         5.0       0.82      0.82      0.82        76
         6.0       0.83      0.80      0.81        30
         7.0       0.62      0.57      0.59        14
         8.0       0.75      0.67      0.71         9
         9.0       1.00      0.62      0.77         8

    accuracy                           0.88       711
   macro avg       0.82      0.75      0.78       711
weighted avg       0.87      0.88      0.88       711

```