# Movie Correlation Analysis
<h3>What are the main characteristics that have the most impact on the movie's gross earnings?</h3>

The dataset used for this analysis was found in Kaggle via <a href = "https://www.kaggle.com/datasets/danielgrijalvas/movies">this link</a>.
The purpose of this project is to perform a correlation analysis of the dataset to determine if there is a correlation between the gross earnings and any other variable in the dataset.

What factor(s) determines how much profit/revenue a movie will make?


I used Python with Jupyter notebook to run this analysis because of the speed and multi-functionality of python.

## Procedures
### Step 1 
I imported the necessary libraries such as:
+ NumPy for calculations
+ Pandas for data wrangling
+ Matplotlib for plotting the graphs
+ Seaborn for aesthetics

### Step 2 
The next step I took was to perform data-wrangling processes which includes:
+ Checking and removal of null values.
+ Converting columns to appropriate data types.
+ Splitting and concatenation columns.
+ Changing column names to appropriate ones.
+ Sorting columns.

### Step 3
The next step I took was to create a correlation heat map to check which variable has the strongest correlation with **gross_earnings**
It should be noted that the correlation heatmap only picks columns with the required data type of either int or float (numerical). It doesn't work with object values.
So to perform further analysis, I converted the rest of the columns into codes so they could become numerical to see if there are columns with stronger correlations. 
The correlation heatmap was plotted again.

## Conclusion
Unlike previous expectations, from my analysis, the **budget** of a movie has the strongest correlation with **gross_earnings** followed by **votes**.
That is the gross earnings of a movie are highly determined by how much is invested in making the movie (budget).
