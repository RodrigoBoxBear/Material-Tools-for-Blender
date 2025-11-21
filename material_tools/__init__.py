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
    "name" : "Material Tools for Blender",
    "author" : "Box Bear", 
    "description" : "Box Bear`s Blender addon to help with the Blender-Unity pipeline.",
    "blender" : (3, 0, 0),
    "version" : (0, 2, 0),
    "location" : "",
    "warning" : "",
    "doc_url": "https://boxbear-my.sharepoint.com/:w:/g/personal/rodrigo_boxbear_co_uk/EQkHoMX2z_BPl-iKoAPfiRIBmy8yLsv5qyo_pMXwCowbeQ?e=axkT1g", 
    "tracker_url": "", 
    "category" : "Material" 
}


import bpy
import bpy.utils.previews


addon_keymaps = {}
_icons = None


def display_collection_id(uid, vars):
    id = f"coll_{uid}"
    for var in vars.keys():
        if var.startswith("i_"):
            id += f"_{var}_{vars[var]}"
    return id


class SNA_UL_display_collection_list_4E9BD(bpy.types.UIList):

    def draw_item(self, context, layout, data, item_4E9BD, icon, active_data, active_propname, index_4E9BD):
        row = layout
        layout.prop(bpy.data.materials[index_4E9BD], 'name', text='', icon_value=0, emboss=True)
        if 'M_' in bpy.data.materials[index_4E9BD].name:
            layout.label(text='Check', icon_value=54)
        else:
            row_9406B = layout.row(heading='', align=False)
            row_9406B.alert = True
            row_9406B.enabled = True
            row_9406B.active = True
            row_9406B.use_property_split = False
            row_9406B.use_property_decorate = False
            row_9406B.scale_x = 1.0
            row_9406B.scale_y = 1.0
            row_9406B.alignment = 'Expand'.upper()
            row_9406B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            row_9406B.label(text='Incorrect', icon_value=46)

    def filter_items(self, context, data, propname):
        flt_flags = []
        for item in getattr(data, propname):
            if not self.filter_name or self.filter_name.lower() in item.name.lower():
                if sna_function_execute_E0F5C(item):
                    flt_flags.append(self.bitflag_filter_item)
                else:
                    flt_flags.append(0)
            else:
                flt_flags.append(0)
        return flt_flags, []


class SNA_PT_NAME_CHECKER_0C8D5(bpy.types.Panel):
    bl_label = 'Name Checker'
    bl_idname = 'SNA_PT_NAME_CHECKER_0C8D5'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Material Tools'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_1E478 = layout.box()
        box_1E478.alert = False
        box_1E478.enabled = True
        box_1E478.active = True
        box_1E478.use_property_split = False
        box_1E478.use_property_decorate = False
        box_1E478.alignment = 'Expand'.upper()
        box_1E478.scale_x = 1.0
        box_1E478.scale_y = 1.0
        if not True: box_1E478.operator_context = "EXEC_DEFAULT"
        coll_id = display_collection_id('4E9BD', locals())
        box_1E478.template_list('SNA_UL_display_collection_list_4E9BD', coll_id, bpy.data, 'materials', bpy.context.scene, 'sna_index', rows=0)


def sna_function_execute_E0F5C(Input):
    return (False if Input.is_grease_pencil else True)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.types.Scene.sna_index = bpy.props.IntProperty(name='Index', description='', default=0, subtype='NONE')
    bpy.utils.register_class(SNA_PT_NAME_CHECKER_0C8D5)
    bpy.utils.register_class(SNA_UL_display_collection_list_4E9BD)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    del bpy.types.Scene.sna_index
    bpy.utils.unregister_class(SNA_PT_NAME_CHECKER_0C8D5)
    bpy.utils.unregister_class(SNA_UL_display_collection_list_4E9BD)
