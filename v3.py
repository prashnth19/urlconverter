import pandas as pd

# Define placeholder values with new default versions
placeholder_values = {
    "jersey_version": "2.36",
    "hamcrest-library.version": "2.2",
    "immutables.version": "3.0.0",
    "maven.jacoco.plugin.version": "0.8.8",
    "commons-compress.version": "1.21",
    "commons-lang3.version": "3.14.0",
    "httpclient.version": "4.5.14",
    "revartifact": "latest",
    "hibernate-core": "5.6.0.Final",
    "hibernate-hikaricp": "5.6.0.Final",
    "hibernate-validator": "6.2.7.Final"
}

def replace_placeholders(url):
    """Replace placeholders in the URL with provided values."""
    for placeholder, value in placeholder_values.items():
        url = url.replace(f"${{{placeholder}}}", value)
    return url

def process_excel(file_path):
    """Read the Excel file and process URLs."""
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        if 'URL' not in df.columns:
            print("The Excel file should have a column named 'URL'.")
            return
        
        df['Updated_URL'] = df['URL'].apply(replace_placeholders)

        # Save the updated URLs back to a new Excel file
        output_file = "updated_urls.xlsx"
        df.to_excel(output_file, index=False)
        print(f"Updated URLs have been saved to {output_file}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Path to your input Excel file
input_excel_file = "input_urls.xlsx"

# Process the input Excel file
process_excel(input_excel_file)
