def read_file(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    lowered = text.lower()

    c_dict = {}

    for c in lowered:
        if c.isalpha():
            if c in c_dict:
                c_dict[c] += 1
            else:
                c_dict[c] = 1

    return c_dict


def main():
    book_path = "books/frankenstein.txt"
    contents = read_file(book_path)
    cw = count_words(contents)
    cc = count_chars(contents)
    cs = dict(sorted(cc.items(), key=lambda item: item[1], reverse=True))
    print(cs['e'])


    print(f"--- Begin report of { book_path } ---")
    print(f"{ cw } words found in the document")
    for c in cs.items():
        print(f"The '{c[0]}' character was found {c[1]} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()
