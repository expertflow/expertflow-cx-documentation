import yaml
import os
import json
from pathlib import Path
import re

def build_map(nav_tree_path, phase4_dir):
    with open(nav_tree_path, 'r') as f:
        nav_data = yaml.safe_load(f)
    
    # 1. Index all files in Phase4 by their stem (filename without .md)
    phase4_path = Path(phase4_dir)
    actual_files = {}
    for md_file in phase4_path.rglob("*.md"):
        actual_files[md_file.stem] = str(md_file.relative_to(phase4_path))
    
    link_map = {}
    
    # 2. Extract slug -> title mappings from the nav tree
    def process_items(items):
        for item in items:
            if 'items' in item:
                process_items(item['items'])
            elif 'slug' in item and 'title' in item:
                slug = item['slug']
                title = item['title']
                # Sanitize title to match possible filename
                clean_title = title.replace(' ', '-').replace('/', '-').replace(':', '').replace('?', '').replace(',', '')
                # Also handle common characters like %2C
                clean_title = clean_title.replace('%2C', '-')
                
                # Try to find the file in Phase4
                # Priority 1: Match title-based filename
                if clean_title in actual_files:
                    link_map[slug] = actual_files[clean_title]
                # Priority 2: Match slug-based filename
                elif slug in actual_files:
                    link_map[slug] = actual_files[slug]
                # Priority 3: Match title exactly
                elif title in actual_files:
                    link_map[slug] = actual_files[title]
                # Priority 4: Search for partial match? (Maybe later)

    process_items(nav_data['navigation_tree'])
    
    # 3. Fallback: Add all actual files to map (to handle new/unlisted files)
    for stem, path in actual_files.items():
        if stem not in link_map:
            link_map[stem] = path
            # Also add variation without ID if present
            match = re.match(r'(.+)_(\d+)', stem)
            if match and match.group(1) not in link_map:
                link_map[match.group(1)] = path

    return link_map

if __name__ == "__main__":
    precise_map = build_map("Phase3/Final_Navigation_Tree_v11.yaml", "Phase4")
    with open("master_link_map.json", "w") as f:
        json.dump(precise_map, f, indent=2)
    print(f"Precise map generated with {len(precise_map)} entries.")
