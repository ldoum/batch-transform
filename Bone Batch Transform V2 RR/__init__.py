bl_info = {
    "name": "Batch transform", 
    "blender": (2, 8, 0),
    "category": "Armature",
    "author": "Lancine Doumbia",
    "version": (2, 0, 0),  
    "location": "View3D > Sidebar", 
    "description": "Apply transform and restriction actions to an unlimited number of bones at once", 
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
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