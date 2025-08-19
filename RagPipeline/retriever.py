def retreiveFromVector(vector):
    retriever = vector.as_retriever(
        search_type = "similarity",  # cosine similarity
        search_kwargs = {"k": 6}     # top 3 results
    )

    return retriever