from sentence_transformers import SentenceTransformer

# download embeddings model
model = SentenceTransformer('all-MiniLM-L6-v2')
model.save('local_models/all-MiniLM-L6-v2') 