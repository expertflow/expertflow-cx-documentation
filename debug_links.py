import os
import re
from pathlib import Path

def check_socket_events_links():
    root_dir = "Phase4/Developer/Socket_Events"
    root_path = Path(root_dir)
    md_files = list(root_path.glob("*.md"))
    
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    broken_links = []
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            links = link_pattern.findall(content)
            
            for text, link in links:
                if link.startswith("http") or link.startswith("#") or link.startswith("mailto:"):
                    continue
                
                clean_link = link.split('#')[0]
                if not clean_link:
                    continue
                
                target_path = (md_file.parent / clean_link).resolve()
                
                if not target_path.exists():
                    # Check if a file without the numeric suffix exists
                    # e.g. subscribePullModeList_2531752.md -> subscribePullModeList.md
                    suggested_fix = None
                    if "_" in clean_link and clean_link.endswith(".md"):
                        base_name = clean_link.split('_')[0] + ".md"
                        test_path = (md_file.parent / base_name).resolve()
                        if test_path.exists():
                            suggested_fix = base_name
                    
                    broken_links.append({
                        "file": str(md_file.name),
                        "link": link,
                        "exists_without_suffix": suggested_fix
                    })
                    
    return broken_links

if __name__ == "__main__":
    broken = check_socket_events_links()
    for b in broken:
        print(f"File: {b['file']} | Link: {b['link']} | Fix: {b['exists_without_suffix']}")
