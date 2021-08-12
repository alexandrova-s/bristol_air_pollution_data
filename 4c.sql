/* Task4 c */
SELECT FK_SiteId, avg(NO2), avg(NO) FROM measurement WHERE YEAR(DateTime) = 2019 AND TIME(DateTime) between '07:45:00' AND '08:15:00' GROUP BY FK_SiteId;