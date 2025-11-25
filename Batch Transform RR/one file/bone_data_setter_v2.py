"""

1000pm 10/11/2025 Saturday
Update my code for the bone batch data transform applier add-on.

1. Removed the transform resetter feature.
2. Added more properties. 23 total.
3. Remove the ARMATURE_MT_RotationModeMenu and replace with a dropdown
4. Removed the rot_type attribute in ARMATURE_OT_SetRotationMode
5. Added poll function to panel to make it appear when an armature is selected and in pose mode
6. Removing ARMATURE_OT_SetRotationMode class as the dropdown paired with the function rotation_status does the work for me
7. Reduced 57 lines of match case decision code down to 3 lines of bool tuples for ARMATURE_OT_Lock_Bone_Axes
8. Removed axis local variable in ARMATURE_OT_Lock_Bone_Axes
9. Renamed ARMATURE_OT_Lock_Bone_Axes to ARMATURE_OT_Apply_Bone_Transform and will make it apply transform data by the press of the button
10. Deleted ARMATURE_OT_AxisLockSetter. The operator was a helper operator of the former ARMATURE_OT_LockBoneAxes class

1114pm 10/12/2025 Sunday
Code update done!

"""
import bpy, math


def rotation_status(self, context):
    print(f"Rotation mode set to {self.rotation}")

class BoneTransformData(bpy.types.PropertyGroup):
 
    #locks
    
    #location [3]
    x_lock_locate: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to lock.", 
        default=False
    )
    y_lock_locate: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to lock.", 
        default=False
    )
    z_lock_locate: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to lock.", 
        default=False
    )
    
    #rotation [6]
    x_lock_rotate: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to lock.", 
        default=False
    )
    y_lock_rotate: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to lock.", 
        default=False
    )
    z_lock_rotate: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to lock.", 
        default=False
    )
    
    #scale [9]
    x_lock_scale: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to lock.", 
        default=False
    )
    y_lock_scale: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to lock.", 
        default=False
    )
    z_lock_scale: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to lock.", 
        default=False
    )
    
    #location properties  [12]   
    x_val_locate: bpy.props.FloatProperty(
        name="X",
        description="An example float property",
        default=0.00,
        min=-100000.00,
        max=100000.00
    )
    y_val_locate: bpy.props.FloatProperty(
        name="Y",
        description="An example float property",
        default=0.00,
        min=-100000.00,
        max=100000.00
    )
    z_val_locate: bpy.props.FloatProperty(
        name="Z",
        description="An example float property",
        default=0.00,
        min=-100000.00,
        max=100000.00
    )
    
    #rotation properties euler [15]
    x_val_rotate_euler: bpy.props.FloatProperty(
        name="X",
        description="An example float property",
        default=0.00,
        min=-360.00,
        max=360.00
    )
    y_val_rotate_euler: bpy.props.FloatProperty(
        name="Y",
        description="An example float property",
        default=0.00,
        min=-360.00,
        max=360.00
    )
    z_val_rotate_euler: bpy.props.FloatProperty(
        name="Z",
        description="An example float property",
        default=0.00,
        min=-360.00,
        max=360.00
    )
    
    #rotation properties quaternion [19]
    w_val_rotate_quaternion: bpy.props.FloatProperty(
        name="W",
        description="An example float property",
        default=1.00,
        min=-1.00,
        max=1.00
    )
    x_val_rotate_quaternion: bpy.props.FloatProperty(
        name="X",
        description="An example float property",
        default=0.00,
        min=-1.00,
        max=1.00
    )
    y_val_rotate_quaternion: bpy.props.FloatProperty(
        name="Y",
        description="An example float property",
        default=0.00,
        min=-1.00,
        max=1.00
    )
    z_val_rotate_quaternion: bpy.props.FloatProperty(
        name="Z",
        description="An example float property",
        default=0.00,
        min=-1.00,
        max=1.00
    )
    
    #scale properties [22]   
    x_val_scale: bpy.props.FloatProperty(
        name="X",
        description="An example float property",
        default=1.00,
        min=-100000.00,
        max=100000.00
    )
    y_val_scale: bpy.props.FloatProperty(
        name="Y",
        description="An example float property",
        default=1.00,
        min=-100000.00,
        max=100000.00
    )
    z_val_scale: bpy.props.FloatProperty(
        name="Z",
        description="An example float property",
        default=1.00,
        min=-100000.00,
        max=100000.00
    )    
        
    ### new prop. [23]  
    rotation: bpy.props.EnumProperty(
        name="Mode",
        description="Choose rotation mode for selected bones",
        items=[
            ('XYZ', "XYZ Euler", "Set rotation mode to XYZ Euler"),
            ('XZY', "XZY Euler", "Set rotation mode to XZY Euler"),
            ('YXZ', "YXZ Euler", "Set rotation mode to YXZ Euler"),
            ('YZX', "YZX Euler", "Set rotation mode to YZX Euler"),
            ('ZXY', "ZXY Euler", "Set rotation mode to ZXY Euler"),
            ('ZYX', "ZYX Euler", "Set rotation mode to ZYX Euler"),
            ('QUATERNION', "Quaternion", "Set rotation mode to Quaternion")
        ],
        default='QUATERNION',
        update=rotation_status,
        
)

