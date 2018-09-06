

def clear_term():
    print(chr(27) + "[2J")
    print(chr(27) + "[37m")


if __name__ == "__main__":
    print(chr(27) + "[31m")
    print("Here's some junk")
    print("that we may want")
    print("to clear away")
    input()
    clear_term()

    print("Hey that worked")
    print("and now I can print as I please!")