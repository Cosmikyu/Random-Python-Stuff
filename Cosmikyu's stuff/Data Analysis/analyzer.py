import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the data from CSV
csv_file = 'bbc_news_data.csv'  # Replace with the path to your CSV file
data = pd.read_csv(csv_file)

# Step 2: Basic Data Exploration
print("First few rows of the dataset:")
print(data.head())

print("\nSummary statistics of the dataset:")
print(data.describe())

print("\nInformation about the dataset:")
print(data.info())

# Step 3: Data Analysis

# Example 1: Count the number of articles per author
articles_per_author = data['author'].value_counts()
print("\nNumber of articles per author:")
print(articles_per_author)

# Example 2: Most frequent words in titles (simple example)
from collections import Counter
import re

def get_most_frequent_words(text_series, num_words=10):
    all_words = ' '.join(text_series).lower()
    all_words = re.findall(r'\b\w+\b', all_words)
    return Counter(all_words).most_common(num_words)

most_frequent_words = get_most_frequent_words(data['title'])
print("\nMost frequent words in titles:")
print(most_frequent_words)

# Example 3: Number of articles over time
# Assuming the 'date' column is in a recognizable date format
data['date'] = pd.to_datetime(data['date'])
articles_over_time = data.set_index('date').resample('M').size()

# Step 4: Data Visualization

# Visualization 1: Articles per Author
plt.figure(figsize=(10, 6))
sns.barplot(x=articles_per_author.values, y=articles_per_author.index)
plt.title('Number of Articles per Author')
plt.xlabel('Number of Articles')
plt.ylabel('Author')
plt.show()

# Visualization 2: Articles Over Time
plt.figure(figsize=(10, 6))
articles_over_time.plot()
plt.title('Number of Articles Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.show()