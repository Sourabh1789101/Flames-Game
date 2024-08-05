import tkinter as tk

def remove_common_chars(name1, name2):
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
        'F': "Friends 😊",
        'L': "Lovers ❤️",
        'A': "Affectionate 🥰",
        'M': "Marriage 💍",
        'E': "Enemies 😠",
        'S': "Siblings 👨‍👩‍👧‍👦"
    }
    return status[letter]

def tell_status():
    player1 = Player1_field.get().lower().replace(" ", "")
    player2 = Player2_field.get().lower().replace(" ", "")

    result_letter = flames_game(player1, player2)
    status = relationship_status(result_letter)

    Status_field.config(state=tk.NORMAL)
    Status_field.delete(0, tk.END)
    Status_field.insert(10, status)
    Status_field.config(state=tk.DISABLED)

def clear_all():
    Player1_field.delete(0, tk.END)
    Player2_field.delete(0, tk.END)
    Status_field.config(state=tk.NORMAL)
    Status_field.delete(0, tk.END)
    Status_field.config(state=tk.DISABLED)
    Player1_field.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300")
    root.title("FLAMES Game")
    root.resizable(0, 0)
    root.configure(bg="#ffcccc")

    title_label = tk.Label(root, text="FLAMES Relationship Calculator", bg="#ffcccc", fg="#800080", font=("Helvetica", 18, "bold"))
    title_label.grid(row=0, columnspan=2, pady=10)

    tk.Label(root, text="Partner 1 Name:", bg="#ffcccc", fg="#333333", font=("Helvetica", 12, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    tk.Label(root, text="Partner 2 Name:", bg="#ffcccc", fg="#333333", font=("Helvetica", 12, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="e")
    tk.Label(root, text="Relationship:", bg="#ffcccc", fg="#333333", font=("Helvetica", 12, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="e")

    Player1_field = tk.Entry(root, font=("Helvetica", 12), bg="#ffecf0")
    Player2_field = tk.Entry(root, font=("Helvetica", 12), bg="#ffecf0")
    Status_field = tk.Entry(root, font=("Helvetica", 12), bg="#ffecf0", state=tk.DISABLED)

    Player1_field.grid(row=1, column=1, padx=10, pady=10)
    Player2_field.grid(row=2, column=1, padx=10, pady=10)
    Status_field.grid(row=3, column=1, padx=10, pady=10)

    button_style = {'bg': "#ff66b2", 'fg': "white", 'font': ("Helvetica", 12, "bold"), 'relief': tk.RAISED, 'bd': 2, 'width': 10}

    tk.Button(root, text="Submit", command=tell_status, **button_style).grid(row=4, column=0, padx=10, pady=20)
    tk.Button(root, text="Clear", command=clear_all, **button_style).grid(row=4, column=1, padx=10, pady=20)

    root.mainloop()
