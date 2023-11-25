from flask import Flask, render_template, request
import os
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import PorterStemmer

app = Flask(__name__)

# Step 3: Read and Parse Documentation
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

# Step 4: Tokenization and Text Processing
nlp = spacy.load("en_core_web_sm")
ps = PorterStemmer()

def preprocess_text(text):
    doc = nlp(text)
    return [ps.stem(token.lemma_) for token in doc if not token.is_stop and not token.is_punct]

processed_docs = [preprocess_text(doc) for doc in documents]

# Step 5: Build a Knowledge Base
knowledge_base = dict(zip(map(tuple, processed_docs), documents))

# Step 7: Answer Retrieval
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([" ".join(doc) for doc in processed_docs])

# History to store chat interactions
chat_history = []

def get_most_similar(query_vector):
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)
    most_similar_index = similarity_scores.argmax()
    return knowledge_base[tuple(processed_docs[most_similar_index])]

def extract_relevant_info(document, query):
    sentences = document.split(". ")  # Split the document into sentences
    query_vector = vectorizer.transform([" ".join(preprocess_text(query))])
    similarity_scores = cosine_similarity(query_vector,
                                          vectorizer.transform([" ".join(preprocess_text(sent)) for sent in sentences]))

    # Set a higher threshold for similarity scores to filter out less relevant answers
    threshold = 0.1  # Adjust this threshold based on your needs

    # Check if there are any sentences in the document
    if len(sentences) == 0:
        return "I can't answer this question."

    # Find the index of the most similar sentence with a score above the threshold
    valid_indices = [i for i, score in enumerate(similarity_scores[0]) if score > threshold]

    if not valid_indices:
        return "I can't answer this question."

    most_similar_sentence_index = valid_indices[0]

    # Check if the index is within the valid range
    if 0 <= most_similar_sentence_index < len(sentences):
        return sentences[most_similar_sentence_index]
    else:
        return "I can't answer this question."

# Intent Recognition
def extract_intent(text):
    doc = nlp(text)
    return doc.cats  # Assuming you have a model trained for intent classification

# Named Entity Recognition (NER)
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Flask routes
@app.route('/')
def index():
    reversed_chat_history = chat_history[::-1]  # Reverse the order
    return render_template('index.html', chat_history=reversed_chat_history)

# Add other routes as needed, such as image display

# Chat route
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    # Extract intent and entities
    intent = extract_intent(user_input)
    entities = extract_entities(user_input)

    # Process text as usual if not an image
    processed_query = preprocess_text(user_input)
    query_vector = vectorizer.transform([" ".join(processed_query)])
    most_similar_document = get_most_similar(query_vector)

    # Extract relevant information from the document based on the user's query
    relevant_info = extract_relevant_info(most_similar_document, user_input)

    chat_history.append({'user_input': user_input, 'intent': intent, 'entities': entities, 'answer': relevant_info})
    return render_template('index.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)
