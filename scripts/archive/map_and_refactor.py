import yaml
import json
import os

def parse_tree(tree, current_path="Phase4"):
    mapping = {}
    if isinstance(tree, list):
        for item in tree:
            mapping.update(parse_tree(item, current_path))
    elif isinstance(tree, dict):
        section = tree.get("section")
        if section:
            # Map section names to folder names
            folder_name = section.replace(" (Amy)", "").replace(" (Sam)", "").replace(" (Eva)", "").replace(" (Quentin)", "").replace(" (Olivia)", "").replace(" (CTO)", "").replace(" (Dev)", "").replace(" (Dave)", "").replace(" (Ian)", "").replace(" (Host)", "").replace(" (Cloud)", "")
            folder_name = folder_name.replace("For Agents", "Agent").replace("For Supervisors", "Supervisor").replace("For Solution Admins", "Solution_Admin").replace("For Quality Managers", "QM").replace("For Human Evaluators", "Evaluator").replace("For Decision Makers", "Decision_Maker").replace("For Frontend Developers", "Developer").replace("For Conversation Designers", "Designer").replace("For Integration Specialists", "Integrator").replace("For AI Quality Specialists", "AI_Specialist").replace("For Multi-tenant Partners", "Partner").replace("For Resellers", "Reseller")
            folder_name = folder_name.replace(" ", "_").replace("&", "").replace("__", "_")
            
            new_path = os.path.join(current_path, folder_name)
            if "items" in tree:
                mapping.update(parse_tree(tree["items"], new_path))
        
        slug = tree.get("slug")
        if slug:
            mapping[slug] = {
                "target_folder": current_path,
                "title": tree.get("title"),
                "type": tree.get("type")
            }
    return mapping

with open("Phase3/Final_Navigation_Tree_v11.yaml", "r") as f:
    tree_data = yaml.safe_load(f)

full_mapping = parse_tree(tree_data["navigation_tree"])

with open("Phase2/Master_Refactoring_Backlog.yaml", "r") as f:
    backlog_data = yaml.safe_load(f)

backlog_ref = {item["source_slug"]: item for item in backlog_data["refactoring_backlog"]}

# Merge mapping with backlog
final_instructions = []
for slug, info in full_mapping.items():
    if info["target_folder"].endswith("_Archive"):
        continue
    
    instr = {
        "slug": slug,
        "target_path": os.path.join(info["target_folder"], slug + ".md"),
        "persona": [],
        "diataxis": info["type"],
        "refactor_instructions": ""
    }
    
    # Extract persona from folder path
    for p in ["Agent", "Supervisor", "Evaluator", "QM", "Solution_Admin", "Decision_Maker", "Developer", "Designer", "Integrator", "AI_Specialist", "Partner", "Reseller"]:
        if p in info["target_folder"]:
            instr["persona"].append(p.lower().replace("_", "-"))
            
    if slug in backlog_ref:
        b = backlog_ref[slug]
        instr["persona"] = b.get("persona", instr["persona"])
        instr["diataxis"] = b.get("diataxis", instr["diataxis"])
        instr["refactor_instructions"] = b.get("refactor_instructions", "")
        instr["target_title"] = b.get("target_title")

    final_instructions.append(instr)

with open("refactor_map.json", "w") as f:
    json.dump(final_instructions, f, indent=2)

print(f"Generated instructions for {len(final_instructions)} pages.")
