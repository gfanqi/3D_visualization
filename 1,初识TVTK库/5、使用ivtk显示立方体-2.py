from tvtk.api import tvtk
from tvtk.tools import ivtk
from pyface.api import GUI


def ivtk_scene(actors):
    win = ivtk.IVTKWithCrustAndBrowser()
    win.open()
    win.scene.add_actor(actors)
    return win


def event_loop():
    gui = GUI()
    gui.start_event_loop()


if __name__ == '__main__':
    s = tvtk.EarthSource()
    m = tvtk.PolyDataMapper(input_connection=s.output_port)
    a = tvtk.Actor(mapper=m)
    win = ivtk_scene(a)
    event_loop()
    pass
