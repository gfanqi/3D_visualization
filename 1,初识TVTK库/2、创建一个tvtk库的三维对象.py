from tvtk.api import tvtk
from pprint import pprint

# 立方体
# pprint(dir(tvtk))


for item in dir(tvtk):
    if item.endswith("Source"):
        print(item)
'''
AMRGaussianPulseSource
ArcSource 圆弧
ArrowSource 箭头
BoundedPointSource
ButtonSource
CapsuleSource 
CellTypeSource
ConeSource 圆锥
CubeSource 立方体
CylinderSource 圆柱
DiagonalMatrixSource
DiskSource
EarthSource
EllipseArcSource
EllipticalButtonSource
EnsembleSource
FrustumSource
HyperTreeGridSource
ImageEllipsoidSource
ImageGaussianSource
ImageGridSource
ImageMandelbrotSource
ImageNoiseSource
ImageSinusoidSource
ImageStencilSource
LassoStencilSource
LineSource
OutlineCornerSource
OutlineSource
PSphereSource
ParametricFunctionSource
PipelineGraphSource
PlaneSource
PlatonicSolidSource
PointSource
PolyLineSource
PolyPointSource
ProgrammableDataObjectSource
ProgrammableSource
ROIStencilSource
RTAnalyticSource
RandomGraphSource
RandomHyperTreeGridSource
RectangularButtonSource
RegularPolygonSource
RendererSource
SQLDatabaseTableSource
SectorSource
SelectionSource
SphereSource
SuperquadricSource
TessellatedBoxSource
TextSource
TexturedSphereSource
UniformHyperTreeGridSource
VideoSource
VolumeOutlineSource
Win32VideoSource
'''

# 立方体
s1 = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
# 圆锥
s2 = tvtk.ConeSource(center=(1, 5, 6))
# pprint(dir(s2))
print(s2)
a = 1
# a.__getattribute__()
# # a.__se
# a.__get
# 显示一个三维度对象
for item in dir(tvtk):
    if not item.endswith("Source"):continue
    try:
        s2 = tvtk.__getattribute__(item)()
        if not hasattr(s2,"output_port"):print(item);continue
        print("on:",item)
        # pprint(dir(s2.output_port))
        m = tvtk.PolyDataMapper(input_connection=s2.output_port)
        a = tvtk.Actor(mapper=m)
        # b = tvtk.Actor(mapper =  tvtk.PolyDataMapper(input_connection=s1.output_port))
        r = tvtk.Renderer(background=(0, 0, 0))
        r.add_actor(a)
        # r.add_actor(b)
        w = tvtk.RenderWindow(size=(500, 500))
        w.add_renderer(r)
        i = tvtk.RenderWindowInteractor(render_window=w)
        # i.initialize()
        i.start()
    except:
        pass
# class