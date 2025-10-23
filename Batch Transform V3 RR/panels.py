import bpy
from .operators import *
from .properties import *

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
        

classes = [ARMATURE_PT_Panel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.register_class(cls)

if __name__ == "__main__":
    register()