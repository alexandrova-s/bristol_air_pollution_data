/* Task4 d */
SELECT FK_SiteId, avg(NO2), avg(NO) FROM measurement WHERE YEAR(DateTime) between 2010 AND 2019 AND TIME(DateTime) between '07:45:00' AND '08:15:00' GROUP BY FK_SiteId ;
