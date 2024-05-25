import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Создадим случайный массив с использованием NumPy
random_array = np.random.rand(5, 5)
print("Random Array:")
print(random_array)

# Создадим DataFrame с использованием Pandas
df = pd.DataFrame(data=random_array, columns=["Column1", "Column2", "Column3", "Column4", "Column5"])
print("\nDataFrame:")
print(df)

# Построим простой график с использованием Matplotlib
plt.plot(df["Column1"], label="Column1")
plt.plot(df["Column2"], label="Column2")
plt.title("Sample Plot")
plt.legend()
plt.show()
