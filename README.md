# Power Outage Predictor

As the name suggests, Power Outage Predictor is a python package dedicated to predict power outages given certain weather conditions. Although the package can be implemented in any, the package was developed using utilities and weather data in Seattle, WA; hence caution should be made on prediction power outage elsewhere. A GUI implementation of the package is also available.

## License
Since we do not plan to commercialize this, this project is under the permissive MIT license. If anything changes, we will be sure to update accordingly. If you do happen to want to use any parts of this project, please do give reference. For more details, please read LICENSE.md

## Software Dependencies

* matplotlib
* scikit-learn
* numpy
* pandas

## Repository Structure

### Data
Contains the data used in this project. It also contains a directory "backup" that contains pre-processed data; this directory should be ignored except by contributors to this project.

### Docs
Documentation regarding this project. To view the API documentation, open the API Documentation.md file. The Presentations and poster directory contains more information about this project. The build\_ directory and the rest of the files are related to Sphinx autodocumentation tool that we are planning to implement. For now, simply open the API documentation.md file.

### GUI demo
The GUI can display the history of outages and the prediction generated from any machine learning algorithm that the user preferred in the project. A web-based user interactive interface is built using Javascript. Users could read the prediction and history outages from the dashboard on any mobile device. Since the data is confidential, the outage data demonstration is only available from 2014/03/01 to 2014/03/30, and the information is hashed.

### Graphs
Workflow and images pertaining to design considerations.

### PowerOutagePredictor
The meat (or tofu if you are vegetarian) of this project. Contains all the python packages and modules of machine learning methods to predict power outages. It contains examples of usage too.

### Group
![Alt](PowerOutagePredictor/Graphs/GroupPhoto.jpg)
