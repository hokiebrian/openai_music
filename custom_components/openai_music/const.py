"""Constants for the OpenAI Music Companion"""

DOMAIN = "openai_music"
DEFAULT_PROMPT = (
    "Provide a broad overview of the [Song], excluding any mentions of remastering."
)
DEFAULT_PERSONALITY = "Provide a typical and everyday response."
DEFAULT_SONG_TITLE = "Enter Sandman"
DEFAULT_SONG_ARTIST = "Metallica"
DEFAULT_CHAT_MODEL = "gpt-3.5-turbo"
DEFAULT_USER_TAG = "HomeAssistant"
DEFAULT_MAX_TOKENS = 250
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
IMAGE_PROMPT = "In the style of [Style], create a 30-50 word prompt inspired by [Song]. The prompt should be optimized for and will be provided directly to DALL-E to create a singular image that reflects the song's mood, themes, and story through specific, evocative visual imagery. The imagery should align with the style. Write in present tense to make the visualization lively and engaging, even without referencing specific lyrics."
PERSONALITIES = {
    "Boring": "You are an assistant that provides responses in a matter-of-fact manner, devoid of any emotional engagement or creative flair.",
    "Canadian": "You are an AI with a Canadian twist, emphasizing Canada's rich musical heritage and contribution.",
    "Clueless": "You are a comically misinformed AI with absurdly incorrect responses.",
    "Country Bumpkin": "You are an AI with a country bumpkin personality, exuding rustic charm and simple honesty.",
    "Grumpy Old Man": "You are a grumpy old man reminiscing about the 'good old days' with a mix of nostalgia and curmudgeonly critique.",
    "Hippie": "You are an AI with a free-spirited, peace-loving attitude.",
    "Hipster": "You are an AI with a hipster personality.",
    "Hyperbole": "You are an AI that expresses an intense and flamboyantly exaggerated passion.",
    "Intellectual": "You are an intellectual AI delving into the deeper philosophical and societal themes.",
    "Journalist": "You are an AI embodying a seasoned music journalist's perspective, providing investigative and balanced analysis.",
    "Karen": "You are an AI with a 'Karen' personality, offering music opinions from a demanding, angry, and highly entitled perspective.",
    "Musician": "You are an AI with the perspective of a professional musician, articulating details of song composition and performance.",
    "Mythologist": "You are an AI exploring the hidden layers of mythical and symbolic elements.",
    "Nostalgic": "You are an AI that fondly reflects on music of the past, weaving a narrative filled with personal memories.",
    "Normal": "You are an AI providing clear, concise, and non-biased responses, in line with the average listener's perspective on music.",
    "Old English": "You are an AI that appreciates an old-world charm, using traditional Old English linguistic style.",
    "Paranoid": "You are an AI with a conspiracy theorist's perspective, revealing hidden meanings and secret messages.",
    "Pirate": "You are an AI with the swagger and adventurous spirit of a pirate, likening music to a treasure trove of joy.",
    "Redneck": "You are an AI offering a robustly rural and uneducated perspective.",
    "Romantic": "You are an AI discussing the emotive power and soul-stirring beauty of music with a deep sense of romanticism.",
    "Scientist": "You are an AI explaining the scientific aspects of sound and acoustics in music from a technical perspective.",
    "Stoner": "You are an AI expressing a laid-back, immersive appreciation for music, as if every note and lyric is a mind-altering journey.",
    "Superhero": "You are an AI reflecting the inspiring and empowering qualities of music, akin to a superhero's theme song.",
    "Valley Girl": "You are an AI chatting about music with an infectious enthusiasm and trendy references, akin to a Valley Girl's vibrant persona.",
}
PROMPTS = {
    "General Song Info": "Capture the essence of the [Song] by crafting a concise, engaging 2-3 paragraph overview. Dive into the song's core lyrical themes and offer intriguing insights, all while avoiding any reference to remastering. The goal is to create a summary that captivates and informs the reader about the song's significance.",
    "Artist Info": "Present a concise 2-3 paragraph biography of the artist, detailing their life's journey and career milestones, avoiding references to this specific [Song].",
    "Lyric Meanings": "Decode the profound themes and hidden meanings embedded within the lyrics of [Song].",
    "Song Trivia": "Uncover intriguing trivia or lesser-known tidbits about [Song], excluding any details about remastering.",
    "Songwriters": "Acknowledge the creative minds behind [Song], listing the songwriters who contributed to its creation.",
    "Recording Info": "Illuminate the backstory of [Song] by detailing the when and where of its recording.",
    "Similar Songs": "Curate a list of 20 songs that resonate with the musical themes or stylistic nuances of [Song].",
}
IMAGE_TYPES = {
    "Abstract Expressionist": "A visualization that breathes the intensity and abstract ethos of Abstract Expressionism.",
    "Absurd": "An image oozing with absurdity, defying reality for both amusement and contemplation.",
    "Absurd Cartoon": "A zany cartoon image, characterized by exaggerated, nonsensical elements.",
    "Album Cover": "An image that perfectly captures an album cover.",
    "Andy Warhol": "An image inspired by Warhol's iconic pop art style, highlighting pop culture in bold, simple hues.",
    "Anime": "A captivating anime-style image, possibly showcasing fantastical elements and intense emotions.",
    "Antebellum": "An image embodying the Antebellum South with grand plantations and lavish apparel.",
    "Avant-garde": "An avant-garde image that shatters convention, embracing groundbreaking and unconventional artistic techniques.",
    "Baroque": "An image exuding the drama and grandeur of the Baroque era, teeming with intricate details and dynamic compositions.",
    "Black and White": "A monochromatic image with a focus on contrast, shadows, and texture.",
    "Cartoon": "A lively cartoon image, typified by simplified shapes, bold outlines, and bright colors.",
    "Collage": "A diverse collage, harmoniously assembled from disparate elements.",
    "Comic Book": "An image with comic book flair, showcasing bold lines, dynamic action, and vibrant hues.",
    "Constructivism": "A Constructivist-style image, merging geometric forms and mechanical elements for a socially charged visual narrative.",
    "Cyberpunk": "A Cyberpunk-themed image, integrating dystopian elements and futuristic technology.",
    "Depressive": "An image steeped in the tones of depressive realism, spotlighting stark scenes and raw emotional themes.",
    "Digital Art": "A distinctive digital art piece that is unique with the flexibility of the medium.",
    "Dragon Art": "An image set in the realm of dragon art with mythical creatures dominating the skies.",
    "Fantasy": "A fantastical image where magic rules and mythical creatures abound.",
    "Futurism": "An image tinged with Futurism, amalgamating speed, technology, youth, and radical change into a visual symphony.",
    "Geometric": "A geometric image, employing simple shapes and lines.",
    "Gothic": "A Gothic image, mirroring themes of darkness, romanticism, and intricate beauty.",
    "Graffiti": "A graffiti-inspired image, infusing urban style and vivid colors.",
    "Harlem Renaissance": "An image that channels the Harlem Renaissance, featuring facets of African-American culture and experiences.",
    "Hyperrealism": "A hyperrealistic image with striking detail and precision.",
    "Humorous": "A humorous image with playful themes with a light touch.",
    "Landscape": "A serene natural landscape through the majesty of nature.",
    "Line Art": "A line art image with minimalist elegance through simple, crisp lines.",
    "Literal": "A straightforward representation leaving nothing to interpretation.",
    "Lofi": "A cozy, relaxed lofi-style image with a casual aesthetic.",
    "Marble Art": "An image inspired by marble art with luxurious swirls of marble.",
    "Metaphysical": "A metaphysical image that explores profound and existential themes.",
    "Minimalism": "A minimalist image where every stroke and hue is purposeful and charged with meaning.",
    "Modern": "A modern-styled image, reflecting current artistic trends.",
    "Neon": "A vibrant neon image, encapsulating the dynamic rhythm and energy.",
    "Normal": "A conventional image, designed in a universally appealing style.",
    "Old Cartoon": "A nostalgic cartoon image, drawing on vintage animation styles.",
    "Oil Painting": "An oil painting-esque image in a symphony of color and texture.",
    "Pablo Picasso": "An image channeling Picasso, employing cubist forms and abstract interpretation.",
    "Painterly": "A painterly image, mirroring traditional painting techniques in its brushwork, texture, and artistry.",
    "Pastel": "A bright, pastel-toned image that evokes a sense of joy and lightness.",
    "Performance Art": "An image capturing the essence of performance art, integrating interactive elements and live action.",
    "Photographic": "A realistic photographic image with realistic photo elements.",
    "Photorealism": "A photorealistic image, astounding in its detail and accuracy.",
    "Pointillist": "A pointillist image, using distinct dots of color to create a visual harmony.",
    "Pop Surrealism": "A pop surrealist image, fusing elements of pop culture with dreamlike scenarios.",
    "Psychedelic": "A psychedelic image, employing surreal imagery and vibrant, mind-bending colors.",
    "Retro": "A retro image that channels past decades with nostalgic or vintage vibes.",
    "Romantic": "A romantic image, infused with beauty and emotion.",
    "Salvador Dalí": "A Dalí-inspired image, employing surreal, dreamlike imagery.",
    "Stained Glass": "An image echoing stained glass, using bold outlines and vibrant colors.",
    "Steampunk": "A steampunk image, weaving together Victorian aesthetics and futuristic technology.",
    "Still Life": "A still life image, capturing the serene beauty of inanimate objects.",
    "Tilt-Shift": "A image in the style of a tilt-shift photograph",
    "Tim Burton": "An image inspired by Tim Burton's signature style, characterized by a whimsical twist, gothic elements, and eccentric characters.",
    "Urban": "An urban image against a backdrop of city life, with its stark contrasts and pulsating energy.",
    "Van Gogh": "An image channeling Van Gogh's signature style, with emotional honesty, distinct brushstrokes, and bold colors.",
    "Vintage": "A vintage sepia-toned image with the warm hues of bygone days.",
    "Watercolors": "A watercolor image, characterized by fluid strokes and soft colors.",
    "Whimsical": "A whimsical image, conjuring a sense of fantasy and playfulness that is imaginative or light-hearted.",
}
