import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is circular.
plt.title('Pie Chart Example')
plt.show()

# line plot
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, color='blue', linewidth=2)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot Example')
plt.grid(True)
plt.show()


# scatter plot
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(1000)
y = np.random.randn(1000)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, s=10, color='red', alpha=0.5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
plt.show()



# histogram
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000)

plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()



# bar chart
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
values = [10, 20, 30, 40]

plt.figure(figsize=(8, 6))
plt.bar(labels, values, color='green')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart Example')
plt.show()



# box plot
import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 5)]

plt.figure(figsize=(8, 6))
plt.boxplot(data, labels=['A', 'B', 'C', 'D'])
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Box Plot Example')
plt.show()


# area plot
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(8, 6))
plt.fill_between(x, y1, y2, where=y2 >= y1, facecolor='green', interpolate=True)
plt.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red', interpolate=True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Area Plot Example')
plt.show()


# subplot
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Subplot 1')

plt.subplot(2, 2, 2)
plt.bar([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Subplot 2')

plt.subplot(2, 2, 3)
plt.scatter([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Subplot 3')

plt.subplot(2, 2, 4)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.title('Subplot 4')

plt.suptitle('Multiple Subplots Example')
plt.show()



# line chart + bar chart
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(5)
y1 = np.random.randint(1, 11, 5)
y2 = np.random.randint(1, 11, 5)

fig, ax1 = plt.subplots(figsize=(8, 6))

ax1.bar(x - 0.2, y1, width=0.4, color='blue')
ax1.set_xlabel('Category')
ax1.set_ylabel('Bar Value', color='blue')
ax1.tick_params('y', colors='blue')

ax2 = ax1.twinx()
ax2.plot(x, y2, '--r', linewidth=2)
ax2.set_ylabel('Line Value', color='red')
ax2.tick_params('y', colors='red')

plt.title('Line Chart + Bar Chart Example')
plt.show()


# normal distribution
import numpy as np
import matplotlib.pyplot as plt

# Generate random data from a normal distribution
data = np.random.normal(0, 1, 1000)

# Create a histogram
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, density=True, edgecolor='black')

# Plot the normal distribution curve
x = np.linspace(-4, 4, 100)
pdf = 1 / (np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)
plt.plot(x, pdf, color='red', linewidth=2)

plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Normal Distribution Example')
plt.show()