# movietopics

Summary:

This is an Python program devised to collect the user's movies in a local database and share information with an internet database.

The local database is created with SQLite, a serverless db, and contains generic data about the movie, retrived from http://omdbapi.com via the urllib module. The search is conducted looking for titles specified by the user in a file or reading file and folder names in a directory. The local database also contains a table of key-based reviews of the movies (to each movie the user can assing an integer value to 15 keys, which serves to characterize the macroscopic contents and style of the movie). Entries in this table are inserted via command line.

The internet database is set with MySQL, with which the user can synchronize its own data via the connector/python module (written by Oracle). The internet database grows with the data of all users and can searched. All queries to the databases are executed with the execute method of the cursor object spawned by the connection object.

The file Setup.py, to be run the first time, sets the environment, the file Movie_Library.py can be run after Setup.py and controls all the functions of the program.

To do:
-Write search functions to look for movies in either local or internet database based on people (actors, director) or key values.
-Write PhP, SQL functions to automate the registration of users to the internet database

To do - version2:
-Write GUI
-Set a real internet database and start testing
