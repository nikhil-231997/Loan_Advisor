#http://localhost:8000/loan/predict/?account_balance=1&duration=1&prev_payment_status=2&purpose=3&credit_amount=1&value_savings=2&length_current_employment=3&instalment_percent=1&sex_and_marital_status=2&guarantors=3&duration_current_add=1&most_valuable_asset=2&age=3&concurrent_credits=1&type_of_apartment=2&no_of_credits=3&occupation=1&no_of_dependents=2&telephone=3&foreign_worker=1
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from django.http import JsonResponse
import json

# Create your views here.
def find_creditability(request):
    account_balance = request.GET['account_balance']
    duration = request.GET['duration']
    prev_payment_status = request.GET['prev_payment_status']
    purpose = request.GET['purpose']
    credit_amount = request.GET['credit_amount']
    value_savings = request.GET['value_savings']
    length_current_employment = request.GET['length_current_employment']
    instalment_percent = request.GET['instalment_percent']
    sex_and_marital_status = request.GET['sex_and_marital_status']
    guarantors = request.GET['guarantors']
    duration_current_add = request.GET['duration_current_add']
    most_valuable_asset = request.GET['most_valuable_asset']
    age = request.GET['age']
    concurrent_credits = request.GET['concurrent_credits']
    type_of_apartment = request.GET['type_of_apartment']
    no_of_credits = request.GET['no_of_credits']
    occupation = request.GET['occupation']
    no_of_dependents = request.GET['no_of_dependents']
    telephone = request.GET['telephone']
    foreign_worker = request.GET['foreign_worker']

    df = pd.read_csv('E:\Loan Advisor\german_credit_final.csv')
    numeric_data = df[['Duration of Credit (month)', 'Credit Amount', 'Age (years)']]

    # print(numeric_data)

    min_max_scaler = MinMaxScaler()
    ##We can use min_max_scaler.fit() and then use min_max_scaler.transform().Advantage:fit() stores the min and max value and hence can use it later.
    scaled = min_max_scaler.fit_transform(numeric_data)
    df_numeric_data = pd.DataFrame({'Duration': scaled[:, 0], 'Amt': scaled[:, 1], 'Age': scaled[:, 2]})

    # print(df_numeric_data.describe())

    # print(df_numeric_data)
    # plt.figure()
    # plt.boxplot([df_numeric_data['Duration'],df_numeric_data['Amt'],df_numeric_data['Age']])
    # plt.show()
    X = df.iloc[:, 1:]
    y = df['Creditability']
    # print(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=41)

    clf_etropy = DecisionTreeClassifier(criterion='entropy', random_state=100)
    clf_etropy.fit(X_train, y_train)


    creditability = clf_etropy.predict([[account_balance,duration,prev_payment_status,purpose,credit_amount,value_savings,length_current_employment,instalment_percent,sex_and_marital_status,guarantors,duration_current_add,most_valuable_asset,age,concurrent_credits,type_of_apartment,no_of_credits,occupation,no_of_dependents,telephone,foreign_worker]])
    data = {
        'creditability':str(creditability[0])
    }
    # result = json.dumps(data)
    # print(clf_etropy.score(X_test, y_test))
    #
    # tree.export_graphviz(clf_etropy,out_file='tree.dot')
    #
    # dot_data = StringIO()
    # tree.export_graphviz(clf_etropy,out_file=dot_data)
    # graph = pydot.graph_from_dot_data(dot_data.getvalue())
    return JsonResponse(data,safe=False)