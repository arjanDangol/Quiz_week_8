import matplotlib.pyplot as plt
import pandas as pd


# Load the CSV file into a DataFrame
dataframe = pd.read_csv(r"./climate.csv")

# Extract values from the "Year" column
years = dataframe['Year'].tolist()

# Print years
print(years)

# Extract values from the "CO2" column
co2 = dataframe['CO2'].tolist()

# Print co2
print(co2)

# Extract values from the "Temperature" column
temp = dataframe['Temperature'].tolist()

# Print temp
print(temp)

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

