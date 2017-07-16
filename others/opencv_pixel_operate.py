import cv2
import numpy as np

def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1]);
        j = int(np.random.random() * img.shape[0]);
        if img.ndim == 2:
            img[j, i] = 255
        elif img.ndim == 3:
            img[j, i, 0] = 255
            img[j, i, 1] = 255
            img[j, i, 2] = 255
    return img


if __name__ == '__main__':
    img = cv2.imread("D:\\butterfly.jpg")
    saltImage = salt(img, 500)
    cv2.imshow("Salt", saltImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#上面的代码需要注意几点：
#1、与C++不同，在Python中灰度图的img.ndim = 2，而C++中灰度图图像的通道数img.channel() =1
#2、为什么使用np.random.random()？
#这里使用了numpy的随机数，Python自身也有一个随机数生成函数。这里只是一种习惯，np.random模块中拥有更多的方法，而Python自带的random只是一个轻量级的模块。不过需要注意的是np.random.seed()不是线程安全的，而Python自带的random.seed()是线程安全的。如果使用随机数时需要用到多线程，建议使用Python自带的random()和random.seed()，或者构建一个本地的np.random.Random类的实例。