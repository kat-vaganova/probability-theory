# На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, от
# математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?

from math import sqrt
count_sigm = (190 - 178) / sqrt(25)
print(f'рост человека, равный 190 см,  отклоняется на {count_sigm} сигм(ы)')
"""
рост человека, равный 190 см,  отклоняется на 2.4 сигм(ы)
"""