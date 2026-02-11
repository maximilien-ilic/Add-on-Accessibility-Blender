bl_info = {
    "name": "Themed Button Navigator",
    "author": "Maximilien Ilic",
    "version": (2, 0),
    "blender": (3, 0, 0),
    "location": "Press ² to navigate themes/operators, Enter to select/execute, Esc to go back",
    "description": "Navigate Blender operators organized by themes",
    "category": "Interface",
}

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
    
    THEMES = {
    "Général": [
        {"id": "ed.undo", "label": "Annuler"},
        {"id": "ed.redo", "label": "Refaire"},
        {"id": "wm.save_mainfile", "label": "Sauvegarder"},
        {"id": "wm.save_as_mainfile", "label": "Sauvegarder sous"},
        {"id": "wm.open_mainfile", "label": "Ouvrir fichier"},
        {"id": "wm.quit_blender", "label": "Quitter Blender"},
        {"id": "wm.search_menu", "label": "Menu de recherche"},
    ],
    
    "Sélection (Object)": [
        {"id": "object.select_all", "label": "Tout sélectionner"},
        {"id": "object.select_random", "label": "Sélection aléatoire"},
        {"id": "object.select_by_type", "label": "Sélectionner par type"},
        {"id": "object.select_grouped", "label": "Sélectionner groupés"},
        {"id": "object.select_linked", "label": "Sélectionner liés"},
        {"id": "object.select_camera", "label": "Sélectionner caméra"},
        {"id": "object.select_hierarchy", "label": "Sélectionner hiérarchie"},
    ],
    
    "Objets - Actions": [
        {"id": "object.delete", "label": "Supprimer objet"},
        {"id": "object.duplicate_move", "label": "Dupliquer"},
        {"id": "object.join", "label": "Joindre objets"},
        {"id": "object.parent_set", "label": "Définir parent"},
        {"id": "object.parent_clear", "label": "Retirer parent"},
        {"id": "object.move_to_collection", "label": "Déplacer vers collection"},
        {"id": "object.hide_view_set", "label": "Masquer/Afficher"},
    ],
    
    "Objets - Ombrage": [
        {"id": "object.shade_smooth", "label": "Ombrage lisse"},
        {"id": "object.shade_flat", "label": "Ombrage plat"},
        {"id": "object.shade_auto_smooth", "label": "Auto smooth"},
    ],
    
    "Objets - Origine & Transform": [
        {"id": "object.origin_set", "label": "Définir origine"},
        {"id": "object.transform_apply", "label": "Appliquer transformations"},
        {"id": "object.location_clear", "label": "Effacer position"},
        {"id": "object.rotation_clear", "label": "Effacer rotation"},
        {"id": "object.scale_clear", "label": "Effacer échelle"},
    ],
    
    "Ajouter - Mesh": [
        {"id": "mesh.primitive_plane_add", "label": "Plan"},
        {"id": "mesh.primitive_cube_add", "label": "Cube"},
        {"id": "mesh.primitive_circle_add", "label": "Cercle"},
        {"id": "mesh.primitive_uv_sphere_add", "label": "Sphère UV"},
        {"id": "mesh.primitive_ico_sphere_add", "label": "Ico Sphère"},
        {"id": "mesh.primitive_cylinder_add", "label": "Cylindre"},
        {"id": "mesh.primitive_cone_add", "label": "Cône"},
        {"id": "mesh.primitive_torus_add", "label": "Tore"},
        {"id": "mesh.primitive_monkey_add", "label": "Suzanne"},
    ],
    
    "Ajouter - Courbes": [
        {"id": "curve.primitive_bezier_curve_add", "label": "Courbe Bézier"},
        {"id": "curve.primitive_bezier_circle_add", "label": "Cercle Bézier"},
        {"id": "curve.primitive_nurbs_curve_add", "label": "Courbe NURBS"},
        {"id": "curve.primitive_nurbs_path_add", "label": "Chemin NURBS"},
    ],
    
    "Ajouter - Autres": [
        {"id": "object.text_add", "label": "Texte"},
        {"id": "object.camera_add", "label": "Caméra"},
        {"id": "object.light_add", "label": "Lumière"},
        {"id": "object.empty_add", "label": "Empty"},
        {"id": "object.armature_add", "label": "Armature"},
    ],
    
    "Edit - Sélection": [
        {"id": "mesh.select_all", "label": "Tout sélectionner"},
        {"id": "mesh.select_more", "label": "Étendre sélection"},
        {"id": "mesh.select_less", "label": "Réduire sélection"},
        {"id": "mesh.select_similar", "label": "Sélectionner similaires"},
        {"id": "mesh.select_linked", "label": "Sélectionner liés"},
        {"id": "mesh.loop_select", "label": "Sélectionner loop"},
        {"id": "mesh.select_mode", "label": "Changer mode sélection"},
    ],
    
    "Edit - Supprimer/Dissoudre": [
        {"id": "mesh.delete", "label": "Supprimer"},
        {"id": "mesh.dissolve_verts", "label": "Dissoudre vertices"},
        {"id": "mesh.dissolve_edges", "label": "Dissoudre edges"},
        {"id": "mesh.dissolve_faces", "label": "Dissoudre faces"},
        {"id": "mesh.dissolve_limited", "label": "Dissoudre limité"},
        {"id": "mesh.delete_edgeloop", "label": "Supprimer edge loop"},
    ],
    
    "Edit - Extrusion": [
        {"id": "mesh.extrude_region_move", "label": "Extruder région"},
        {"id": "mesh.extrude_faces_move", "label": "Extruder faces"},
        {"id": "mesh.extrude_edges_move", "label": "Extruder edges"},
        {"id": "mesh.extrude_vertices_move", "label": "Extruder vertices"},
    ],
    
    "Edit - Modélisation": [
        {"id": "mesh.inset", "label": "Inset faces"},
        {"id": "mesh.bevel", "label": "Bevel"},
        {"id": "mesh.bridge_edge_loops", "label": "Bridge edge loops"},
        {"id": "mesh.solidify", "label": "Solidifier"},
        {"id": "mesh.poke", "label": "Poke faces"},
    ],
    
    "Edit - Subdivision": [
        {"id": "mesh.subdivide", "label": "Subdiviser"},
        {"id": "mesh.subdivide_edgering", "label": "Subdiviser edge ring"},
        {"id": "mesh.unsubdivide", "label": "Un-subdiviser"},
    ],
    
    "Edit - Outils de coupe": [
        {"id": "mesh.loop_cut", "label": "Loop cut"},
        {"id": "mesh.knife_tool", "label": "Outil couteau"},
        {"id": "mesh.knife_project", "label": "Knife project"},
        {"id": "mesh.bisect", "label": "Bisect"},
    ],
    
    "Edit - Remplissage": [
        {"id": "mesh.fill", "label": "Remplir"},
        {"id": "mesh.fill_grid", "label": "Remplir grille"},
        {"id": "mesh.beautify_fill", "label": "Beautify fill"},
        {"id": "mesh.edge_face_add", "label": "Ajouter edge/face"},
    ],
    
    "Edit - Fusion/Nettoyage": [
        {"id": "mesh.merge", "label": "Fusionner"},
        {"id": "mesh.remove_doubles", "label": "Supprimer doublons"},
        {"id": "mesh.vertices_smooth", "label": "Lisser vertices"},
        {"id": "mesh.separate", "label": "Séparer"},
        {"id": "mesh.split", "label": "Split"},
    ],
    
    "Edit - Normales": [
        {"id": "mesh.flip_normals", "label": "Inverser normales"},
        {"id": "mesh.normals_make_consistent", "label": "Recalculer normales"},
        {"id": "mesh.set_normals_from_faces", "label": "Normales depuis faces"},
    ],
    
    "UV Mapping": [
        {"id": "uv.unwrap", "label": "Unwrap UV"},
        {"id": "uv.smart_project", "label": "Smart UV Project"},
        {"id": "uv.cube_project", "label": "Cube projection"},
        {"id": "uv.cylinder_project", "label": "Cylinder projection"},
        {"id": "uv.sphere_project", "label": "Sphere projection"},
        {"id": "uv.project_from_view", "label": "Project depuis vue"},
        {"id": "uv.reset", "label": "Reset UV"},
        {"id": "uv.pack_islands", "label": "Pack islands"},
    ],
    
    "Modificateurs": [
        {"id": "object.modifier_add", "label": "Ajouter modificateur"},
        {"id": "object.modifier_apply", "label": "Appliquer modificateur"},
        {"id": "object.modifier_copy", "label": "Copier modificateur"},
        {"id": "object.modifier_remove", "label": "Retirer modificateur"},
        {"id": "object.modifier_move_up", "label": "Monter modificateur"},
        {"id": "object.modifier_move_down", "label": "Descendre modificateur"},
    ],
    
    "Contraintes": [
        {"id": "object.constraint_add", "label": "Ajouter contrainte"},
        {"id": "constraint.apply", "label": "Appliquer contrainte"},
        {"id": "constraint.delete", "label": "Supprimer contrainte"},
        {"id": "constraint.move_up", "label": "Monter contrainte"},
        {"id": "constraint.move_down", "label": "Descendre contrainte"},
    ],
    
    "Matériaux": [
        {"id": "object.material_slot_add", "label": "Ajouter slot matériau"},
        {"id": "object.material_slot_remove", "label": "Retirer slot matériau"},
        {"id": "object.material_slot_assign", "label": "Assigner matériau"},
        {"id": "object.material_slot_select", "label": "Sélectionner matériau"},
        {"id": "material.new", "label": "Nouveau matériau"},
    ],
    
    "Transformations": [
        {"id": "transform.translate", "label": "Déplacer (G)"},
        {"id": "transform.rotate", "label": "Rotation (R)"},
        {"id": "transform.resize", "label": "Échelle (S)"},
        {"id": "transform.shear", "label": "Shear"},
        {"id": "transform.mirror", "label": "Miroir"},
        {"id": "transform.snap", "label": "Snap"},
    ],
    
    "Animation": [
        {"id": "anim.keyframe_insert", "label": "Insérer keyframe"},
        {"id": "anim.keyframe_insert_menu", "label": "Menu keyframe"},
        {"id": "anim.keyframe_delete", "label": "Supprimer keyframe"},
        {"id": "anim.keyframe_clear_v3d", "label": "Effacer toutes keyframes"},
    ],
    
    "Render": [
        {"id": "render.render", "label": "Render image"},
        {"id": "render.view_show", "label": "Afficher render"},
        {"id": "render.view_cancel", "label": "Annuler render"},
        {"id": "render.play_rendered_anim", "label": "Jouer animation render"},
    ],
    
    "Sculpt": [
        {"id": "sculpt.dynamic_topology_toggle", "label": "Toggle dynamic topology"},
        {"id": "sculpt.symmetrize", "label": "Symétriser"},
        {"id": "sculpt.optimize", "label": "Optimiser mesh"},
        {"id": "paint.hide_show", "label": "Masquer/Afficher"},
    ],
    
    "Paint": [
        {"id": "paint.texture_paint_toggle", "label": "Toggle texture paint"},
        {"id": "paint.vertex_paint_toggle", "label": "Toggle vertex paint"},
        {"id": "paint.weight_paint_toggle", "label": "Toggle weight paint"},
    ],
    
    "Collections": [
        {"id": "collection.create", "label": "Créer collection"},
        {"id": "collection.objects_remove", "label": "Retirer de collection"},
        {"id": "collection.objects_add_active", "label": "Ajouter à collection active"},
    ],
    
    "Screen/Animation": [
        {"id": "screen.screen_full_area", "label": "Plein écran"},
        {"id": "screen.animation_play", "label": "Jouer animation"},
        {"id": "screen.animation_cancel", "label": "Arrêter animation"},
        {"id": "screen.frame_jump", "label": "Sauter à la frame"},
    ],
}

