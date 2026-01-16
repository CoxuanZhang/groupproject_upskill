from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from visualisation import visualise

app = Flask(__name__)
CORS(app)

@app.route('/visualisation', methods=['POST'])
@app.route('/generate-graph', methods=['POST'])
def generate_graph():
    """API endpoint to generate a single graph"""
    print("DEBUG: generate_graph() was called!")
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
            return jsonify({
                'success': False,
                'error': 'No data available'
            }), 500
        
        print(f"DEBUG: image_base64 length: {len(image_base64)}")
        
        return jsonify({
            'success': True,
            'image': image_base64,
            'criteria': criteria,
            'professor': professor_name
        })
    
    except Exception as e:
        print(f"DEBUG: Exception occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=5000)