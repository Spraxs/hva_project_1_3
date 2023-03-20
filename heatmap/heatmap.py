import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_a = pd.read_csv("metingen/frequency_a.csv", delimiter=";")
df_b = pd.read_csv("metingen/frequency_b.csv", delimiter=";")
df_c = pd.read_csv("metingen/frequency_c.csv", delimiter=";")


def generate(dfs):
    # Create a grid of subplots with 1 row and 3 columns
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))

    fig.tight_layout(pad=2)

    for i in range(len(dfs)):
        df = dfs[i]
        df_matrix = df.pivot("x (m)", "y (m)", "nagalmtijd (s)")

        # Plot the heatmap with origin in the left corner
        sns.heatmap(df_matrix, cmap="YlGnBu", annot=True, fmt=".1f", cbar=False, ax=axs[i])
        axs[i].set_title("Heatmap " + str(i + 1))
        axs[i].set_xlabel("X-axis (m)")
        axs[i].set_ylabel("Y-axis (m)")

    # Add a colorbar for all heatmaps
    cbar = fig.colorbar(axs[0].collections[0], ax=axs, location="right", shrink=1)
    cbar.ax.set_ylabel("Nagalmtijd (s)", rotation=270, labelpad=20)

    plt.show()


generate([df_a, df_b, df_c])