# ========== VARIABLES GLOBALES ==========
current_theme_index = 0
current_operator_index = 0
in_theme_mode = True  # True = navigation thèmes, False = navigation opérateurs
theme_names = list(THEMES.keys())
addon_keymaps = []


# ========== OPÉRATEUR DE NAVIGATION ==========
class NavigateButtonsOperator(bpy.types.Operator):
    bl_idname = "wm.navigate_buttons"
    bl_label = "Navigate"
    bl_description = "Navigate through themes or operators"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        global current_theme_index, current_operator_index, in_theme_mode, theme_names
        
        if in_theme_mode:
            # Navigation dans les thèmes00
            current_theme_index = (current_theme_index + 1) % len(theme_names)
            theme_name = theme_names[current_theme_index]
            num_ops = len(THEMES[theme_name])
            message = f"THÈME [{current_theme_index + 1}/{len(theme_names)}]: {theme_name} ({num_ops} opérateurs)"
            self.report({'INFO'}, message)
        else:
            # Navigation dans les opérateurs du thème actuel
            theme_name = theme_names[current_theme_index]
            operators = THEMES[theme_name]
            
            if len(operators) == 0:
                self.report({'WARNING'}, "Aucun opérateur dans ce thème")
                return {'CANCELLED'}
            
            current_operator_index = (current_operator_index + 1) % len(operators)
            current_op = operators[current_operator_index]
            message = f"{theme_name} [{current_operator_index + 1}/{len(operators)}]: {current_op['label']}"
            self.report({'INFO'}, message)
        
        return {'FINISHED'}
    
