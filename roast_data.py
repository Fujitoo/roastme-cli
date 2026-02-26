"""
Roast templates database for RoastMe CLI.
Organized by style and difficulty level.
"""

ROAST_TEMPLATES = {
    "academic": {
        "easy": [
            "Wow, {name}. Your GPA must be on life support.",
            "I've seen syllabi more organized than your life, {name}.",
            "{name}, your major called. It wants its disappointment back.",
            "Is {major} even a real degree? Asking for a confused employer.",
            "Your report card looks like a heart rate monitor during a nap.",
        ],
        "medium": [
            "{name}, you're the reason the professor drinks before 9 AM.",
            "Your transcript is the academic equivalent of a participation trophy.",
            "I've seen community college dropouts with more direction than {name}.",
            "{major}? More like {major}... into unemployment.",
            "Your study habits make a goldfish look like a Nobel laureate.",
        ],
        "savage": [
            "{name}, your degree is basically a receipt for wasted tuition.",
            "The only thing you're majoring in is disappointment.",
            "Your academic performance is a cry for help in GPA form.",
            "{name}, even the library's Dewey Decimal System has given up on you.",
            "Your thesis advisor is actively looking for a new advisee.",
        ],
    },
    "nerd": {
        "easy": [
            "{name}, your GitHub has more forks than your actual social life.",
            "I bet your hobby is 'debugging' and your major is 'loneliness'.",
            "Your confidence is {confidence}/10 but your social skills are 2/10.",
            "{name}, you probably have a favorite programming language. Pathetic.",
            "Your browser history is 90% Stack Overflow and 10% regret.",
        ],
        "medium": [
            "{name}, your code has more bugs than lines. Just like your social life.",
            "You spend more time with your keyboard than humans. And it shows.",
            "{hobby}? Cute. Does it come with a mechanical keyboard upgrade?",
            "Your IDE has seen more of you than your own family.",
            "{name}, you're the human equivalent of a 404 error.",
        ],
        "savage": [
            "{name}, your code is so bad, even the compiler judges you.",
            "You've memorized ASCII tables but can't remember how to make friends.",
            "Your GitHub contributions look like a desert. Empty and sad.",
            "{name}, you debug code but can't debug your life choices.",
            "Your hobby is {hobby}? More like your hobby is avoiding sunlight.",
        ],
    },
    "overconfident": {
        "easy": [
            "Confidence level {confidence}? Bold for someone named {name}.",
            "{name}, your ego is writing checks your skills can't cash.",
            "That {confidence}/10 confidence is adorable. Like a toddler with a sword.",
            "You walk like you own the place. The place is a community college, {name}.",
            "{name}, your self-esteem is impressive. Your resume? Not so much.",
        ],
        "medium": [
            "With {confidence}/10 confidence, you could fail spectacularly in style.",
            "{name}, you're not confident. You're just unaware of your limitations.",
            "Your confidence is {confidence}/10 but your results say otherwise.",
            "You strut like a peacock. A bald, directionless peacock named {name}.",
            "{name}, your LinkedIn says 'visionary'. Your bank account says 'delusional'.",
        ],
        "savage": [
            "{name}, your confidence is a glitch in the simulation.",
            "You're {confidence}/10 confident? The Dunning-Kruger effect is real.",
            "{name}, you're not a main character. You're not even an NPC.",
            "Your ego could fill an arena. Your achievements? A thimble.",
            "{name}, you're the human equivalent of an participation trophy with delusions.",
        ],
    },
    "existential": {
        "easy": [
            "{name}, in the grand scheme of the universe, your {hobby} doesn't matter.",
            "We're all stardust. You're stardust that chose {major}. Interesting choice.",
            "{name}, entropy will eventually fix your life choices.",
            "The universe is expanding. Your opportunities are not, {name}.",
            "In 100 years, no one will remember your {hobby}. Or you.",
        ],
        "medium": [
            "{name}, you're a speck of dust worrying about {major}. How quaint.",
            "The void stares back. It's as confused about your life choices as you are.",
            "Your existence is a statistical anomaly. Your success? Pure luck.",
            "{name}, Sisyphus had more purpose. At least he had a rock.",
            "The universe is indifferent to your {hobby}. Just like everyone else.",
        ],
        "savage": [
            "{name}, you're a cosmic accident with delusions of purpose.",
            "Your life is a footnote in the universe's indifferent diary.",
            "{name}, even the heat death of the universe won't care about your {major}.",
            "You're not lost in the void. You ARE the void.",
            "{name}, your existence proves the universe has a dark sense of humor.",
        ],
    },
    "lifestyle": {
        "easy": [
            "{name}, your {hobby} is cute. Does it pay rent?",
            "Your room probably smells like instant noodles and regret.",
            "{name}, your sleep schedule is a crime against humanity.",
            "I bet your fridge has more expiration dates than your calendar.",
            "Your 'self-care' is scrolling TikTok until 4 AM, {name}.",
        ],
        "medium": [
            "{name}, your lifestyle is a Pinterest board gone wrong.",
            "Your plant collection is dying. Just like your motivation.",
            "{hobby}? That's your personality now? Bold strategy.",
            "{name}, your coffee addiction is funding an entire industry.",
            "Your workout routine is 'walking to the fridge'. I can tell.",
        ],
        "savage": [
            "{name}, your life is a browser tab you forgot to close.",
            "Your apartment is a fire hazard. Your life choices? Also a fire hazard.",
            "{name}, your sleep schedule is in a different time zone. Permanently.",
            "Your diet is 90% caffeine and 10% questionable decisions.",
            "{name}, your 'minimalist aesthetic' is just being broke with good taste.",
        ],
    },
}

