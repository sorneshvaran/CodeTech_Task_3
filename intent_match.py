from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import preprocess_text

class IntentMatcher:
    def __init__(self, patterns, preprocessed_patterns):
        self.patterns = patterns
        self.preprocessed_patterns = preprocessed_patterns

    def match(self, processed_input):
        # Use similarity (e.g., Jaccard, spaCy, etc.)
        best_score = 0
        best_index = None
        for i, pattern in enumerate(self.preprocessed_patterns):
            score = self.similarity(processed_input, pattern)
            if score > best_score:
                best_score = score
                best_index = i
        return best_index, best_score

    def similarity(self, a, b):
        # Simple Jaccard similarity for demonstration
        set_a = set(a.split())
        set_b = set(b.split())
        if not set_a or not set_b:
            return 0
        return len(set_a & set_b) / len(set_a | set_b)