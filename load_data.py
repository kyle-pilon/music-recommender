import os
import json
import pandas as pd

def load_single_file(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data

def load_all_files(directory_path):
    data_list = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                data = load_single_file(file_path)
                data_list.append(data)
    df = pd.DataFrame(data_list)
    return df

# Load all data
df = load_all_files('C:\\Users\\pilonk\\projects\\music-recommender\\lastfm_subset')

# Save the DataFrame to a CSV file
df.to_csv('C:\\Users\\pilonk\\projects\\music-recommender\\data.csv', index=False)

print("Data successfully saved to 'data.csv'")