# ========== OPÉRATEUR D'ACTIVATION/VALIDATION ==========

class UnNavigateButtonsOperator(bpy.types.Operator):
    bl_idname = "wm.unnavigate_buttons"
    bl_label = "UnNavigate"
    bl_description = "Navigate backward through themes or operators"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        global current_theme_index, current_operator_index, in_theme_mode, theme_names
        
        if in_theme_mode:
            # Navigation arrière dans les thèmes
            current_theme_index = (current_theme_index - 1) % len(theme_names)
            theme_name = theme_names[current_theme_index]
            num_ops = len(THEMES[theme_name])
            message = f"THÈME [{current_theme_index + 1}/{len(theme_names)}]: {theme_name} ({num_ops} opérateurs)"
            self.report({'INFO'}, message)
        else:
            # Navigation arrière dans les opérateurs
            theme_name = theme_names[current_theme_index]
            operators = THEMES[theme_name]
            
            if len(operators) == 0:
                self.report({'WARNING'}, "Aucun opérateur dans ce thème")
                return {'CANCELLED'}
            
            current_operator_index = (current_operator_index - 1) % len(operators)
            current_op = operators[current_operator_index]
            message = f"{theme_name} [{current_operator_index + 1}/{len(operators)}]: {current_op['label']}"
            self.report({'INFO'}, message)
        
        return {'FINISHED'}
    
