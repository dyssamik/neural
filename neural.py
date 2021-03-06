import numpy as np

# Сигмоида, также её производная (deriv == True)
def sigmoid(x, deriv=False):
    if deriv == True:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

# 3 входных узла и 4 тренировочных примера
x = np.array([[1, 0, 1],
              [1, 0, 1],
              [0, 1, 0],
              [0, 1, 0]])

# Выходные данные, к которым стремится программа
y = np.array([[0, 0, 1, 1]]).T

# Благодаря этому случайное распределение каждый запуск будет одним и тем же
np.random.seed(1)

# Матрица весов сети. l0 имеет размер 3, а l1 – 1. Поскольку мы связываем все узлы в l0 со всеми узлами l1, нам требуется матрица размерности (3, 1). Инициализируется случайным образом, и среднее значение равно нулю
syn0 = 2 * np.random.random((3, 1)) - 1

# Основной код тренировки сети. Цикл с кодом повторяется многократно и оптимизирует сеть для набора данных
for iter in range(10000):
    # Первый слой, просто данные
    l0 = x
    # Шаг предсказания. Позволяем сети попробовать предсказать вывод на основе ввода, затем смотрим, как это у неё получается, чтобы можно было подправить её в сторону улучшения
    l1 = sigmoid(np.dot(l0, syn0))
    # Поскольку в l1 содержатся догадки, мы можем сравнить их разницу с реальностью, вычитая её (l1) из правильного ответа (y). 
    l1_err = y - l1
    # Производная, взвешенная по ошибкам
    l1_delta = l1_err * sigmoid(l1, True)
    # Обновление весов
    syn0 += np.dot(l0.T, l1_delta)

print("Выходные данные после тренировки")
print(l1)
