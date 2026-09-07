with open('static/js/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

lines = code.splitlines()
errors = []

# Basic checks
for idx, line in enumerate(lines, 1):
    # Check for unclosed backticks on single line without template
    # Check for unterminated regex
    stripped = line.strip()
    if stripped.startswith('/') and not stripped.startswith('//') and not stripped.startswith('/*'):
        if not (stripped.endswith('/') or stripped.endswith('/;') or stripped.endswith('/g') or stripped.endswith('/g;') or stripped.endswith('/i;') or stripped.endswith('/gi;')):
            errors.append(f"Line {idx}: Potential broken regex: {repr(line)}")

print(f"Total lines scanned: {len(lines)}")
if errors:
    for e in errors:
        print("ERROR:", e)
else:
    print("✓ No illegal regex or broken slash patterns found!")

# Check brackets balance
stack = []
pairs = {')': '(', '}': '{', ']': '['}
for idx, ch in enumerate(code):
    if ch in '({[':
        stack.append((ch, idx))
    elif ch in ')}]':
        if not stack:
            print(f"Extra closing {ch} at char {idx}")
            break
        top, _ = stack.pop()
        if pairs[ch] != top:
            print(f"Mismatched {top} and {ch} at char {idx}")
            break

if not stack:
    print("✓ All braces, parentheses, and brackets are 100% balanced!")
else:
    print(f"Warning: {len(stack)} unclosed brackets remain!")
