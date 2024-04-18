    import matplotlib.pyplot as plt
    import pandas as pd
    
    data = pd.read_csv("cbb.csv")
    average_winning_ratio = data.groupby('TEAM')['W'].mean()
    top_5_teams = average_winning_ratio.nlargest(5)
    plt.figure(figsize=(10, 6))
    plt.pie(top_5_teams, labels=top_5_teams.index, autopct='%1.1f%%', startangle=140)
    plt.title('Top 5 Teams with Highest Winning Ratio')
    plt.axis('equal')
    plt.show()