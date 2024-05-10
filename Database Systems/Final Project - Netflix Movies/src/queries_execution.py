# Establishes a connection to the MySQL database using the mysql.connector module,
# initializes necessary imports and variables, and creates a cursor object for executing SQL queries.
import mysql.connector
from mysql.connector import errorcode
from create_db_script import TABLES
from api_data_retrieve import prepare_data, updates
from queries_db_script import query_1, query_2, query_3, query_4, query_5, query_6, query_7, query_8, query_9, query_10, query_11, query_12

# Username and password have been deleted for security reasons
cnx = mysql.connector.connect(user='username', password= 'password', host='localhost' , database='db', port=3305)
cursor = cnx.cursor()

"""

Description: This function creates database tables if they do not exist already. 
It iterates through the dictionary TABLES, which contains table names as keys and corresponding SQL table creation statements as values, and executes these SQL statements to create tables in the database.
Output: Prints status messages indicating whether tables were created successfully or if they already existed.

"""
def insert_tables():
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ". format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists")
            else:
                print(err.msg)
        else:
            print("OK")


"""

Description: This function inserts prepared movie data into the respective tables of the database. 
It first checks if there are any existing records in the MOVIES table. 
If there are none, it proceeds to insert data into the MOVIES, DIRECTORS, CAST, COUNTRY, and LISTED_IN tables.
Output: Prints status messages indicating whether data insertion was successful.

"""
def insert_data():
    # Check if there are existing records in the MOVIES table.
    cursor.execute("SELECT COUNT(*) FROM MOVIES")
    result = cursor.fetchone()
    if result[0] > 0:
        print("Inserting data: already exists")
    else:
        print("Inserting data: ")
        for i in range(5):
            # insert data into DB
            for data in res[i]:
                cursor.execute(updates[i], data)
        cnx.commit()
        print("OK")


def example_1(movie_search):
    """
    Purpose:
        Retrieve movie details based on a keyword or phrase in titles or descriptions.

    Parameters:
        movie_search (str): Keyword or phrase to search for in movie titles or descriptions.

    Returns:
        list: A list of lists containing movie details matching the keyword or phrase.
    """

    return help_examples([movie_search], str, query_1())


def example_2(cast_name):
    """
    Purpose:
        Retrieve movie details based on a cast member's name.

    Parameters:
        cast_name (str): Name of the cast member to search for.

    Returns:
        list: A list of lists containing movie details in which the specified cast member appears.
    """

    return help_examples([cast_name], str, query_2())


def example_3():
    """
    Purpose:
        Retrieve all movies directed by the director with the most movies directed.

    Returns:
        list: A list of lists containing movie details directed by the director with the most movies directed.
    """
    return help_examples([], None, query_3())


def example_4(genre):
    """
    Purpose:
        Retrieve the shortest movie in a specified genre.

    Parameters:
        genre (str): Genre for which to find the shortest movie.

    Returns:
        list: A list of lists containing details of the shortest movie in the specified genre.
    """

    # Note: 'genre' parameter is used twice because we search for the specified genre twice in the query.
    return help_examples([genre, genre], str, query_4())


def example_5(country_name):
    """
    Purpose:
        Retrieve the percentage representation of each movie genre in a specific country.

    Parameters:
        country_name (str): Name of the country.

    Returns:
        list: A list of lists containing each movie genre and its corresponding percentage representation.
    """

    return help_examples([country_name], str, query_5())


def example_6():
    """
    Purpose:
        Retrieve detailed information about all movies available on the Netflix platform.

    Returns:
        list: A list of lists containing detailed information about each movie,
        ordered by release year in descending order and title in ascending order.
    """
    return help_examples([], None, query_6())


def example_7(year):
    """
    Purpose:
        Retrieve specific information about movies stored in the database that have a duration shorter than a specified threshold.

    Parameters:
        duration_threshold (int): The maximum duration allowed for the movies to be retrieved.

    Returns:
        list: A list of lists containing movie details meeting the specified duration threshold.
    """

    return help_examples([year], int, query_7())


def example_8(rating):
    """
    Purpose:
        Retrieve specific information about movies stored in the database that match a particular rating.

    Parameters:
        rating (str): The rating of the movies to retrieve.

    Returns:
        list: A list of lists containing movie details matching the specified rating.
    """

    return help_examples([rating], str, query_8())


def example_9(start_year, end_year):
    """
    Purpose:
        Retrieve specific information about movies stored in the database that were released within a specified range of years.

    Parameters:
        start_year (int): The starting year of the range.
        end_year (int): The ending year of the range.

    Returns:
        list: A list of lists containing movie details released within the specified range of years.
    """

    return help_examples([start_year, end_year], int, query_9())


def example_10(director_name):
    """
    Purpose:
        Retrieve specific information about movies stored in the database that were directed by a particular director.

    Parameters:
        director_name (str): The name of the director.

    Returns:
        list: A list of lists containing movie details directed by the specified director.
    """

    return help_examples([director_name], str, query_10())


def example_11(country):
    """
    Purpose:
        Retrieve specific information about movies stored in the database that belong to a particular country.

    Parameters:
        country_name (str): The name of the country.

    Returns:
        list: A list of lists containing movie details produced in the specified country.
    """

    return help_examples([country], str, query_11())


def example_12(genre):
    """
    Purpose:
        Retrieve specific information about movies stored in the database that are listed under a particular genre.

    Parameters:
        genre (str): The name of the genre.

    Returns:
        list: A list of lists containing movie details categorized under the specified genre.
    """

    return help_examples([genre], str, query_12())


"""
Purpose:
    This function executes SQL queries based on provided parameters and the query string.
    It ensures that each parameter in the 'params' list adheres to the specified data type.

Parameters:
    params (list): List of parameters to be used in the SQL query.
    type (type): Data type that each parameter in the 'params' list should adhere to.
    query_i (str): SQL query string to be executed.

Returns:
    list: A list of lists containing the records retrieved from the database.
"""
def help_examples(params, type, query_i):
    # Check if 'params' are of type 'type'
    for param in params:
        if not isinstance(param, type):
            print("Invalid parameter: must be " + str(type)[8:11])
            return

    # Execute the SQL query if parameters are valid
    cursor.execute(query_i, params)
    records = []
    for tup in cursor:
        records.append(list(tup))
    return records


# Initializes database tables, prepares data, and inserts records (Commented out).

#insert_tables()
res = prepare_data()
updates = updates()
#insert_data()

# Functions and examples used in the user manual for retrieving, inserting, and querying movie-related data from the database.

#print(example_1("father"))
#print(example_2("luna"))
#print(example_3())
#print(example_4("Documentaries"))
#print(example_5("Austria"))
#print(example_6())
#print(example_7(90))
#print(example_8("R"))
#print(example_9(2019, 2021))
#print(example_10("Kirsten Johnson"))
#print(example_11("France"))
#print(example_12("Comedies"))

cnx.close()
