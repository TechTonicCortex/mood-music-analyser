import random

# ── COLOURS ───────────────────────────────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
PINK   = "\033[95m"
RED    = "\033[91m"
BLUE   = "\033[94m"
DIM    = "\033[2m"

# ── MOOD DATABASE ─────────────────────────────────────────────────
# Each mood has: keywords, vibe name, emoji, energy, colour, genres, songs
MOODS = {
    "happy": {
        "keywords": ["happy", "great", "amazing", "fantastic", "good", "joyful",
                     "excited", "awesome", "wonderful", "brilliant", "ecstatic",
                     "cheerful", "glad", "pleased", "elated", "pumped", "stoked"],
        "vibe": "Pure Sunshine",
        "emoji": "☀️",
        "energy": "HIGH",
        "energy_bar": "█████████░",
        "colour": YELLOW,
        "genres": ["Pop", "Dance", "Funk", "Feel-Good Hip Hop"],
        "songs": [
            "Pharrell Williams — Happy",
            "Justin Timberlake — Can't Stop the Feeling",
            "Dua Lipa — Levitating",
            "Bruno Mars — Uptown Funk",
            "Lizzo — About Damn Time",
            "Katy Perry — Roar",
            "Carly Rae Jepsen — Call Me Maybe",
            "Meghan Trainor — All About That Bass",
            "Ariana Grande — 7 Rings",
            "Taylor Swift — Shake It Off",
        ]
    },
    "sad": {
        "keywords": ["sad", "unhappy", "down", "depressed", "miserable", "crying",
                     "heartbroken", "upset", "lonely", "empty", "hopeless", "low",
                     "blue", "gloomy", "tearful", "hurt", "broken", "lost"],
        "vibe": "Rainy Window",
        "emoji": "🌧️",
        "energy": "LOW",
        "energy_bar": "██░░░░░░░░",
        "colour": BLUE,
        "genres": ["Indie Folk", "Sad Pop", "Acoustic", "Ambient"],
        "songs": [
            "Billie Eilish — when the party's over",
            "Lewis Capaldi — Someone You Loved",
            "Adele — Someone Like You",
            "Phoebe Bridgers — Motion Sickness",
            "Sufjan Stevens — Death With Dignity",
            "Radiohead — The Bends",
            "Bon Iver — Skinny Love",
            "Taylor Swift — All Too Well",
            "The Fray — How to Save a Life",
            "James Blunt — You're Beautiful",
        ]
    },
    "angry": {
        "keywords": ["angry", "mad", "furious", "rage", "annoyed", "frustrated",
                     "irritated", "hate", "pissed", "livid", "fuming", "fed up",
                     "stressed", "aggressive", "intense", "fired up", "heated"],
        "vibe": "Red Zone",
        "emoji": "🔥",
        "energy": "MAXIMUM",
        "energy_bar": "██████████",
        "colour": RED,
        "genres": ["Metal", "Punk", "Rage Rap", "Hard Rock"],
        "songs": [
            "Linkin Park — In The End",
            "System of a Down — Chop Suey",
            "Eminem — Till I Collapse",
            "Rage Against the Machine — Killing in the Name",
            "Kendrick Lamar — m.A.A.d city",
            "NF — The Search",
            "Bring Me the Horizon — Throne",
            "Twenty One Pilots — Jumpsuit",
            "Slipknot — Before I Forget",
            "Machine Gun Kelly — Papercuts",
        ]
    },
    "chill": {
        "keywords": ["chill", "relaxed", "calm", "peaceful", "easy", "mellow",
                     "laid back", "chilling", "chillin", "vibing", "zen", "cosy",
                     "comfortable", "lazy", "breezy", "soft", "quiet", "serene"],
        "vibe": "Sunday Afternoon",
        "emoji": "🌿",
        "energy": "LOW-MED",
        "energy_bar": "████░░░░░░",
        "colour": GREEN,
        "genres": ["Lo-fi", "Chillhop", "Indie Pop", "Soft R&B"],
        "songs": [
            "Frank Ocean — Nights",
            "Tyler the Creator — See You Again",
            "Mac Miller — Ladders",
            "Daniel Caesar — Get You",
            "SZA — Good Days",
            "Rex Orange County — Loving is Easy",
            "Still Woozy — Goodie Bag",
            "Clairo — Sofia",
            "Conan Gray — Heather",
            "Surfaces — Sunday Best",
        ]
    },
    "motivated": {
        "keywords": ["motivated", "focused", "productive", "grind", "hustle",
                     "determined", "driven", "ready", "energetic", "powerful",
                     "confident", "strong", "unstoppable", "goals", "working",
                     "studying", "concentrating", "ambitious"],
        "vibe": "In The Zone",
        "emoji": "⚡",
        "energy": "HIGH",
        "energy_bar": "█████████░",
        "colour": CYAN,
        "genres": ["Workout Hip Hop", "Electronic", "Cinematic", "Drum & Bass"],
        "songs": [
            "Kanye West — Power",
            "Jay-Z — Empire State of Mind",
            "Rocky — Everyday",
            "Hans Zimmer — Time (Inception)",
            "The Weeknd — Blinding Lights",
            "Drake — Started From the Bottom",
            "Kendrick Lamar — DNA",
            "Post Malone — Rockstar",
            "Travis Scott — Antidote",
            "21 Savage — Bank Account",
        ]
    },
    "romantic": {
        "keywords": ["romantic", "love", "crush", "relationship", "dating",
                     "girlfriend", "boyfriend", "in love", "affectionate", "tender",
                     "sweet", "passionate", "intimate", "adore", "devoted", "smitten"],
        "vibe": "Golden Hour",
        "emoji": "✨",
        "energy": "MED",
        "energy_bar": "██████░░░░",
        "colour": PINK,
        "genres": ["R&B", "Soul", "Romantic Pop", "Neo-Soul"],
        "songs": [
            "Ed Sheeran — Perfect",
            "John Legend — All of Me",
            "Beyoncé — Crazy in Love",
            "The Weeknd — Call Out My Name",
            "Frank Ocean — Thinkin Bout You",
            "Daniel Caesar — Best Part",
            "H.E.R. — Focus",
            "Bruno Mars — Just the Way You Are",
            "Harry Styles — Watermelon Sugar",
            "Shawn Mendes — Stitches",
        ]
    },
    "anxious": {
        "keywords": ["anxious", "nervous", "worried", "scared", "afraid", "fear",
                     "panic", "overwhelmed", "overthinking", "tense", "uneasy",
                     "restless", "uncertain", "stressed", "jittery", "on edge"],
        "vibe": "Deep Breath",
        "emoji": "🌊",
        "energy": "MED",
        "energy_bar": "█████░░░░░",
        "colour": CYAN,
        "genres": ["Ambient", "Classical", "Calming Indie", "Meditation"],
        "songs": [
            "Brian Eno — Music for Airports",
            "Weightless — Marconi Union",
            "Coldplay — Fix You",
            "Sigur Rós — Hoppípolla",
            "Imogen Heap — Hide and Seek",
            "Nils Frahm — Says",
            "Max Richter — On the Nature of Daylight",
            "Hammock — Breathturn",
            "Olafur Arnalds — Near Light",
            "Jon Hopkins — Immunity",
        ]
    },
    "nostalgic": {
        "keywords": ["nostalgic", "memories", "miss", "remember", "throwback",
                     "childhood", "old times", "past", "vintage", "classic",
                     "reminisce", "retro", "long ago", "back then", "used to"],
        "vibe": "Polaroid Memories",
        "emoji": "📷",
        "energy": "MED",
        "energy_bar": "█████░░░░░",
        "colour": YELLOW,
        "genres": ["Classic Rock", "80s Pop", "90s R&B", "Oldies"],
        "songs": [
            "Toto — Africa",
            "Michael Jackson — Billie Jean",
            "Whitney Houston — I Will Always Love You",
            "Fleetwood Mac — Dreams",
            "The Beatles — Let It Be",
            "Queen — Bohemian Rhapsody",
            "Nirvana — Smells Like Teen Spirit",
            "TLC — No Scrubs",
            "Backstreet Boys — I Want It That Way",
            "Destiny's Child — Say My Name",
        ]
    }
}

