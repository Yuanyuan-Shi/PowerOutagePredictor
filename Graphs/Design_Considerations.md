Use case considerations: ![Alt](https://github.com/rkastilani/PowerOutagePredictor/blob/master/Graphs/usecase.png)

Here is the design for the final GUI: ![Alt](https://github.com/rkastilani/PowerOutagePredictor/blob/master/Graphs/GUIDesign.png)

* Input Data: 
	* day length hours
	* temperature: max, mean, min
	* humidity: max, mean, min
	* visibility miles: max, mean, min
	* wind speed: max, mean
	* max gust speed
	* precipitation
	* weather events: snow, thunderstorm etc

* Output (prediction):
	* class of outage status
	   * normal: 0 - 2 outages
	   * bad:    3 - 7 outages
	   * extreme:   8+ outages
	
	* probabilities of each class for a given day

* Machine Learning methods: Tree-based, SVM, and NN.

* Chanlenge: imbalabce between classes
* Solution: balance the samples from differenet classes
