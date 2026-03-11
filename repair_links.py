import os
import json
import re
from pathlib import Path
import sys

def repair_file(file_path, link_map, root_dir):
    file_path = Path(file_path)
    root_path = Path(root_dir).resolve()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find markdown links: [text](link)
    link_pattern = re.compile(r'(\[([^\]]+)\]\(([^)]+)\))')
    
    def replace_link(match):
        full_match = match.group(1)
        text = match.group(2)
        link = match.group(3)
        
        # Skip external links and anchors
        if link.startswith("http") or link.startswith("#") or link.startswith("mailto:"):
            return full_match
        
        # Extract the base identifier (filename stem)
        # Handle cases like "Path/To/Slug_ID.html#anchor" or just "Slug_ID"
        clean_link = link.split('#')[0]
        anchor = link.split('#')[1] if '#' in link else ""
        
        # Remove extension if present
        link_stem = Path(clean_link).stem
        
        # Look up in the master map
        target_rel_path = None
        if link_stem in link_map:
            target_rel_path = link_map[link_stem]
        elif link_stem.split('_')[0] in link_map: # Try without ID
            target_rel_path = link_map[link_stem.split('_')[0]]
            
        if target_rel_path:
            # Calculate the new relative path from current file to target
            target_abs_path = (root_path / target_rel_path).resolve()
            current_dir = file_path.parent.resolve()
            
            try:
                new_rel_path = os.path.relpath(target_abs_path, current_dir)
                if anchor:
                    new_rel_path = f"{new_rel_path}#{anchor}"
                return f"[{text}]({new_rel_path})"
            except ValueError:
                return full_match # Keep original if error
                
        return full_match

    new_content = link_pattern.sub(replace_link, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 repair_links.py <dir1> <dir2> ...")
        sys.exit(1)
        
    with open("master_link_map.json", 'r') as f:
        link_map = json.load(f)
        
    root_dir = "Phase4"
    dirs_to_process = sys.argv[1:]
    
    total_repaired = 0
    for d in dirs_to_process:
        path = Path(d)
        if not path.exists():
            print(f"Directory {d} does not exist. Skipping.")
            continue
            
        for md_file in path.rglob("*.md"):
            if repair_file(md_file, link_map, root_dir):
                total_repaired += 1
                
    print(f"Repaired links in {total_repaired} files in {', '.join(dirs_to_process)}")

if __name__ == "__main__":
    main()
