def sort_on(dict):
    return dict["num"]

def main():
    cur_file_path = "books/frankenstein"
    with open(cur_file_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        #print(file_contents)
        #print(words)

        char_dict = {}

        for char in file_contents.lower():
            if char.isalpha():
                char_dict[char] = char_dict.get(char, 0) + 1
        
        #print(char_dict)

        new_dict = []

        for char, count in char_dict.items():
            temp_dict = {}
            temp_dict["char"] = char
            temp_dict["num"] = count
            new_dict.append(temp_dict)

        new_dict.sort(reverse=True, key=sort_on)
        #print(new_dict)

        print(f"--- Begin report of {cur_file_path}.txt ---")
        print(f"{len(words)} words found in the document")
        print()

        for i in range(len(new_dict)):
            print(f"The '{new_dict[i]["char"]}' character was found {new_dict[i]["num"]} times")

        print("--- End report ---")


main()