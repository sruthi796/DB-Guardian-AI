import pandas as pd
import time
import numpy as np
from sklearn.linear_model import LinearRegression

def predict_metric(df, column_name):
    recent = df.tail(10)
    X = np.array(range(len(recent))).reshape(-1, 1)
    y = recent[column_name].values
    model = LinearRegression().fit(X, y)
    # Predict where the metric will be in 5 seconds
    return model.predict([[15]])[0]

def run_guardian():
    print("🛡️ Guardian watching all metrics...")
    while True:
        try:
            df = pd.read_csv("db_metrics.csv")
            if len(df) > 10:
                cpu_pred = predict_metric(df, 'cpu_usage')
                lat_pred = predict_metric(df, 'query_latency')
                
                print(f"--- Predictions ---")
                print(f"CPU Next: {round(cpu_pred, 1)}% | Latency Next: {round(lat_pred, 1)}ms")
                
                if cpu_pred > 85 or lat_pred > 100:
                    print("🚨 ALERT: Critical trend detected in system vitals!")
        except:
            pass 
        time.sleep(2)

if __name__ == "__main__":
    run_guardian()