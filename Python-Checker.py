import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_md")

def preprocess_text(text):
    """
    Preprocess the text by converting it to lowercase and removing unnecessary spaces.
    """
    return ' '.join(text.lower().strip().split())

def calculate_similarity(text1, text2):
    """
    Calculate the similarity between two texts using spaCy.
    """
    # Preprocess the texts
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)
    
    # Convert the texts to spaCy Doc objects
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    
    # Calculate the similarity
    similarity = doc1.similarity(doc2)
    return similarity

def main():
    # Example texts
    text1 = """
    Natural language processing (NLP) is a field of artificial intelligence that focuses on the interaction
    between computers and humans through natural language. The ultimate objective of NLP is to enable computers
    to understand, interpret, and generate human language in a way that is both meaningful and useful.
    NLP, or natural language processing, is an area of AI that deals with the interaction between computers and humans
    using natural language. The goal is to enable machines to understand, interpret, and produce human language in a
    valuable and meaningful manner.
    """
    
    text2 = """
    NLP, or natural language processing, is an area of AI that deals with the interaction between computers and humans
    using natural language. The goal is to enable machines to understand, interpret, and produce human language in a
    valuable and meaningful manner.
    """
    
    # Calculate similarity
    similarity_score = calculate_similarity(text1, text2)
    print(f"Similarity Score: {similarity_score:.2f}")
    
    # Check for plagiarism (example threshold)
    threshold = 0.75
    if similarity_score > threshold:
        print("Potential plagiarism detected!")
    else:
        print("No significant plagiarism detected.")

if __name__ == "__main__":
    main()
