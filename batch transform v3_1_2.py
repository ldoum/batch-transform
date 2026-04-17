bl_info = {
    "name": "Batch transform v3",
    "author": "Lancine Doumbia",
    "version": (3, 1, 2),
    "blender": (2, 8, 0),
    "location": "View3D > Sidebar",
    "description": "Apply transform and restriction actions to an unlimited number of objects / armature bones at once",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

import bpy, math 

def rotation_status(self, context):
    print(f"Rotation mode set to {self.rotation_m}")

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
    rotation_m: bpy.props.EnumProperty(
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

#location [26]
    x_locate_field_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
    y_locate_field_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
    z_locate_field_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
    
    #rotation [30]
    w_rotate_field_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate..", 
        default=False
    )
    x_rotate_field_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate..", 
        default=False
    )
    y_rotate_field_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
    z_rotate_field_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
    
    #scale [33]
    x_scale_field_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
    y_scale_field_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
    z_scale_field_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
    
    
    
    #new buttons to activate fields [36]
    
    x_locate_lock_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
    y_locate_lock_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
    z_locate_lock_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
   
    x_rotate_lock_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate..", 
        default=False
    )
    y_rotate_lock_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
    z_rotate_lock_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
    
    x_scale_lock_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
    y_scale_lock_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
    z_scale_lock_on: bpy.props.BoolProperty(
        name="Enable", 
        description="Click once to activate. Again to deactivate.", 
        default=False
    )
    
    rotation_mode_field_on: bpy.props.BoolProperty(
        name="Enable",
        description="Click once to activate. Again to deactivate.",
        default=False
    )
    
###################################################################################
    
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
            
            ### location data
            
            # location lock 
            if self.prop_t.x_locate_lock_on and self.prop_t.x_lock_locate:
                item.lock_location[0] = True
                
            if self.prop_t.x_locate_lock_on and not self.prop_t.x_lock_locate:    
                item.lock_location[0] = False
                
            if self.prop_t.y_locate_lock_on and self.prop_t.y_lock_locate:
                item.lock_location[1] = True
            
            if self.prop_t.y_locate_lock_on and not self.prop_t.y_lock_locate:
                item.lock_location[1] = False
                
            if self.prop_t.z_locate_lock_on and self.prop_t.z_lock_locate:    
                item.lock_location[2] = True
            
            if self.prop_t.z_locate_lock_on and not self.prop_t.z_lock_locate:
                item.lock_location[2] = False
            
            # location values
            if self.prop_t.x_locate_field_on:
                item.location[0] = self.prop_t.x_val_locate
                
            if self.prop_t.y_locate_field_on:
                item.location[1] = self.prop_t.y_val_locate
                
            if self.prop_t.z_locate_field_on:
                item.location[2] = self.prop_t.z_val_locate
            
            
            ### rotation data 
            
            # lock rotation
            if self.prop_t.x_rotate_lock_on and self.prop_t.x_lock_rotate:
                item.lock_rotation[0] = True
            
            if self.prop_t.x_rotate_lock_on and not self.prop_t.x_lock_rotate:
                item.lock_rotation[0] = False
                
            if self.prop_t.y_rotate_lock_on and self.prop_t.y_lock_rotate:
                item.lock_rotation[1] = True
            
            if self.prop_t.y_rotate_lock_on and not self.prop_t.y_lock_rotate:
                item.lock_rotation[1] = False
                
            if self.prop_t.z_rotate_lock_on and self.prop_t.z_lock_rotate:
                item.lock_rotation[2] = True
            
            if self.prop_t.z_rotate_lock_on and not self.prop_t.z_lock_rotate:
                item.lock_rotation[2] = False
            
            # rotation values
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
            
            
            ### rotation mode enabled
            if self.prop_t.rotation_mode_field_on:
                item.rotation_mode = self.prop_t.rotation_m
            
            
            ### scale data
            
            # scale lock
            if self.prop_t.x_scale_lock_on and self.prop_t.x_lock_scale:
                item.lock_scale[0] = True
                
            if self.prop_t.x_scale_lock_on and not self.prop_t.x_lock_scale:
                item.lock_scale[0] = False
                
            if self.prop_t.y_scale_lock_on and self.prop_t.y_lock_scale:
                item.lock_scale[1] = True
                
            if self.prop_t.y_scale_lock_on and not self.prop_t.y_lock_scale:
                item.lock_scale[1] = False
                
            if self.prop_t.z_scale_lock_on and self.prop_t.z_lock_scale:
                item.lock_scale[2] = True
                
            if self.prop_t.z_scale_lock_on and not self.prop_t.z_lock_scale:
                item.lock_scale[2] = False
             
        
            # scale values
            if self.prop_t.x_scale_field_on:
                item.scale[0] = self.prop_t.x_val_scale
                
            if self.prop_t.y_scale_field_on:
                item.scale[1] = self.prop_t.y_val_scale
                
            if self.prop_t.z_scale_field_on:
                item.scale[2] = self.prop_t.z_val_scale
                
                
