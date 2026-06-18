bl_info = {
    "name": "Batch transform",
    "author": "Lancine Doumbia",
    "version": (4, 0, 1),
    "blender": (2, 8, 0),
    "location": "View3D > Sidebar",
    "description": "Apply transform and restriction actions to an unlimited number of objects / armature bones at once",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

import bpy, math 

class TRANSFORMADDON_PG_Transform_Data(bpy.types.PropertyGroup):
 
    #locks
    
    #location [3]
    x_lock_locate: bpy.props.BoolProperty(
        name="", 
        description="Click once to lock.", 
        default=False
    )
    y_lock_locate: bpy.props.BoolProperty(
        name="", 
        description="Click once to lock.", 
        default=False
    )
    z_lock_locate: bpy.props.BoolProperty(
        name="", 
        description="Click once to lock.", 
        default=False
    )
    
    #rotation [6]
    x_lock_rotate: bpy.props.BoolProperty(
        name="", 
        description="Click once to lock.", 
        default=False
    )
    y_lock_rotate: bpy.props.BoolProperty(
        name="", 
        description="Click once to lock.", 
        default=False
    )
    z_lock_rotate: bpy.props.BoolProperty(
        name="", 
        description="Click once to lock.", 
        default=False
    )
    
    #scale [9]
    x_lock_scale: bpy.props.BoolProperty(
        name="", 
        description="Click once to lock.", 
        default=False
    )
    y_lock_scale: bpy.props.BoolProperty(
        name="", 
        description="Click once to lock.", 
        default=False
    )
    z_lock_scale: bpy.props.BoolProperty(
        name="", 
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
    mode_of_rotation: bpy.props.EnumProperty(
        name="Mode",
        description="Choose rotation mode for selected bones/objects",
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
        
    )
    
    # [24]
    mode_of_lock: bpy.props.EnumProperty(
        name="Set lock mode",
        description="Choose lock mode for selected bones/objects",
        items=[
            ('ENABLE', "Lock", "Lock items"),
            ('DISABLE', "Unlock", "Unlock items"),
            
        ],
        default='ENABLE',
    )


def apply_lock_data(context, items):

    trans_edit = context.scene.trans_edit
  
    #add feature to set mode first before setting sequence and then apply it
    if trans_edit.mode_of_lock == "ENABLE":
        activate = True
    else:
        activate = False
        
    for item in items: 
            
        #location data
        if trans_edit.x_lock_locate:
            item.lock_location[0] = activate
        
        if trans_edit.y_lock_locate: 
            item.lock_location[1] = activate
        
        if trans_edit.z_lock_locate:
            item.lock_location[2] = activate
       
        #rotation data 
        if trans_edit.x_lock_rotate:
            item.lock_rotation[0] = activate
        
        if trans_edit.y_lock_rotate:
            item.lock_rotation[1] = activate
        
        if trans_edit.z_lock_rotate:
            item.lock_rotation[2] = activate
        
        #scale data 
        if trans_edit.x_lock_scale:
            item.lock_scale[0] = activate
        
        if trans_edit.y_lock_scale:
            item.lock_scale[1] = activate
        
        if trans_edit.z_lock_scale:
            item.lock_scale[2] = activate

      
def apply_rotation_mode(context, items):
    
    trans_edit = context.scene.trans_edit

    for item in items: 
        
        #set mode of rotation
        item.rotation_mode = trans_edit.mode_of_rotation  
        
    
def apply_transform_values(context, items):   
         
    trans_edit = context.scene.trans_edit

    for item in items:  
      
        #location data
        item.location = (
            trans_edit.x_val_locate, 
            trans_edit.y_val_locate, 
            trans_edit.z_val_locate
        )
    
        if trans_edit.mode_of_rotation == "QUATERNION":
            
            #rotation data 
            item.rotation_quaternion = (
                trans_edit.w_val_rotate_quaternion,
                trans_edit.x_val_rotate_quaternion,
                trans_edit.y_val_rotate_quaternion,
                trans_edit.z_val_rotate_quaternion
            )
            
        else:
            
            #rotation data 
            item.rotation_euler = (
                math.radians(trans_edit.x_val_rotate_euler),
                math.radians(trans_edit.y_val_rotate_euler),
                math.radians(trans_edit.z_val_rotate_euler)
            )
         
        #scale data 
        item.scale = (
            trans_edit.x_val_scale,
            trans_edit.y_val_scale,
            trans_edit.z_val_scale,
        )   
   

class TRANSFORMADDON_OT_Apply_Lock_Data(bpy.types.Operator):
    bl_idname = "transformaddon.apply_lock_data"
    bl_label = "Apply Lock Data"
    bl_description = "Set a sequence of enabled and disabled locks."
    bl_options = {"REGISTER","UNDO"}
    
    def execute(self, context):
        
        if context.mode == "OBJECT":
            apply_lock_data(context, context.selected_objects)
            self.report({'INFO'}, "Lock data applied to objects")
        if context.mode == "POSE":
            apply_lock_data(context, context.selected_pose_bones)
            self.report({'INFO'}, "Lock data applied to bones")
    
        return {'FINISHED'}


class TRANSFORMADDON_OT_Apply_Rotation_Mode(bpy.types.Operator):
    bl_idname = "transformaddon.apply_rotation_mode"
    bl_label = "Apply Mode of Rotation"
    bl_description = "Set a sequence of enabled and disabled locks."
    bl_options = {"REGISTER","UNDO"}
    
    def execute(self, context):
        
        if context.mode == "OBJECT":
            apply_rotation_mode(context, context.selected_objects)
            self.report({'INFO'}, "Rotation mode applied to objects")
        if context.mode == "POSE":
            apply_rotation_mode(context, context.selected_pose_bones)
            self.report({'INFO'}, "Rotation mode applied to bones")
    
        return {'FINISHED'}


class TRANSFORMADDON_OT_Apply_Transform_Data(bpy.types.Operator):
    bl_idname = "transformaddon.apply_transform_data"
    bl_label = "Apply Transform Data"
    bl_description = "Set the value."
    bl_options = {"REGISTER","UNDO"}
    
    def execute(self, context):
        
        if context.mode == "OBJECT":
            apply_transform_values(context, context.selected_objects)
            self.report({'INFO'}, "Transform data applied to objects")
        if context.mode == "POSE":
            apply_transform_values(context, context.selected_pose_bones)
            self.report({'INFO'}, "Transform data applied to bones")
    
        return {'FINISHED'}


class TRANSFORMADDON_OT_Reset_Transform_Data(bpy.types.Operator):
    bl_idname = "transformaddon.reset_transform_data"
    bl_label = "Reset transform data"
    bl_description = "Press to Reset"
    
    def execute(self, context):
        
        trans_edit = context.scene.trans_edit
        
        ### reset locks
        trans_edit.x_lock_locate = False
        trans_edit.y_lock_locate = False
        trans_edit.z_lock_locate = False
        
        trans_edit.x_lock_rotate = False
        trans_edit.y_lock_rotate = False
        trans_edit.z_lock_rotate = False
        
        trans_edit.x_lock_scale = False
        trans_edit.y_lock_scale = False
        trans_edit.z_lock_scale = False
        
        ### reset fields
        trans_edit.x_val_locate = 0.00
        trans_edit.y_val_locate = 0.00
        trans_edit.z_val_locate = 0.00 
    
        trans_edit.x_val_rotate_euler = 0.00 
        trans_edit.y_val_rotate_euler = 0.00 
        trans_edit.z_val_rotate_euler = 0.00 
        
        trans_edit.w_val_rotate_quaternion = 1.00 
        trans_edit.x_val_rotate_quaternion = 0.00 
        trans_edit.y_val_rotate_quaternion = 0.00 
        trans_edit.z_val_rotate_quaternion = 0.00 
        
        trans_edit.x_val_scale = 1.00
        trans_edit.y_val_scale = 1.00
        trans_edit.z_val_scale = 1.00
        
        return {"FINISHED"}


class TRANSFORMADDON_PT_Panel(bpy.types.Panel):
    bl_idname = "TRANSFORMADDON_PT_Panel"
    bl_label = "Batch Transform"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Item"
    
    #appear in object mode and pose mode only
    @classmethod
    def poll(cls,context):
        if context.mode == 'OBJECT' or context.mode == 'POSE':
            return True
    
    def draw(self, context):
        layout = self.layout
        trans_edit = context.scene.trans_edit 
        
        icon = "LOCKED"
        
        if trans_edit.mode_of_lock == "ENABLE":
            icon = "LOCKED"
        else: 
            icon = "UNLOCKED"
             
        #################################################################
        layout.label(text="Location")
        
        location_row = layout.row(align=True)
        loc_column_float = location_row.column(align=True) #floats
        loc_column_lock = location_row.column(align=True) #lock buttons
        
        #################################################################
        ### location fields
        
        loc_column_float.prop(trans_edit, "x_val_locate")
        loc_column_float.prop(trans_edit, "y_val_locate")
        loc_column_float.prop(trans_edit, "z_val_locate")
        
        #################################################################
        ### lock buttons 
        
        loc_column_lock.prop(trans_edit, "x_lock_locate", icon=icon, toggle=True)
        loc_column_lock.prop(trans_edit, "y_lock_locate", icon=icon, toggle=True)
        loc_column_lock.prop(trans_edit, "z_lock_locate", icon=icon, toggle=True)
        
        ##########################################################################
        ##########################################################################
        layout.label(text="Rotation")
        
        rotation_row_w = layout.row(align=True) #w axis row
        
        rot_column_float_w = rotation_row_w.column(align=True) #w float
    
        rotation_row = layout.row(align=True) #rest of the grid; 1 row, 2 columns 
        rot_column_float = rotation_row.column(align=True) #floats
        rot_column_lock = rotation_row.column(align=True) #lock buttons
        
        #################################################################
        ### rotation fields
        
        if trans_edit.mode_of_rotation == 'QUATERNION':
            rot_column_float_w.prop(trans_edit, "w_val_rotate_quaternion")
        
            rot_column_float.prop(trans_edit, "x_val_rotate_quaternion")
            rot_column_float.prop(trans_edit, "y_val_rotate_quaternion")
            rot_column_float.prop(trans_edit, "z_val_rotate_quaternion")
        else:
            rot_column_float.prop(trans_edit, "x_val_rotate_euler")
            rot_column_float.prop(trans_edit, "y_val_rotate_euler")
            rot_column_float.prop(trans_edit, "z_val_rotate_euler")
   
        #################################################################
        ### lock buttons 
            
        rot_column_lock.prop(trans_edit, "x_lock_rotate", icon=icon, toggle=True)
        rot_column_lock.prop(trans_edit, "y_lock_rotate", icon=icon, toggle=True)
        rot_column_lock.prop(trans_edit, "z_lock_rotate", icon=icon, toggle=True)
      
        ##########################################################################
        layout.label(text="Scale")
        
        scale_row = layout.row(align=True)
        scl_column_float = scale_row.column(align=True) #floats
        scl_column_lock = scale_row.column(align=True) #lock buttons
        
        #################################################################
        ### rotation fields
        
        scl_column_float.prop(trans_edit, "x_val_scale")
        scl_column_float.prop(trans_edit, "y_val_scale")
        scl_column_float.prop(trans_edit, "z_val_scale")
        
        #################################################################
        ### lock buttons 
            
        scl_column_lock.prop(trans_edit, "x_lock_scale", icon=icon, toggle=True)
        scl_column_lock.prop(trans_edit, "y_lock_scale", icon=icon, toggle=True)
        scl_column_lock.prop(trans_edit, "z_lock_scale", icon=icon, toggle=True)
        
        ######################################################
   
        layout.prop(trans_edit, "mode_of_lock", expand=True)
        
        row = layout.row(align=True)
        row.operator(TRANSFORMADDON_OT_Apply_Transform_Data.bl_idname, text="Values")
        row.operator(TRANSFORMADDON_OT_Apply_Lock_Data.bl_idname, text="Locks")
        
        ### Rotation dropdown ############################################
        
        layout.prop(trans_edit, "mode_of_rotation")
        
        layout.operator(TRANSFORMADDON_OT_Apply_Rotation_Mode.bl_idname, text="Apply R mode")
        
        ##########################################################################
        
        layout.operator(TRANSFORMADDON_OT_Reset_Transform_Data.bl_idname, text="Reset")
        
        
classes = [
TRANSFORMADDON_PG_Transform_Data,
TRANSFORMADDON_OT_Apply_Lock_Data,
TRANSFORMADDON_OT_Apply_Rotation_Mode,
TRANSFORMADDON_OT_Apply_Transform_Data,
TRANSFORMADDON_OT_Reset_Transform_Data,
TRANSFORMADDON_PT_Panel,    
        
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.trans_edit = bpy.props.PointerProperty(type=TRANSFORMADDON_PG_Transform_Data)
    
    
def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.trans_edit
    
if __name__ == "__main__":
    register()
