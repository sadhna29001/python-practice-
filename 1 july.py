import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset
tips = sns.load_dataset("tips")

# Create a scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips)

# Add labels and title
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Tip vs Total Bill")

# Show the plot
plt.show()




import seaborn as sns
import matplotlib.pyplot as plt

# Load example data
fmri = sns.load_dataset("fmri")

# Create line plot
sns.lineplot(x="timepoint", y="signal", data=fmri)
plt.title("Signal Over Time")
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Load example data
tips = sns.load_dataset("tips")

# Create histogram
sns.histplot(tips["total_bill"])
plt.title("Distribution of Total Bills")  
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Load example data 
tips = sns.load_dataset("tips")

# Create bar plot
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Average Total Bill by Day")
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Load example data
flights = sns.load_dataset("flights")

# Create pivot table 
flights_pivot = flights.pivot("month", "year", "passengers")

# Create heatmap
sns.heatmap(flights_pivot)
plt.title("Passengers by Year and Month")
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Load example data
tips = sns.load_dataset("tips")

# Create scatter plot 
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Tip vs Total Bill")
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset
tips = sns.load_dataset("tips")

# Create the KDE plot
sns.kdeplot(data=tips, x="total_bill")

# Add labels and title
plt.xlabel("Total Bill")
plt.ylabel("Density")
plt.title("Distribution of Total Bills")

# Show the plot
plt.show()