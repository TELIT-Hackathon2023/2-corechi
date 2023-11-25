from flask import Flask, render_template, request
import os
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import PorterStemmer

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
ps = PorterStemmer()


def preprocess_text(text):
    doc = nlp(text)
    return [ps.stem(token.lemma_) for token in doc if not token.is_stop and not token.is_punct]


processed_docs = [preprocess_text(doc) for doc in documents]

knowledge_base = dict(zip(map(tuple, processed_docs), documents))

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([" ".join(doc) for doc in processed_docs])

chat_history = []


def get_most_similar(query_vector):
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)
    most_similar_index = similarity_scores.argmax()
    return knowledge_base[tuple(processed_docs[most_similar_index])]


def extract_relevant_info(document, query):
    sentences = document.split(". ")
    query_vector = vectorizer.transform([" ".join(preprocess_text(query))])
    similarity_scores = cosine_similarity(query_vector,
                                          vectorizer.transform([" ".join(preprocess_text(sent)) for sent in sentences]))

    threshold = 0.1

    if len(sentences) == 0:
        return "Please enter valid input."

    valid_indices = [i for i, score in enumerate(similarity_scores[0]) if score > threshold]

    if not valid_indices:
        # zavolať JiraCreatePY na vytvorenie JIRA Ticketu
        # JiraCreatePY.create_jira_ticket()
        return "I can't answer this question. Jira Ticket will be created "

    most_similar_sentence_index = valid_indices[0]

    if 0 <= most_similar_sentence_index < len(sentences):
        return sentences[most_similar_sentence_index]
    else:
        # zavolať JiraCreatePY na vytvorenie JIRA Ticketu
        # JiraCreatePY.create_jira_ticket()
        return "I can't answer this question. Jira Ticket will be created "


def extract_intent(text):
    doc = nlp(text)
    return doc.cats


def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities


@app.route('/')
def index():
    reversed_chat_history = chat_history[::-1]
    return render_template('index.html', chat_history=reversed_chat_history)


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    intent = extract_intent(user_input)
    entities = extract_entities(user_input)

    processed_query = preprocess_text(user_input)
    query_vector = vectorizer.transform([" ".join(processed_query)])
    most_similar_document = get_most_similar(query_vector)

    relevant_info = extract_relevant_info(most_similar_document, user_input)

    chat_history.append({'user_input': user_input, 'intent': intent, 'entities': entities, 'answer': relevant_info})
    return render_template('index.html', chat_history=chat_history)


if __name__ == '__main__':
    app.run(debug=True)