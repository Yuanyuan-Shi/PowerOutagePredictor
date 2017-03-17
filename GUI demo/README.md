## GUI

[Check out Index.html](https://github.com/rkastilani/PowerOutagePredictor/blob/master/GUI%20demo/index.html)

The GUI can display the history of outages and the prediction data generated from any machine learning algorithm that the user preferred in the project. A web-based user interactive interface is built using Javascript. Users could read the prediction and history outages from the dashboard on any mobile device. Since the data is confidential, the outage data demonstration is only available from 2014/03/01 to 2014/03/30, and the information is hashed.

## Features:
1. The webpage could refresh daily, so the perdiction results can update daily.
2. Users could select the date range from date picker, they can read the history data from the table.
3. Users could sort ascending or descending by any header of the table.
4. Users could zoom in/out of the Google map, and it will automatically center the map based on the markers.
5. Once users click markers, it will display infomation window that provides detailed outages data.
6. Users could easily read the distribution of the outages
7. Users could study any date range they want.
8. It is mobile device friendly. The layout will automatically change based on the device.

![Alt](https://github.com/rkastilani/PowerOutagePredictor/blob/master/GUI%20demo/GUI_demo.png)

## Documentation
### js folder
`main.js` stores the interactive Javascript code including Gooogle Map Javascript API v3, Backgrid and Datepicker.

### css folder
`bootstrap.min.css` sotres Responsive web design (RWD) css styles which is an approach to web design aimed at allowing desktop webpages to be viewed in response to the size of the screen or web browser one is viewing with.

`gridpicker.css` stores the backgrid (talbe) and daypicker css styles.

`styles.css` stores the general HTML body, navigation bar etc. css styles.

### data folder
`prediction.txt` stores the results that generated from any machine learning method.

I must follow a format (.txt file) like this
[1st line] Number of Tomorrow's Outages Prediction
[2nd line] Chance of Tomorrow's Outages Prediction
[3rd line] Number of Weather-caused Failure
[4th line] Number of Equiptment Failure

For example,
0 - 2 outages
83%
0 - 2 outages
0 - 2 outages



