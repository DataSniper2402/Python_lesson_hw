import threading
from collections import Counter

def process_lines(lines, result_list, index):
    word_count = Counter()
    for line in lines:
        words = line.strip().split()
        word_count.update(words)
    result_list[index] = word_count

def threaded_word_count(file_path, num_threads=4):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    threads = []
    results = [None] * num_threads

    step = len(lines) // num_threads
    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i < num_threads - 1 else len(lines)
        t = threading.Thread(target=process_lines, args=(lines[start:end], results, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    
    final_count = Counter()
    for r in results:
        final_count.update(r)

    return final_count


if __name__ == "__main__":
    word_counts = threaded_word_count("sample.txt", num_threads=3)
    print("Word occurrences:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")
