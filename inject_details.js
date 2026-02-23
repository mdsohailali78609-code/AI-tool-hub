const fs = require('fs');
const content = fs.readFileSync('c:/antigravity/script.js', 'utf8');

const lines = content.split('\n');
const newLines = [];
let inToolsArray = false;
let bracketDepth = 0;
let currentName = '';

for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    if (line.includes('const aiTools = [')) {
        inToolsArray = true;
    }

    if (inToolsArray) {
        if (line.includes('{')) bracketDepth += (line.match(/\{/g) || []).length;
        if (line.includes('}')) bracketDepth -= (line.match(/\}/g) || []).length;

        const nameMatch = line.match(/name:\s*"([^"]+)"/);
        if (nameMatch) {
            currentName = nameMatch[1];
        }

        if (line.match(/^\s*},\s*$/) || line.match(/^\s*}\s*];\s*$/)) {
            if (bracketDepth === 1 || (bracketDepth === 0 && line.includes('];'))) {
                const bestFor = `Users looking to maximize their efficiency and output using ${currentName}'s unique approach.`;
                const limitations = `May require a learning curve to fully master all advanced features of ${currentName}.`;
                const verdict = `Overall, ${currentName} is an exceptionally powerful tool in its category, highly recommended for its core use cases.`;

                if (newLines.length > 0 && !newLines[newLines.length - 1].trim().endsWith(',') && !newLines[newLines.length - 1].trim().endsWith('{')) {
                    newLines[newLines.length - 1] += ',';
                }

                const indent = "        ";
                newLines.push(`${indent}bestFor: "${bestFor}",`);
                newLines.push(`${indent}limitations: "${limitations}",`);
                newLines.push(`${indent}verdict: "${verdict}"`);
                currentName = '';
            }
        }
    }
    newLines.push(line);

    if (inToolsArray && bracketDepth === 0 && line.includes('];')) {
        inToolsArray = false;
    }
}

fs.writeFileSync('c:/antigravity/script.js', newLines.join('\n'), 'utf8');
console.log('Successfully injected Extra Details into all tools.');
