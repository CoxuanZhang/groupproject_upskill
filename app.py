from flask import Flask, render_template, request, jsonify
from visualisation import visualise

app = Flask(__name__)

@app.route('/generate-graph', methods=['POST'])
def generate_graph():
    """API endpoint to generate a single graph"""
    try:
        data = request.get_json()
        professor_name = data.get('professor', 'Unknown Professor')
        criteria = data.get('criteria', 'criteria1')
        lowest_grade = data.get('lowest_grade', 'P')
        
        # Generate the visualization
        image_base64 = visualise(professor_name, criteria, lowest_grade)
        
        return jsonify({
            'success': True,
            'image': image_base64,
            'criteria': criteria,
            'professor': professor_name
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)