import matplotlib
import tensorflow as tf
import tensorflow.keras

# библиотека для вывода изображений
import matplotlib.pyplot as plt

# -- Импорт для построения модели: --
# импорт слоев
from tensorflow.keras import layers
from tensorflow.keras.layers import Dense, Flatten
# импорт модели
from tensorflow.keras.models import Sequential
# импорт оптимайзера
from tensorflow.keras.optimizers import Adam

# Импортируем набор данных MNIST
from tensorflow.keras.datasets import mnist

# загружаем тренировочные и тестовые данные
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Узнаем длины полученных массивов
print(len(X_train), len(y_train), len(X_test), len(y_train))

# Проверка типа и размера данных
print(X_train[0].shape, X_train[0].dtype)

# Выведем первый элемент массива на экран
print(X_train[0])

print(y_train[0])

# Выведем на экран хранящееся в X_train[0] изображение
plt.imshow(X_train[0], cmap='binary')
plt.axis('off')

# Преобразование данных в матрицах изображений
# X_train.max() возвращает значение 255
X_train = X_train/X_train.max()
X_test = X_test/X_test.max()

# Преобразуем целевые значения методом «one-hot encoding»
y_train = tensorflow.keras.utils.to_categorical(y_train, 10)
y_test = tensorflow.keras.utils.to_categorical(y_test, 10)

model = Sequential([
    layers.Dense(32, activation='relu', input_shape=(X_train[0].shape)),
    layers.Dense(64, activation='relu'),
    layers.Dense(128, activation='relu'),
    layers.Dense(256, activation='relu'),
    layers.Dense(512, activation='relu'),
    layers.Flatten(),
    layers.Dense(10, activation='sigmoid')
])
# Выведем полученную модель на экран
model.summary()

#Компиляция модели
model.compile(loss='binary_crossentropy',
            optimizer = Adam(lr=0.00024),
             metrics = ['binary_accuracy'])

# Функция ранней остановки
stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', verbose=1, patience=6)

# Запускаем обучение модели
history = model.fit(X_train, y_train, batch_size=500, verbose=1,
                    epochs= 50, validation_split = 0.2, callbacks=[stop])

# Предсказываем результат для тестовой выборки
pred = model.predict(X_test)

print(pred[0])

for i in range(len(pred)):
    for j in range(10):
        if(pred[i][j]>0.5):
            pred[i][j]=1
        else:
            pred[i][j]=0

print(pred[3], y_test[3])