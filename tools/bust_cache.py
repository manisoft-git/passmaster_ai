with open('templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update script tag with cache-buster
import time
v = int(time.time())
html = html.replace('/static/js/app.js', f'/static/js/app.js?v={v}')
html = html.replace('/static/css/styles.css', f'/static/css/styles.css?v={v}')

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Updated index.html with cache-buster ?v={v}!")
