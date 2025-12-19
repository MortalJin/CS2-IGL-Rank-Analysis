# Data from HLTV.org (Apr 19, 2025)
# rating is data of the player's performance over the past three months

import pandas as pd

# Example 1

# Creating a dataframe using dictionary
data = {
    'ID': ["apEX", "chopper", "Brollan", "MAJ3R", "Aleksib", "Snax", "bLitz", "karrigan", "kyxsan", "electroNic"],
    'rating': [1.04, 0.95, 0.94, 0.9, 0.87, 0.87, 1.04, 0.87, 0.92, 0.91],
    'age': [32, 28, 22, 34, 28, 31, 23, 35, 24, 26],
    'worldrank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

df = pd.DataFrame(data)

# Add a new column of team name data
teams = ["Vitality", "Spirit", "MOUZ", "Aurora", "Natus Vincere",
         "G2", "The MongolZ", "FaZe", "Falcons", "Virtus.pro"]
df['teams'] = teams
print(f"In-Game Leader(IGL) stats for the world's top 10 teams \n {df}")

# Example 2

# Find players in the dataframe with rating > 1.0.
high_rating = df[df['rating'] > 1.0]

# Find players in the dataframe with age > 30
older_player = df[df['age'] > 30]

# Calculation of average age and rating
means = df.drop(columns=['ID', 'worldrank', 'teams']).mean(axis=0)


print(f"\nMean age and rating of the 10 players:\n{means}\n")
print(f"IGLs in top 10 teams with rating above 1.0: \n{high_rating}\n")
print(f"IGLs in top 10 teams age over 30:\n{older_player}\n")

# Example 3

# Ask the user how they want to sort this dataframe
while True:
    user_input = input(
        "Do you want to sort the data by using age/rating/worldrank:").strip().lower()

    if user_input == "age":
        print(df.sort_values(by='age', ascending=True))
        break

    if user_input == "rating":
        print(df.sort_values(by='rating', ascending=True))
        break

    if user_input == "worldrank":
        print(df.sort_values(by='worldrank', ascending=True))
        break
    else:
        print("Invalid input! Please enter only 'age' , 'rating', or 'worldrank'.")
        continue
