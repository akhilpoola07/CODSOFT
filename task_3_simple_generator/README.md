# Password Generator

## Project Description
A professional **Python Password Generator** built for the **CodSoft Internship Task 3**. The application generates strong, random passwords based on user‑defined length and complexity, offers advanced features such as a strength meter, clipboard copy, history, and the option to exclude visually similar characters. It provides a sleek **dark‑themed GUI** using Tkinter, making it beginner‑friendly yet polished enough for a GitHub portfolio.

## Features
- **Adjustable password length**
- **Complexity levels**: Easy (letters), Medium (letters + numbers), Strong (letters + numbers + symbols)
- **Exclude similar characters** (`O, 0, l, 1, I`)
- **Real‑time entropy/strength meter**
- **Copy to clipboard** button
- **Save passwords** to a local `passwords.txt` file
- **Session history** panel showing previously generated passwords
- **Robust input validation** with clear error messages
- **Dark‑theme Tkinter UI** with modern styling

## Technologies Used
- **Python 3.10+**
- Standard library modules: `random`, `string`, `math`, `tkinter`, `tkinter.ttk`
- No external dependencies (Tkinter ships with Python)

## How to Run the Project
1. **Clone the repository** (or copy the folder) to your local machine.
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```
3. Install requirements (none required for core functionality):
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```
   The GUI window will appear, allowing you to generate passwords instantly.

## Example Output
```
Password Length: 16
Complexity: Strong
Generated Password: a9&K$3pL!bQz*2Xm
Entropy: 95.8 bits
```
The GUI displays the password, a strength bar, and the entropy value.

## Internship Task Details
- **Task**: Build a professional password generator as part of CodSoft Internship Task 3.
- **Deliverables**: Source code, README, screenshots, and a ready‑to‑upload GitHub repository.
- **Evaluation Criteria**: Code quality, UI/UX, documentation, and additional advanced features.

## Screenshots
Add screenshots of the application in the `screenshots/` directory and reference them here.

---
*This project is ready to be pushed to GitHub and showcased on LinkedIn.*
