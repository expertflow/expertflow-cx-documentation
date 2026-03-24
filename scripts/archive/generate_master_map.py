import os
import json
from pathlib import Path
import re

def generate_map(root_dir):
    root_path = Path(root_dir)
    md_files = list(root_path.rglob("*.md"))
    
    link_map = {}
    
    for md_file in md_files:
        rel_path = str(md_file.relative_to(root_path))
        # Add entry for the filename without extension
        name = md_file.stem
        
        # Standardize for mapping: convert to lowercase and replace underscores/spaces with dashes?
        # Actually, let's keep it as is, but maybe add normalized versions
        
        # Key 1: Direct filename stem
        link_map[name] = rel_path
        
        # Key 2: If it has a slug/ID pattern like Name_12345, map the Name part too
        match = re.match(r'(.+)_(\d+)', name)
        if match:
            link_map[match.group(1)] = rel_path
            
    return link_map

if __name__ == "__main__":
    link_map = generate_map("Phase4")
    with open("master_link_map.json", "w") as f:
        json.dump(link_map, f, indent=2)
    print(f"Mapped {len(link_map)} variations to {len(set(link_map.values()))} files in Phase4.")