# ========== OPÉRATEUR DE NAVIGATION ARRIERE ==========
class ActivateCurrentButtonOperator(bpy.types.Operator):
    bl_idname = "wm.activate_current_button"
    bl_label = "Activate/Enter"
    bl_description = "Enter theme or execute operator"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        global current_theme_index, current_operator_index, in_theme_mode, theme_names
        
        if in_theme_mode:
            # Entrer dans le thème sélectionné
            in_theme_mode = False
            current_operator_index = 0
            theme_name = theme_names[current_theme_index]
            operators = THEMES[theme_name]
            
            if len(operators) > 0:
                message = f">>> DANS: {theme_name} [{current_operator_index + 1}/{len(operators)}]: {operators[0]['label']}"
                self.report({'INFO'}, message)
            else:
                self.report({'WARNING'}, f"Thème vide: {theme_name}")
                in_theme_mode = True
        else:
            # Exécuter l'opérateur sélectionné
            theme_name = theme_names[current_theme_index]
            operators = THEMES[theme_name]
            
            if current_operator_index >= len(operators):
                self.report({'ERROR'}, "Index invalide")
                return {'CANCELLED'}
            
            op_to_execute = operators[current_operator_index]
            op_id = op_to_execute["id"]
            
            parts = op_id.split('.')
            if len(parts) != 2:
                self.report({'ERROR'}, f"Format invalide: {op_id}")
                return {'CANCELLED'}
            
            category = parts[0]
            operation = parts[1]
            
            try:
                op_category = getattr(bpy.ops, category)
                op_function = getattr(op_category, operation)
                op_function('INVOKE_DEFAULT')
                self.report({'INFO'}, f"✓ {op_to_execute['label']}")
            except AttributeError:
                self.report({'ERROR'}, f"Opérateur introuvable: {op_id}")
                return {'CANCELLED'}
            except RuntimeError as e:
                self.report({'WARNING'}, f"Impossible: {e}")
                return {'CANCELLED'}
        
        return {'FINISHED'}


