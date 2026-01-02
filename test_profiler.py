from data_loader import DataLoader
from data_profiler import DataProfiler

loader = DataLoader("test.csv")
df = loader.load_csv()

profiler = DataProfiler(df)
profile = profiler.profile()

print(profile)
