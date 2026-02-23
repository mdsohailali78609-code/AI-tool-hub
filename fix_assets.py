import os
import re

# Base directory
base_dir = r"c:/antigravity"
assets_dir = os.path.join(base_dir, "assets")

# Ensure assets directory exists
os.makedirs(assets_dir, exist_ok=True)

# Read script.js
script_path = os.path.join(base_dir, "script.js")
with open(script_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find all image paths
matches = re.findall(r'image:\s*"assets/([^"]+)"', content)

missing_files = []
for filename in matches:
    filepath = os.path.join(assets_dir, filename)
    if not os.path.exists(filepath):
        missing_files.append(filename)

print(f"Found {len(missing_files)} missing logos: {missing_files}")

# Generate simple SVGs for missing ones
svg_template = """<svg xmlns="http://www.w3.org/200.svg" viewBox="0 0 100 100" width="100%" height="100%">
    <rect width="100" height="100" rx="20" fill="{color}"/>
    <text x="50" y="55" font-family="Inter, sans-serif" font-size="40" font-weight="bold" fill="white" text-anchor="middle" dominant-baseline="middle">{text}</text>
</svg>"""

colors = ["#4f46e5", "#ec4899", "#10b981", "#f59e0b", "#3b82f6", "#8b5cf6", "#ef4444"]

import random
for filename in missing_files:
    # Use first two letters of filename (excluding .svg)
    name_base = filename.replace(".svg", "").upper()
    text = name_base[:2] if len(name_base) >= 2 else (name_base[0] if name_base else "AI")
    
    color = random.choice(colors)
    svg_content = svg_template.format(color=color, text=text)
    
    filepath = os.path.join(assets_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {filename}")

if len(missing_files) == 0:
    print("All logos are present.")
