from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    repo_url = data.get('repo_url')

    if not repo_url:
        return jsonify({'error': 'Repo URL missing'}), 400

    # Temporary dummy response
    return jsonify({
        'score': {
            'total': 75,
            'breakdown': {
                'documentation': 20,
                'code_quality': 25,
                'testing': 15,
                'community': 15
            }
        },
        'summary': 'The repository is well structured but lacks automated tests.',
        'roadmap': 'Add unit tests, improve README, set up CI/CD.'
    })

if __name__ == '__main__':
    app.run(debug=True)
