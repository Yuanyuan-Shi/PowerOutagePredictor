## Data set:

* Seattle power outage data during the past 16 years (2000–2016). There are 5,664 records included. 
* For each record, It contains 10 fields: outage start time, end time, event number, feeder number, outage location, cause of the outage, category, affected customer number, outage duration, total affected customer hour
* The data in use for this project is de-identified, removing all customer sensitive information. For debugging and unit tests, we only use the part of the data (1 year). Then we run the developed algorithm on the whole dataset.
* The distribution of our data in use 

![Alt](https://github.com/rkastilani/PowerOutagePredictor/blob/master/Graphs/classDistribution.png)


## Data Processing

We studied the Seattle secondary network outage events caused by equipment, treefall, animal and lighting-caused failures from 2000/09/11 to 2016/03/14. We incorporated weather data including temperature, wind speed, precipitation, visibility, humidity, weather event (rain, fog, snow, lightening etc.), and day length. We consider each outage happens independently, so it is only correlated with the weather data itself. We considered it as classification problem: a normal (0 - 2 outages), bad (3 - 7 outages), and extreme (8+ outages) cases are studied.

![Alt](https://github.com/rkastilani/PowerOutagePredictor/blob/master/Graphs/DataProcessing.png)


## Data Sources

We collect a daily Seattle Weather dataset from 2000/09/11 - 2016/03/14.

There are lots of free weather data available on the Internet, but most of them have problems such as limited history data, wrong and missing data. There are some commertial weather data websies but they are not free. For example: https://www.meteoblue.com/en/weather/archive/export/basel_switzerland_2661604

We collected 16 years weather data from https://www.wunderground.com/history/airport/KSEA, Daylight length: http://sunrise-sunset.org/, and we clean and organize the data by hand. This weather dataset contains the day length, min/max/ave temperature, humidity, windspeed, visibility and events (snow, rain, thunderstorm and etc.)


## Lessons leaned from the extreme cases

1. Tons of failures were reported because

a. trees in wire, mainly accociated with high wind speed (average highest wind speed 35.3 mph, and average maximum wind gust 49.0 mph).

b. lighitning, mostly accoviated with "thunderstorm" in the "Event" catagory. Need to exam more weather data to see whether it is a sufficient condition.

2. On most of the extreme days, though the majority of the records are catogried as OH, there are on average 2 records of equipment failure (trans + gen) and 1 UG. 

3. One of the days was mostly because of the snow. 

4. May need to separate the days with extreme weather conditions.
