# cs50-final

<h2> Final project </h2>

I extracted box office information from BOXOFFICEMOJO.com using HTML requests rather than thhe BeautifulSoup implementation. You are able to input the year you would like to read the info for, as well as a duration e.g. '2020 10' will create tables of data from 2011 to 2020 into a new file called 'data'.

<h2> See the code in web-scraper.py </h2>

I pulled data from https://www.boxofficemojo.com/year/world/{year} in web-scraper.py.

To compile successfully, run "python movie-scraper.py {year of your choosing} {duration of your choosing}"

For example if you run "python movie-scaper.py 2020 10", this will pull information from 2011 to 2020.

I have also created a file called 'table-movies.py' where you can run queries on this data using an SQLITE3 database.
If this is not to your liking, I have also created 'movie-roster'.py where you can find the rank of any movie from the databases by running "python3 movie-roster.py YEAR RANK".

As a complete beginner to programming in general, I've had a great time learning the fundamentals with CS50.

Thank you, CS50 :)
