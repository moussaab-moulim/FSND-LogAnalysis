# Moussaab MOULIM log analysis projoct. (FSND)

## setup envirement
1. install virtualbox where we will install ubunto to run the programs and also instal the database programm Postgres
    [Link for virtual box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
2. install vagrant to connect to the virtual machine from the host and run your command from it
    [Link for vagrant](https://www.vagrantup.com/)
3. clone this github directory https://github.com/udacity/fullstack-nanodegree-vm . you will need it to install the proper configuration needed to run this project
4. open your terminal change directory to Vagrant directory inside the cloned directory
and run this command
    ```
    vagrant up
    ```
    it will install the virtual machine and python and all dependencies needed as well as Postgres (it will take some time)
you can check the file Vagrantfile inside vagrant directory to see all the commands will be running with the vagrant up
5. after the command finish run to login to the virtual machine
    ```
    vagrant ssh
    ```
    now the vagrant file in your hose is shared with the virtual machine too
6. download data for news database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
unzip it and put newsdata.sql insite vagrant file
7. change directory to vagrant file and run this commade to load the data
    ```
    psql -d news -f newsdata.sql
    ```
    the news database is already setup with vagrant up command from configuration file


now you are up and running 
## First Query
on the first query i used join on the articles table with the log table on the slug column from articles with the path column from log
but path and slug dont have same syntax!
so i used the Postgres split_part function to get the proper format to use join.
[link to split_part() docs](https://w3resource.com/PostgreSQL/split_part-function.php)
i used a condition on status to make sure the article was visited before i count it

## Second Query
second query was pretty much similiair to the first one i just had to join the authors name column and count based on the name of author instead of article title on first one

## Third Query
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
and round() function to only get 1 number after ','.

[docs for cast()](http://www.postgresqltutorial.com/postgresql-cast/) 

[docs for round()](https://www.w3resource.com/PostgreSQL/round-function.php)

## How to run

- create the views in the news database from fullstack nano degree course
- run log.py using 
```
python log.py
```


**Thank you for reading**