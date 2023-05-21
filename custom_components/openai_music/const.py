"""Constants for the OpenAI Music Companion"""

DOMAIN = "openai_music"
DEFAULT_PROMPT = "Give me info about the song"
DEFAULT_PERSONALITY = "You are a Music Companion"
DEFAULT_SONG_TITLE = "One"
DEFAULT_SONG_ARTIST = "Metallica"
DEFAULT_CHAT_MODEL = "gpt-3.5-turbo"
DEFAULT_MAX_TOKENS = 500
DEFAULT_MAX_IMG_TOKENS = 200
DEFAULT_TEMPERATURE = 0.3
DEFAULT_IMAGE_TYPE = "cartoon"
DEFAULT_IMAGE_RESOLUTION = "1024x1024"
API_URL = "https://api.openai.com/v1/chat/completions"
IMAGE_API_URL = "https://api.openai.com/v1/images/generations"
PERSONALITIES = {
    "Normal": "Answer like a Music Expert",
    "Hipster": "Answer like a hipster who is really into the scene",
    "Stoner": "Answer like a stoner who loves music",
    "Musician": "Answer like a fellow musician",
    "Grumpy Old Man": "Answer like a grumpy old man",
    "Intellectual": "Answer like an intellectual who knows everything",
    "Pirate": "Answer like a pirate that is very excited to talk about music",
    "Scientist": "Answer like a scientist that uses a lot of scientific terms",
    "Clueless": "Answer like someone who is clueless with comically wrong information",
    "Old English": "Answer like an Old English speaker",
    "Superhero": "Answer like a superhero who gains power from music",
    "Valley Girl": "Answer like a valley girl that really has no clue about music",
    "Karen": "Answer like a Karen that complains about everytying",
    "Paranoid": "Answer like a paranoid conspiracy theorist",
    "Canadian": "Answer like a sterotypical proud Canadian",
    "Hyperbole": "Answer like someone who only speaks in hyperbole",
}
PROMPTS = {
    "General Song Info": "Give me info about the song",
    "Lyric Meanings": "How are the lyrics generally interpreted for",
    "Song Trivia": "Tell me some trivia about the song",
    "Songwriters": "Who wrote the song",
    "Recording info": "When and where was this song recorded:",
    "Similar Songs": "What are 20 songs similar to",
}
IMAGE_TYPES = {
    "Abstract Expressionist": "abstract expressionist style",
    "Album Cover": "album cover style",
    "Andy Warhol": "Andy Warhol style",
    "Cartoon": "cartoon",
    "Comic Book": "comic book cover style",
    "Frida Kahlo": "Frida Kahlo style",
    "Futurism": "futurism style",
    "Gothic": "gothic style",
    "Hyperrealism": "hyperrealism style",
    "Humorous": "humorous",
    "Landscape": "landscape style",
    "Metaphysical": "metaphysical style",
    "Minimalism": "minimalism style",
    "Modern": "modern style",
    "Normal": "Normal",
    "Old Cartoon": "Old cartoon style",
    "Oil Painting": "oil paining style",
    "Pablo Picasso": "Pablo Picasso style",
    "Pastel": "pastel style",
    "Photorealism": "photorealism style",
    "Psychedelic": "psychedelic style",
    "Salvador Dalí": "Salvador Dalí style",
    "Still Life": "still life style",
    "Tim Burton": "Tim Burton style",
    "Van Gogh": "Van Gogh style",
    "Yayoi Kusama": "Yayoi Kusama style",
}