#####################################            
            
################lock buttons
 
class OT_Toggle_Location_X_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.loc_x_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.x_lock_locate = not self.prop_t.x_lock_locate
        return {'FINISHED'}
 
class OT_Toggle_Location_Y_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.loc_y_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.y_lock_locate = not self.prop_t.y_lock_locate
        return {'FINISHED'}
        
class OT_Toggle_Location_Z_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.loc_z_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.z_lock_locate = not self.prop_t.z_lock_locate   
        return {'FINISHED'}

        
class OT_Toggle_Rotation_X_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_x_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.x_lock_rotate = not self.prop_t.x_lock_rotate
        return {'FINISHED'}

class OT_Toggle_Rotation_Y_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_y_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.y_lock_rotate = not self.prop_t.y_lock_rotate
        return {'FINISHED'}
    
class OT_Toggle_Rotation_Z_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_z_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.z_lock_rotate = not self.prop_t.z_lock_rotate  
        return {'FINISHED'}

        
class OT_Toggle_Scale_X_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.scl_x_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.x_lock_scale = not self.prop_t.x_lock_scale
        return {'FINISHED'}
    
class OT_Toggle_Scale_Y_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.scl_y_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.y_lock_scale = not self.prop_t.y_lock_scale
        return {'FINISHED'}
    
class OT_Toggle_Scale_Z_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.scl_z_lock"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.z_lock_scale = not self.prop_t.z_lock_scale          
        return {'FINISHED'}

########### enable buttons
 
class OT_Activate_Location_X_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.loc_x_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.x_locate_field_on = not self.prop_t.x_locate_field_on
        return {'FINISHED'}
 
class OT_Activate_Location_Y_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.loc_y_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.y_locate_field_on = not self.prop_t.y_locate_field_on
        return {'FINISHED'}
        
class OT_Activate_Location_Z_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.loc_z_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.z_locate_field_on = not self.prop_t.z_locate_field_on   
        return {'FINISHED'}

class OT_Activate_Rotation_W_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_w_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.w_rotate_field_on = not self.prop_t.w_rotate_field_on
        return {'FINISHED'}
        
class OT_Activate_Rotation_X_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_x_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.x_rotate_field_on = not self.prop_t.x_rotate_field_on
        return {'FINISHED'}

class OT_Activate_Rotation_Y_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_y_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.y_rotate_field_on = not self.prop_t.y_rotate_field_on
        return {'FINISHED'}
    
class OT_Activate_Rotation_Z_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_z_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.z_rotate_field_on = not self.prop_t.z_rotate_field_on  
        return {'FINISHED'}

        
class OT_Activate_Scale_X_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.scl_x_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.x_scale_field_on = not self.prop_t.x_scale_field_on
        return {'FINISHED'}
    
class OT_Activate_Scale_Y_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.scl_y_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.y_scale_field_on = not self.prop_t.y_scale_field_on
        return {'FINISHED'}
    
class OT_Activate_Scale_Z_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.scl_z_field_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.z_scale_field_on = not self.prop_t.z_scale_field_on          
        return {'FINISHED'}    
    
### new ops

class OT_Activate_Location_X_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.loc_x_lock_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.x_locate_lock_on = not self.prop_t.x_locate_lock_on   
        return {'FINISHED'}  

class OT_Activate_Location_Y_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.loc_y_lock_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.y_locate_lock_on = not self.prop_t.y_locate_lock_on   
        return {'FINISHED'}  

class OT_Activate_Location_Z_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.loc_z_lock_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.z_locate_lock_on = not self.prop_t.z_locate_lock_on   
        return {'FINISHED'}  
    
class OT_Activate_Rotation_X_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_x_lock_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.x_rotate_lock_on = not self.prop_t.x_rotate_lock_on   
        return {'FINISHED'}  

class OT_Activate_Rotation_Y_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_y_lock_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.y_rotate_lock_on = not self.prop_t.y_rotate_lock_on   
        return {'FINISHED'}  

class OT_Activate_Rotation_Z_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rot_z_lock_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.z_rotate_lock_on = not self.prop_t.z_rotate_lock_on   
        return {'FINISHED'}     
    
