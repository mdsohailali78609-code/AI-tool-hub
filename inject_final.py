import re

with open('c:/antigravity/script.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern: match lines ending with "}," but only inside the aiTools array context
new_text = re.sub(
    r'(?m)^(\s*)(},|\}\s*];)\s*$',
    r'\1    bestFor: "Highly recommended for users needing to maximize efficiency in its core use case.",\n\1    limitations: "May require some initial learning to leverage all advanced features.",\n\1    verdict: "An exceptionally powerful AI tool that sets the standard in its category."\n\1\2',
    text
)

with open('c:/antigravity/script.js', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Injection done.')
