import tkinter as tk
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

# Store history
history = []

# ---------- Sentiment Analysis ----------
def analyze_text():
    text = text_box.get("1.0", tk.END).strip()

    if text == "":
        result_label.config(text="Please enter text", fg="orange")
        return

    analysis = TextBlob(text)
    score = analysis.sentiment.polarity

    if score > 0.3:
        mood = "Happy "
        color = "green"
    elif score < -0.3:
        mood = "Sad/Angry "
        color = "red"
    else:
        mood = "Neutral   "
        color = "blue"

    result_label.config(text=f"Mood: {mood}", fg=color)
    score_label.config(text=f"Score: {score:.2f}")

    history.append(score)

# ---------- Show Chart ----------
def show_chart():
    if len(history) == 0:
        return

    df = pd.DataFrame(history, columns=["Sentiment Score"])

    plt.figure()
    plt.plot(df["Sentiment Score"], marker='o')
    plt.title("Sentiment Trend")
    plt.xlabel("Entry Number")
    plt.ylabel("Sentiment Score")
    plt.show()

# ---------- Clear Text ----------
def clear_text():
    text_box.delete("1.0", tk.END)
    result_label.config(text="Mood:")
    score_label.config(text="")

# ---------- GUI ----------
root = tk.Tk()
root.title("AI Sentiment Dashboard")
root.geometry("520x420")
root.configure(bg="#0f172a")

card = tk.Frame(root, bg="white")
card.place(relx=0.5, rely=0.5, anchor="center", width=470, height=360)

title = tk.Label(card, text="AI Sentiment Dashboard",
                 font=("Segoe UI",20,"bold"), bg="white")
title.pack(pady=15)

text_box = tk.Text(card, height=5, width=45)
text_box.pack(pady=10)

button_frame = tk.Frame(card, bg="white")
button_frame.pack(pady=10)

analyze_btn = tk.Button(button_frame,text="Analyze",
                        bg="#2563eb",fg="white",
                        command=analyze_text)
analyze_btn.grid(row=0,column=0,padx=10)

clear_btn = tk.Button(button_frame,text="Clear",
                      bg="#ef4444",fg="white",
                      command=clear_text)
clear_btn.grid(row=0,column=1,padx=10)

chart_btn = tk.Button(button_frame,text="Show Chart",
                      bg="#10b981",fg="white",
                      command=show_chart)
chart_btn.grid(row=0,column=2,padx=10)

result_label = tk.Label(card,text="Mood:",font=("Segoe UI",16,"bold"),bg="white")
result_label.pack(pady=15)

score_label = tk.Label(card,text="",font=("Segoe UI",12),bg="white")
score_label.pack()

root.mainloop()