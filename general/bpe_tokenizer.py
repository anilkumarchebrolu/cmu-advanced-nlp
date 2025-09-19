from collections import Counter, defaultdict

# Our tiny corpus
corpus_words = ["low", "lower", "hell", "hello", "hello"]

# Turn each word into a list of chars + end marker
def tokenize(word):
    return list(word) + ["</w>"]

corpus = [tokenize(w) for w in corpus_words]

def get_stats(corpus):
    """Count frequency of adjacent pairs in the corpus."""
    pairs = Counter()
    for word in corpus:
        for i in range(len(word)-1):
            pairs[(word[i], word[i+1])] += 1
    return pairs

def merge_pair(pair, corpus):
    """Merge all occurrences of a given pair in the corpus."""
    new_corpus = []
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word in corpus:
        i = 0
        new_word = []
        while i < len(word):
            # If next two symbols match the pair, merge them
            if i < len(word)-1 and (word[i], word[i+1]) == pair:
                new_word.append(replacement)
                i += 2
            else:
                new_word.append(word[i])
                i += 1
        new_corpus.append(new_word)
    return new_corpus

# BPE loop
vocab = set()  # for demonstration

print("Initial Corpus:", corpus)

for step in range(5):  # do a few merges
    pairs = get_stats(corpus)
    if not pairs:
        break
    best = max(pairs, key=pairs.get)
    print(f"\nStep {step+1} - Most frequent pair: {best} (count={pairs[best]})")
    corpus = merge_pair(best, corpus)
    print("New Corpus:", corpus)
    vocab.add(''.join(best))

print("\nFinal Corpus:", corpus)
print("Collected merged tokens:", vocab)
