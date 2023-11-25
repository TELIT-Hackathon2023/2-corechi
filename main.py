from flask import Flask, render_template, request
import os
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)


docs_folder = "DTIT TARDIS AI ChatBot -- Hackathon Kosice 2023/customer_handbook/docs"


def read_docs(folder):
    documents = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    documents.append(f.read())
    return documents


documents = read_docs(docs_folder)


nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):
    doc = nlp(text)
    return [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]


processed_docs = [preprocess_text(doc) for doc in documents]


knowledge_base = dict(zip(map(tuple, processed_docs), documents))


vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([" ".join(doc) for doc in processed_docs])


def get_most_similar(query_vector):
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)
    most_similar_index = similarity_scores.argmax()
    return knowledge_base[tuple(processed_docs[most_similar_index])]


def extract_relevant_info(document, query):
    sentences = document.split(". ")  
    query_vector = vectorizer.transform([" ".join(preprocess_text(query))])
    similarity_scores = cosine_similarity(query_vector, vectorizer.transform([" ".join(preprocess_text(sent)) for sent in sentences]))
    most_similar_sentence_index = similarity_scores.argmax()
    return sentences[most_similar_sentence_index]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/obrazok')
def display_image():
    return render_template('D:/python_projekty/docs/obrazok.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    if '![' in user_input and '](img/' in user_input:
        img_src = user_input.split('](img/')[1].split(')')[0]

        img_path = os.path.join(os.path.dirname(__file__), 'static', 'img', img_src)
        if os.path.exists(img_path):
            return render_template('index.html', user_input=user_input, img_src=img_src)

    processed_query = preprocess_text(user_input)
    query_vector = vectorizer.transform([" ".join(processed_query)])
    most_similar_document = get_most_similar(query_vector)

    relevant_info = extract_relevant_info(most_similar_document, user_input)

    return render_template('index.html', user_input=user_input, answer=relevant_info)


if __name__ == '__main__':
    app.run(debug=True)
