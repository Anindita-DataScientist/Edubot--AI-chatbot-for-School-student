age = int(input("Enter your age: "))

if age < 10:
    print("Children")
elif age > 60:
    print("Senior Citizens")
else:
    print("Normal Citizen")


# Input
gender = input("Enter gender (male/female): ").lower()
age = int(input("Enter age: "))
fare = float(input("Enter base fare: "))

# Determine final fare
if gender == "male":
    if age >= 60:
        final_fare = fare * 0.70  # 70% of fare
    else:
        final_fare = fare         # 100% of fare
elif gender == "female":
    if age >= 60:
        final_fare = fare * 0.50  # 50% of fare
    else:
        final_fare = fare * 0.70  # 70% of fare
else:
    final_fare = fare  # default (if input is invalid)

# Output
print("Final ticket price:", final_fare)


num = int(input("Enter a number: "))

if num > 0 and num % 5 == 0:
    print("The number is positive and divisible by 5.")
else:
    print("The number is either not positive or not divisible by 5.")

list1 = [1, 5.5, (10+20j), 'data science']

# Print all default functions (attributes and methods)
print("Default functions/methods available for a list:")
print(dir(list1))


# Example: create a sequence from 1 to 10
sequence = list(range(1, 30))
print(sequence)


n = int(input("Enter a number: "))
print("Sequence up to", n, "is:")

for i in range(1, n + 1):
    print(i, end=' ')


# Define the lists
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# Create dictionary using zip() and dict()
num_dict = dict(zip(list2, list1))

# Print the resulting dictionary
print("Dictionary with words as keys and numbers as values:")
print(num_dict)

list1 = [3, 4, 5, 6, 7, 8]

# Apply conditions: Add 10 to even numbers, multiply odd numbers by 5
list2 = [x + 10 if x % 2 == 0 else x * 5 for x in list1]

print("Original List:", list1)
print("Transformed List:", list2)





def greet(name, message="How are you"):
    print(f"Hello ---{name}---, {message}")

# Examples:
greet("Radha")  # Uses default message
greet("Radha", "Hope you’re having a great day!")  # Custom message

def find_max(a, b, c):
    """Function to find the maximum of three numbers."""
    return max(a, b, c)

# Example usage:
result = find_max(10, 25, 15)
print(f"The maximum number is: {result}")

def sum_of_list(numbers):
    """Function to sum all the numbers in a list."""
    return sum(numbers)

# Example usage:
numbers_list = [1, 2, 3, 4, 10]
result = sum_of_list(numbers_list)
print(f"The sum of the list is: {result}")

import pandas as pd
from sklearn.impute import SimpleImputer

# Load the dataset
df = pd.read_csv("E:\DataScience Certificates\Python\Module 7 Python for data analytics Assignment (2)\Data Set (13)\datasets\Data.csv")

# Handle missing data using SimpleImputer
# For numeric columns, we can fill missing data with the mean of that column
imputer = SimpleImputer(strategy="mean")

# Assuming columns with missing values are numeric, let's apply the imputer to them
df_imputed = df.copy()

# Apply imputation on each numeric column
df_imputed[df_imputed.select_dtypes(include=["float64", "int64"]).columns] = imputer.fit_transform(
    df_imputed.select_dtypes(include=["float64", "int64"])
)

# Filter data where Salary is less than 70,000
df_filtered = df_imputed[df_imputed['Salaries'] < 70000]

# Display the result
print(df_filtered)

# Optionally, you can save the filtered dataset to a new CSV
# df_filtered.to_csv("Filtered_Data.csv", index=False)


from datetime import date

# Create date objects for May 9th, 2007 and December 13th, 2007
start = date(2007, 5, 9)
end = date(2007, 10, 13)

# Subtract start date from end date to get the difference
days_difference = end - start

# Print the number of days between the two dates
print(f"Number of days between May 9th, 2007 and December 13th, 2007: {days_difference.days}")


from datetime import date

# Create a date object for August 26, 1992
Andrew = date(1992, 8, 26)

# Print the date in different formats
print("Format 'YYYY-MM':", Andrew.strftime('%Y-%m'))
print("Format 'YYYY-DDD':", Andrew.strftime('%Y-%j'))
print("Format 'MONTH (YYYY)':", Andrew.strftime('%B (%Y)'))
