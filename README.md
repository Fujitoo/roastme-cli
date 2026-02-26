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
cd tt

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start roasting!
python main.py start
```

That's it! You're ready to get roasted! 🔥

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

### 🎮 Interactive Mode (Recommended for First-Time Users)

Start a full roast session with personalized questions:

```bash
python main.py start
```

**What happens:**
1. You'll be asked for your name, hobby, major, and confidence level
2. The game generates 5 personalized roasts
3. You can type a comeback and get rated

### 🎯 Customizing Your Experience

#### Choose Difficulty Level

```bash
# Gentle teasing (safe for work)
python main.py start --level easy

# Sharp sarcasm (default)
python main.py start --level medium

# Brutal honesty (not for the sensitive)
python main.py start --level savage
```

#### Choose Roast Style

```bash
# Academic-focused roasts
python main.py start --style academic

# Tech/nerd roasts
python main.py start --style nerd

# Mix all styles (default)
python main.py start --style all
```

#### Combine Options

```bash
# Savage academic roasts
python main.py start --level savage --style academic

# Easy lifestyle roasts
python main.py start --level easy --style lifestyle
```

### ⚡ Quick Roast Mode

Roast someone instantly without answering questions:

```bash
# Basic quick roast
python main.py roast "John"

# With custom difficulty and count
python main.py roast "Sarah" --level savage --count 5

# Specific style
python main.py roast "Mike" --style nerd --level medium
```

---

## 📚 Commands Reference

### Main Commands

| Command | Description | Example |
|---------|-------------|---------|
| `start` | Interactive roast session | `python main.py start` |
| `roast` | Quick roast a name | `python main.py roast "Alex"` |
| `styles` | Show all roast styles | `python main.py styles` |
| `levels` | Show difficulty levels | `python main.py levels` |
| `--help` | Show help message | `python main.py --help` |

### Options for `start`

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--level` | `-l` | Difficulty: easy, medium, savage | medium |
| `--style` | `-s` | Style: academic, nerd, overconfident, existential, lifestyle, all | all |

### Options for `roast`

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--level` | `-l` | Difficulty: easy, medium, savage | medium |
| `--style` | `-s` | Roast style (or "all") | all |
| `--count` | `-c` | Number of roasts (1-10) | 3 |

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

### Example 1: First-Time User

```bash
$ python main.py start

🔥 ROASTME CLI 🔥

📝 Let's get to know you...

Enter your name: Alex
Enter your hobby: gaming
Enter your major: Computer Science
Rate your confidence: 7

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
```

### Example 2: Quick Roast a Friend

```bash
$ python main.py roast "Dave" --level savage --count 5

🔥 ROASTME CLI 🔥

🎤 Roasting Dave at savage difficulty (All Styles)...

[1] Dave, your degree is basically a receipt for wasted tuition.
[2] Dave, you're the human equivalent of a 404 error.
[3] Dave, your confidence is a glitch in the simulation.
[4] Dave, you're a cosmic accident with delusions of purpose.
[5] Dave, your life is a browser tab you forgot to close.
```

### Example 3: Style-Specific Roasting

```bash
$ python main.py start --style academic --level easy

# Only academic-themed gentle roasts
```

---

## 📁 Project Structure

```
tt/
├── main.py             # CLI entry point with all commands
├── roast_engine.py     # Roast generation logic and randomization
├── roast_data.py       # 75+ roast templates organized by style/level
├── requirements.txt    # Python dependencies (typer, rich)
└── README.md          # This documentation file
```

### File Descriptions

| File | Purpose | Lines of Code |
|------|---------|---------------|
| `main.py` | CLI commands, user interface, input handling | ~240 |
| `roast_engine.py` | Roast generation, comeback rating, randomization | ~135 |
| `roast_data.py` | Template database, judgments, greetings | ~120 |
| `requirements.txt` | Package dependencies | 2 |

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

### Q: Is this appropriate for work?
**A:** The "easy" difficulty is generally workplace-safe. Avoid "savage" mode around HR.

### Q: Can I roast someone without them knowing?
**A:** Use `python main.py roast "Name"` for quick anonymous roasting!

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
- [Typer](https://typer.tiangolo.com/) - CLI framework
- [Rich](https://rich.readthedocs.io/) - Terminal formatting

Made with ❤️ for bored students everywhere.

---

**Enjoy getting roasted!** 🔥
