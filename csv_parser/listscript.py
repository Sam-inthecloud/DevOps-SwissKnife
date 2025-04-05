import pandas as pd

# Read the CSV file
df = pd.read_csv('cleaned_scms_latest.csv')

# Print all column names
print("Available columns in your CSV file:")
for col in df.columns:
    print(col)

# Ask user which column to analyze
column_name = input("\nEnter the name of the column you want to analyze (copy-paste from above): ")

# Check if the column exists
if column_name in df.columns:
    # Group by the selected column and count the number of rows
    site_counts = df.groupby(column_name).size().reset_index(name='count')

    # Sort by count in descending order
    site_counts_sorted = site_counts.sort_values('count', ascending=False)

    # Get the top 10
    top_10_sites = site_counts_sorted.head(10)

    # Print the results
    print(f"\nTop 10 entries with the most amount of data for column '{column_name}':")
    for index, row in top_10_sites.iterrows():
        print(f"{row[column_name]}: {row['count']} rows")

    # Optionally save to CSV
    save_option = input("\nWould you like to save these results to a CSV file? (yes/no): ")
    if save_option.lower() == 'yes':
        output_filename = f'top_10_{column_name}.csv'
        top_10_sites.to_csv(output_filename, index=False)
        print(f"Results saved to {output_filename}")

else:
    print(f"Error: Column '{column_name}' not found in the CSV file.")