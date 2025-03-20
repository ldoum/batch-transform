import bpy
from .properties import GroupOfProperties
from .operators import *

###sub panel###
class ARMATURE_MT_RotationModeMenu(bpy.types.Menu):
    """
    A custom Blender menu for selecting rotation modes.
    This acts as a dynamic dropdown. 

    """
    bl_label = "Please select:"
    bl_idname = "my_custom_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("selected_armature.set_rotation", text="XYZ").rot_type = "xyz"
        layout.operator("selected_armature.set_rotation", text="XZY").rot_type = "xzy"
        layout.operator("selected_armature.set_rotation", text="YXZ").rot_type = "yxz"
        layout.operator("selected_armature.set_rotation", text="YZX").rot_type = "yzx"
        layout.operator("selected_armature.set_rotation", text="ZXY").rot_type = "zxy"
        layout.operator("selected_armature.set_rotation", text="ZYX").rot_type = "zyx"
        layout.operator("selected_armature.set_rotation", text="Quaternion").rot_type = "quaternion"  
        
### main panel ###        
class ARMATURE_PT_Panel(bpy.types.Panel):
    """
    The main Blender panel for managing armature settings.

    This panel appears in the 'Item' tab of the 3D Viewport 
    and provides buttons to lock axes, set rotation modes, and reset transform actions of bones in an armature.

    Attributes:
        bl_label (str): The name displayed on the panel.
        bl_idname (str): The internal ID for this panel.
        bl_space_type (str): The editor where the panel appears.
        bl_region_type (str): The UI region for the panel.
        bl_category (str): The tab where the panel is placed.
    """
    bl_idname = "panelname"
    bl_label = "Batch Transform"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Item"

    def draw(self, context):
        layout = self.layout
        switch_icon = context.scene.inst.indicate
        lock_status = context.scene.inst.mode
        
        ### Batch axis locker ###
        layout.label(text="Location")
        column1 = layout.column(align=True)
        column1.operator("selected_armature.lock_axes", text="X", icon=switch_icon).axis = 'loc_x'
        column1.operator("selected_armature.lock_axes", text="Y", icon=switch_icon).axis = 'loc_y'
        column1.operator("selected_armature.lock_axes", text="Z", icon=switch_icon).axis = 'loc_z'
        
        layout.label(text="Rotation")
        column2 = layout.column(align=True)
        column2.operator("selected_armature.lock_axes", text="X", icon=switch_icon).axis = 'rot_x'
        column2.operator("selected_armature.lock_axes", text="Y", icon=switch_icon).axis = 'rot_y'
        column2.operator("selected_armature.lock_axes", text="Z", icon=switch_icon).axis = 'rot_z'
        
        layout.label(text="Scale")
        column3 = layout.column(align=True)
        column3.operator("selected_armature.lock_axes", text="X", icon=switch_icon).axis = 'scl_x'
        column3.operator("selected_armature.lock_axes", text="Y", icon=switch_icon).axis = 'scl_y'
        column3.operator("selected_armature.lock_axes", text="Z", icon=switch_icon).axis = 'scl_z'
        
        layout.label(text="")
        layout.operator("selected_armature.lock_setter", text=lock_status)
        layout.label(text="")
        
        ### Batch rotation setter ###
        layout.label(text="Rotation mode")
        layout.menu("my_custom_menu") #Go to ARMATURE_MT_RotationModeMenu
        layout.label(text="")
        
        ### Batch transform resetter###
        layout.label(text="Reset position")
        column = layout.column(align=True)
        column.operator("selected_armature.default_transform", text="Translation").reset = 1
        column.operator("selected_armature.default_transform", text="Rotation").reset = 2
        column.operator("selected_armature.default_transform", text="Scale").reset = 3
        column.operator("selected_armature.default_transform", text="All Transform").reset = 4
        layout.label(text="")
        
classes=[ARMATURE_PT_Panel, ARMATURE_MT_RotationModeMenu]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