# Comeback judgments based on rating
COMEBACK_JUDGMENTS = {
    (1, 3): [
        "Oof. That comeback needed a participation trophy.",
        "Did your brain buffer on that one?",
        "That comeback has the energy of a dial-up modem.",
        "I've seen stronger insults in children's cartoons.",
        "Your comeback just filed a missing person report for its dignity.",
    ],
    (4, 5): [
        "Mediocre. Like your {hobby}.",
        "Not terrible, but I've heard better from chatbots.",
        "That's... something. I guess.",
        "Your comeback is trying its best. Bless.",
        "Solid C- effort. Your professor would be proud.",
    ],
    (6, 7): [
        "Okay, that actually landed. Don't get cocky.",
        "Not bad for someone majoring in {major}.",
        "Your brain works! Science was wrong about you.",
        "That comeback has potential. Unlike your career.",
        "Impressive. Your confidence might be justified. Might.",
    ],
    (8, 9): [
        "DANG. You've been holding out on us, {name}!",
        "That comeback just earned its own zip code.",
        "Okay comedian, when's your Netflix special?",
        "Your wit is sharper than your career prospects.",
        "That's the energy! Too bad it's wasted here.",
    ],
    (10, 10): [
        "PERFECTION. The roast master has been roasted!",
        "That comeback deserves its own standing ovation.",
        "You win this round, {name}. Enjoy it.",
        "Legendary. They'll tell stories of this comeback.",
        "10/10 comeback. Still not fixing your GPA though.",
    ],
}

# Greeting messages
GREETINGS = [
    "Welcome to RoastMe CLI, where your feelings are optional!",
    "Ready to get emotionally damaged? Let's go!",
    "Warning: Roasts may cause temporary sadness. Proceed anyway!",
    "Your therapist warned you about this moment.",
    "Brace yourself, {name}. Roasts incoming!",
]

# Farewell messages
FAREWELLS = [
    "Come back when you need another ego check!",
    "Remember: these roasts are free. Therapy isn't.",
    "Your confidence survived! Barely.",
    "Until next time, stay humble and touch grass.",
    "Go forth and spread the roasted wisdom!",
]
