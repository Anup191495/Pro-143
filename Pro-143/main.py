from flask import Flask, jsonify, request
from demographic_filtering import output
from content_filtering import get_recommendation, cosine_sim
from storage import all_articles, liked_articles, not_liked_articles

app = Flask(__name__)

def get_next_recommendation():
    return "Next Recommendation"

@app.route('/get_initial_article', methods=['GET'])
def get_initial_article():
    if all_articles:
        initial_article = all_articles[0]
        return jsonify({
            'article': initial_article,
            'status': 'success'
        })
    else:
        return jsonify({'status': 'no more articles'})

@app.route('/like_article/<int:contentId>', methods=['POST'])
def like_article(contentId):
    liked_articles.append(contentId)
    
    next_recommendation = get_next_recommendation()
    
    return jsonify({
        'status': 'success',
        'next_recommendation': next_recommendation
    })

@app.route('/dislike_article/<int:contentId>', methods=['POST'])
def dislike_article(contentId):
    not_liked_articles.append(contentId)
    
    next_recommendation = get_next_recommendation()
    
    return jsonify({
        'status': 'success',
        'next_recommendation': next_recommendation
    })

if __name__ == '__main__':
    app.run(debug=True)
