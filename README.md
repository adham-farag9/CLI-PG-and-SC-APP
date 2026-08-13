# 🔐 Day 03 - PG&SC: Cryptographically Secure Password Generator & Strength Checker

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Security Level](https://img.shields.io/badge/security-CSPRNG-success.svg)]()
[![Status](https://img.shields.io/badge/status-completed-brightgreen.svg)]()

A command-line tool designed to generate cryptographically secure passwords and perform quantitative strength analysis using **Shannon Entropy** metrics, heuristic character-class classification, and pattern penalties.

Developed as **Day 03** of my **30 Days of Python Challenge**, with an emphasis on cybersecurity fundamentals, CSPRNGs (Cryptographically Secure Pseudo-Random Number Generators), and defensive programming.

---

## 📌 Features

- 🛡️ **Cryptographically Secure Generation:** Uses Python’s standard `secrets` module (System Random) instead of `random` to guarantee high-entropy randomness resistant to prediction.
- 📐 **Shannon Entropy Estimation:** Measures the raw information density of passwords in bits ($E = L \times \log_2(R)$).
- 🧠 **Smart Heuristic Scoring System:** Scores passwords from `0 to 100` based on:
  - Base Entropy score.
  - Length bonuses ($\ge 8$ and $\ge 12$ characters).
  - Character diversity coverage (Uppercase, Lowercase, Digits, Symbols).
  - Common passwords blocklist filtering.
- 🚫 **Pattern Penalty Engine:** Detects and penalizes vulnerability patterns using Regular Expressions (e.g., repeated characters like `aaa` or sequential numbers like `123`, `567`).
- 💻 **Interactive CLI Menu:** Clean command-line user menu with instant feedback and improvement recommendations.

---

## 🏗️ Technical Architecture & Evaluation Pipeline

```text
[ Input Password / Generator ]
             │
             ├──> Common Password Filter ──(Match)──> Score: 0 (Immediate Fail)
             │
             ├──> Calculate Shannon Entropy ──> Base Score (Max 70)
             │
             ├──> Check Diversity & Length ───> Add Bonus (+5 to +25)
             │
             └──> Regex Pattern Matcher ──────> Apply Penalties (-8 to -10)
                                                        │
                                                        ▼
                                             [ Final Score & Feedback ]
🧮 Mathematical ModelShannon Entropy Formula:$$E = L \cdot \log_2(R)$$Where:$L$: Password Length.$R$: Character Pool Size ($26 \text{ lowercase} + 26 \text{ uppercase} + 10 \text{ digits} + 32 \text{ symbols} = 94 \text{ max}$).💻 How to RunPrerequisitesPython 3.8+ installed on your system.Running the ApplicationClone the repository:Bashgit clone [https://github.com/adham-farag/30-Days-Of-Python.git](https://github.com/adham-farag/30-Days-Of-Python.git)
cd "30-Days-Of-Python/Week-1/PG&SC"
Run the tool:Bashpython3 PG&SC.py
📖 Sample OutputPlaintext==== PG&SC Tool ====
1. Generate Password
2. Check Password Strength
3. Exit
Choose Option: 1

Generated Password:  k#8P!vQ92m@X

Assessment: 
- Strong Password!
- Entropy: 78.7 bits. Score: 95/100.
💡 Key Technical LearningsCSPRNG vs Pseudo-Random: Understanding why secrets must be used for security sensitive applications instead of standard PRNGs (random).Information Theory: Applying Shannon Entropy in Python to mathematically quantify password guessability.Regex Pattern Matching: Using re for lookahead/repeated sequence detection ((.)\1\1) and sequence matching (123|234|...).Defensive Engineering: Guaranteeing at least one character from every enabled character set before shuffling.👨‍💻 Author: Adham Farag🚀 Part of: 30 Days of Python Projects Challenge
