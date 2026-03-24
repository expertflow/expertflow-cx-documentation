import os
import re
from pathlib import Path

def fix_socket_events_links():
    root_dir = "Phase4/Developer/Socket_Events"
    root_path = Path(root_dir)
    md_files = list(root_path.glob("*.md"))
    
    # Pattern to match [text](link)
    link_pattern = re.compile(r'(\[[^\]]+\])\(([^)]+)\)')
    
    # List of known files in the directory for case-insensitive matching if needed
    known_files = {f.name.lower(): f.name for f in md_files}
    
    files_fixed = 0
    links_fixed = 0
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        matches = list(link_pattern.finditer(content))
        
        # Work backwards to avoid offset issues
        for match in reversed(matches):
            text_part = match.group(1)
            link = match.group(2)
            
            # Skip external links and anchors
            if link.startswith("http") or link.startswith("#") or link.startswith("mailto:"):
                continue
            
            clean_link = link.split('#')[0]
            anchor = "#" + link.split('#')[1] if '#' in link else ""
            
            if not clean_link:
                continue
                
            target_path = (md_file.parent / clean_link).resolve()
            
            if not target_path.exists():
                suggested_fix = None
                
                # Rule 1: Remove numeric suffix
                if "_" in clean_link and clean_link.endswith(".md"):
                    # Check if it's a known pattern like JoinAsBargin -> JoinAsBargeIn
                    if "JoinAsBargin" in clean_link:
                        suggested_fix = "./JoinAsBargeIn.md"
                    else:
                        base_name = clean_link.split('_')[0] + ".md"
                        # Handle cases like topicUnsubscription_2531762.md where base name might be topicUnsubscription.md
                        # But wait, topicUnsubscription_.md also exists.
                        # If base_name exists, use it.
                        test_path = (md_file.parent / base_name).resolve()
                        if test_path.exists():
                            suggested_fix = base_name
                
                # Rule 2: Case sensitivity / small typos
                if not suggested_fix:
                    # Try lower case match
                    filename = Path(clean_link).name.lower()
                    if filename in known_files:
                        suggested_fix = str(Path(clean_link).parent / known_files[filename])
                
                if suggested_fix:
                    print(f"Fixing in {md_file.name}: {link} -> {suggested_fix}{anchor}")
                    new_link = f"{suggested_fix}{anchor}"
                    new_content = new_content[:match.start(2)] + new_link + new_content[match.end(2):]
                    links_fixed += 1
        
        if new_content != content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            files_fixed += 1
            
    print(f"Total files fixed: {files_fixed}")
    print(f"Total links fixed: {links_fixed}")

if __name__ == "__main__":
    fix_socket_events_links()
