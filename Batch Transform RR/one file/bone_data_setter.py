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
        default=False
        )
    mode: bpy.props.StringProperty(
        name="Lock/Unlock mode", 
        description="Tells you if buttons are set to lock or not.", 
        default="Unlock"
        )
    indicate: bpy.props.StringProperty(
        name="Icon switch", 
        description="Dynamic icon switching", 
        default="UNLOCKED"
        )

###################################################

#class1
class ARMATURE_OT_AxisLockSetter(bpy.types.Operator):
    """
    This operator toggles the mode of the lock buttons.
    This operator is a helper operator of the ARMATURE_OT_LockBoneAxes class

    Features:
    Updates the string values of mode and indicate properties for the ARMATURE_OT_LockBoneAxes operator
    - dynamic self report message
    - dynamic icon indication
    """
    bl_idname = "selected_armature.lock_setter"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    bl_options = {
        "REGISTER",
        "UNDO"
    }
    
    def execute(self, context):
        set = context.scene.inst
        
        set.activate = not set.activate #set mode when button for operator is pressed
        set.mode = 'Unlock' if set.activate else 'Lock' #dynamic label
        set.indicate = 'LOCKED' if set.activate else 'UNLOCKED' #dynamic icon
        
        self.report({'INFO'}, f"{'Lock' if set.activate else 'Unlock'}") #inform user of locking status
        
        return {"FINISHED"}

#class2
class ARMATURE_OT_LockBoneAxes(bpy.types.Operator):
    """
    This operator locks N number of bones in an armature at once. Ignores W axis if included bones are in quaternion mode.
    """
    bl_idname = "selected_armature.lock_axes"
    bl_label = "Lock axes of bones"
    bl_description = "Click to lock. Click again to unlock."
    bl_options = {
        "REGISTER",
        "UNDO"
    }
    
    axis: bpy.props.StringProperty() #retrieve axis id

    def execute(self, context):
       
        set_lock = context.scene.inst.activate #retrieves bool value
        
        selected_bones = context.selected_pose_bones 
    
        for bone in selected_bones: #perform action on each bone. If set_lock is True, lock. If not, unlock
            match(self.axis):
                case 'loc_x': #button 1A
                    bone.lock_location[0] = set_lock
                    self.report({'INFO'}, f"X Location axe(s) {'lock' if set_lock else 'unlock'}ed")
                case 'loc_y': #button 1B
                    bone.lock_location[1] = set_lock
                    self.report({'INFO'}, f"Y Location axe(s) {'lock' if set_lock else 'unlock'}ed")
                case 'loc_z': #button 1C
                    bone.lock_location[2] = set_lock
                    self.report({'INFO'}, f"Z Location axe(s) {'lock' if set_lock else 'unlock'}ed")
                case 'rot_x': #button 2A
                    bone.lock_rotation[0] = set_lock
                    self.report({'INFO'}, f"X Rotation axe(s) {'lock' if set_lock else 'unlock'}ed")
                case 'rot_y': #button 2B
                    bone.lock_rotation[1] = set_lock
                    self.report({'INFO'}, f"Y Rotation axe(s) {'lock' if set_lock else 'unlock'}ed")
                case 'rot_z': #button 2C
                    bone.lock_rotation[2] = set_lock
                    self.report({'INFO'}, f"Z Rotation axe(s) {'lock' if set_lock else 'unlock'}ed")
                case 'scl_x': #button 3A
                    bone.lock_scale[0] = set_lock
                    self.report({'INFO'}, f"X Scale axe(s) {'lock' if set_lock else 'unlock'}ed")
                case 'scl_y': #button 3B
                    bone.lock_scale[1] = set_lock
                    self.report({'INFO'}, f"Y Scale axe(s) {'lock' if set_lock else 'unlock'}ed")
                case 'scl_z': #button 3C
                    bone.lock_scale[2] = set_lock
                    self.report({'INFO'}, f"Z Scale axe(s) {'lock' if set_lock else 'unlock'}ed")
                case _:  
                    pass

        return {"FINISHED"}


