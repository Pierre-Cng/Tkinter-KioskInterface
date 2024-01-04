import pandas as pd
import time
import os 

def read(filename):
    try:
        while True:
            df = pd.read_csv(filename)  # Read the CSV file into a DataFrame
            last_100 = df.tail(100)  # Retrieve the last 100 rows
            print('\n'.join(last_100.apply(lambda row: ', '.join(map(str, row)), axis=1)))
            time.sleep(0.1)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

file_to_read = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.csv')
read(file_to_read)