# ========== OPÉRATEUR RETOUR ARRIÈRE ==========
class GoBackOperator(bpy.types.Operator):
    bl_idname = "wm.go_back_theme"
    bl_label = "Go Back"
    bl_description = "Return to theme selection"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        global in_theme_mode, current_theme_index, theme_names
        
        if not in_theme_mode:
            # Retourner à la sélection de thèmes
            in_theme_mode = True
            theme_name = theme_names[current_theme_index]
            message = f"<<< RETOUR - THÈME [{current_theme_index + 1}/{len(theme_names)}]: {theme_name}"
            self.report({'INFO'}, message)
        else:
            self.report({'INFO'}, "Déjà en mode thèmes")
        
        return {'FINISHED'}


# ========== ENREGISTREMENT ==========
def register():
    bpy.utils.register_class(NavigateButtonsOperator)
    bpy.utils.register_class(UnNavigateButtonsOperator)
    bpy.utils.register_class(ActivateCurrentButtonOperator)

    bpy.utils.register_class(GoBackOperator)
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    
    if kc:
        km = kc.keymaps.new(name='Window', space_type='EMPTY')
        
        # Touche ² pour naviguer
        kmi_navigate = km.keymap_items.new(
            idname='wm.navigate_buttons',
            type='QUOTE',
            value='PRESS'
        )
        
        # Touche Entrée pour valider/exécuter
        kmi_activate = km.keymap_items.new(
            idname='wm.activate_current_button',
            type='RET',
            value='PRESS'
        )


        # Touche ² + MAJ pour naviguer arriere 
        kmi_unnavigate = km.keymap_items.new(
            idname='wm.unnavigate_buttons',  
            type='QUOTE',
            value='PRESS',
            shift=True
        )


        # Touche Échap pour retour arrière
        kmi_back = km.keymap_items.new(
            idname='wm.go_back_theme',
            type='ESC',
            value='PRESS'
        )
        
        addon_keymaps.append((km, kmi_navigate))
        addon_keymaps.append((km, kmi_activate))
        addon_keymaps.append((km, kmi_back))
        addon_keymaps.append((km, kmi_unnavigate))

# ========== DÉSENREGISTREMENT ==========
def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
    bpy.utils.unregister_class(GoBackOperator)
    bpy.utils.unregister_class(UnNavigateButtonsOperator)
    bpy.utils.unregister_class(ActivateCurrentButtonOperator)
    bpy.utils.unregister_class(NavigateButtonsOperator)


# ========== POINT D'ENTRÉE ==========
if __name__ == "__main__":
    register()