####################################################
#class3
class ARMATURE_OT_SetRotationMode(bpy.types.Operator):
    """
    This operator sets the mode of rotation for the bones. Includes quaternion mode.

    """
    bl_idname = "selected_armature.set_rotation"
    bl_label = "Set rotation mode"
    bl_description = "Description that shows in blender tooltips"
    bl_options = {
        "REGISTER",
        "UNDO"
    }
    rot_type: bpy.props.StringProperty()  #retrieve rotation type id
    
    def execute(self, context):

        selected_bones = bpy.context.selected_pose_bones
        for bone in selected_bones:
            match(self.rot_type):
                case 'xyz': #option 1
                    bone.rotation_mode = 'XYZ'
                    self.report({'INFO'}, f"Rotation mode set to {bone.rotation_mode} Euler")
                case 'xzy': #option 2
                    bone.rotation_mode = 'XZY'
                    self.report({'INFO'}, f"Rotation mode set to {bone.rotation_mode} Euler")
                case 'yxz': #option 3
                    bone.rotation_mode = 'YXZ'
                    self.report({'INFO'}, f"Rotation mode set to {bone.rotation_mode} Euler")
                case 'yzx': #option 4
                    bone.rotation_mode = 'YZX'
                    self.report({'INFO'}, f"Rotation mode set to {bone.rotation_mode} Euler")
                case 'zxy': #option 5
                    bone.rotation_mode = 'ZXY'
                    self.report({'INFO'}, f"Rotation mode set to {bone.rotation_mode} Euler")
                case 'zyx': #option 6
                    bone.rotation_mode = 'ZYX'
                    self.report({'INFO'}, f"Rotation mode set to {bone.rotation_mode} Euler") 
                case 'quaternion': #option 7
                    bone.rotation_mode = 'QUATERNION'
                    self.report({'INFO'}, f"Rotation mode set to {bone.rotation_mode}")
                case _:
                    self.report({'INFO'}, f"Invalid rotation mode")  
                    pass

        return {"FINISHED"}

#class4
class ARMATURE_OT_TransformResetter(bpy.types.Operator):
    """
    This operator resets transform data of selected bones to their default values.

    """
    bl_idname = "selected_armature.default_transform"
    bl_label = "Transform Resetter"
    bl_description = "Description that shows in blender tooltips"
    bl_options = {
        "REGISTER",
        "UNDO"
    }
    
    reset: bpy.props.IntProperty() #retrieve number id for type of transform reset

    def execute(self, context):

        match(self.reset):
            case 1:
                #button 1
                bpy.ops.pose.loc_clear() 
                self.report({'INFO'}, "Location reset") 
            case 2:
                #button 2
                bpy.ops.pose.rot_clear()
                self.report({'INFO'}, "Rotation reset")

            case 3:
                #button 3
                bpy.ops.pose.scale_clear()
                self.report({'INFO'}, "Scale reset")

            case 4:
                #button 4
                bpy.ops.pose.loc_clear()   
                bpy.ops.pose.rot_clear()
                bpy.ops.pose.scale_clear()
                self.report({'INFO'}, "All transforms reset")
            case _:  
                self.report({'INFO'}, "Invalid reset id")
        
        return {"FINISHED"}

#####################################################
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
        

bl_info = {
    "name": "Batch transform", 
    "blender": (2, 8, 0),
    "category": "Armature",
    "author": "Lancine Doumbia",
    "version": (1, 0, 0), 
    "location": "View3D > Sidebar", 
    "description": "Apply transform and restriction actions to an unlimited number of bones at once", 
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
}

classes = [GroupOfProperties, ARMATURE_PT_Panel, ARMATURE_MT_RotationModeMenu, ARMATURE_OT_TransformResetter, ARMATURE_OT_SetRotationMode, ARMATURE_OT_LockBoneAxes, ARMATURE_OT_AxisLockSetter]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.inst = bpy.props.PointerProperty(type=GroupOfProperties)
    
def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.inst

if __name__ == "__main__":
    register()
