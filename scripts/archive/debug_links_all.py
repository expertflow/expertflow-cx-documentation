import os
import re
from pathlib import Path

def check_socket_events_links_all():
    root_dir = "/Users/macm1/ai/Documentation/DocWithGeminiCLI"
    socket_events_dir = Path(root_dir) / "Phase4/Developer/Socket_Events"
    md_files = list(socket_events_dir.glob("*.md"))
    
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
                
                # Resolve the link relative to the current file
                target_path = (md_file.parent / clean_link).resolve()
                
                # Check if target exists
                if not target_path.exists():
                    broken_links.append({
                        "file": str(md_file.relative_to(socket_events_dir)),
                        "link": link,
                        "target": str(target_path)
                    })
                    
    return broken_links

if __name__ == "__main__":
    broken = check_socket_events_links_all()
    for b in broken:
        print(f"File: {b['file']} | Link: {b['link']} | Target: {b['target']}")
