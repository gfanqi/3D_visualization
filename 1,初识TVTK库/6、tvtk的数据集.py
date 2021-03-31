from tvtk.api import tvtk
import numpy as np

# 1、ImageData 数据集
# 数据点的位置是隐式的
image = tvtk.ImageData(spacing=(1, 1, 1),
                       origin=(1, 2, 3),
                       dimensions=(3, 4, 5))
a = image.get_point(0)
# print(a)
for i in range(10):
    print(image.get_point(i))

# 2、RectilinearGrid 数据集
# 间距不均匀的网格，所有的点都在正交的网格上
x = np.array([0, 3, 9, 15])
y = np.array([0, 1, 5])
z = np.array(([0, 2, 3]))
r = tvtk.RectilinearGrid()
r.x_coordinates = x
r.y_coordinates = y
r.z_coordinates = z
r.dimensions = len(x), len(y), len(z)

# 3、StructuredGrid
# 创建任意形状的网格，需要指定点的坐标

# 4、Polydata 数据集
# 有一系列的点、点之间的联系以及有点构成的多边形组成
# 如之前所了解的 CubeSource


