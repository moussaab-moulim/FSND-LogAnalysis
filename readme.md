# Moussaab MOULIM log analysis projoct. (FSND)

## 1. First Query
on the first query i used join on the articles table with the log table on the slug column from articles with the path column from log
but path and slug dont have same syntax!
so i used the Postgres split_part function to get the proper format to use join.
[link to split_part() docs](https://w3resource.com/PostgreSQL/split_part-function.php)
i used a condition on status to make sure the article was visited before i count it

## 2. Second Query
second query was pretty much similiair to the first one i just had to join the authors name column and count based on the name of author instead of article title on first one

## 3. Third Query
on the third query i used two views:
- the first one to count number of succes request on each day
```sql
create view successcount
as select time::date as ntime,count(status) as sucess from log 
where status like'%200%' 
group by time::date
;
```

- the Second one to count number of failed request on each day
```sql
create view failurecount
as select time::date as ntime,count(status) as failure from log 
where status like'%404%' 
group by time::date
;
```

then i joined the in the query calculating the pourcentage of failed request on each day using this formula
```
100*failed_request/failed_request+succes_request
```

i used the cast() function on one of the fields to turn the results to decimal value
and round() function to only get 1 number after ','
[docs for cast()](http://www.postgresqltutorial.com/postgresql-cast/)
[docs for round()](https://www.w3resource.com/PostgreSQL/round-function.php)

## how to run

- create the views in the news database from fullstack nano degree course
- run log.py using 
```
python log.py
```


**Thank you for reading**