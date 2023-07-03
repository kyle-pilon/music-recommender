import os
import json
import pandas as pd

# Function to load a single JSON file
def load_single_file(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data

# Function to load all JSON files in a directory
def load_all_files(directory_path):
    data_list = []
    # os.walk generates the file names in a directory tree
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # check if file is a JSON file
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                data = load_single_file(file_path)
                data_list.append(data)
    # Convert the list of dictionaries into a DataFrame
    df = pd.DataFrame(data_list)
    return df

# Load all data
df = load_all_files('C:\\Users\\pilonk\\projects\\music-recommender\\lastfm_subset')

# Print the first few rows of the DataFrame
print(df.head())
