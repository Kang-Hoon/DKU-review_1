from sklearn.linear_model import LinearRegression

X = [1,2,3,4,5] 
Y = [1,3,5,7,9]

model = LinearRegression()
model.fit(X, Y)

X_predict = []  # put the dates of which you want to predict kwh here
Y_predict = model.predict(X_predict)
