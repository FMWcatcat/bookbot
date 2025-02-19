def main():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        word_count = len(file_contents.split())

        
        char_count = ({})
        #keys = char_count.keys()
        #values = char_count.values()
        for c in file_contents.lower():
            if c.isalpha():
                if c in char_count:
                    char_count [c] += 1
                else:
                    char_count [c] = 1
        char_count2 = [{'character': key, 'num': value} for key, value in char_count.items()]
        def sort_on(char_count2):
            return char_count2['num']
        
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print("")
        char_count2.sort(reverse=True, key=sort_on)
        for char_dict in char_count2:

            print(f"The '{char_dict['character']}' character was found {char_dict['num']} times")
        

        

        
main()