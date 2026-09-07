with open('static/js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any broken split or replace
import re

text = re.sub(
    r'const clean = text\.replace\(/\[\*\_\#🎯⚠️💡👉📌🔥⚡\]/g, ""\)\.split\(\s*"\s*"\)\.join\("\. "\);',
    'const clean = text.replace(/[*_#🎯⚠️💡👉📌🔥⚡]/g, "").split(String.fromCharCode(10)).join(". ");',
    text
)

# Also replace literal newlines inside strings if any
lines = text.splitlines()
fixed_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if 'function speakCoachText' in line:
        fixed_lines.append(line)
        fixed_lines.append('  if (!window.speechSynthesis || !audioEnabled) return;')
        fixed_lines.append('  window.speechSynthesis.cancel();')
        fixed_lines.append('  const clean = text.replace(/[*_#🎯⚠️💡👉📌🔥⚡]/g, "").split(String.fromCharCode(10)).join(". ");')
        fixed_lines.append('  const utter = new SpeechSynthesisUtterance(clean);')
        fixed_lines.append('  utter.rate = 1.0;')
        fixed_lines.append('  utter.pitch = 1.0;')
        fixed_lines.append('  window.speechSynthesis.speak(utter);')
        fixed_lines.append('}')
        # skip to next function
        while i < len(lines) and not lines[i].strip().startswith('async function loadMistakeVault'):
            i += 1
        continue
    else:
        fixed_lines.append(line)
        i += 1

with open('static/js/app.js', 'w', encoding='utf-8') as f:
    f.write('\n'.join(fixed_lines) + '\n')

print("Replacement complete via tools/fix_js.py!")
