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
    
    #new. Encapsulating this code to make add-on have ability to apply transform to objects and armature bones. Combining both add-ons into 1.
    def apply_transform(self, selected):
        for item in selected: 
            
            #location data
            item.lock_location = (
                self.prop_t.x_lock_locate, 
                self.prop_t.y_lock_locate, 
                self.prop_t.z_lock_locate
            )
            
            if self.prop_t.x_locate_field_on:
                item.location[0] = self.prop_t.x_val_locate
            if self.prop_t.y_locate_field_on:
                item.location[1] = self.prop_t.y_val_locate
            if self.prop_t.z_locate_field_on:
                item.location[2] = self.prop_t.z_val_locate
            
            
            #rotation data 
            item.lock_rotation = (self.prop_t.x_lock_rotate, self.prop_t.y_lock_rotate, self.prop_t.z_lock_rotate)
            
            if self.prop_t.rotation_m != "QUATERNION":
                
                if self.prop_t.x_rotate_field_on:
                    item.rotation_euler[0] = math.radians(self.prop_t.x_val_rotate_euler)
                    
                if self.prop_t.y_rotate_field_on:
                    item.rotation_euler[1] = math.radians(self.prop_t.y_val_rotate_euler)
                    
                if self.prop_t.z_rotate_field_on:
                    item.rotation_euler[2] = math.radians(self.prop_t.z_val_rotate_euler)  
                
            else:
                
                if self.prop_t.w_rotate_field_on:
                    item.rotation_quaternion[0] = self.prop_t.w_val_rotate_quaternion
                
                if self.prop_t.x_rotate_field_on:
                    item.rotation_quaternion[1] = self.prop_t.x_val_rotate_quaternion

                if self.prop_t.y_rotate_field_on:
                    item.rotation_quaternion[2] = self.prop_t.y_val_rotate_quaternion

                if self.prop_t.z_rotate_field_on:
                    item.rotation_quaternion[3] = self.prop_t.z_val_rotate_quaternion 
            
            
            item.rotation_mode = self.prop_t.rotation_m
            
            #scale data
            item.lock_scale = (
                self.prop_t.x_lock_scale, 
                self.prop_t.y_lock_scale, 
                self.prop_t.z_lock_scale
            ) 
        
            if self.prop_t.x_scale_field_on:
                item.scale[0] = self.prop_t.x_val_scale
                
            if self.prop_t.y_scale_field_on:
                item.scale[1] = self.prop_t.y_val_scale
                
            if self.prop_t.z_scale_field_on:
                item.scale[2] = self.prop_t.z_val_scale
            
            
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

########### enable buttons
 
class ARMATURE_OT_Activate_Location_X_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.loc_x_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.x_locate_field_on = not self.prop_t.x_locate_field_on
        return {'FINISHED'}
 
class ARMATURE_OT_Activate_Location_Y_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.loc_y_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.y_locate_field_on = not self.prop_t.y_locate_field_on
        return {'FINISHED'}
        
class ARMATURE_OT_Activate_Location_Z_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.loc_z_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.z_locate_field_on = not self.prop_t.z_locate_field_on   
        return {'FINISHED'}

class ARMATURE_OT_Activate_Rotation_W_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_w_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.w_rotate_field_on = not self.prop_t.w_rotate_field_on
        return {'FINISHED'}
        
class ARMATURE_OT_Activate_Rotation_X_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_x_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.x_rotate_field_on = not self.prop_t.x_rotate_field_on
        return {'FINISHED'}

class ARMATURE_OT_Activate_Rotation_Y_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_y_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.y_rotate_field_on = not self.prop_t.y_rotate_field_on
        return {'FINISHED'}
    
class ARMATURE_OT_Activate_Rotation_Z_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_z_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.z_rotate_field_on = not self.prop_t.z_rotate_field_on  
        return {'FINISHED'}

        
class ARMATURE_OT_Activate_Scale_X_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.scl_x_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.x_scale_field_on = not self.prop_t.x_scale_field_on
        return {'FINISHED'}
    
class ARMATURE_OT_Activate_Scale_Y_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.scl_y_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.y_scale_field_on = not self.prop_t.y_scale_field_on
        return {'FINISHED'}
    
class ARMATURE_OT_Activate_Scale_Z_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.scl_z_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.z_scale_field_on = not self.prop_t.z_scale_field_on          
        return {'FINISHED'}    
    
    
    
