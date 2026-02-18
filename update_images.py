
import os
import re

DOCS_DIR = '/home/sdd/Documents/campaign-bay-testing/docs/CampaignBay.github.io/docs'
PUBLIC_DIR_REL = '../public' # Standard relative path from subdirectories, might vary

# Slug mapping
SLUGS = {
    'scheduled-discounts.md': 'scheduled',
    'quantity-discounts.md': 'quantity',
    'early-bird-discounts.md': 'early-bird',
    'bogo-discounts.md': 'bogo',
    'bogo-advanced-discounts.md': 'bogo-advanced',
    'product-in-cart-discounts.md': 'product-in-cart',
    'global-settings.md': 'settings-global',
    'product-settings.md': 'settings-product',
    'cart-settings.md': 'settings-cart',
    'advanced-settings.md': 'settings-advanced',
    'targeting.md': 'core-targeting',
    'conditions.md': 'core-conditions',
    'scheduling-and-automation.md': 'core-scheduling',
    'understanding-the-engine.md': 'core-engine',
    'dashboard.md': 'dashboard',
    'installation.md': 'installation',
    'index.md': 'home',
    'faq.md': 'faq',
    'settings/index.md': 'settings-overview',
    'campaigns/index.md': 'campaigns-overview'
}

# Image exceptions
EXCEPTIONS = [
    'common-campaign-title.png',
    'common-save-actions.png',
    'logo-2.png'
]

# Prefixes to explicitly rename if found in campaign/settings pages
COMMON_PREFIXES = ['common-', 'sidebar-', 'conditions-']

# Function to determine new image name
def get_new_image_name(old_name, slug):
    if old_name in EXCEPTIONS:
        return old_name
    
    # Remove path components if any
    basename = os.path.basename(old_name)
    
    # If it's already specific to the slug, maybe keep it?
    # But user wants "separate ss for common fields".
    # E.g. sidebar-usage-limit.png -> scheduled-sidebar-usage-limit.png
    
    new_name = basename
    
    # Check if it starts with a common prefix
    is_common = False
    for prefix in COMMON_PREFIXES:
        if basename.startswith(prefix):
            is_common = True
            # Strip the prefix to make it [slug]-[rest] or just [slug]-[basename]?
            # common-target-settings.png -> scheduled-target-settings.png
            # sidebar-usage-limit.png -> scheduled-usage-limit.png
            clean_base = basename.replace(prefix, '')
            
            # Special handling for common prefix replacement
            if prefix == 'sidebar-':
                new_name = f"{slug}-sidebar-{clean_base}"
            elif prefix == 'conditions-':
                new_name = f"{slug}-conditions-{clean_base}"
            elif prefix == 'common-':
                new_name = f"{slug}-{clean_base}"
            break
    
    if not is_common:
        # It's a specific image. 
        # e.g. scheduled-discount-percentage.png inside scheduled-discounts.md
        # If the slug is already in the name, keep it.
        # If not (e.g. selection-scheduled.png), maybe prefix?
        if basename.startswith(slug):
            new_name = basename
        elif basename.startswith('selection-'):
             new_name = f"{slug}-selection.png"
        elif basename.startswith('settings-') and slug.startswith('settings-'):
            # settings-enable-discount.png inside settings-global
            # -> settings-global-enable-discount.png
            clean_base = basename.replace('settings-', '')
            new_name = f"{slug}-{clean_base}"
        else:
            # Fallback: Prefix it to ensure uniqueness if reused, or just keep it unique
            # But we want to standardize.
            # let's only prefix if it doesn't look like it belongs to the slug
            new_name = f"{slug}-{basename}"
            # cleanup double slugs
            if new_name.startswith(f"{slug}-{slug}-"):
                new_name = new_name.replace(f"{slug}-{slug}-", f"{slug}-")

    return new_name

new_image_list = set()

for root, dirs, files in os.walk(DOCS_DIR):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            
            # Determine slug
            rel_path = os.path.relpath(filepath, DOCS_DIR)
            # handle subdirs in SLUGS mapping 
            # (keys in SLUGS are relative to DOCS_DIR or just filenames? 
            # My logic above used just filenames for some, relative for others. Let's fix.)
            
            # key strategy: try matches
            # 1. full rel path match
            slug = SLUGS.get(rel_path)
            # 2. filename match
            if not slug:
                slug = SLUGS.get(file)
            
            if not slug:
                # Default slug from filename
                slug = file.replace('.md', '')
            
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Regex to find images: ![alt](path)
            # We capture the whole path part
            def replacement(match):
                alt = match.group(1)
                full_path = match.group(2)
                
                # Check if it's an external link
                if full_path.startswith('http'):
                    return match.group(0)
                
                # Extract filename
                filename = os.path.basename(full_path)
                
                # Calculate new filename
                new_filename = get_new_image_name(filename, slug)
                
                # Reconstruct path. Keep the directory structure (usually relative)
                # But typically it's ./../public/ or ./public/ or ../public/
                # The user said "store in public". 
                # We should preserve the relative path prefix but change the filename.
                dir_part = os.path.dirname(full_path)
                new_full_path = os.path.join(dir_part, new_filename)
                
                if filename != 'logo-2.png': # Don't list logo
                     new_image_list.add(new_filename)
                
                return f"![{alt}]({new_full_path})"
            
            new_content = re.sub(r'!\[(.*?)\]\((.*?)\)', replacement, content)
            
            if new_content != content:
                print(f"Updating {rel_path}...")
                with open(filepath, 'w') as f:
                    f.write(new_content)

# Print unique images sorted
print("\n--- NEW IMAGE LIST ---")
for img in sorted(list(new_image_list)):
    print(img)
