import bpy
from .properties import *

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
        
        







classes = [ARMATURE_PT_Panel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.register_class(cls)

if __name__ == "__main__":
    register()