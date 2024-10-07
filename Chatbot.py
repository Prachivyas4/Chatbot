import tkinter as tk
from nltk.chat.util import Chat


# Define chatbot pairs (same as your code)
pairs = [
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
[
        r"what is your name ?",
        ["I am a bot created by Prachi Vyas. you can call me Bot!", ]
    ],

    [
        r"Improve Flexibility",
        ["Surya namaskar can be helpful in improving flexibility", ]
    ],

[
        r"lower back pain",
        ["Pelvic tilts and Cat-cow stretch can help with lower back pain", ]
    ],
    [
        r"Knee pain",
        ["Straight Leg raises and Seated leg extensions an help with knee pain", ]
    ],
    [
        r"Menstrual pain",
        ["Pelvic tilt and child Pose can help with menstrual pain", ]
    ],
    [
        r"Arthritis related joint pain",
        ["Range of motion exercises and low impact activities such as walking,cycling etc can help ", ]
    ],

    [
        r"thanks",
        ["Your welcome"]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
    [
    r"(.*)",
    ["I'm sorry, I don't understand. Could you please rephrase your question or provide more information?"]
    ]
]


def get_response(user_input):
  """
  Processes user input using the Chat class
  """
  chat = Chat(pairs)
  return chat.respond(user_input)


def send_message(event=None):
  """
  Gets user input, finds a matching response, and displays it.
  """

  user_input = entry.get().lower()
  chat_history.insert(tk.END, "You: " + user_input + "\n")

  entry.delete(0, tk.END)  # Clear entry field

  bot_response = get_response(user_input)

  chat_history.insert(tk.END, "Chatbot: " + bot_response + "\n\n")
  chat_history.see(tk.END)  # Scroll to the end of the chat history


# Create the main window
root = tk.Tk()
root.title("Chatbot - Home Fitness App by Prachi Vyas")
root.configure(bg="darkgray")

# Create chat history text area
chat_history = tk.Text(root, height=5, width=20)
chat_history.pack(fill=tk.BOTH, expand=True)

# Create user input entry field with styling
entry_style = {"background": "lightblue", "font": ("Arial", 14)}
entry = tk.Entry(root, width=50, **entry_style)
entry.bind("<Return>", send_message)  # Send message on Enter key press
entry.pack(fill=tk.X, padx=10, pady=10)

# Create send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.BOTTOM)

# Start the main event loop
root.mainloop()


