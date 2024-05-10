
def query_1():
    """
    Retrieve movies based on a keyword or phrase in their titles or descriptions.
    Returns:
        str: SQL query string to select movie details matching the keyword or phrase and sorted by release year in descending order and title in ascending order.
    """
    return "SELECT title, release_year, rating, duration, description " \
           "FROM MOVIES " \
           "WHERE MATCH(title, description) AGAINST (%s IN NATURAL LANGUAGE MODE) " \
           "ORDER BY release_year DESC, title ASC"


def query_2():
    """
    Retrieve movies based on a cast member's name.

    Returns:
        str: SQL query string to select movie details in which the specified cast member appears, ordered by cast name in ascending order and release year in descending order.
    """
    return "SELECT CAST.cast_name, MOVIES.title, MOVIES.release_year, MOVIES.description " \
           "FROM MOVIES " \
           "JOIN CAST ON MOVIES.movie_id = CAST.movie_id " \
           "WHERE MATCH(cast_name) AGAINST (%s IN NATURAL LANGUAGE MODE) " \
           "ORDER BY CAST.cast_name ASC, release_year DESC"


def query_3():
    """
    Retrieve all movies directed by the director with the most movies directed.

    Returns:
        str: SQL query string to select all movies directed by the director with the most movies directed, sorted by release year in descending order.
    """
    return "SELECT d.director_name, m.title, m.release_year, m.rating, m.duration, m.description " \
           "FROM DIRECTORS d " \
           "JOIN (" \
           "SELECT d.director_name, COUNT(m.movie_id) AS num_movies " \
           "FROM DIRECTORS d " \
           "JOIN MOVIES m ON d.movie_id = m.movie_id " \
           "GROUP BY d.director_name " \
           "ORDER BY num_movies DESC " \
           "LIMIT 1" \
           ") best_director ON best_director.director_name = d.director_name " \
           "JOIN MOVIES m ON d.movie_id = m.movie_id " \
           "ORDER BY release_year DESC"


def query_4():
    """
    Retrieve the shortest movie in a specified genre.

    Note:
        The user chooses one genre, and it's used twice in this query.

    Returns:
        str: SQL query string to select the shortest movie in the specified genre.
    """
    return "SELECT m.title, m.duration, m.description " \
           "FROM MOVIES as m JOIN LISTED_IN as li on m.movie_id = li.movie_id " \
           "WHERE li.listed_in_name = %s " \
           "AND m.duration <= ALL (" \
           "SELECT m2.duration " \
           "FROM MOVIES as m2 JOIN LISTED_IN as li2 on m2.movie_id = li2.movie_id " \
           "AND li2.listed_in_name = %s" \
           ")"


def query_5():
    """
    Purpose:
        This query calculates the percentage of each movie genre in a specific country based on the total count of movies in that country.

    Returns:
        str: SQL query string to calculate the percentage of each genre in the specified country.
    """
    return "SELECT li.listed_in_name AS genre, ROUND((COUNT(li.listed_in_name) / total_movies.total_count) * 100, 2) AS percentage " \
           "FROM COUNTRY c " \
           "JOIN LISTED_IN li ON c.movie_id = li.movie_id " \
           "JOIN (" \
           "SELECT country_name, COUNT(movie_id) AS total_count " \
           "FROM COUNTRY " \
           "GROUP BY country_name" \
           ") total_movies ON c.country_name = total_movies.country_name " \
           "WHERE c.country_name = %s " \
           "GROUP BY c.country_name, li.listed_in_name " \
           "ORDER BY percentage DESC"


def query_6():
    """
    Retrieve detailed information about all movies available on the Netflix platform.

    Returns:
        str: SQL query string to select details of all movies from the database, ordered by release year in descending order and title in ascending order.
    """
    return "SELECT title, release_year, rating, duration, description " \
           "FROM MOVIES " \
           "ORDER BY release_year DESC, title ASC"

def query_7():
    """
    Retrieve specific information about movies stored in the database with a duration shorter than a specified threshold.

    Returns:
        str: SQL query string to select movie details with a duration less than the specified value, ordered by duration in descending order.
    """
    return "SELECT title, release_year, rating, duration, description " \
           "FROM MOVIES " \
           "WHERE duration < %s " \
           "ORDER BY duration DESC"


def query_8():
    """
    Purpose: This query retrieves specific information about movies stored in the database that match a particular rating.
    It selects the title, release year, duration, and description of each movie from the "MOVIES" table that corresponds to the specified rating.

    Returns:
        str: SQL query string to select movie details with the specified rating.
    """
    return "SELECT title, release_year, duration, description " \
           "FROM MOVIES " \
           "WHERE rating = %s"


def query_9():
    """
    Purpose: This query retrieves specific information about movies stored in the database that were released within a specified range of years.
    It selects the title, release year, rating, duration, and description of each movie from the "MOVIES" table that falls within the specified release year range.

    Returns:
        str: SQL query string to select movie details released within the specified range of years.
    """
    return "SELECT title, release_year, rating, duration, description " \
           "FROM MOVIES " \
           "WHERE release_year BETWEEN %s AND %s"


def query_10():
    """
    Purpose: This query retrieves specific information about movies stored in the database that were directed by a particular director.
    It selects the title, release year, rating, duration, and description of each movie from the "MOVIES" table."
    Returns:
        str: SQL query string to select movie details directed by the specified director.
    """
    return "SELECT m.title, m.release_year, m.rating, m.duration, m.description " \
           "FROM MOVIES m " \
           "JOIN DIRECTORS d ON m.movie_id = d.movie_id " \
           "WHERE d.director_name = %s"


def query_11():
    """
    Purpose: This query retrieves specific information about movies stored in the database that belong to a particular country.
    It selects the title, release year, rating, duration, and description of each movie from the "MOVIES" table."
    Returns:
        str: SQL query string to select movie details produced in the specified country.
    """
    return "SELECT m.title, m.release_year, m.rating, m.duration, m.description " \
           "FROM MOVIES m " \
           "JOIN COUNTRY c ON m.movie_id = c.movie_id " \
           "WHERE c.country_name = %s"


def query_12():
    """
    Purpose: This query retrieves specific information about movies stored in the database that are listed under a particular category or genre.
    It selects the title, release year, rating, duration, and description of each movie from the "MOVIES" table."
    Returns:
        str: SQL query string to select movie details categorized under the specified genre.
    """
    return "SELECT m.title, m.release_year, m.rating, m.duration, m.description " \
           "FROM MOVIES m " \
           "JOIN LISTED_IN l ON m.movie_id = l.movie_id " \
           "WHERE l.listed_in_name = %s"
