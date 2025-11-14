import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#ex1
def numpy_array():
    arr = np.arange(1, 101, 5)
    print(arr)

#ex2
def mean_median_deviation(data):
    mean = np.mean(data)
    median = np.median(data)
    deviation = np.std(data)

    print(f"Данные: {data} \n Среднее {mean} \n Медиана: {median} \n Стандартное отклонение {deviation}")

#ex3
def csv(file):
    csv = pd.read_csv(file)
    df = pd.DataFrame(csv)
    print(df.describe())

#ex4
def histograms():
    plt.figure(figsize=(10, 6))
    random_data = np.random.normal(0, 1, 10000)
    plt.hist(random_data, bins=30, alpha=0.7, color='blue', edgecolor='black')
    plt.title('Гистограмма распределения случайных чисел (задание 4)')
    plt.xlabel('Значения')
    plt.ylabel('Частота')
    plt.grid(True, alpha=0.3)
    plt.show()

#ex5
def chart():
    plt.figure(figsize=(10, 6))
    x = np.linspace(-10, 10, 100)
    y = x**2
    plt.plot(x, y, 'r-', linewidth=2)
    plt.title('y = x^2 (задание 5)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

#ex6
def dataframe_merge(df1, df2):
    merged = pd.merge(df1, df2, on="ID")
    print (merged)


#ex7
def numpy_matrix(matrix_a, matrix_b):
    matrix_sum = matrix_a + matrix_b
    matrix_product = np.dot(matrix_a, matrix_b)
    print(f"Cумма матриц: \n {matrix_sum} \n Произведение матриц: \n {matrix_product}")

#ex8
def curves():
    plt.figure(figsize=(10, 6))
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) * np.cos(x)

    plt.plot(x, y1, label='sin(x)', linewidth=2)
    plt.plot(x, y2, label='cos(x)', linewidth=2)
    plt.plot(x, y3, label='sin(x)*cos(x)', linewidth=2)

    plt.title('График с несколькими кривыми (задание 8)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

#ex9
def filtering(file):
    csv = pd.read_csv(file)
    df = pd.DataFrame(csv)
    filtered_data = df[(df['Age'] > 28) & (df['Salary'] > 55000)]
    print(filtered_data)

#ex10
def scatterplot():
    plt.figure(figsize=(10, 6))
    x_scatter = np.random.normal(0, 1, 100)
    y_scatter = np.random.normal(0, 1, 100) + 0.5 * x_scatter + np.random.normal(0, 0.3, 100)

    plt.title('Диаграмма рассеяния для случайного набора данных (задание 10)')
    plt.scatter(x_scatter, y_scatter, alpha=0.6, c='green', edgecolors='black')
    plt.xlabel('X значения')
    plt.ylabel('Y значения')
    plt.grid(True, alpha=0.3)
    plt.show()

numpy_array()
data = np.array([23, 45, 67, 12, 89, 34, 56, 78, 90, 15])
mean_median_deviation(data)

csv("data.csv")

histograms()

chart()

df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28]
})
df2 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Salary': [50000, 60000, 70000, 55000],
    'Department': ['IT', 'HR', 'IT', 'Finance']
})

dataframe_merge(df1, df2)

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

numpy_matrix(matrix_a, matrix_b)

curves()

filtering("data.csv")

scatterplot()
