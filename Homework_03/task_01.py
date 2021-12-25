# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean)
# среднее арифметическое, среднее квадратичное отклонение,
# смещенную и несмещенную оценки дисперсий для данной выборки.
from math import sqrt
from statistics import mean
from numpy import var
array = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]


# среднее арифметическое
my_mean = sum(array) / len(array)
print(f'среднее арифметическое {my_mean}')
# проверка
st_mean = mean(array)
print(f'среднее арифметическое {st_mean}')
"""
среднее арифметическое 65.3
"""

# смещенную и несмещенную оценки дисперсий для данной выборки.
spam = []
for el in array:
    spam.append(((el - my_mean) ** 2))
variance = sum(spam) / len(array)
print(f"смещенную оценки дисперсий {variance}")
# проверка
st_variance = var(array)
print(f"смещенную оценки дисперсий {st_variance}")
"""
смещенную оценки дисперсий 950.11
"""

variance_off = sum(spam) / (len(array) - 1)
print(f"несмещенную оценки дисперсий {round(variance_off, 2)}")
# проверка
st_variance_off = var(array, ddof=1)
print(f"несмещенную оценки дисперсий {round(st_variance_off, 2)}")
"""
несмещенную оценки дисперсий 1000.12
"""

#  среднее квадратичное отклонение
standard_deviation = sqrt(variance)
print(f"среднее квадратичное отклонение {round(standard_deviation, 2)}")
"""
среднее квадратичное отклонение 30.82
"""