import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("nolan_movies.csv")

df["Box_Office_Billion"] = df["Box_Office_USD"] / 1e8

fig, axes = plt.subplots(3, 1, figsize=(10, 15), sharex=True)

axes[0].bar(df["Movie"], df["Running_Time_Minutes"], color="skyblue", alpha=0.7, label="Running Time (min)")
axes[0].plot(df["Movie"], df["Running_Time_Minutes"], color="blue", marker="o", label="Trend")
axes[0].set_ylabel("Minutes")
axes[0].set_title("Running Time of Nolan Movies")
axes[0].legend()

axes[1].bar(df["Movie"], df["Box_Office_Billion"], color="lightgreen", alpha=0.7, label="Box Office (100M USD)")
axes[1].plot(df["Movie"], df["Box_Office_Billion"], color="green", marker="o", label="Trend")
axes[1].set_ylabel("Box Office (100M USD)")
axes[1].set_title("Box Office of Nolan Movies")
axes[1].legend()

axes[2].bar(df["Movie"], df["Rotten_Tomatoes_Score"], color="salmon", alpha=0.7, label="Rotten Tomatoes Score (%)")
axes[2].plot(df["Movie"], df["Rotten_Tomatoes_Score"], color="red", marker="o", label="Trend")
axes[2].set_ylabel("Score (%)")
axes[2].set_title("Rotten Tomatoes Score of Nolan Movies")
axes[2].legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
