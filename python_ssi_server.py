from flask import Flask, request, jsonify
from flask_cors import CORS
from sentence_transformers import SentenceTransformer
import numpy as np

app = Flask(__name__)
CORS(app)  # Allow browser to access localhost

# Load the model once at startup (768-dimensional embeddings)
print("Loading Sentence-BERT model...")
model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
print("Model loaded successfully!")

@app.route('/calculate_ssi', methods=['POST'])
def calculate_ssi():
    try:
        data = request.json
        texts = data['texts']
        
        if len(texts) < 2:
            return jsonify({'error': 'At least 2 texts required'}), 400
        
        # Generate embeddings for all texts
        embeddings = model.encode(texts)
        
        # Calculate pairwise cosine similarities
        n = len(embeddings)
        sum_similarities = 0
        pair_count = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                # Cosine similarity
                similarity = np.dot(embeddings[i], embeddings[j]) / (
                    np.linalg.norm(embeddings[i]) * np.linalg.norm(embeddings[j])
                )
                sum_similarities += similarity
                pair_count += 1
        
        # Calculate SSI using formula: 2/(n(n-1)) * sum of pairwise similarities
        ssi = (2 / (n * (n - 1))) * sum_similarities
        
        return jsonify({
            'ssi': float(ssi),
            'n_texts': n,
            'n_pairs': pair_count
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'running', 'model': 'all-mpnet-base-v2'})

if __name__ == '__main__':
    print("\nStarting SSI Calculator Backend Server...")
    print("Server running on http://localhost:5000")
    print("Press CTRL+C to stop\n")
    app.run(host='localhost', port=5000, debug=True)
