import os
import socket
from collections import Counter

directory = "/home/data"
files_to_read = ['IF.txt', 'Limerick-1.txt']
output_file_path = "/home/output/result.txt"

def list_text_files():
    text_files = [file for file in os.listdir(directory) if file.endswith('.txt')]
    
    return text_files

def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()

    return len(words)
        
def top_3_words():
    with open("/home/data/IF.txt", 'r') as file:
        text = file.read()
        words = text.split()
        word_counts = Counter(words)

        top_3 = word_counts.most_common(3)
        
    return top_3

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    return ip_address
    
def main():
    if not os.path.exists(output_file_path):
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    
    with open(output_file_path, 'w') as output_file:
        #List all text files
        text_files = list_text_files()
        output_file.write("All text files:\n")
        for file in text_files:
            output_file.write(f"{file}\n")

        #Count words
        total_words = 0
        output_file.write("Word counts for text files in directory:\n")

        for file_name in files_to_read:
            file_path = os.path.join(directory, file_name)

            if os.path.exists(file_path):
                word_count = count_words_in_file(file_path)
                total_words += word_count
                output_file.write(f"{file_name}: {word_count} words\n")
            else:
                output_file.write(f"{file_name}: File not found\n")

        output_file.write(f"Total number of words: {total_words} words\n")

        #Top 3 words in IF.txt
        top_3 = top_3_words()
        output_file.write(f"Top 3 words with maximum counts:\n")
        for word, count in top_3:
            output_file.write(f"{word}: {count} times\n")
        
        #IP address
        ip_address = get_ip_address()
        output_file.write("IP Address: " + ip_address)

    #Print 
    with open(output_file_path, 'r') as output_file:
        content = output_file.read()
        print(content)

if __name__ == "__main__":
    main()
