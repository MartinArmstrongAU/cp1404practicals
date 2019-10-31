import wikipedia


def main():
    user_search = input("What would you like to search for on wikipedia? ")
    while user_search != "":
        try:
            # page_summary = wikipedia.summary(user_search)
            # print(page_summary)
            entire_page = wikipedia.page(user_search)
            print(entire_page.title)
            print(entire_page.summary)
            print(entire_page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)

        user_search = input("What would you like to search for on wikipedia?")


if __name__ == '__main__':
    main()