import pandas as pd

def analyze_user_data(data_path):
  """
  Analyzes user data from a CSV file and returns insights.

  Args:
      data_path: Path to the CSV file containing user data.

  Returns:
      A dictionary containing various insights about the user data.
  """

  # Read data from CSV using pandas
  df = pd.read_csv(data_path)

  print(df.loc[20:40,["track_name","price"]])



# Example usage
file_path = input("Input the file name: ")
data_path = file_path
user_data_analysis = analyze_user_data(data_path)
print(user_data_analysis)







