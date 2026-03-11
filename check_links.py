import os
import re
from pathlib import Path

def check_markdown_links(root_dir):
    root_path = Path(root_dir)
    md_files = list(root_path.rglob("*.md"))
    
    # Regex to find markdown links: [text](link)
    # This specifically looks for the (link) part
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    broken_links = []
    total_links_checked = 0
    
    print(f"Checking {len(md_files)} files in {root_dir}...")
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            links = link_pattern.findall(content)
            
            for text, link in links:
                # Skip external links and anchors starting with #
                if link.startswith("http") or link.startswith("#") or link.startswith("mailto:"):
                    continue
                
                total_links_checked += 1
                
                # Split link at '#' to handle internal anchors
                clean_link = link.split('#')[0]
                if not clean_link:
                    continue
                
                # Resolve the link relative to the current file
                target_path = (md_file.parent / clean_link).resolve()
                
                # Check if target exists
                if not target_path.exists():
                    broken_links.append({
                        "file": str(md_file.relative_to(root_path)),
                        "link": link,
                        "target": str(target_path)
                    })
                    
    return total_links_checked, broken_links

if __name__ == "__main__":
    total, broken = check_markdown_links("Phase4")
    
    print(f"\n--- Link Check Summary ---")
    print(f"Total files scanned: {len(list(Path('Phase4').rglob('*.md')))}")
    print(f"Total internal links checked: {total}")
    
    if not broken:
        print("✅ SUCCESS: No broken internal links found!")
    else:
        print(f"❌ FAILED: Found {len(broken)} broken links:")
        # Sort by file for better readability
        broken.sort(key=lambda x: x['file'])
        for b in broken:
            print(f"File: {b['file']}")
            print(f"  Link: {b['link']}")
            print(f"  Error: Target file not found")
            print("-" * 20)
