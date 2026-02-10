import bpy

class REGION_OT_scale_under_mouse(bpy.types.Operator):
    bl_idname = "region.scale_under_mouse"
    bl_label = "Scale Region Under Mouse"
    
    scale_factor: bpy.props.FloatProperty(default=1.1)
    
    def invoke(self, context, event):
        mouse_x = event.mouse_x
        mouse_y = event.mouse_y
        
        target_region = None
        target_area = None
        
        for area in context.screen.areas:
            if (area.x <= mouse_x <= area.x + area.width and 
                area.y <= mouse_y <= area.y + area.height):
                
                for region in area.regions:
                    if (region.x <= mouse_x <= region.x + region.width and
                        region.y <= mouse_y <= region.y + region.height):
                        target_region = region
                        target_area = area
                        break
                break
        
        if target_region:
            # Méthode correcte pour modifier l'échelle UI
            prefs = context.preferences.view
            current_scale = prefs.ui_scale
            new_scale = current_scale * self.scale_factor
            new_scale = max(0.5, min(2.0, new_scale))
            
            # Appliquer la nouvelle échelle
            prefs.ui_scale = new_scale
            
            # Redessiner toutes les régions pour voir le changement
            for area in context.screen.areas:
                for region in area.regions:
                    region.tag_redraw()
            
            self.report({'INFO'}, f"{target_region.type} → Scale {new_scale:.2f}x")
        else:
            self.report({'WARNING'}, "Aucune région sous la souris")
        
        return {'FINISHED'}

def register():
    bpy.utils.register_class(REGION_OT_scale_under_mouse)
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    
    if kc:
        km = kc.keymaps.new(name='Screen', space_type='EMPTY')
        
        # Ctrl + Molette
        kmi = km.keymap_items.new('region.scale_under_mouse', 
                                   'WHEELUPMOUSE', 'PRESS', ctrl=True)
        kmi.properties.scale_factor = 1.1
        
        kmi = km.keymap_items.new('region.scale_under_mouse', 
                                   'WHEELDOWNMOUSE', 'PRESS', ctrl=True)
        kmi.properties.scale_factor = 0.9
        
        # Ctrl + Numpad (alternative)
        kmi = km.keymap_items.new('region.scale_under_mouse', 
                                   'NUMPAD_PLUS', 'PRESS', ctrl=True)
        kmi.properties.scale_factor = 1.1
        
        kmi = km.keymap_items.new('region.scale_under_mouse', 
                                   'NUMPAD_MINUS', 'PRESS', ctrl=True)
        kmi.properties.scale_factor = 0.9

def unregister():
    bpy.utils.unregister_class(REGION_OT_scale_under_mouse)

if __name__ == "__main__":
    register()
    print("✓ Scale région activé (Ctrl + Molette)")
