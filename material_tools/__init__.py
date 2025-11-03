# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Material Tools",
    "author" : "Box Bear", 
    "description" : "",
    "blender" : (3, 0, 0),
    "version" : (1, 0, 0),
    "location" : "",
    "warning" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "Material" 
}


import bpy
import bpy.utils.previews


addon_keymaps = {}
_icons = None
class SNA_PT_BOX_BEAR_MATERIAL_TOOLS_D9B27(bpy.types.Panel):
    bl_label = 'Box Bear Material Tools'
    bl_idname = 'SNA_PT_BOX_BEAR_MATERIAL_TOOLS_D9B27'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'material'
    bl_category = 'New Category'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        op = layout.operator('sna.material_check_ca36c', text='Check Material', icon_value=614, emboss=True, depress=False)


class SNA_OT_Material_Check_Ca36C(bpy.types.Operator):
    bl_idname = "sna.material_check_ca36c"
    bl_label = "Material Check"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if bpy.context.view_layer.objects.selected:
            print('Just started an operator!', 'message 2', 'message 3', 'and 4')
        else:
            self.report({'ERROR'}, message='Please have a GameObject selected')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.utils.register_class(SNA_PT_BOX_BEAR_MATERIAL_TOOLS_D9B27)
    bpy.utils.register_class(SNA_OT_Material_Check_Ca36C)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(SNA_PT_BOX_BEAR_MATERIAL_TOOLS_D9B27)
    bpy.utils.unregister_class(SNA_OT_Material_Check_Ca36C)
