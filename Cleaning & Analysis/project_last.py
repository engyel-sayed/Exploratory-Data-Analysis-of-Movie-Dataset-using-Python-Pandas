# import pandas
import pandas as pd
# read dataset
df = pd.read_csv('Exploratory-Data-Analysis-of-Movie-Dataset-using-Python-Pandas\\Data Set\\movies.csv')
# clean duplicates
df = df.drop_duplicates()
# clean missing value in title , rating
df = df.dropna(subset=['movie_title','tomatometer_rating']) 
# convert missing to nan and delete it
df['tomatometer_rating'] = pd.to_numeric(df['tomatometer_rating'], errors = 'coerce') 
df = df.dropna(subset=['tomatometer_rating']) 
# convert missing to date
df['original_release_date'] = pd.to_datetime(df['original_release_date'],errors = 'coerce')
#convert to num, error set to Nan
df['runtime'] = pd.to_numeric(df['runtime'], errors = 'coerce') 
#fill missing with unknown
df['genres'] = df['genres'].fillna('unknown')
#fill missing with unknown
df['directors'] = df['directors'].fillna('unknown')
#fill missing with unknown
df['critics_consensus'] = df['critics_consensus'].fillna('unknown')

####################################################################################################



# 1. Top 10 highest-rated movies

top_movies = df.sort_values(by='tomatometer_rating', ascending=False).head(10)
# print(top_movies[['movie_title','tomatometer_rating']].reset_index(drop=True))




##########################################################################################



#2. Count of movies per genre with pandas

count = df['genres'].value_counts()
# print(count)


##########################################################################################



# 3. Filter movies released before 2000

old_movies = df[df['original_release_date']<'2000-01-01']
# print(old_movies[['movie_title','original_release_date']])


##########################################################################################


# 4. Movies with rating above average

avg_rating = df['tomatometer_rating'].mean()
above_avg = df[df['tomatometer_rating']> avg_rating]
# print(above_avg[['movie_title','tomatometer_rating']])


##########################################################################################


# 5. Director with highest average rating

director_avg = df.groupby('directors')['tomatometer_rating'].mean()
top_director = director_avg.sort_values(ascending=False).head(1)
# print(top_director)


##########################################################################################



# 6. Count reviews > 100 characters

long_review = df[df['critics_consensus'].str.len() > 100]
count_review = long_review.shape[0]
# print(count_review)



##########################################################################################



# 7. Avg rating per year (group by year)

df['year'] = df['original_release_date'].dt.year
year = df.groupby('year')['tomatometer_rating'].mean()
# print(year)



##########################################################################################


# 8. Count movies for each individual genre (split multiple genres)

genre_counts = df['genres'].str.split(r',|&').explode().str.strip().value_counts()
# print(genre_counts)


##########################################################################################


# Bouns:--------------------------------

# 9. Compare average rating of long vs. short movies (>120 mins)

df['length_category'] = df['runtime'].apply(lambda x: 'Long' if x > 120 else 'Short')
avg_ratings = df.groupby('length_category')['tomatometer_rating'].mean()
# print(avg_ratings)

##########################################################################################


# 10. Top-rated movie per genre

df['genre_temp'] = df['genres'].str.split(r',|&')
df_exploded = df.explode('genre_temp')
df_exploded['genre_temp'] = df_exploded['genre_temp'].str.strip()
top_movies_per_genre = df_exploded.loc[df_exploded.groupby('genre_temp')['tomatometer_rating'].idxmax()]
# print(top_movies_per_genre[['genre_temp','movie_title','tomatometer_rating']])


# CLI
# - Build a CLI to filter and display results
def filter():
    print('\n Filter options:')
    print('1. Top 10 highest-rated movies')
    print('2. Count of movies per genre')
    print('3. Filter movies released before 2000')
    print('4. Movies with rating above average')
    print('5. Director with highest average rating')
    print('6. Count reviews > 100 characters')
    print('7. Avg rating per year (group by year)')
    print('8. Count movies for each individual genre (split multiple genres)')
    print('9. Compare average rating of long vs. short movies (>120 mins)')
    print('10. Top-rated movie per genre')
    choice = int (input('Enter your choice (1-10):'))
    if choice ==1:
        print(top_movies[['movie_title','tomatometer_rating']].reset_index(drop=True))
    elif choice ==2:
        print(count) 
    elif choice == 3:
        print(old_movies[['movie_title','original_release_date']])
    elif choice == 4:
        print(above_avg[['movie_title','tomatometer_rating']])
    elif choice == 5:
        print(top_director)
    elif choice == 6:
        print(count_review)
    elif choice == 7:
        print(year)
    elif choice == 8:
        print(genre_counts)
    elif choice ==9:
        print(avg_ratings)
    elif choice == 10:
        print(top_movies_per_genre[['genre_temp','movie_title','tomatometer_rating']]) 
    else:
        print('invalid choice, please enter number between 1& 10')
filter()