class OT_Activate_Scale_X_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.scl_x_lock_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.x_scale_lock_on = not self.prop_t.x_scale_lock_on   
        return {'FINISHED'}  

class OT_Activate_Scale_Y_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.scl_y_lock_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.y_scale_lock_on = not self.prop_t.y_scale_lock_on   
        return {'FINISHED'}  

class OT_Activate_Scale_Z_Lock(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.scl_z_lock_on"
    bl_label = "Axis lock status prompt"
    bl_description = "Click to lock. Click again to unlock."
    
    def execute(self, context):
        self.prop_t.z_scale_lock_on = not self.prop_t.z_scale_lock_on   
        return {'FINISHED'}         
      
    
class OT_Activate_Rotation_Mode_Field(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.rotation_mode_field_on"
    bl_label = "Rotation mode status prompt"
    bl_description = "Click to activate. Click again to deactivate."
    
    def execute(self, context):
        self.prop_t.rotation_mode_field_on = not self.prop_t.rotation_mode_field_on
        return {'FINISHED'}    
    
    
############################## main ops #######################################

class OT_Apply_Bone_Transform(BaseOperator, bpy.types.Operator):
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
    
class OT_Apply_Object_Transform(BaseOperator, bpy.types.Operator):
    bl_idname = "armature.apply_obj_transform"
    bl_label = "Apply transform of objects"
    bl_description = "Press to format"
    
    def execute(self, context):
       
        self.apply_transform(context.selected_objects)
        
        return {"FINISHED"}
    
class OT_Reset_Transform(BaseOperator, bpy.types.Operator):
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
        
        #new
        self.prop_t.rotation_mode_field_on = False
        
        self.prop_t.x_locate_lock_on = False
        self.prop_t.y_locate_lock_on = False
        self.prop_t.z_locate_lock_on = False
        
        self.prop_t.x_rotate_lock_on = False
        self.prop_t.y_rotate_lock_on = False
        self.prop_t.z_rotate_lock_on = False
        
        self.prop_t.x_scale_lock_on = False
        self.prop_t.y_scale_lock_on = False
        self.prop_t.z_scale_lock_on = False
        
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

###############################main panel#####################################
class BasePanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Item"
 
class PT_Panel(BasePanel, bpy.types.Panel):
    
    bl_idname = "panelname.batch_transform_panel"
    bl_label = "Batch Transform"
    
    def draw(self, context):
        layout = self.layout
        inst = context.scene.inst 
        
        #################################################################
        layout.label(text="Location")
        
        location_row = layout.row(align=True)
        loc_column_float = location_row.column(align=True) #floats
        loc_column_trans_enable = location_row.column(align=True) #float enable buttons
        loc_column_lock = location_row.column(align=True) #lock buttons
        loc_column_lock_enable = location_row.column(align=True) #lock enable buttons
        
        #################################################################
        ### location fields
        
        loc_column_float.prop(inst, "x_val_locate")
        loc_column_float.prop(inst, "y_val_locate")
        loc_column_float.prop(inst, "z_val_locate")
        
        #######################################################
        ### enable buttons
        
        loc_column_trans_enable.operator(OT_Activate_Location_X_Field.bl_idname, text="", icon="CHECKMARK" if inst.x_locate_field_on else "X", depress=inst.x_locate_field_on)
        loc_column_trans_enable.operator(OT_Activate_Location_Y_Field.bl_idname, text="", icon="CHECKMARK" if inst.y_locate_field_on else "X", depress=inst.y_locate_field_on)
        loc_column_trans_enable.operator(OT_Activate_Location_Z_Field.bl_idname, text="", icon="CHECKMARK" if inst.z_locate_field_on else "X", depress=inst.z_locate_field_on)
        
        
        #################################################################
        ### lock buttons 
        
        loc_column_lock.operator(OT_Toggle_Location_X_Lock.bl_idname, text="", icon="LOCKED" if inst.x_lock_locate else "UNLOCKED", depress=inst.x_lock_locate)
        loc_column_lock.operator(OT_Toggle_Location_Y_Lock.bl_idname, text="", icon="LOCKED" if inst.y_lock_locate else "UNLOCKED", depress=inst.y_lock_locate)
        loc_column_lock.operator(OT_Toggle_Location_Z_Lock.bl_idname, text="", icon="LOCKED" if inst.z_lock_locate else "UNLOCKED", depress=inst.z_lock_locate)
        
        #######################################################
        ### enable buttons
        
        loc_column_lock_enable.operator(OT_Activate_Location_X_Lock.bl_idname, text="", icon="CHECKMARK" if inst.x_locate_lock_on else "X", depress=inst.x_locate_lock_on)
        loc_column_lock_enable.operator(OT_Activate_Location_Y_Lock.bl_idname, text="", icon="CHECKMARK" if inst.y_locate_lock_on else "X", depress=inst.y_locate_lock_on)
        loc_column_lock_enable.operator(OT_Activate_Location_Z_Lock.bl_idname, text="", icon="CHECKMARK" if inst.z_locate_lock_on else "X", depress=inst.z_locate_lock_on)
        
        
        ##########################################################################
        ##########################################################################
        layout.label(text="Rotation")
        
        rotation_row_w = layout.row(align=True) #w axis row
        
        rot_column_float_w = rotation_row_w.column(align=True) #w float
        rot_column_trans_enable_w = rotation_row_w.column(align=True) #lock buttons
        
        rotation_row = layout.row(align=True) #rest of the grid; 1 row, 2 columns 
        rot_column_float = rotation_row.column(align=True) #floats
        rot_column_trans_enable = rotation_row.column(align=True) #float enable buttons
        rot_column_lock = rotation_row.column(align=True) #lock buttons
        rot_column_lock_enable = rotation_row.column(align=True) #lock enable buttons
        
        #################################################################
        ### rotation fields
        
        if inst.rotation_m == 'QUATERNION':
            rot_column_float_w.prop(inst, "w_val_rotate_quaternion")
            rot_column_trans_enable_w.operator(OT_Activate_Rotation_W_Field.bl_idname, text="", icon="CHECKMARK" if inst.w_rotate_field_on else "X", depress=inst.w_rotate_field_on)
            
            rot_column_float.prop(inst, "x_val_rotate_quaternion")
            rot_column_float.prop(inst, "y_val_rotate_quaternion")
            rot_column_float.prop(inst, "z_val_rotate_quaternion")
        else:
            rot_column_float.prop(inst, "x_val_rotate_euler")
            rot_column_float.prop(inst, "y_val_rotate_euler")
            rot_column_float.prop(inst, "z_val_rotate_euler")
            
        #######################################################
        ### enable buttons
        
        rot_column_trans_enable.operator(OT_Activate_Rotation_X_Field.bl_idname, text="", icon="CHECKMARK" if inst.x_rotate_field_on else "X", depress=inst.x_rotate_field_on)
        rot_column_trans_enable.operator(OT_Activate_Rotation_Y_Field.bl_idname, text="", icon="CHECKMARK" if inst.y_rotate_field_on else "X", depress=inst.y_rotate_field_on)
        rot_column_trans_enable.operator(OT_Activate_Rotation_Z_Field.bl_idname, text="", icon="CHECKMARK" if inst.z_rotate_field_on else "X", depress=inst.z_rotate_field_on)
        
        
        #################################################################
        ### lock buttons 
            
        rot_column_lock.operator(OT_Toggle_Rotation_X_Lock.bl_idname, text="", icon="LOCKED" if inst.x_lock_rotate else "UNLOCKED", depress=inst.x_lock_rotate)
        rot_column_lock.operator(OT_Toggle_Rotation_Y_Lock.bl_idname, text="", icon="LOCKED" if inst.y_lock_rotate else "UNLOCKED", depress=inst.y_lock_rotate)
        rot_column_lock.operator(OT_Toggle_Rotation_Z_Lock.bl_idname, text="", icon="LOCKED" if inst.z_lock_rotate else "UNLOCKED", depress=inst.z_lock_rotate)
        
        #######################################################
        ### enable buttons
        
        rot_column_lock_enable.operator(OT_Activate_Rotation_X_Lock.bl_idname, text="", icon="CHECKMARK" if inst.x_rotate_lock_on else "X", depress=inst.x_rotate_lock_on)
        rot_column_lock_enable.operator(OT_Activate_Rotation_Y_Lock.bl_idname, text="", icon="CHECKMARK" if inst.y_rotate_lock_on else "X", depress=inst.y_rotate_lock_on)
        rot_column_lock_enable.operator(OT_Activate_Rotation_Z_Lock.bl_idname, text="", icon="CHECKMARK" if inst.z_rotate_lock_on else "X", depress=inst.z_rotate_lock_on)
        
        ### Rotation dropdown ############################################
        rotation_mode_row = layout.row(align=True)
        rotation_mode_row.prop(inst, "rotation_m")
        rotation_mode_row.operator(OT_Activate_Rotation_Mode_Field.bl_idname, text="", icon="CHECKMARK" if inst.rotation_mode_field_on else "X", depress=inst.rotation_mode_field_on)
        
        ##########################################################################
        ##########################################################################
        layout.label(text="Scale")
        
        scale_row = layout.row(align=True)
        scl_column_float = scale_row.column(align=True) #floats
        scl_column_trans_enable = scale_row.column(align=True) #floats
        scl_column_lock = scale_row.column(align=True) #lock buttons
        scl_column_lock_enable = scale_row.column(align=True) #lock enable buttons
        
        #################################################################
        ### rotation fields
        
        scl_column_float.prop(inst, "x_val_scale")
        scl_column_float.prop(inst, "y_val_scale")
        scl_column_float.prop(inst, "z_val_scale")
        
        
        #######################################################
        ### enable buttons
        
        scl_column_trans_enable.operator(OT_Activate_Scale_X_Field.bl_idname, text="", icon="CHECKMARK" if inst.x_scale_field_on else "X", depress=inst.x_scale_field_on)
        scl_column_trans_enable.operator(OT_Activate_Scale_Y_Field.bl_idname, text="", icon="CHECKMARK" if inst.y_scale_field_on else "X", depress=inst.y_scale_field_on)
        scl_column_trans_enable.operator(OT_Activate_Scale_Z_Field.bl_idname, text="", icon="CHECKMARK" if inst.z_scale_field_on else "X", depress=inst.z_scale_field_on)
        
        
        #################################################################
        ### lock buttons 
            
        scl_column_lock.operator(OT_Toggle_Scale_X_Lock.bl_idname, text="", icon="LOCKED" if inst.x_lock_scale else "UNLOCKED", depress=inst.x_lock_scale)
        scl_column_lock.operator(OT_Toggle_Scale_Y_Lock.bl_idname, text="", icon="LOCKED" if inst.y_lock_scale else "UNLOCKED", depress=inst.y_lock_scale)
        scl_column_lock.operator(OT_Toggle_Scale_Z_Lock.bl_idname, text="", icon="LOCKED" if inst.z_lock_scale else "UNLOCKED", depress=inst.z_lock_scale)
        
        #######################################################
        ### enable buttons
        
        scl_column_lock_enable.operator(OT_Activate_Scale_X_Lock.bl_idname, text="", icon="CHECKMARK" if inst.x_scale_lock_on else "X", depress=inst.x_scale_lock_on)
        scl_column_lock_enable.operator(OT_Activate_Scale_Y_Lock.bl_idname, text="", icon="CHECKMARK" if inst.y_scale_lock_on else "X", depress=inst.y_scale_lock_on)
        scl_column_lock_enable.operator(OT_Activate_Scale_Z_Lock.bl_idname, text="", icon="CHECKMARK" if inst.z_scale_lock_on else "X", depress=inst.z_scale_lock_on)
        
        #added
        #############################################################
        last_row = layout.row()
        
        if OT_Apply_Bone_Transform.poll(context):
            last_row.operator(OT_Apply_Bone_Transform.bl_idname, text="To Bones") #press when done
        else:
            last_row.operator(OT_Apply_Object_Transform.bl_idname, text="To Objects") #press when done
        
        last_row.operator(OT_Reset_Transform.bl_idname, text="Reset")
        

classes = [
BoneTransformData,
    
#28 operators
OT_Apply_Bone_Transform, 
OT_Apply_Object_Transform,
OT_Reset_Transform, 

OT_Toggle_Location_X_Lock,
OT_Toggle_Location_Y_Lock,
OT_Toggle_Location_Z_Lock,
OT_Toggle_Rotation_X_Lock,
OT_Toggle_Rotation_Y_Lock,  
OT_Toggle_Rotation_Z_Lock,      
OT_Toggle_Scale_X_Lock,
OT_Toggle_Scale_Y_Lock,
OT_Toggle_Scale_Z_Lock,

OT_Activate_Location_X_Field,
OT_Activate_Location_Y_Field,
OT_Activate_Location_Z_Field,
OT_Activate_Rotation_W_Field,
OT_Activate_Rotation_X_Field,
OT_Activate_Rotation_Y_Field,
OT_Activate_Rotation_Z_Field,
OT_Activate_Scale_X_Field,
OT_Activate_Scale_Y_Field,
OT_Activate_Scale_Z_Field,

OT_Activate_Location_X_Lock,
OT_Activate_Location_Y_Lock,
OT_Activate_Location_Z_Lock,
OT_Activate_Rotation_X_Lock,
OT_Activate_Rotation_Y_Lock,
OT_Activate_Rotation_Z_Lock,
OT_Activate_Scale_X_Lock,
OT_Activate_Scale_Y_Lock,
OT_Activate_Scale_Z_Lock,
OT_Activate_Rotation_Mode_Field,
   
PT_Panel,    
        
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