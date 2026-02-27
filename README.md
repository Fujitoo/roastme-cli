# 🔥 RoastMe CLI

> **The savage terminal game that turns your boredom into comedy gold!**

RoastMe CLI is a humorous command-line game that generates witty, sarcastic roasts based on your input. Perfect for bored students in lectures, developers needing a laugh, or anyone who enjoys light-hearted sarcasm.

---

## 📋 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Commands Reference](#-commands-reference)
- [Roast Styles](#-roast-styles)
- [Difficulty Levels](#-difficulty-levels)
- [Examples](#-examples)
- [Project Structure](#-project-structure)
- [Customization](#-customization)
- [FAQ](#-faq)
- [License](#-license)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎭 **5 Roast Styles** | Academic, Nerd, Overconfident, Existential, Lifestyle |
| 📊 **3 Difficulty Levels** | Easy (gentle), Medium (spicy), Savage (brutal) |
| 💬 **Comeback Mode** | Defend yourself and get rated 1-10 |
| 🎲 **75+ Templates** | Randomized roasts for endless entertainment |
| 🎨 **Beautiful UI** | Colorful terminal interface powered by Rich |
| ⚡ **Instant Launch** | No setup, runs immediately after install |

---

## 🚀 Quick Start

**Already have Python?** Run these 3 commands:

```bash
# 1. Clone or download this project
cd RoastMe

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start roasting!
python main.py
```

That's it! You're ready to get roasted! 🔥

The app launches with an interactive menu - no commands to remember!

---

## 📦 Installation

### Prerequisites

| Requirement | Version | How to Check |
|-------------|---------|--------------|
| Python | 3.8+ | `python --version` |
| pip | Any | `pip --version` |

### Step-by-Step Installation

```bash
# Navigate to the project folder
cd /path/to/tt

# Install required packages (typer + rich)
pip install -r requirements.txt

# Optional: Make executable on Linux/Mac
chmod +x main.py
```

### Troubleshooting

| Problem | Solution |
|---------|----------|
| `pip not found` | Try `pip3` instead of `pip` |
| `python not found` | Try `python3` instead of `python` |
| Permission denied | Add `--user` flag: `pip install --user -r requirements.txt` |

---

## 📖 Usage Guide

### 🎮 Main Menu Interface

Simply run the app and navigate through menus:

```bash
python main.py
```

**Main Menu Options:**
```
🔥 ROASTME CLI 🔥

Select an option:

  1. 🎮 Start Roast Session
  2. ⚡ Quick Roast
  3. 🎭 View Styles
  4. 📊 View Levels
  5. 🚪 Exit
```

### 🎯 Full Roast Session (Option 1)

A complete personalized roast experience:

1. **Select Difficulty** - Choose easy, medium, or savage
2. **Select Style** - Pick a roast style or mix all
3. **Enter Profile** - Name, hobby, major, confidence level
4. **Get Roasted** - Receive 5 personalized roasts
5. **Comeback Mode** - Defend yourself and get rated 1-10

### ⚡ Quick Roast (Option 2)

Roast someone instantly:

1. Enter the name to roast
2. Select difficulty level
3. Select roast style
4. Choose number of roasts (1-10)
5. Get instant roasts!

### 🎭 View Styles (Option 3)

See all available roast styles with descriptions and best-use cases.

### 📊 View Levels (Option 4)

See all difficulty levels with intensity ratings.

---

## 📚 Commands Reference

The app now uses a **menu-driven interface** - no commands to remember!

| Menu Option | Description | What It Does |
|-------------|-------------|--------------|
| **1. Start Roast Session** | Full interactive experience | Collects your profile, generates 5 personalized roasts, rates your comeback |
| **2. Quick Roast** | Fast roasting | Enter a name, select options, get instant roasts |
| **3. View Styles** | Browse roast styles | See all 5 roast styles with descriptions |
| **4. View Levels** | Browse difficulty levels | See all 3 difficulty levels with intensity ratings |
| **5. Exit** | Quit the app | Returns to terminal |

### Navigation Tips

- All selections use **numbered menus** (1-5, 1-3, 1-6, etc.)
- Press **Enter** to accept default selections
- After each session, press **Enter** to return to the main menu

---

## 🎭 Roast Styles

Each style targets a different aspect of your life. Choose wisely!

| Style | Icon | Description | Best For | Sample Roast |
|-------|------|-------------|----------|--------------|
| **Academic** | 📚 | Roasts about grades, study habits, and academic choices | Students, researchers | *"Your GPA must be on life support."* |
| **Nerd** | 🤓 | Tech-focused burns for the digitally obsessed | Developers, gamers | *"Your GitHub has more forks than your social life."* |
| **Overconfident** | 💪 | Roasts for big egos with small results | Show-offs, braggers | *"Your ego is writing checks your skills can't cash."* |
| **Existential** | 🌌 | Deep, philosophical roasts about life's meaning | Philosophers, overthinkers | *"In 100 years, no one will remember your hobby."* |
| **Lifestyle** | 🏠 | Burns about daily habits and living situations | Everyone with bad habits | *"Your fridge has more expiration dates than your calendar."* |

### View Styles In Terminal

```bash
python main.py styles
```

---

## 📊 Difficulty Levels

Choose your pain level!

| Level | Icon | Intensity | Description | When to Use |
|-------|------|-----------|-------------|-------------|
| **Easy** | 🧸 | ☆☆☆ | Playful teasing with gentle jabs. Safe for work and sensitive feelings. | First time, coworkers, sensitive friends |
| **Medium** | 🌶️ | ★★☆ | Sharp sarcasm with actual burns. Use with friends who can take a joke. | Friends, classmates, regular use |
| **Savage** | 🔥 | ★★★ | Brutal honesty with maximum damage. Not for the faint of heart. | Close friends, rivals, revenge mode |

### View Levels In Terminal

```bash
python main.py levels
```

---

## 💡 Examples

### Example 1: Full Roast Session

```bash
$ python main.py

🔥 ROASTME CLI 🔥

Select an option:

  1. 🎮 Start Roast Session
  2. ⚡ Quick Roast
  3. 🎭 View Styles
  4. 📊 View Levels
  5. 🚪 Exit

Enter your choice [1]: 1

📊 Select Difficulty Level:

  1. 🧸 Easy   - Playful teasing, gentle jabs
  2. 🌶️ Medium - Sharp sarcasm, actual burns
  3. 🔥 Savage - Brutal honesty, maximum damage

Choose level [2]: 2

🎭 Select Roast Style:

  1. 📚 Academic    - Roasts about grades & study habits
  2. 🤓 Nerd        - Tech-focused burns
  3. 💪 Overconfident - For big egos, small results
  4. 🌌 Existential - Deep, philosophical roasts
  5. 🏠 Lifestyle   - Daily habits & living situations
  6. 🎲 All Styles  - Mix of everything (default)

Choose style [6]: 

📝 Let's get to know you...

Enter your name: Alex
Enter your hobby: gaming
Enter your major: Computer Science
Rate your confidence [5]: 7

╭─ 🎯 Your Profile ─╮
Name: Alex
Hobby: gaming
Major: Computer Science
Confidence: 7/10
Difficulty: 🌶️ Medium
Style: All Styles
╰───────────────────╯

Ready to get emotionally damaged? Let's go!

🎤 ROAST MODE ACTIVATED

╭─ Roast #1 ─╮
Alex, your GitHub has more forks than your actual social life.
╰────────────╯

... (4 more roasts)

💬 COMEBACK MODE
Time to defend yourself! Type your comeback below.

Your comeback: At least I don't debug code for fun!

╭─ 📊 Comeback Analysis ─╮
Comeback Rating: 7/10
[███████░░░]

Not bad for someone majoring in Computer Science.
╰────────────────────────╯

Until next time, stay humble and touch grass.

Press Enter to continue
```

### Example 2: Quick Roast a Friend

```bash
$ python main.py

🔥 ROASTME CLI 🔥

Select an option:

  1. 🎮 Start Roast Session
  2. ⚡ Quick Roast
  3. 🎭 View Styles
  4. 📊 View Levels
  5. 🚪 Exit

Enter your choice [1]: 2

Enter name to roast: Dave

📊 Select Difficulty Level:
Choose level [2]: 3  # Savage!

🎭 Select Roast Style:
Choose style [6]: 

Number of roasts [3]: 5

🎤 Roasting Dave at savage difficulty (All Styles)...

╭─ Roast #1 ─╮
Dave, your degree is basically a receipt for wasted tuition.
╰────────────╯

╭─ Roast #2 ─╮
Dave, you're the human equivalent of a 404 error.
╰────────────╯

... (3 more roasts)

Press Enter to continue
```

### Example 3: View Available Styles

```bash
$ python main.py

# Select option 3 to see all roast styles in a formatted table
```

---

## 📁 Project Structure

```
RoastMe/
├── main.py             # Menu-driven CLI entry point
├── roast_engine.py     # Roast generation logic and randomization
├── roast_data.py       # 75+ roast templates organized by style/level
├── requirements.txt    # Python dependencies (rich)
└── README.md          # This documentation file
```

### File Descriptions

| File | Purpose | Lines of Code |
|------|---------|---------------|
| `main.py` | Menu system, user interface, input handling | ~260 |
| `roast_engine.py` | Roast generation, comeback rating, randomization | ~135 |
| `roast_data.py` | Template database, judgments, greetings | ~120 |
| `requirements.txt` | Package dependencies | 1 |

---

## 🛠️ Customization

### Adding New Roasts

Edit `roast_data.py` and add templates to the `ROAST_TEMPLATES` dictionary:

```python
ROAST_TEMPLATES = {
    "your_new_style": {
        "easy": [
            "Your gentle roast template with {name} here",
        ],
        "medium": [
            "Your spicy roast template with {name} here",
        ],
        "savage": [
            "Your brutal roast template with {name} here",
        ],
    },
}
```

### Available Placeholders

| Placeholder | Replaced With |
|-------------|---------------|
| `{name}` | User's name |
| `{hobby}` | User's hobby |
| `{major}` | User's major |
| `{confidence}` | User's confidence rating (1-10) |

### Adding New Comeback Judgments

Edit the `COMEBACK_JUDGMENTS` dictionary in `roast_data.py`:

```python
COMEBACK_JUDGMENTS = {
    (1, 3): [
        "Your new low-rating judgment here",
    ],
    # ... more ranges
}
```

---

## ❓ FAQ

### Q: How do I use the app?
**A:** Just run `python main.py` and follow the menu prompts! No commands to remember.

### Q: Can I still use command-line arguments?
**A:** No, the app now uses a fully interactive menu system for easier navigation.

### Q: Is this appropriate for work?
**A:** The "easy" difficulty is generally workplace-safe. Avoid "savage" mode around HR.

### Q: Can I roast someone without them knowing?
**A:** Use the "Quick Roast" option (Option 2) for fast anonymous roasting!

### Q: How many unique roasts are there?
**A:** 75+ templates across 5 styles and 3 difficulty levels.

### Q: Can I add my own roasts?
**A:** Yes! See the [Customization](#-customization) section above.

### Q: The roasts hit too close to home...
**A:** That means they're working! But seriously, use "easy" mode if you're sensitive.

### Q: Can I use this in my own project?
**A:** Absolutely! It's MIT licensed. Go wild!

---

## 📄 License

**MIT License** - Do whatever you want with it!

```
Copyright (c) 2024 RoastMe CLI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

---

## ⚠️ Disclaimer

This is a **fun project** meant for entertainment only. 

- 🎯 All roasts are generated randomly
- 😄 Don't take them personally
- 🚫 Not intended to be genuinely mean-spirited
- 💙 If you're easily offended, maybe try a meditation app instead

**Remember:** It's all in good fun! Roast responsibly! 🔥

---

## 🙏 Credits

Built with:
- [Rich](https://rich.readthedocs.io/) - Terminal formatting library

Made with ❤️ for bored students everywhere.

---

**Enjoy getting roasted!** 🔥
