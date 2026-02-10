import bpy

# ========== OPÉRATEURS ORGANISÉS PAR THÈMES ==========
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