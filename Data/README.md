## Data Processing

We studied the Seattle secondary network outage events caused by equipment, treefall, animal and lighting-caused failures from 2000/09/11 to 2016/03/14. We incorporated weather data including temperature, wind speed, precipitation, visibility, humidity, weather event (rain, fog, snow, lightening etc.), and day length. We consider each outage happens independently, so it is only correlated with the weather data itself. We considered it as classification problem: a normal (0 - 2 outages), bad (3 - 7 outages), and extreme (8+ outages) cases are studied.

![Alt](https://github.com/rkastilani/PowerOutagePredictor/blob/master/Graphs/DataProcessing.png)
