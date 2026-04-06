# 🃏 Blackjack Game (Python)

A simple command-line Blackjack game built using Python.  
This project simulates a basic version of the classic casino game where the player competes against the computer.

---

## 🚀 Features

- Random card distribution  
- User vs Computer gameplay  
- Ace handling (11 → 1 automatically)  
- Score calculation and comparison  
- Simple text-based interface  
- ASCII logo display  

---

## 📂 Project Structure

Blackjack/  
│  
├── main.py      # Main game logic  
├── art.py       # ASCII logo design  

---

## 🧠 How the Game Works

- Player and computer are each dealt 2 cards  
- Player can choose:  
  - y → draw another card  
  - n → pass  
- If total exceeds 21 → Bust (lose)  
- Computer draws cards until it reaches at least 17  
- Final scores are compared to determine the winner  

---

## 🃏 Card Values

- Number cards → face value  
- Face cards (J, Q, K) → 10  
- Ace → 11 or 1 (auto-adjusts to prevent bust)  

---

## ▶️ How to Run

1. Clone the repository:
   git clone https://github.com/your-username/python-projects.git  

2. Navigate to the project folder:
   cd Blackjack  

3. Run the game:
   python main.py  

---

## 🎮 Example Gameplay

Do you want to play blackjack? type y/n: y  
Your cards: [10, 7], total: 17  
Computer first card: 9  

Do you want another card? y/n: n  

Final Results:  
Your total: 17  
Computer total: 19  
Computer wins.  

---

## 💡 Concepts Used

- Python lists and loops  
- Conditional statements  
- Functions and modular design  
- Random module  
- Input/output handling  

---

## 📌 Future Improvements

- Add betting system  
- Add multiple rounds  
- Improve UI (GUI version)  
- Add split/double options
