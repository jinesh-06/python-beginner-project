import pandas as pd

df =pd.read_csv('Dataset/StudentsPerformance.csv')

print("First 5 rows of the dataset:")
print(df.head(5))

print("\nDataset shape:")
print(df.shape)

print("\nDataset information:")
df.info()

print("\nMissing values handling with sum():")
print(df.isnull().sum())

df = df.drop_duplicates()
print("\nDataset shape after removing duplicates:")
print(df.shape)

df["average_score"] = (df["math score"]+ df["reading score"]+ df["writing score"]) / 3
print("\nFirst 5 rows after adding average_score column:")
print(df.head(5))

print("\nGrading students based on average_score:")
df["performance"] = df["average_score"].apply(lambda score: "High" if score >= 80 else "Medium" if score >= 50 else "Low")

print("\nFirst 5 rows after adding performance column:")
print(df.head(5))

print("\nQ1: Average math score by gender")
print(df.groupby("gender")["math score"].mean().round(2))

print("\nQ2: Average score by test preparation")
print(df.groupby("test preparation course")["average_score"].mean().round(2))

print("\nQ3: Average reading score by parental education")
print(df.groupby("parental level of education")["reading score"].mean().round(2))

print("\nQ4: Average scores by lunch type")
print(df.groupby("lunch")[
    ["math score", "reading score", "writing score"]
].mean().round(2))

print("\nQ5: High-performing students")
high_performers = df[df["average_score"] >= 80]

print(high_performers[
    ["gender", "math score", "reading score",
     "writing score", "average_score", "performance"]
])

print("\nNumber of high-performing students:", len(high_performers))


df.to_csv("clean.csv", index=False)

print("\nCleaned dataset saved as clean.csv")
