## Summary of Linear Regression (based on the number of outages in 2014 data)

|                      Score |  Total Outages  | Equipment-caused |   Trees-caused  |  Animals-caused | Lightening-caused |
|---------------------------:|:---------------:|:----------------:|:---------------:|:---------------:|:----------------:|
| Multiple Linear Regression | 0.1667171986050 | -1.5447683981400 | 0.1818649511060 | 0.2532823415820 |  0.0247362585258 |
|            Lasso           | 0.1617593567730 |  0.0596682123769 | 0.1817794584870 | 0.2496187402510 |  0.0237563308299 |
|            Ridge           | 0.1660278564960 |  0.0602058576606 | 0.1812308034260 | 0.2500356676360 |  0.0241210915243 |

### Conclusion
1. We can expect the results capture better Trees, and Animals because it is closely related to tree-fall events and animal event. We use day length to capture the feature of seasons.
2. The reason that the prediction of Equipment failure is bad is because the input features, weather, are not closely related to equipment failure. If we could have equipment age as a feature, we might have better prediction on this type of failure.
3. The lightening prediction is bad is because there are only few lightening events in 2014, we could not have a good training data set.

### Take away
Machine learning algorithm could work better only if the data is normally distributed.
