from data_loader import DataLoader

loader = DataLoader("test.csv")
df = loader.load_csv()

print("CSV loaded successfully")
print(df)


