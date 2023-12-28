import pandas as pd

# Function to generate data for a linear function (y = mx + c)
def generate_linear_data(start, end, step, slope, intercept):
    x_values = []
    y_values = []

    for x in range(start, end + 1, step):
        y = slope * x + intercept
        x_values.append(x)
        y_values.append(y)

    return {'x': x_values, 'y': y_values}

# Generate data for a linear function: y = 2x + 3 (example function)
data = generate_linear_data(1, 10, 1, 6, 0)

# Create a DataFrame from the generated data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('output2.csv', index=False)

print("CSV file 'output2.csv' generated successfully.")
