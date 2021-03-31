import numpy
from mayavi import mlab

s = numpy.random.random((100, 100))
img = mlab.imshow(s, colormap='gist_earth')
mlab.show()
