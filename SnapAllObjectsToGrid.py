bl_info = {
    "name": "Snap all objects to grid",
    "category": "Object",
}

import bpy

class SnapAllObjectsToGrid(bpy.types.Operator):
    """Snap all objects to grid"""
    bl_idname = "object.snapalltogrid"
    bl_label = "Snap all objects to grid"
    bl_options = {'REGISTER', 'UNDO'}

    def snap(self, value, divisor=1.0):
        value *= divisor
        value = round(value)
        value = value / divisor
        return value

    def execute(self, context):
        objects = bpy.context.scene.objects
        for object in objects:
            object.location.x = self.snap(object.location.x)
            object.location.y = self.snap(object.location.y)
            object.location.z = self.snap(object.location.z)
            object.scale.x = self.snap(object.scale.x,10)
            object.scale.y = self.snap(object.scale.y,10)
            object.scale.z = self.snap(object.scale.z,10)
        return {'FINISHED'}

addon_keymaps = []

def register():
    bpy.utils.register_class(SnapAllObjectsToGrid)
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(
        name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(
        SnapAllObjectsToGrid.bl_idname, 'SPACE', 'PRESS', ctrl=True, shift=True)
    # kmi.properties.total = 4
    addon_keymaps.append(km)


def unregister():
    bpy.utils.unregister_class(SnapAllObjectsToGrid)
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
