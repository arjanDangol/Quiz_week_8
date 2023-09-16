import matplotlib.pyplot as plt
import sqlite3

years = []
co2 = []
temp = []

if __name__ == "__main__":
    # Connect to the database climate.db
    connection = sqlite3.connect(r"./climate.db")
    cursor = connection.cursor()

    # SQL cmd for extracting column year from ClimateData table
    sql_cmd_year = """
        SELECT Year FROM ClimateData;
        """
    # SQL cmd for extracting column year from ClimateData table
    sql_cmd_co2 = """
            SELECT CO2 FROM ClimateData;
            """
    # SQL cmd for extracting column year from ClimateData table
    sql_cmd_temperature = """
            SELECT Temperature FROM ClimateData;
            """
    # Execute a SQL query to select the values from the "year" column
    cursor.execute(sql_cmd_year)

    # Fetch all the values into a year list
    years = [row[0] for row in cursor.fetchall()]

    # Execute a SQL query to select the values from the "CO2" column
    cursor.execute(sql_cmd_co2)

    # Fetch all the values into a co2 list
    co2 = [row[0] for row in cursor.fetchall()]

    # Execute a SQL query to select the values from the "Temperature" column
    cursor.execute(sql_cmd_temperature)

    # Fetch all the values into a temp list
    temp = [row[0] for row in cursor.fetchall()]

    # Close the database connection
    connection.close()

    # Print or use the years as needed
    print(years)
    # Print or use the CO2 as needed
    print(co2)
    # Print or use the temperature as needed
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
plt.savefig("co2_temp_1.png")
