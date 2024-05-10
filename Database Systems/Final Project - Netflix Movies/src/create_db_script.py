TABLES = {}


"""
This table maintains information about movies, including their unique identifier (movie_id), title, date added, release year, rating, duration, and description. 
It also includes indexes for faster retrieval based on duration and release year.
"""
TABLES['MOVIES'] =(
"CREATE TABLE `MOVIES`("
" `movie_id` int(11) NOT NULL,"
" `title` varchar(500) NOT NULL,"
" `release_year` int(11) NOT NULL,"
" `rating` varchar(100) NOT NULL,"   
" `duration` int(11) NOT NULL,"      
" `description` varchar(1500)  NOT NULL,"
" PRIMARY KEY (`movie_id`),"
" FULLTEXT INDEX idx_description (`title`, `description`),"
" INDEX duration_index (`duration`),"
" INDEX release_year_index (`release_year`)"
") ENGINE = InnoDB")


"""
This table establishes a many-to-many relationship between movies and directors. 
It contains the movie_id and director_name columns, forming a composite primary key to ensure uniqueness. 
Foreign key constraint on movie_id references the movie_id column in the MOVIES table.
Note: There are no null directors in this table. If we don't find the id of the movie, then there are no directors for it.
"""
TABLES['DIRECTORS'] =(
"CREATE TABLE `DIRECTORS` ("
"`movie_id` int(11) NOT NULL,"
"`director_name` varchar(100) NOT NULL,"
"PRIMARY KEY (`director_name`, `movie_id`),"
"FOREIGN KEY (`movie_id`) REFERENCES MOVIES(`movie_id`)"
") ENGINE = InnoDB"
)


"""
This table records the cast members associated with each movie. It includes the movie_id and cast_name columns, forming a composite primary key to ensure uniqueness. 
Foreign key constraint on movie_id references the movie_id column in the MOVIES table. 
It also includes a full-text index for efficient searching based on cast names.
Note: There is no null cast in this table. If we don't find the id of the movie, then there is no cast for it.
"""
TABLES['CAST']=(
"CREATE TABLE `CAST` ("
"`movie_id` int(11) NOT NULL,"
"`cast_name` varchar(100) NOT NULL,"
"PRIMARY KEY ( `cast_name` , `movie_id`),"
"FOREIGN KEY (`movie_id`) REFERENCES MOVIES(`movie_id`),"
"FULLTEXT INDEX idx_cast_name (`cast_name`)"
") ENGINE = InnoDB"
)


"""
This table maintains the countries associated with each movie. 
It includes the movie_id and country_name columns, forming a composite primary key to ensure uniqueness. 
Foreign key constraint on movie_id references the movie_id column in the MOVIES table.
Note: There is no null country in this table. If we don't find the id of the movie, then there is no country for it.
"""
TABLES['COUNTRY']=(
"CREATE TABLE `COUNTRY` ("
"`movie_id` int(11) NOT NULL,"
"`country_name` varchar(100) NOT NULL,"
"PRIMARY KEY (`country_name` , `movie_id`),"
"FOREIGN KEY (`movie_id`) REFERENCES MOVIES(`movie_id`)"
") ENGINE=InnoDB"
)


"""
This table maintains the genres or categories associated with each movie. 
It includes the movie_id and listed_in_name columns, forming a composite primary key to ensure uniqueness. 
Foreign key constraint on movie_id references the movie_id column in the MOVIES table.
Note: There is no null listed_in in this table. If we don't find the id of the movie, then there is no listed_in for it.
"""
TABLES['LISTED_IN']=(
"CREATE TABLE `LISTED_IN` ("
"`movie_id` int(11) NOT NULL,"
"`listed_in_name` varchar(100) NOT NULL,"
"PRIMARY KEY (`listed_in_name` ,`movie_id`),"
"FOREIGN KEY (`movie_id`) REFERENCES MOVIES(`movie_id`)"
") ENGINE=InnoDB"
)
