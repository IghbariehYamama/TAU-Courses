import csv

csv_file = 'netflix_titles.csv'
file = open(csv_file, encoding='utf-8-sig')
csv_reader = csv.reader(file)
header = next(csv_reader)

""""

This function reads data from a CSV file containing information about movies and prepares it to be inserted into the database.
It extracts details such as movie title, director, cast, country, listed categories, release year, rating, duration, and description.
Returns: A list containing lists of movie details categorized by type, directors, cast, countries, and listed categories.

"""
def prepare_data():
  MOVIES = []
  DIRECTORS = []
  COUNTRY = []
  CAST = []
  LISTED_IN = []
  count_movies = 0
  for row in csv_reader:

    """
    If there are null values in the title, release_year, rating, duration, or description columns, we do not insert them. 
    We have defined these columns in our tables to not be null.
    """
    if row[1] != "Movie" or '' in [row[6], row[7], row[8], row[9], row[11]]:
      continue
    count_movies += 1

    # for movies
    movie = [0]*6
    movie[0] = count_movies
    movie[1] = row[2]
    movie[2] = row[7]
    movie[3] = row[8]
    movie[4] = int(row[9][:-4])
    movie[5] = row[11]
    MOVIES.append(movie)

    # for directors
    help_prepare_data(DIRECTORS, row[3], count_movies)

    # for cast
    help_prepare_data(CAST, row[4], count_movies)

    # for country
    help_prepare_data(COUNTRY, row[5], count_movies)

    # for listed_in
    help_prepare_data(LISTED_IN, row[10], count_movies)

  return [MOVIES, DIRECTORS, CAST, COUNTRY, LISTED_IN]


"""
Purpose:
    This function assists in preparing data extracted from a CSV file to be inserted into the database.

Parameters:
    father_list (list): The list to which the prepared data will be appended.
    row_i (str): The data extracted from the CSV row to be processed.
    count_movies (int): The unique identifier of the movie.

Returns:
    None
"""
def help_prepare_data(father_list, row_i, count_movies):
  if row_i != "":
    child_list = row_i.split(", ")
    for name in child_list:
      if name == "":
        continue
      father_list.append([count_movies, name])


"""
Purpose:
    Prepare SQL statements for inserting data into different tables of the database.
    Duplicate entries are ignored.

Returns:
    list: A list containing prepared SQL statements for inserting data into the MOVIES, DIRECTORS, CAST, 
          COUNTRY, and LISTED_IN tables.
"""
def updates():
  """
  SQL statement to insert data into the MOVIES table while ignoring duplicate entries.
  """
  add_movie = (
    "INSERT IGNORE INTO MOVIES"
    "(movie_id, title, release_year, rating, duration, description)"
    " VALUES(%s, %s, %s, %s, %s, %s)")

  """
  SQL statement to insert director data into the DIRECTORS table, ignoring duplicate entries.
  """
  add_director = (
    "INSERT IGNORE INTO DIRECTORS"
    "(movie_id, director_name)"
    " VALUES(%s, %s)")

  """
  SQL statement to insert cast data into the CAST table, ignoring duplicate entries.
  """
  add_cast = (
    "INSERT IGNORE INTO CAST "
    "(movie_id, cast_name)"
    " VALUES(%s, %s)")

  """
  SQL statement to insert country data into the COUNTRY table, ignoring duplicate entries.
  """
  add_country = (
    "INSERT IGNORE INTO COUNTRY"
    "(movie_id, country_name)"
    " VALUES(%s, %s)")

  """
  SQL statement to insert listed category data into the LISTED_IN table, ignoring duplicate entries.
  """
  add_listed_in = (
    "INSERT IGNORE INTO LISTED_IN"
    "(movie_id, listed_in_name)"
    " VALUES(%s, %s)")
  return [add_movie, add_director, add_cast, add_country, add_listed_in]

