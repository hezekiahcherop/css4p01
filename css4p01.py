
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'movie_dataset.csv'
movies_df = pd.read_csv(file_path)

# Replace spaces in column names with underscores
movies_df.columns = movies_df.columns.str.replace(' ', '_')

# Summary statistics
summary_stats = movies_df.describe()

# Count of unique values in certain columns
unique_counts = movies_df[['Title',	'Genre', 'Description', 'Director', 'Actors', 'Year', 'Runtime_(Minutes)', 'Rating', 'Votes', 'Revenue_(Millions)', 'Metascore'
]].nunique()

# Average duration of movies
average_duration = movies_df['Runtime_(Minutes)'].mean()
average_Revenue = movies_df['Revenue_(Millions)'].mean()

# Top 5 movies with the highest revenue
top_revenue_movies = movies_df.nlargest(5, 'Revenue_(Millions)')
top_rated_movies = movies_df.nlargest(5, 'Rating')
specific_year = 2016

# Select movies from a specific year, 2016
#selected_movies_2016 = movies_df[movies_df['Year'] == 2016]
movies_in_specific_year = movies_df[movies_df['Year'] == specific_year]

# Count the number of movies in the selected year
#num_movies_2016 = selected_movies_2016.shape[0]
num_movies_in_specified_year = len(movies_in_specific_year)

# Filter movies from 2015 to 2017
selected_movies = movies_df[(movies_df['Year'] >= 2015) & (movies_df['Year'] <= 2017)]

# Calculate the average revenue
average_revenue_2015_to_2017 = selected_movies['Revenue_(Millions)'].mean()

# Movies directed by Christopher Nolan
nolan_movies = movies_df[movies_df['Director'] == 'Christopher Nolan']

# Count the number of movies directed by Christopher Nolan
num_nolan_movies = nolan_movies.shape[0]

#Number of movies with rating of at least 8.0
Movies_8 = movies_df[movies_df['Rating'] >= 8]
num_Movies_8 = Movies_8.shape[0]

average_rating_by_year = movies_df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

# Count the number of movies for 2006 and 2016
num_movies_2006 = movies_df[movies_df['Year'] == 2006].shape[0]
num_movies_2016 = movies_df[movies_df['Year'] == 2016].shape[0]

# Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

# Calculate the median rating of movies directed by Christopher Nolan
median_rating_nolan_movies = nolan_movies['Rating'].median()

all_actors = [actor.split(', ') for actor in movies_df['Actors']]
all_actors_flat = [actor for sublist in all_actors for actor in sublist]

# Count the occurrences of each actor
actor_counts = pd.Series(all_actors_flat).value_counts()

# Find the most common actor
most_common_actor = actor_counts.idxmax()
count_most_common_actor = actor_counts.max()

num_unique_genres = movies_df['Genre'].nunique()

# Filter out missing values in 'Year', 'Rating', and 'Genre'
filtered_movies_df = movies_df.dropna(subset=['Year', 'Rating', 'Genre'])

# Create a scatter plot
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Year', y='Rating', hue='Genre', data=filtered_movies_df, palette='viridis', s=100)

plt.title('Scatter Plot of Rating vs. Year by Genre')
plt.xlabel('Year')
plt.ylabel('Rating')

plt.legend(title='Genre', bbox_to_anchor=(1, 1))

# Show the plot
plt.show()


# Print or use the insights as needed
print("\nAverage Duration of Movies:", average_duration)
print("\nTop 5 Movies with Highest Revenue:\n", top_revenue_movies)
print("\nTop 5 Movies with Highest Rating:\n", top_rated_movies)
print("\nNumber of movies released in 2016: ", num_movies_in_specified_year)
print(f"\nAverage revenue of movies from 2015 to 2017: {average_revenue_2015_to_2017:.2f} million")
print("\nNumber of movies directed by Christopher Nolan: ", num_nolan_movies)
print("\nNumber of movies with rating of at least 8.0: ", num_Movies_8)
print(f"\nMedian rating of movies directed by Christopher Nolan: {median_rating_nolan_movies:.2f}")
print("\nYear with the highest average rating: ", year_highest_average_rating)
print(f"\nHighest average rating: {highest_average_rating:.2f}")
print(f"\nPercentage increase in the number of movies between 2006 and 2016: {percentage_increase:.2f}%")
print("\nMean Revenue: ", average_Revenue)
print(f"\nMost common actor in all movies: {most_common_actor} (appeared in {count_most_common_actor} movies)")
print(f"\nNumber of unique genres in the dataset: {num_unique_genres}")