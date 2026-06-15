import os

# Neo strip light workspace
neo_dir = r"c:\Users\ACER\Documents\Neo strip light"
neo_index = os.path.join(neo_dir, "index.html")
neo_product = os.path.join(neo_dir, "product.html")

# HI-Tech workspace
hi_dir = r"c:\Users\ACER\Documents\HI-Tech"
hi_index = os.path.join(hi_dir, "index.html")
hi_product = os.path.join(hi_dir, "product.html")

def replace_in_file(filepath, replacements):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements.items():
        content = content.replace(old, new)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Fix Neo strip light (currently has Hi-Tech stuff)
replace_in_file(neo_index, {
    "<title>Hi-Tech</title>": "<title>Neo brights</title>",
    '<div class="brand">Hi-Tech</div>': '<div class="brand">Neo brights</div>',
    'Hi-Tech Electronics <span class="white-point"></span>': 'Neo LED Strip Light <span class="white-point"></span>'
})

replace_in_file(neo_product, {
    "<title>Product Details - Hi-Tech</title>": "<title>Product Details - Neo brights</title>",
    '<div class="brand">product</div>': '<div class="brand">Neo brights</div>',
    '<div class="brand">Hi-Tech</div>': '<div class="brand">Neo brights</div>'
})

# Fix HI-Tech (currently has Neo brights stuff)
replace_in_file(hi_index, {
    "<title>Neo brights</title>": "<title>Hi-Tech</title>",
    '<div class="brand">Neo brights</div>': '<div class="brand">Hi-Tech</div>',
    'Neo LED Strip Light <span class="white-point"></span>': 'Hi-Tech Electronics <span class="white-point"></span>'
})

replace_in_file(hi_product, {
    "<title>Product Details - Neo brights</title>": "<title>Product Details - Hi-Tech</title>",
    '<div class="brand">Neo brights</div>': '<div class="brand">Hi-Tech</div>'
})

print("Brands successfully renamed!")
