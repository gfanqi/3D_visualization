from pprint import pprint

from tvtk.api import tvtk


def read_data():  # 读入数据
    plot3d = tvtk.MultiBlockPLOT3DReader(
        xyz_file_name="combxyz.bin",  # 网格文件
        q_file_name="combq.bin",  # 空气动力学结果文件
        scalar_function_number=100,  # 设置标量数据数量
        vector_function_number=200  # 设置矢量数据数量
    )
    plot3d.update()
    return plot3d


plot3d = read_data()
grid = plot3d.output.get_block(0)

pprint(dir(grid))
print(grid)
# from utils.Tvtkfunc import ivtk_scene, event_loop
#
# ivtk_scene(plot3d)
# event_loop()
