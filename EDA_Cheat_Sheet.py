# Function to get counts by levels in categorical variable
def countplot(column):
    plt.figure(dpi=100)
    sns.countplot(train_data[column])
    plt.show()

