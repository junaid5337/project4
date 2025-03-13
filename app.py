import streamlit as st
import random

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

st.title("Rock, Paper, Scissors Game")

options = ["Rock", "Paper", "Scissors"]
user_choice = st.selectbox("Choose your move:", options)

if st.button("Play"):
    computer_choice = random.choice(options)
    st.write(f"Computer chose: {computer_choice}")
    result = get_winner(user_choice, computer_choice)
    st.subheader(result)
