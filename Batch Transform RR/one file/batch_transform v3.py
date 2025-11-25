import bpy, math   
"""
v3.0.0

1. remove panel poll method
2. Add operator OBJECT_OT_Apply_Object_Transform
3. Using OpClassName.bl_idname technique for dynamic referencing.
4. Added if else statements to switch buttons depending on conditions. If armatures are selected and youre in pose mode, the apply bone transform button appears. Otherwise the apply object transform button appears.
5. Centralized the code to apply transform data into a shared mixin method.
6. Add 9 operators for toggling enable function for the property fields  
7. Add 9 respective properties to toggle enable for the fields.
8. Added an extra operator and property to accomodate for W axis data application
9. Add if statements to apply transform data if True
10. Add reset button to set add-on data to default states

"""
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
    """
    This operator locks N number of bones in an armature at once. Ignores W axis if included bones are in quaternion mode.
    """
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
    bl_label = "Apply transform of bones"
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

#####################################################

class BasePanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Item"
 
class ARMATURE_PT_Panel(BasePanel, bpy.types.Panel):
    
    bl_idname = "panelname"
    bl_label = "Batch Transform"
    
    def draw(self, context):
        layout = self.layout
        inst = context.scene.inst 
        
        #################################################################
        layout.label(text="Location")
        
        location_row = layout.row(align=True)
        loc_column_float = location_row.column(align=True) #floats
        loc_column_trans_enable = location_row.column(align=True) #lock buttons
        loc_column_lock = location_row.column(align=True) #lock buttons
      
        #################################################################
        ### location fields
        
        loc_column_float.prop(inst, "x_val_locate")
        loc_column_float.prop(inst, "y_val_locate")
        loc_column_float.prop(inst, "z_val_locate")
        
        #######################################################
        ### enable buttons
        
        loc_column_trans_enable.operator(ARMATURE_OT_Activate_Location_X_Field.bl_idname, text="", icon="CHECKMARK" if inst.x_locate_field_on else "X", depress=inst.x_locate_field_on)
        loc_column_trans_enable.operator(ARMATURE_OT_Activate_Location_Y_Field.bl_idname, text="", icon="CHECKMARK" if inst.y_locate_field_on else "X", depress=inst.y_locate_field_on)
        loc_column_trans_enable.operator(ARMATURE_OT_Activate_Location_Z_Field.bl_idname, text="", icon="CHECKMARK" if inst.z_locate_field_on else "X", depress=inst.z_locate_field_on)
        
        
        #################################################################
        ### lock buttons 
        
        loc_column_lock.operator(ARMATURE_OT_Toggle_Location_X_Lock.bl_idname, text="", icon="LOCKED" if inst.x_lock_locate else "UNLOCKED", depress=inst.x_lock_locate)
        loc_column_lock.operator(ARMATURE_OT_Toggle_Location_Y_Lock.bl_idname, text="", icon="LOCKED" if inst.y_lock_locate else "UNLOCKED", depress=inst.y_lock_locate)
        loc_column_lock.operator(ARMATURE_OT_Toggle_Location_Z_Lock.bl_idname, text="", icon="LOCKED" if inst.z_lock_locate else "UNLOCKED", depress=inst.z_lock_locate)
        
        
        ##########################################################################
        ##########################################################################
        layout.label(text="Rotation")
        
        rotation_row_w = layout.row(align=True) #w axis row
        
        rot_column_float_w = rotation_row_w.column(align=True)
        rot_column_trans_enable_w = rotation_row_w.column(align=True) #lock buttons
        
        rotation_row = layout.row(align=True) #rest of the grid; 1 row, 2 columns 
        rot_column_float = rotation_row.column(align=True) #floats
        rot_column_trans_enable = rotation_row.column(align=True) #lock buttons
        rot_column_lock = rotation_row.column(align=True) #lock buttons
        
        
        #################################################################
        ### rotation fields
        
        if inst.rotation_m == 'QUATERNION':
            rot_column_float_w.prop(inst, "w_val_rotate_quaternion")
            rot_column_trans_enable_w.operator(ARMATURE_OT_Activate_Rotation_W_Field.bl_idname, text="", icon="CHECKMARK" if inst.w_rotate_field_on else "X", depress=inst.w_rotate_field_on)
            
            rot_column_float.prop(inst, "x_val_rotate_quaternion")
            rot_column_float.prop(inst, "y_val_rotate_quaternion")
            rot_column_float.prop(inst, "z_val_rotate_quaternion")
        else:
            rot_column_float.prop(inst, "x_val_rotate_euler")
            rot_column_float.prop(inst, "y_val_rotate_euler")
            rot_column_float.prop(inst, "z_val_rotate_euler")
            
        #######################################################
        ### enable buttons
        
        rot_column_trans_enable.operator(ARMATURE_OT_Activate_Rotation_X_Field.bl_idname, text="", icon="CHECKMARK" if inst.x_rotate_field_on else "X", depress=inst.x_rotate_field_on)
        rot_column_trans_enable.operator(ARMATURE_OT_Activate_Rotation_Y_Field.bl_idname, text="", icon="CHECKMARK" if inst.y_rotate_field_on else "X", depress=inst.y_rotate_field_on)
        rot_column_trans_enable.operator(ARMATURE_OT_Activate_Rotation_Z_Field.bl_idname, text="", icon="CHECKMARK" if inst.z_rotate_field_on else "X", depress=inst.z_rotate_field_on)
        
        
        #################################################################
        ### lock buttons 
            
        rot_column_lock.operator(ARMATURE_OT_Toggle_Rotation_X_Lock.bl_idname, text="", icon="LOCKED" if inst.x_lock_rotate else "UNLOCKED", depress=inst.x_lock_rotate)
        rot_column_lock.operator(ARMATURE_OT_Toggle_Rotation_Y_Lock.bl_idname, text="", icon="LOCKED" if inst.y_lock_rotate else "UNLOCKED", depress=inst.y_lock_rotate)
        rot_column_lock.operator(ARMATURE_OT_Toggle_Rotation_Z_Lock.bl_idname, text="", icon="LOCKED" if inst.z_lock_rotate else "UNLOCKED", depress=inst.z_lock_rotate)
        
        
        ### Rotation dropdown ############################################
        layout.prop(inst, "rotation_m")
        
        ##########################################################################
        ##########################################################################
        layout.label(text="Scale")
        
        scale_row = layout.row(align=True)
        scl_column_float = scale_row.column(align=True) #floats
        scl_column_trans_enable = scale_row.column(align=True) #floats
        scl_column_lock = scale_row.column(align=True) #lock buttons
        
        
        #################################################################
        ### rotation fields
        
        scl_column_float.prop(inst, "x_val_scale")
        scl_column_float.prop(inst, "y_val_scale")
        scl_column_float.prop(inst, "z_val_scale")
        
        
        #######################################################
        ### enable buttons
        
        scl_column_trans_enable.operator(ARMATURE_OT_Activate_Scale_X_Field.bl_idname, text="", icon="CHECKMARK" if inst.x_scale_field_on else "X", depress=inst.x_scale_field_on)
        scl_column_trans_enable.operator(ARMATURE_OT_Activate_Scale_Y_Field.bl_idname, text="", icon="CHECKMARK" if inst.y_scale_field_on else "X", depress=inst.y_scale_field_on)
        scl_column_trans_enable.operator(ARMATURE_OT_Activate_Scale_Z_Field.bl_idname, text="", icon="CHECKMARK" if inst.z_scale_field_on else "X", depress=inst.z_scale_field_on)
        
        
        #################################################################
        ### lock buttons 
            
        scl_column_lock.operator(ARMATURE_OT_Toggle_Scale_X_Lock.bl_idname, text="", icon="LOCKED" if inst.x_lock_scale else "UNLOCKED", depress=inst.x_lock_scale)
        scl_column_lock.operator(ARMATURE_OT_Toggle_Scale_Y_Lock.bl_idname, text="", icon="LOCKED" if inst.y_lock_scale else "UNLOCKED", depress=inst.y_lock_scale)
        scl_column_lock.operator(ARMATURE_OT_Toggle_Scale_Z_Lock.bl_idname, text="", icon="LOCKED" if inst.z_lock_scale else "UNLOCKED", depress=inst.z_lock_scale)
        
        #added
        #############################################################
        last_row = layout.row()
        
        if ARMATURE_OT_Apply_Bone_Transform.poll(context):
            last_row.operator(ARMATURE_OT_Apply_Bone_Transform.bl_idname, text="To Bones") #press when done
        else:
            last_row.operator(OBJECT_OT_Apply_Object_Transform.bl_idname, text="To Objects") #press when done
        
        last_row.operator(OBJECT_OT_Reset_Transform.bl_idname, text="Reset")
        
        
         
classes = [

BoneTransformData, 

ARMATURE_PT_Panel, 

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
    bpy.types.Scene.inst = bpy.props.PointerProperty(type=BoneTransformData)
    
def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.inst

if __name__ == "__main__":
    register()


