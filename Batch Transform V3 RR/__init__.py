bl_info = {
    "name": "Batch transform v3",
    "author": "Lancine Doumbia",
    "version": (3, 0, 1),
    "blender": (2, 8, 0),
    "location": "View3D > Sidebar",
    "description": "Apply transform and restriction actions to an unlimited number of objects / armature bones at once",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

from . import operators, panels, properties

def register():
    properties.register()
    panels.register()
    operators.register()

def unregister():
    panels.unregister()
    operators.unregister()
    properties.unregister()

if __name__ == "__main__":

    register()
