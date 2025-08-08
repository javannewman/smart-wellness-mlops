import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn

df = pd.read_csv("data/wellness_data.csv")
X = df[["heart_rate", "sleep_hours", "steps"]]
y = df["wellness_score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)

mlflow.set_tracking_uri("file:///mlruns")

with mlflow.start_run():
    mlflow.log_metric("r2_score", score)
    mlflow.sklearn.log_model(model, "model")
    joblib.dump(model, "models/model.joblib")
