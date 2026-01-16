from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from visualisation import visualise

app = Flask(__name__)
# Allow CORS for frontend at http://127.0.0.1:3000
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:3000"}}, supports_credentials=True)

@app.route('/visualisation', methods=['POST'])
@app.route('/generate-graph', methods=['POST'])
def generate_graph():
    """API endpoint to generate a single graph"""
    print("DEBUG: generate_graph() was called!")
        # Handle preflight OPTIONS request for CORS
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
        response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
    try:
        data = request.get_json()
        print(f"DEBUG: request.get_json() returned: {data}")
        
        professor_name = data.get('professor', 'Unknown Professor')
        criteria = data.get('criteria', 'criteria1')
        lowest_grade = data.get('lowest_grade', 'P')
        
        print(f"DEBUG: Received professor={professor_name}, criteria={criteria}, lowest_grade={lowest_grade}")
        
        # Generate the visualization
        image_base64 = visualise(professor_name, criteria, lowest_grade)
        
        if not image_base64:
            print("DEBUG: visualise() returned empty/None")
            response = jsonify({
                    'success': False,
                    'error': 'No data available'
                })
            response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
            response.headers['Access-Control-Allow-Credentials'] = 'true'
            return response, 500
        
        print(f"DEBUG: image_base64 length: {len(image_base64)}")
        
        response = jsonify({
                'success': True,
                'image': image_base64,
                'criteria': criteria,
                'professor': professor_name
            })
        response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
    
    except Exception as e:
        print(f"DEBUG: Exception occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        response = jsonify({
                'success': False,
                'error': str(e)
            })
        response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response, 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=5000)