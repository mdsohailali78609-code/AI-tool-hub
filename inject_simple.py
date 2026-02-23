with open('c:/antigravity/script.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Root level object closes with exactly 4 spaces and a closing brace
    # Handle \n and \r\n endings robustly
    stripped_line = line.strip()
    if line.startswith('    ') and not line.startswith('     ') and (stripped_line == '},' or stripped_line == '}' or stripped_line == '}];' or stripped_line == '];'):
        best_for = 'Highly recommended for its core use cases to maximize efficiency and output.'
        limitations = 'May require a learning curve to fully master all advanced features.'
        verdict = 'An exceptionally powerful tool in its category, highly recommended.'
        
        new_lines.append(f'        bestFor: "{best_for}",\n')
        new_lines.append(f'        limitations: "{limitations}",\n')
        new_lines.append(f'        verdict: "{verdict}"\n')
        
        # Note: if the line was "}," we should add a comma to verdict, but since it's the last property before }, we don't need to except standard JSON doesn't strictly require it, JS objects do just fine without trailing comma.
        # Wait, if we append it BEFORE '    },', the previous property needs a comma!
        # The line before line is new_lines[-1]
        if len(new_lines) > 0 and not new_lines[-1].strip().endswith(',') and not new_lines[-1].strip().endswith('{'):
            new_lines[-1] = new_lines[-1].rstrip('\r\n') + ',\n'
            
    new_lines.append(line)

with open('c:/antigravity/script.js', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Done!')
