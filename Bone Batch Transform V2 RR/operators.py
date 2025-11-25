import bpy, math
from .properties import *

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

classes = [
    #10 ops
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

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":

    register()
