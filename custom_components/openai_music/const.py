"""Constants for the OpenAI Music Companion"""

DOMAIN = "openai_music"
DEFAULT_PROMPT = "Give me general info about the song"
DEFAULT_PERSONALITY = "Answer like a music expert"
DEFAULT_SONG_TITLE = "One"
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
DEFAULT_IMAGE_TYPE = "normal"
DEFAULT_IMAGE_RESOLUTION = "1024x1024"
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
    "General Song Info": "Give me general info about the song",
    "Artist Info": "Tell me about the artist only, nothing about the song",
    "Lyric Meanings": "How are the lyrics generally interpreted for",
    "Song Trivia": "Tell me some trivia about the song",
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
    "Anime": "anime",
    "Antebellum": "Antebellum",
    "Black and White": "black and white photograph",
    "Cartoon": "cartoon",
    "Collage": "collage",
    "Comic Book": "comic book cover",
    "Cyberpunk": "cyberpunk style",
    "Depressive": "contemporary depressive realism",
    "Futurism": "futurism",
    "Gothic": "gothic",
    "Hyperrealism": "hyperrealism",
    "Humorous": "humorous",
    "Landscape": "non-cartoon natural landscape",
    "Metaphysical": "metaphysical",
    "Minimalism": "minimalism",
    "Modern": "modern",
    "Neon": "neon colors",
    "Normal": "Typical",
    "Old Cartoon": "old timey cartoon",
    "Oil Painting": "oil paining",
    "Pablo Picasso": "Pablo Picasso",
    "Pastel": "bright pastel colors",
    "Photographic": "photographic",
    "Photorealism": "photorealism",
    "Pop Surrealism": "pop surrealism",
    "Psychedelic": "psychedelic",
    "Salvador Dalí": "Salvador Dalí",
    "Steampunk": "steampunk",
    "Still Life": "still life",
    "Tim Burton": "Tim Burton",
    "Van Gogh": "Van Gogh",
    "Vintage": "vintage sepia toned photograph",
    "Watercolors": "watercolors",
    "Whimsical": "whimsical",
}