# ── MATCHING ENGINE ───────────────────────────────────────────────
def analyse_mood(user_input):
    text = user_input.lower()
    scores = {}

    for mood_name, mood_data in MOODS.items():
        score = 0
        for keyword in mood_data["keywords"]:
            if keyword in text:
                score += 1
        if score > 0:
            scores[mood_name] = score

    if not scores:
        return None

    # Return the highest scoring mood
    best_mood = max(scores, key=scores.get)
    return MOODS[best_mood]

# ── DISPLAY FUNCTIONS ─────────────────────────────────────────────
def print_header():
    print("\n" + "═" * 50)
    print(f"{BOLD}{PINK}    🎵  MOOD MUSIC ANALYSER  🎵{RESET}")
    print("═" * 50)
    print(f"{DIM}  Describe how you're feeling and we'll{RESET}")
    print(f"{DIM}  find the perfect playlist vibe for you.{RESET}")
    print("═" * 50 + "\n")

def print_result(mood):
    c = mood["colour"]
    print("\n" + "─" * 50)
    print(f"{BOLD}{c}  {mood['emoji']}  VIBE: {mood['vibe']}{RESET}")
    print("─" * 50)

    # Energy bar
    print(f"\n  {BOLD}ENERGY LEVEL{RESET}")
    print(f"  {c}{mood['energy_bar']}{RESET}  {BOLD}{mood['energy']}{RESET}")

    # Genres
    print(f"\n  {BOLD}RECOMMENDED GENRES{RESET}")
    for genre in mood["genres"]:
        print(f"  {c}▸{RESET} {genre}")

    # Song recommendations (pick 5 random ones)
    picks = random.sample(mood["songs"], 5)
    print(f"\n  {BOLD}YOUR PLAYLIST{RESET}")
    for i, song in enumerate(picks, 1):
        print(f"  {c}{i}.{RESET} {song}")

    print("\n" + "─" * 50)

def print_unknown():
    print(f"\n  {YELLOW}🤔 Hmm, couldn't quite read that vibe.{RESET}")
    print(f"  {DIM}Try describing your mood differently —{RESET}")
    print(f"  {DIM}e.g. 'I feel really chill today' or 'I'm so angry'{RESET}\n")

# ── MAIN LOOP ─────────────────────────────────────────────────────
def main():
    print_header()

    while True:
        print(f"{CYAN}How are you feeling right now?{RESET}")
        print(f"{DIM}(or type 'quit' to exit){RESET}")
        user_input = input(f"\n{BOLD}→ {RESET}").strip()

        if user_input.lower() in ["quit", "exit", "q"]:
            print(f"\n{GREEN}Stay in good vibes. See you! 🎵{RESET}\n")
            break

        if not user_input:
            continue

        mood = analyse_mood(user_input)

        if mood:
            print_result(mood)
        else:
            print_unknown()

        print(f"\n{DIM}Press Enter to analyse another mood...{RESET}")
        input()
        print("\n" + "═" * 50 + "\n")

if __name__ == "__main__":
    main()
