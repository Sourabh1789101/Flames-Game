def remove_common_chars(name1, name2):
    # Convert names to lists to remove characters
    name1_list = list(name1)
    name2_list = list(name2)

    for char in name1:
        if char in name2_list:
            name1_list.remove(char)
            name2_list.remove(char)

    return len(name1_list) + len(name2_list)

def flames_game(player1, player2):
    count = remove_common_chars(player1, player2)
    flames = list("FLAMES")

    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]

    return flames[0]

def relationship_status(letter):
    status = {
        'F': "Friends",
        'L': "Lovers",
        'A': "Affectionate",
        'M': "Marriage",
        'E': "Enemies",
        'S': "Siblings"
    }
    return status[letter]

def main():
    player1 = input("Enter the first name: ").lower().replace(" ", "")
    player2 = input("Enter the second name: ").lower().replace(" ", "")

    result_letter = flames_game(player1, player2)
    status = relationship_status(result_letter)

    print(f"The relationship status between {player1} and {player2} is: {status}")

if __name__ == "__main__":
    main()
