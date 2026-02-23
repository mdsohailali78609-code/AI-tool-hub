import re

with open('c:/antigravity/script.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove all incorrectly injected lines
text = re.sub(r'^\s*bestFor:.*$\n', '', text, flags=re.MULTILINE)
text = re.sub(r'^\s*limitations:.*$\n', '', text, flags=re.MULTILINE)
text = re.sub(r'^\s*verdict:.*$\n', '', text, flags=re.MULTILINE)

# Now, we should inject them EXACTLY ONCE right before the closing brace of each object.
# Find the featured: true or false lines (which are the last lines of each object currently)
# and append our new fields with a comma.

# Example:
#         featured: true
#     },
# Becomes:
#         featured: true,
#         bestFor: "...",
#         limitations: "...",
#         verdict: "..."
#     },

def replacer(match):
    featured_line = match.group(1) # e.g. "        featured: true"
    closing_brace = match.group(2) # e.g. "    }," or "    }"
    
    # If the featured line doesn't end with a comma, add one
    if not featured_line.strip().endswith(','):
        featured_line += ','
        
    best_for = '        bestFor: "Highly recommended for its core use cases to maximize efficiency and output.",\n'
    limitations = '        limitations: "May require a learning curve to fully master all advanced features.",\n'
    verdict = '        verdict: "An exceptionally powerful tool in its category, highly recommended."\n'
    
    return featured_line + '\n' + best_for + limitations + verdict + closing_brace

# Replace featured lines that are immediately followed by the closing brace
new_text = re.sub(r'(^[ \t]*featured:\s*(?:true|false)[^\n]*\n)([ \t]*},|[ \t]*})', replacer, text, flags=re.MULTILINE)

with open('c:/antigravity/script.js', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Clean and inject done.')
