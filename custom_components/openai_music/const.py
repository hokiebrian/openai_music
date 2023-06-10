"""Constants for the OpenAI Music Companion"""

DOMAIN = "openai_music"
DEFAULT_PROMPT = "Give me general info about the song ignore references to remastering"
DEFAULT_PERSONALITY = "Answer like a music expert"
DEFAULT_SONG_TITLE = "Enter Sandman"
DEFAULT_SONG_ARTIST = "Metallica"
DEFAULT_CHAT_MODEL = "gpt-3.5-turbo"
DEFAULT_USER_TAG = "HomeAssistant"
DEFAULT_MAX_TOKENS = 500
DEFAULT_MAX_IMG_TOKENS = 250
DEFAULT_TEMPERATURE = 0.5
DEFAULT_IMG_TEMPERATURE = 0.2
DEFAULT_TOP_P = 1.0
DEFAULT_IMG_TOP_P = 1.0
DEFAULT_IMG_COUNT = 1
DEFAULT_IMAGE_TYPE = "Normal"
DEFAULT_IMAGE_RESOLUTION = "256x256"
ERROR_IMG = "https://brands.home-assistant.io/openai_music/icon@2x.png"
MAX_RETRIES = 2
PERSONALITIES = {
    "Normal": "Answer like a Music Expert",
    "Hipster": "Answer like a hipster who is really into the scene",
    "Stoner": "Answer like a stoner who loves music",
    "Musician": "Answer like a musician with technical details",
    "Grumpy Old Man": "Answer like a grumpy old man",
    "Intellectual": "Answer like an intellectual who knows everything",
    "Pirate": "Answer like a pirate that is very excited to talk about music",
    "Scientist": "Answer like a scientist that uses a lot of scientific terms",
    "Clueless": "Answer like someone who is clueless with comically wrong information",
    "Old English": "Answer like an Old English speaker",
    "Superhero": "Answer like a superhero who gains power from music",
    "Valley Girl": "Answer like a valley girl that really has no clue about music",
    "Karen": "Answer like a Karen that complains about everything",
    "Paranoid": "Answer like a paranoid conspiracy theorist",
    "Canadian": "Answer like a sterotypical proud Canadian",
    "Hyperbole": "Answer like someone who only speaks in hyperbole",
    "Country Bumpkin": "Answer like a country bumpkin",
    "Hippie": "Answer like a confused hippie",
    "Redneck": "Answer like an very angry redneck",
}
PROMPTS = {
    "General Song Info": "Give me general info about the song ignore references to remastering",
    "Artist Info": "Tell me about the artist only, nothing about the song",
    "Lyric Meanings": "How are the lyrics generally interpreted for",
    "Song Trivia": "Tell me some trivia about the song ignore references to remastering",
    "Songwriters": "Who wrote the song",
    "Recording info": "When and where was this song recorded:",
    "Similar Songs": "What are 20 songs similar to",
}
IMAGE_TYPES = {
    "Abstract Expressionist": "abstract expressionist",
    "Absurd": "ridiculous absurdist photo",
    "Absurd Cartoon": "ridiculous absurdist cartoon",
    "Album Cover": "album cover",
    "Andy Warhol": "Andy Warhol",
    "Anime": "modern anime",
    "Antebellum": "Antebellum",
    "Avant-garde": "Avant-garde",
    "Baroque": "baroque",
    "Black and White": "black and white photograph",
    "Cartoon": "cartoon",
    "Collage": "collage",
    "Comic Book": "comic book cover",
    "Constructivism": "constructivism",
    "Cyberpunk": "cyberpunk",
    "Depressive": "contemporary depressive realism",
    "Digital Art": "digital art",
    "Dragon Art": "dragon art",
    "Fantasy": "fantasy art",
    "Futurism": "futurism",
    "Geometric": "geometric",
    "Gothic": "gothic",
    "Graffiti": "graffiti art",
    "Harlem Renaissance": "Harlem renaissance",
    "Hyperrealism": "hyperrealism",
    "Humorous": "humorous",
    "Landscape": "non-cartoon natural landscape",
    "Line Art": "line art",
    "Lofi": "lofi",
    "Marble Art": "marble art",
    "Metaphysical": "metaphysical",
    "Minimalism": "minimalism",
    "Modern": "modern",
    "Neon": "neon colors",
    "Normal": "Typical",
    "Old Cartoon": "old timey cartoon",
    "Oil Painting": "oil paining",
    "Pablo Picasso": "Pablo Picasso",
    "Painterly": "painterly",
    "Pastel": "bright pastel colors",
    "Performance Art": "performance art",
    "Photographic": "realistic photographic",
    "Photorealism": "photorealism",
    "Pointillist": "pointillist",
    "Pop Surrealism": "pop surrealism",
    "Psychedelic": "psychedelic",
    "Retro": "retro aesthetic",
    "Romantic": "romantic",
    "Salvador Dalí": "Salvador Dalí",
    "Stained Glass": "stained glass",
    "Steampunk": "steampunk",
    "Still Life": "still life",
    "Tim Burton": "Tim Burton",
    "Urban": "urban",
    "Van Gogh": "Van Gogh",
    "Vintage": "vintage sepia toned photograph",
    "Watercolors": "watercolors",
    "Whimsical": "whimsical",
}
