import os
import glob
import re
from bs4 import BeautifulSoup

# Try to import html2text, fallback to a simpler method if not available
try:
    import html2text
    HAS_HTML2TEXT = True
except ImportError:
    HAS_HTML2TEXT = False

def convert_sbt_to_md(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    html_files = glob.glob(os.path.join(input_dir, "*.html"))
    print(f"Found {len(html_files)} files to convert.")

    if HAS_HTML2TEXT:
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.body_width = 0
        h.ignore_images = False
        h.mark_code = True
    else:
        print("html2text not found. Using simplified conversion.")

    inventory = []

    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')

            # Extract Title
            title = soup.title.string if soup.title else os.path.basename(html_file)
            title = title.replace(" - Expertflow CX Knowledgebase - Confluence", "").strip()

            # Extract Main Content
            # Confluence exports usually put the content in a div with id "main-content"
            content_div = soup.find(id="main-content") or soup.find("body")
            
            if HAS_HTML2TEXT:
                md_content = h.handle(str(content_div))
            else:
                md_content = content_div.get_text()

            # Create MD filename based on original HTML filename
            base_name = os.path.splitext(os.path.basename(html_file))[0]
            md_filename = f"{base_name}.md"
            md_path = os.path.join(output_dir, md_filename)

            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(md_content)

            inventory.append((title, base_name, html_file))
        except Exception as e:
            print(f"Error converting {html_file}: {e}")

    print(f"Successfully converted {len(inventory)} files to {output_dir}")

if __name__ == "__main__":
    convert_sbt_to_md('SBT', 'SBT_MD')
