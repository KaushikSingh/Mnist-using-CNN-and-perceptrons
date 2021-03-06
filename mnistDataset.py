from keras.datasets import mnist
import matplotlib.pyplot as plt
# load (downloaded if needed) the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# plot 4 images as gray scale
plt.subplot(221)
plt.imshow(X_train[2], cmap=plt.get_cmap('cool'))
plt.subplot(222)
plt.imshow(X_train[4], cmap=plt.get_cmap('Oranges'))
plt.subplot(223)
plt.imshow(X_train[5], cmap=plt.get_cmap('Purples'))
plt.subplot(224)
plt.imshow(X_train[6], cmap=plt.get_cmap('gray'))
# show the plot
plt.show()
