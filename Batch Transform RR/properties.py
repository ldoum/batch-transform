import bpy

class GroupOfProperties(bpy.types.PropertyGroup):
    """
    This property group stores properties for the operators to share.

    Classes that use these properties:
        ARMATURE_OT_LockBoneAxes: activate
        ARMATURE_OT_AxisLockSetter: activate, mode, indicate

    """
    activate: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to lock.", 
        default=False #match
        )
    mode: bpy.props.StringProperty(
        name="Lock/Unlock mode", 
        description="Tells you if buttons are set to lock or not.", 
        default="Lock"
        )
    indicate: bpy.props.StringProperty(
        name="Icon switch", 
        description="Dynamic icon switching", 
        default="UNLOCKED" #match
        )

def register():
    bpy.utils.register_class(GroupOfProperties)
    bpy.types.Scene.inst = bpy.props.PointerProperty(type=GroupOfProperties)
    
def unregister():
    bpy.utils.unregister_class(GroupOfProperties)
    del bpy.types.Scene.inst