with open('app.py', 'r', encoding='utf-8') as f:
    code = f.read()

after_req = """
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
"""

if 'def add_header' not in code:
    code = code.replace("app = Flask(__name__)", "app = Flask(__name__)\n" + after_req)
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Added no-cache headers to app.py!")
else:
    print("Already present.")
