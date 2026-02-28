import pandas as pd
import random
import time
import os

def run_simulator():
    file = "db_metrics.csv"
    # Headers for all your metrics
    columns = ['timestamp', 'cpu_usage', 'query_latency', 'memory_usage']
    
    if not os.path.exists(file):
        pd.DataFrame(columns=columns).to_csv(file, index=False)

    print("🚀 Simulator Started. Logging all metrics to CSV...")
    while True:
        now = time.strftime('%H:%M:%S')
        cpu = round(random.uniform(20, 45), 2)
        # Random spike for testing
        if random.random() > 0.95: cpu = round(random.uniform(85, 98), 2)
        
        latency = round(random.uniform(5, 15), 2)  # in milliseconds
        memory = round(random.uniform(40, 60), 2)   # in percentage
        
        # Save all data points at once
        new_row = pd.DataFrame([[now, cpu, latency, memory]], columns=columns)
        new_row.to_csv(file, mode='a', header=False, index=False)
        
        print(f"[{now}] CPU: {cpu}% | Latency: {latency}ms | Mem: {memory}%")
        time.sleep(1)

if __name__ == "__main__":
    run_simulator()