import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("students.csv")
print(data)
plt.bar(data["Name"],data["Average"])
plt.show()
plt.hist(data["Maths],bins=5)
         plt.show()
