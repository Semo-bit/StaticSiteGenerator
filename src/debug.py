from markdown_blocks import (
        block_to_htmlnode,
        markdown_to_blocks,
        block_to_block_type,
        markdown_to_html_node,
        block_to_htmlnode,
        quote_to_html
index.md
        )

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

md = """
> This is a
> blockquote block

this is paragraph text

"""
lists  = """
### This is a list

1. This is an `ordered` list
2. with items
3. and more items

"""

headings  = """
# this is an h1

this is paragraph text

## this is an h2
"""

print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to directory...")
    copy_files_recursively(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
            os.path.join(dir_path_content, "index.md"),
            template_path,
            os.path.join(dir_path_public, "index.html")
           )
    
node = markdown_to_html_node(md)
html = node.to_html()
print(html)
