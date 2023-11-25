from flask import Flask, render_template, request
import os
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Step 3: Read and Parse Documentation
docs_folder = "docs"


def read_docs(folder):
    documents = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    documents.append(f.read())
    return documents


documents = read_docs(docs_folder)

# Step 4: Tokenization and Text Processing
nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):
    doc = nlp(text)
    return [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]


processed_docs = [preprocess_text(doc) for doc in documents]

# Step 5: Build a Knowledge Base
knowledge_base = dict(zip(map(tuple, processed_docs), documents))

# Step 7: Answer Retrieval
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([" ".join(doc) for doc in processed_docs])


def get_most_similar(query_vector):
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)
    most_similar_index = similarity_scores.argmax()
    return knowledge_base[tuple(processed_docs[most_similar_index])]


def extract_relevant_info(document, query):
    sentences = document.split(". ")  # Split the document into sentences
    query_vector = vectorizer.transform([" ".join(preprocess_text(query))])
    similarity_scores = cosine_similarity(query_vector, vectorizer.transform([" ".join(preprocess_text(sent)) for sent in sentences]))
    most_similar_sentence_index = similarity_scores.argmax()
    return sentences[most_similar_sentence_index]


# Flask routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/obrazok')
def display_image():
    return render_template('D:/python_projekty/docs/obrazok.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    # Check if the input contains an image tag
    if '![' in user_input and '](img/' in user_input:
        # Extract the image source from the input
        img_src = user_input.split('](img/')[1].split(')')[0]

        # Check if the image file exists
        img_path = os.path.join(os.path.dirname(__file__), 'static', 'img', img_src)
        if os.path.exists(img_path):
            return render_template('index.html', user_input=user_input, img_src=img_src)

    # Process text as usual if not an image
    processed_query = preprocess_text(user_input)
    query_vector = vectorizer.transform([" ".join(processed_query)])
    most_similar_document = get_most_similar(query_vector)

    # Extract relevant information from the document based on the user's query
    relevant_info = extract_relevant_info(most_similar_document, user_input)

    return render_template('index.html', user_input=user_input, answer=relevant_info)


if __name__ == '__main__':
    app.run(debug=True)
