/* Task4 b */
SELECT measurement.FK_SiteId as SiteID, geolocation.Location, measurement.DateTime, max(measurement.CO) 
FROM measurement
LEFT JOIN geolocation ON measurement.FK_SiteId = geolocation.SiteId;