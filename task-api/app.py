import os
import yaml
from flask import Flask, jsonify, render_template_string, send_from_directory, redirect

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Route /openapi.json (trả về toàn bộ nội dung OpenAPI dạng JSON)
@app.route('/openapi.json', methods=['GET'])
def get_openapi_json():
    # Tìm file openAI.yaml hoặc openapi.yaml
    file_name = 'openAI.yaml' if os.path.exists(os.path.join(BASE_DIR, 'openAI.yaml')) else 'openapi.yaml'
    yaml_path = os.path.join(BASE_DIR, file_name)
    
    with open(yaml_path, 'r', encoding='utf-8') as f:
        spec = yaml.safe_load(f)
    return jsonify(spec)

# 2. Hỗ trợ phục vụ các file YAML con trong paths/ và components/ khi Swagger UI gọi $ref
@app.route('/paths/<path:filename>', methods=['GET'])
def serve_paths(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'paths'), filename)

@app.route('/components/<path:filename>', methods=['GET'])
def serve_components(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'components'), filename)

# 3. Route /docs (Giao diện Swagger UI trực quan)
SWAGGER_UI_HTML = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Book Management API - Swagger UI</title>
  <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css" />
  <style>
    body { margin: 0; padding: 0; background: #fafafa; }
    .topbar { display: none; }
  </style>
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script>
    window.onload = () => {
      SwaggerUIBundle({
        url: '/openapi.json',
        dom_id: '#swagger-ui',
        deepLinking: true,
        presets: [SwaggerUIBundle.presets.apis],
        layout: "BaseLayout"
      });
    };
  </script>
</body>
</html>"""

@app.route('/docs', methods=['GET'])
def get_docs():
    return render_template_string(SWAGGER_UI_HTML)

# Tự động chuyển hướng từ trang chủ vào /docs
@app.route('/')
def home():
    return redirect('/docs')

if __name__ == '__main__':
    print("====================================================")
    print("🚀 Flask Server đang chạy tại: http://localhost:5000")
    print("👉 Xem tài liệu Swagger UI:  http://localhost:5000/docs")
    print("👉 Xem file OpenAPI JSON:     http://localhost:5000/openapi.json")
    print("====================================================")
    app.run(host='0.0.0.0', port=5000, debug=True)
