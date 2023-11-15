from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

df = pd.read_csv('articles.csv')
df = df.dropna(subset=['title'])

df = df[df['lang'] == 'en']

count = CountVectorizer()
count_matrix = count.fit_transform(df['title'])

cosine_sim = cosine_similarity(count_matrix, count_matrix)

df = df.set_index('title')

def get_recommendation(contentId, cosine_sim):
    idx = df.index[df['contentId'] == contentId][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    recommendations = df.iloc[sim_scores].index.tolist()
    return recommendations
