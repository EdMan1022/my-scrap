

def clear_term():
    print(chr(27) + "[2J")


if __name__ == "__main__":

    clear_term()
    
    print("Here's some junk")
    print("that we may want")
    print("to clear away")
    input()
    clear_term()

    print("Hey that worked")
    print("and now I can print as I please!")