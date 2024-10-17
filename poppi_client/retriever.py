import base64
import faiss


class VectorStoreRetriever:
    def __init__(self, decoded_data):
        self.data = decoded_data
        self.index = faiss.deserialize_index(self.data)

    # def load_index(self):
    #     # Load the serialized binary data from MongoDB
    #     stored_data = self.collection.find_one({"_id": "your_index_id"})  # Adjust as necessary
    #     binary_data = stored_data["index_binary"]
    #     self.index = load_index_from_binary(binary_data)

    def search_index(self, query_vector, k=3):
    # Convert the query vector to the required shape
        if len(query_vector.shape) == 1:
            query_vector = query_vector.reshape(1, -1)
        
        # Perform the search (k nearest neighbors)
        distances, indices = self.index.search(query_vector, k)
        return distances, indices

    def retrieve(self, query_vector, k=3):
        # Ensure the index is loaded
        if not hasattr(self, 'index'):
            self.load_index()

        # Search the index for similar vectors
        distances, indices = self.search_index(self.index, query_vector, k)
        
        # Get metadata or texts based on the retrieved indices
        retrieved_items = []
        for idx in indices[0]:
            retrieved_items.append(self.collection.find_one({"vector_index": idx}))
        
        return retrieved_items
