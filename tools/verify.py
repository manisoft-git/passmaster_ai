with open('static/js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(len(lines)):
    if 'function speakCoachText' in lines[i]:
        for j in range(i, min(i + 12, len(lines))):
            print(f"{j+1}: {repr(lines[j])}")
        break
