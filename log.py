# Database code for the DB Forum.
#
# This is still NOT the full solution!

import psycopg2
import bleach

DBNAME = "news"


def get_top_articles():
    # Return top 3 most viewed articles
    # i used split_part function to get only the slug part from path in logs so
    # i can use is in join with slug in articles
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = "select a.title,count(l.path) as visits " \
            + "from articles a " \
            + "join log l  " \
            + "on a.slug=split_part(l.path,'/',3) " \
            + "where l.status like '%200%' " \
            + "group by a.title " \
            + "order by visits desc " \
            + "limit 3;"
    c.execute(query)
    articles = c.fetchall()
    db.close()
    return articles


def get_top_authors():
    # Return top 3 most viewed articles
    # i used split_part function to get only the slug part from path in logs so
    # i can use is in join with slug in articles
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = "select au.name , count(l.path) visits " \
            + "from (articles a join authors u on a.author=u.id) au " \
            + "join log l " \
            + "on au.slug=split_part(l.path,'/',3) " \
            + "where l.status like '%200%' " \
            + "group by au.name " \
            + "order by visits desc "

    c.execute(query)
    authors = c.fetchall()
    db.close()
    return authors


def get_days_with_errors():
  # Return top 3 most viewed articles
  # i used split_part function to get only the slug part from path in logs so
  # i can use is in join with slug in articles
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  query = "select s.ntime ,"\
          + "ROUND((100*cast(f.failure as decimal )/(f.failure+s.sucess)), 1) as f_perc"\
          + " from successcount s join failurecount f on s.ntime=f.ntime"\
          + " where (100*cast(f.failure as decimal )/(f.failure+s.sucess))> 1"\
          + " group by s.ntime,s.sucess,f.failure;"

  c.execute(query)
  errors = c.fetchall()
  db.close()
  return errors


print("1. What are the most popular three articles of all time?")
for line in get_top_articles():
    print('"' + line[0] + '"' + " -- " + str(line[1]) + " views")

print("2. Who are the most popular article authors of all time?")
for line in get_top_authors():
    print(line[0] + " -- " + str(line[1]) + " views")
print("3. On which days did more than 1% of requests lead to errors?")
for line in get_days_with_errors():
    print(str(line[0]) + " -- " + str(line[1]) + "% errors")
