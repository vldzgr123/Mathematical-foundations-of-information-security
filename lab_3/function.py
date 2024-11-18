import re
import matplotlib.pyplot as plt
import math
from collections import Counter

def get_kgram(text, k):
    processed_text = preprocess_text(text)
    return [processed_text[i:i+k] for i in range(len(text) - k + 1) if len(processed_text[i:i+k]) == k]

def calculate_frequency_kgram(text, k):
    kgram = get_kgram(text, k)

    kgram_count = Counter(kgram)

    kgram_sum = sum(kgram_count.values())

    freqs = {key: value / kgram_sum for key, value in kgram_count.items()}
    
    return freqs

def calculate_entropy_kgrams(text, k):
    freqs = calculate_frequency_kgram(text, k)

    entropy = -sum(p * math.log2(p) for p in freqs.values())

    return entropy

def preprocess_text(text):
    return ''.join(re.findall(r'[а-яё]', text.lower()))

def calculate_entropy_normalized(text, k):
    entropy = calculate_entropy_kgrams(text, k)

    return entropy / k

def plot_entropy_vs_k(text, max_k):
    ks = range(1, max_k + 1)
    entropies = [calculate_entropy_kgrams(text, k) for k in ks]
    entropies_norm = [calculate_entropy_normalized(text, k) for k in ks]
    print(f'Hk(T): {entropies}\nHk(T)/k: {entropies_norm}')

    plt.figure(figsize=(8, 5))
    plt.plot(ks, entropies_norm, marker='o', linestyle='-', color='b')
    plt.title("Зависимость H_k(T)/k от k")
    plt.xlabel("k (длина k-грамм)")
    plt.ylabel("H_k(T)/k")
    plt.xticks(ks)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    text_input = "Я был разбужен спозаранку Щелчком оконного стекла. Размокшей каменной баранкой В воде Венеция плыла. Все было тихо, и, однако, Во сне я слышал крик, и он Подобьем смолкнувшего знака Еще тревожил небосклон."
    plot_entropy_vs_k(text_input, 5)
