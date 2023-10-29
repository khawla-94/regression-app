# regression-app

![logo](https://github.com/khawla-94/regression-app/assets/80429328/fd0056b8-9cf2-4ced-9f6f-465a3d16af63)


The project aims to answer the answer of how some variables/features can affect the change of property prices over a period of time. The dataset is an official record of all property sales in England and Wales by the HM Land Registry, responsible for administrating the real estate under the Open Government Licence v3.0.
The dataset that will be used include 16 features are as follows:

•	Transaction unique identifier: A reference number which is generated automatically recording each published sale. The number is unique and will change each time a sale is recorded;

•	Price: Sale price stated on the transfer deed;

•	Date of Transfer: Date when the sale was completed, as stated on the transfer deed;

•	Postcode: This is the postcode used at the time of the original transaction. (Note that postcodes can be reallocated and these changes are not reflected in the Price Paid Dataset);

•	Property Type	: D = Detached, S = Semi-Detached, T = Terraced, F = Flats/Maisonettes, O = Other;

•	Old/New: Indicates the age of the property and applies to all price paid transactions, residential and non-residential. (Y = a newly built property, N = an established residential building);

•	Duration: Relates to the tenure: F = Freehold, L= Leasehold etc.;

•	PAON: Primary Addressable Object Name. Typically, the house number or name.

•	SAON: Secondary Addressable Object Name. Where a property has been divided into separate units (for example, flats), the PAON (above) will identify the building and a SAON will be specified that identifies the separate unit/flat.

•	Street	

•	Locality	

•	Town/City	

•	District	

•	County	

•	PPD Category Type: Indicates the type of Price Paid transaction. (A = Standard Price Paid entry, includes single residential property sold for value. B = Additional Price Paid entry including transfers under a power of sale/repossessions, buy-to-lets (where they can be identified by a Mortgage), transfers to non-private individuals and sales where the property type is classed as ‘Other’);

•	Record Status: monthly file only Indicates additions, changes and deletions to the records. (A = Addition, C = Change, D = Delete)
We will use the machine learning algorithms for their importance and advanced exploring techniques which will help us retrieve patterns and understand relationships. Not only this, but machine Learning is known for its scalability; handling large datasets.
In addition to this, ML can handle complex and non- linear relationships effectively but also create predictive models and help make decisions based on actual values.
Doing so, we will use a variety of ML algorithms to predict house prices, each has its own advantages and disadvantages:
1.	Linear regression: It models the relationship between the target variable and one or more independent variables by fitting a linear equation to the observed data.
2.	Ridge and Lasso regression: regularized linear regression methods.
3.	Random forest: technique that uses multiple decision trees to make predictions. It can handle complex relationships and reduce overfitting.
4.	Gradient Boosting: builds an additive model of decision trees. It sequentially corrects the errors of the previous models to improve accuracy.
5.	Support Vector Machine (SVM): It finds the optimal hyperplane that best fits the data while minimizing the error.
6.	K-Nearest Neighbors (KNN): predicts the target variable by averaging the values of its k-nearest neighbors in the feature space.
7.	XGBoost :
8.	Decision Trees Regression: uses decision trees to model the relationship between input features and the target variable.
9.	Bayesian Regression: incorporate prior beliefs about the data to make probabilistic predictions.
10.	Extra Trees Regression:
