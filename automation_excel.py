

import pandas as pd
# خواندن فایل و چاپ کردن آن در ترمینال برای دیدن ستون‌های جدید
df = pd.read_excel("customers.xlsx")
print(df[["Customer Name", "System Status", "AI Final Response"]])
