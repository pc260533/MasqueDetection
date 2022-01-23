import matplotlib.pyplot as plt
import glob

fig = plt.figure()
for index, imageName in enumerate(glob.glob('result/detect/exp/*.jpg')[:10]):
    ax = fig.add_subplot(2, 5, index + 1)
    ax.imshow(plt.imread(imageName))
    ax.set_axis_off()

plt.show()