##############################

class ARMATURE_OT_Apply_Bone_Transform(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.apply_bone_transform"
    bl_label = "Apply transform of bones"
    bl_description = "Press to format"
    
    #added this
    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return obj and obj.type == 'ARMATURE' and context.mode == 'POSE'
    
    def execute(self, context):
       
        self.apply_transform(context.selected_pose_bones)
        
        return {"FINISHED"}
    
class OBJECT_OT_Apply_Object_Transform(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.apply_obj_transform"
    bl_label = "Apply transform of objects"
    bl_description = "Press to format"
    
    def execute(self, context):
       
        self.apply_transform(context.selected_objects)
        
        return {"FINISHED"}
    
class OBJECT_OT_Reset_Transform(BaseOperator, bpy.types.Operator):
    bl_idname = "object.reset_transform"
    bl_label = "Apply transform of bones"
    bl_description = "Press to format"
    
    def execute(self, context):
        
        ### reset locks
        self.prop_t.x_lock_locate = False
        self.prop_t.y_lock_locate = False
        self.prop_t.z_lock_locate = False
        
        self.prop_t.x_lock_rotate = False
        self.prop_t.y_lock_rotate = False
        self.prop_t.z_lock_rotate = False
        
        self.prop_t.x_lock_scale = False
        self.prop_t.y_lock_scale = False
        self.prop_t.z_lock_scale = False
        
        ### reset enable
        self.prop_t.x_locate_field_on = False
        self.prop_t.y_locate_field_on = False
        self.prop_t.z_locate_field_on = False
        
        self.prop_t.w_rotate_field_on = False
        
        self.prop_t.x_rotate_field_on = False
        self.prop_t.y_rotate_field_on = False
        self.prop_t.z_rotate_field_on = False
        
        self.prop_t.x_scale_field_on = False
        self.prop_t.y_scale_field_on = False
        self.prop_t.z_scale_field_on = False
        
        ### reset fields
        self.prop_t.x_val_locate = 0.00
        self.prop_t.y_val_locate = 0.00
        self.prop_t.z_val_locate = 0.00 
        
        self.prop_t.x_val_rotate_euler = 0.00 
        self.prop_t.y_val_rotate_euler = 0.00 
        self.prop_t.z_val_rotate_euler = 0.00 
        
        self.prop_t.w_val_rotate_quaternion = 1.00 
        self.prop_t.x_val_rotate_quaternion = 0.00 
        self.prop_t.y_val_rotate_quaternion = 0.00 
        self.prop_t.z_val_rotate_quaternion = 0.00 
        
        self.prop_t.rotation_m = 'QUATERNION'
        
        self.prop_t.x_val_scale = 1.00
        self.prop_t.y_val_scale = 1.00
        self.prop_t.z_val_scale = 1.00
        
        return {"FINISHED"}

classes = [
    
#22 operators
ARMATURE_OT_Apply_Bone_Transform, 
OBJECT_OT_Apply_Object_Transform,

ARMATURE_OT_Toggle_Location_X_Lock,
ARMATURE_OT_Toggle_Location_Y_Lock,
ARMATURE_OT_Toggle_Location_Z_Lock,
ARMATURE_OT_Toggle_Rotation_X_Lock,
ARMATURE_OT_Toggle_Rotation_Y_Lock,  
ARMATURE_OT_Toggle_Rotation_Z_Lock,      
ARMATURE_OT_Toggle_Scale_X_Lock,
ARMATURE_OT_Toggle_Scale_Y_Lock,
ARMATURE_OT_Toggle_Scale_Z_Lock,

ARMATURE_OT_Activate_Location_X_Field,
ARMATURE_OT_Activate_Location_Y_Field,
ARMATURE_OT_Activate_Location_Z_Field,
ARMATURE_OT_Activate_Rotation_W_Field,
ARMATURE_OT_Activate_Rotation_X_Field,
ARMATURE_OT_Activate_Rotation_Y_Field,
ARMATURE_OT_Activate_Rotation_Z_Field,
ARMATURE_OT_Activate_Scale_X_Field,
ARMATURE_OT_Activate_Scale_Y_Field,
ARMATURE_OT_Activate_Scale_Z_Field,

OBJECT_OT_Reset_Transform,    
    
        
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.register_class(cls)

if __name__ == "__main__":
    register()