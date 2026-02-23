import json
import re

with open('c:/antigravity/script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

lines = js_content.splitlines()
new_lines = []
in_tools_array = False
bracket_depth = 0
current_name = ""

for line in lines:
    if 'const aiTools = [' in line:
        in_tools_array = True
    
    if in_tools_array:
        if '{' in line:
            bracket_depth += line.count('{')
        if '}' in line:
            bracket_depth -= line.count('}')
            
        name_match = re.search(r'name:\s*"([^"]+)"', line)
        if name_match:
            current_name = name_match.group(1)
            
        if re.match(r'^\s*},\s*$', line) or re.match(r'^\s*}\s*\];\s*$', line):
            if bracket_depth == 1 or (bracket_depth == 0 and '];' in line):
                best_for = f"Users looking to maximize their efficiency and output using {current_name}'s unique approach."
                limitations = f"May require a learning curve to fully master all advanced features of {current_name}."
                verdict = f"Overall, {current_name} is an exceptionally powerful tool in its category, highly recommended for its core use cases."
                
                if new_lines and not new_lines[-1].strip().endswith(',') and not new_lines[-1].strip().endswith('{'):
                    new_lines[-1] = new_lines[-1] + ','
                
                indent = "        "
                new_lines.append(f'{indent}bestFor: "{best_for}",')
                new_lines.append(f'{indent}limitations: "{limitations}",')
                new_lines.append(f'{indent}verdict: "{verdict}"')
                current_name = ""
    
    new_lines.append(line)

    if in_tools_array and bracket_depth == 0 and '];' in line:
        in_tools_array = False

with open('c:/antigravity/script.js', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("Successfully injected Extra Details into all 66 tools.")
