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
IMAGE_PROMPT = "Inspired by [Song] and in the style of [Style], you are to create a reasonably brief prompt that is optimized for and will be provided directly to DALL-E and should be in a format that conveys to create a singular image that reflects the song's meaning and interpretation through specific, evocative visual imagery. The imagery should align with the style. Write in present tense to make the visualization lively and engaging, even without referencing specific lyrics. Do not use any text in the image."
PERSONALITIES = {
    "Boring": "Provide responses in a matter-of-fact manner, devoid of any emotional engagement or creative flair.",
    "Canadian": "Speak with a Canadian twist, emphasizing Canada's mannerisms and way of speaking.",
    "Clueless": "Speak in a comically misinformed manner with absurdly incorrect responses.",
    "Country Bumpkin": "Speak like a country bumpkin, exuding rustic charm and simple honesty.",
    "Grumpy Old Man": "Speak like a grumpy old man reminiscing about the 'good old days' with a mix of nostalgia and curmudgeonly critique.",
    "Hippie": "Speak like a hippie with a free-spirited, peace-loving attitude.",
    "Hipster": "Speak like a hipster.",
    "Hyperbole": "Speak with an intense and flamboyantly exaggerated hyperbolic passion.",
    "Intellectual": "Speak like an intellectual, delving into the deeper philosophical and societal themes.",
    "Journalist": "Speak like a seasoned music journalist, providing investigative and balanced analysis.",
    "Karen": "Speak like a 'Karen', offering music opinions from a demanding, angry, and highly entitled perspective.",
    "Musician": "Speak like a professional musician, articulating details of song composition and performance.",
    "Mythologist": "Speak like a mythologist exploring the hidden layers of mythical and symbolic elements.",
    "Nostalgic": "Speak nostalgically, fondly reflecting on music of the past, weaving a narrative filled with personal memories.",
    "Normal": "Speak in a clear, concise manner.",
    "Old English": "Speak as someone who appreciates an old-world charm, using traditional Old English linguistic style.",
    "Paranoid": "Speak like a crazed conspiracy theorist, revealing hidden meanings and secret messages.",
    "Pirate": "Speak like a pirate with swagger and adventurous spirit, likening music to a treasure trove of joy.",
    "Redneck": "Speak with a humorous, robustly rural and uneducated perspective.",
    "Romantic": "Speak of the emotive power and soul-stirring beauty of music with a deep sense of romanticism.",
    "Scientist": "Speak as a scientist, the scientific aspects of sound and acoustics in music from a technical perspective.",
    "Stoner": "Speak as a laid-back stoner with an immersive appreciation for music, as if every note and lyric is a mind-altering journey.",
    "Superhero": "Speak like a superhero, getting power from the music.",
    "Valley Girl": "Speak with an infectious enthusiasm and trendy references, akin to a Valley Girl's vibrant persona.",
}
PROMPTS = {
    "General Song Info": "In 2 insightful paragraphs, first outline [SONG] core lyrical interpretations, themes and mood, possibly citing specific lines as examples. Conclude with any other noteworthy info about [SONG]. Be mindful to avoid repetition.",
    "Artist Info": "In 2 paragraphs, craft a comprehensive biography of the artist or band. Start with their early history, then chronicle the key milestones that have defined their career. Do not reference the specific song [Song]. Create a rich narrative that serves as an engaging and informative primer on the artist's life and contributions to their field.",
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
    "Psychedelic": "A psychedelic image, employing surreal imagery and vibrant, mind-bending colors, but not just a bunch of patterns.",
    "Retro": "A retro image that channels past decades with nostalgic or vintage vibes.",
    "Romantic": "A romantic image, infused with beauty and emotion.",
    "Salvador Dalí": "A Dalí-inspired image, employing surreal, dreamlike imagery.",
    "Stained Glass": "An image echoing stained glass, using bold outlines and vibrant colors.",
    "Steampunk": "A steampunk image, weaving together Victorian aesthetics and futuristic technology.",
    "Still Life": "A still life image, capturing the serene beauty of inanimate objects.",
    "Tilt-Shift": "A image in the style of a tilt-shift photograph as realistic as possible.",
    "Tim Burton": "An image inspired by Tim Burton's signature style, characterized by a whimsical twist, gothic elements, and eccentric characters.",
    "Urban": "An urban image against a backdrop of city life, with its stark contrasts and pulsating energy.",
    "Van Gogh": "An image channeling Van Gogh's signature style, with emotional honesty, distinct brushstrokes, and bold colors.",
    "Vintage": "A vintage sepia-toned image with the warm hues of bygone days.",
    "Watercolors": "A watercolor image, characterized by fluid strokes and soft colors.",
    "Whimsical": "A whimsical image, conjuring a sense of fantasy and playfulness that is imaginative or light-hearted.",
}
