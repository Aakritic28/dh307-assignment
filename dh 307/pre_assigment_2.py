import pandas as pd
import matplotlib.pyplot as plt

file_path = '2023_2024_score_bins.csv'
data = pd.read_csv(file_path)

data_2023 = data[data['year'] == 2023]
data_2024 = data[data['year'] == 2024]


grouped_2023 = data_2023.groupby('score_bin')['frequency'].sum().reset_index()
grouped_2024 = data_2024.groupby('score_bin')['frequency'].sum().reset_index()


merged_data = pd.merge(grouped_2023, grouped_2024, on='score_bin', suffixes=('_2023', '_2024'))

# Plotting
plt.figure(figsize=(14, 7))
plt.plot(merged_data['score_bin'], merged_data['frequency_2023'], marker='o', label='2023')
plt.plot(merged_data['score_bin'], merged_data['frequency_2024'], marker='o', label='2024')
plt.title('Comparative Distribution of NEET-UG Scores for 2023 and 2024')
plt.xlabel('Score Bin')
plt.ylabel('Number of Students')
plt.legend()
plt.grid(True)
plt.show()

