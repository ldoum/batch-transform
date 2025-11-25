import bpy

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


classes = [BoneTransformData]

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

