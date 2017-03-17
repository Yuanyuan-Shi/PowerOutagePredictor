## Data set:

* Seattle power outage data during the past 16 years (2000–2016). There are 5,664 records included. 
* For each record, It contains 10 fields: outage start time, end time, event number, feeder number, outage location, cause of the outage, category, affected customer number, outage duration, total affected customer hour
* The data in use for this project is de-identified, removing all customer sensitive information. For debugging and unit tests, we only use the part of the data (1 year). Then we run the developed algorithm on the whole dataset.
* The distribution of our data in use 

![Alt](https://github.com/rkastilani/PowerOutagePredictor/blob/master/Graphs/classDistribution.png)

## Data Processing

We studied the Seattle secondary network outage events caused by equipment, treefall, animal and lighting-caused failures from 2000/09/11 to 2016/03/14. We incorporated weather data including temperature, wind speed, precipitation, visibility, humidity, weather event (rain, fog, snow, lightening etc.), and day length. We consider each outage happens independently, so it is only correlated with the weather data itself. We considered it as classification problem: a normal (0 - 2 outages), bad (3 - 7 outages), and extreme (8+ outages) cases are studied.

![Alt](https://github.com/rkastilani/PowerOutagePredictor/blob/master/Graphs/DataProcessing.png)