###################################################
###################################################

####################OPERATORS###################

#mixin
class BaseOperator:
    bl_options = {
        "REGISTER",
        "UNDO"
    }
    
    @property
    def prop_t(self):
        return bpy.context.scene.inst

################lock buttons
 
class ARMATURE_OT_Toggle_Location_X_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.loc_x_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.x_lock_locate = not self.prop_t.x_lock_locate
        return {'FINISHED'}
 
class ARMATURE_OT_Toggle_Location_Y_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.loc_y_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.y_lock_locate = not self.prop_t.y_lock_locate
        return {'FINISHED'}
        
class ARMATURE_OT_Toggle_Location_Z_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.loc_z_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.z_lock_locate = not self.prop_t.z_lock_locate   
        return {'FINISHED'}

        
class ARMATURE_OT_Toggle_Rotation_X_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_x_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.x_lock_rotate = not self.prop_t.x_lock_rotate
        return {'FINISHED'}

class ARMATURE_OT_Toggle_Rotation_Y_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_y_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.y_lock_rotate = not self.prop_t.y_lock_rotate
        return {'FINISHED'}
    
class ARMATURE_OT_Toggle_Rotation_Z_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_z_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.z_lock_rotate = not self.prop_t.z_lock_rotate  
        return {'FINISHED'}

        
class ARMATURE_OT_Toggle_Scale_X_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.scl_x_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.x_lock_scale = not self.prop_t.x_lock_scale
        return {'FINISHED'}
    
class ARMATURE_OT_Toggle_Scale_Y_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.scl_y_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.y_lock_scale = not self.prop_t.y_lock_scale
        return {'FINISHED'}
    
class ARMATURE_OT_Toggle_Scale_Z_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.scl_z_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.z_lock_scale = not self.prop_t.z_lock_scale          
        return {'FINISHED'}
    

class ARMATURE_OT_Apply_Bone_Transform(BaseOperator, bpy.types.Operator):
    """
    This operator locks N number of bones in an armature at once. Ignores W axis if included bones are in quaternion mode.
    """
    bl_idname = "armature.apply_transform"
    bl_label = "Apply transform of bones"
    bl_description = "Press to format"
    
    def execute(self, context):
       
        selected_bones = context.selected_pose_bones 
    
        for bone in selected_bones: 
            
            #location data
            bone.lock_location = (self.prop_t.x_lock_locate, self.prop_t.y_lock_locate, self.prop_t.z_lock_locate)
            bone.location = (self.prop_t.x_val_locate, self.prop_t.y_val_locate, self.prop_t.z_val_locate)
            
            #rotation data 
            bone.lock_rotation = (self.prop_t.x_lock_rotate, self.prop_t.y_lock_rotate, self.prop_t.z_lock_rotate)
            
            if self.prop_t.rotation != "QUATERNION":
                bone.rotation_euler = (math.radians(self.prop_t.x_val_rotate_euler), math.radians(self.prop_t.y_val_rotate_euler), math.radians(self.prop_t.z_val_rotate_euler))
            else:
                bone.rotation_quaternion = (self.prop_t.w_val_rotate_quaternion, self.prop_t.x_val_rotate_quaternion, self.prop_t.y_val_rotate_quaternion, self.prop_t.z_val_rotate_quaternion)
            
            bone.rotation_mode = self.prop_t.rotation
            
            #scale data
            bone.lock_scale = (self.prop_t.x_lock_scale, self.prop_t.y_lock_scale, self.prop_t.z_lock_scale) 
            bone.scale = (self.prop_t.x_val_scale, self.prop_t.y_val_scale, self.prop_t.z_val_scale)
            
        return {"FINISHED"}

#####################################################

class BasePanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Item"
    
    #make panel visible if item selected is an armature and you're in pose mode.
    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return obj and obj.type == 'ARMATURE' and context.mode == 'POSE'

    
class ARMATURE_PT_Panel(BasePanel, bpy.types.Panel):
    
    bl_idname = "panelname"
    bl_label = "Bone Batch Transform"
    
    def draw(self, context):
        layout = self.layout
        inst = context.scene.inst 
        
        ### Batch axis locker ###
        layout.label(text="Location")
        
        row1 = layout.row(align=True)
        column1 = row1.column(align=True) #floats
        column2 = row1.column(align=True) #lock buttons
        
        column1.prop(inst, "x_val_locate")
        column1.prop(inst, "y_val_locate")
        column1.prop(inst, "z_val_locate")
        
        column2.operator("armature.loc_x_lock", text="", icon="LOCKED" if inst.x_lock_locate else "UNLOCKED", depress=inst.x_lock_locate)
        column2.operator("armature.loc_y_lock", text="", icon="LOCKED" if inst.y_lock_locate else "UNLOCKED", depress=inst.y_lock_locate)
        column2.operator("armature.loc_z_lock", text="", icon="LOCKED" if inst.z_lock_locate else "UNLOCKED", depress=inst.z_lock_locate)
        
        ##########################################################################
        layout.label(text="Rotation")
        
        row2A = layout.row(align=True) #w axis row
        row2B = layout.row(align=True) #rest of the grid; 1 row, 2 columns 
        
        column3 = row2B.column(align=True) #floats
        column4 = row2B.column(align=True) #lock buttons
        
        if inst.rotation == 'QUATERNION':
            row2A.prop(inst, "w_val_rotate_quaternion")
            column3.prop(inst, "x_val_rotate_quaternion")
            column3.prop(inst, "y_val_rotate_quaternion")
            column3.prop(inst, "z_val_rotate_quaternion")
        else:
            column3.prop(inst, "x_val_rotate_euler")
            column3.prop(inst, "y_val_rotate_euler")
            column3.prop(inst, "z_val_rotate_euler")
            
        column4.operator("armature.rot_x_lock", text="", icon="LOCKED" if inst.x_lock_rotate else "UNLOCKED", depress=inst.x_lock_rotate)
        column4.operator("armature.rot_y_lock", text="", icon="LOCKED" if inst.y_lock_rotate else "UNLOCKED", depress=inst.y_lock_rotate)
        column4.operator("armature.rot_z_lock", text="", icon="LOCKED" if inst.z_lock_rotate else "UNLOCKED", depress=inst.z_lock_rotate)
        
        
        ### Batch rotation setter ###
        layout.prop(inst, "rotation")
        
        ##########################################################################
        layout.label(text="Scale")
        row3 = layout.row(align=True)
        column5 = row3.column(align=True) #floats
        column6 = row3.column(align=True) #lock buttons
        
        column5.prop(inst, "x_val_scale")
        column5.prop(inst, "y_val_scale")
        column5.prop(inst, "z_val_scale")
        
        column6.operator("armature.scl_x_lock", text="", icon="LOCKED" if inst.x_lock_scale else "UNLOCKED", depress=inst.x_lock_scale)
        column6.operator("armature.scl_y_lock", text="", icon="LOCKED" if inst.y_lock_scale else "UNLOCKED", depress=inst.y_lock_scale)
        column6.operator("armature.scl_z_lock", text="", icon="LOCKED" if inst.z_lock_scale else "UNLOCKED", depress=inst.z_lock_scale)
        
        
        layout.operator("armature.apply_transform", text="Apply") #press when done
        
        
         
classes = [

BoneTransformData, 

ARMATURE_PT_Panel, 

#10 operators
ARMATURE_OT_Apply_Bone_Transform, 
ARMATURE_OT_Toggle_Location_X_Lock,
ARMATURE_OT_Toggle_Location_Y_Lock,
ARMATURE_OT_Toggle_Location_Z_Lock,
ARMATURE_OT_Toggle_Rotation_X_Lock,
ARMATURE_OT_Toggle_Rotation_Y_Lock,  
ARMATURE_OT_Toggle_Rotation_Z_Lock,      
ARMATURE_OT_Toggle_Scale_X_Lock,
ARMATURE_OT_Toggle_Scale_Y_Lock,
ARMATURE_OT_Toggle_Scale_Z_Lock,

]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.inst = bpy.props.PointerProperty(type=BoneTransformData)
    
def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.inst

if __name__ == "__main__":
    register()
