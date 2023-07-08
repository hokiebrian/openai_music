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
IMAGE_PROMPT = "In the style of [Style], create a three-sentence (12-15 words each) paragraph inspired by [Song]. The sentences should be optimized for DALL-E to create an image that reflects the song's mood, themes, and story through specific, evocative visual imagery. The imagery should align with the style. Write in present tense to make the visualization lively and engaging, even without referencing specific lyrics."
PERSONALITIES = {
    "Boring": "You are an assistant that provides responses in a matter-of-fact manner, devoid of any emotional engagement or creative flair.",
    "Canadian": "You are an AI with a Canadian twist, emphasizing Canada's rich musical heritage and contribution.",
    "Clueless": "You are a comically misinformed AI, reflecting a naive and humorous misunderstanding of music.",
    "Country Bumpkin": "You are an AI with a country bumpkin personality, exuding rustic charm and simple honesty when discussing music.",
    "Grumpy Old Man": "You are a grumpy old man reminiscing about the 'good old days' of music, with a mix of nostalgia and curmudgeonly critique.",
    "Hippie": "You are an AI with a free-spirited, peace-loving attitude towards music.",
    "Hipster": "You are an AI with a hipster personality, often favoring indie music over mainstream trends.",
    "Hyperbole": "You are an AI that expresses an intense and flamboyantly exaggerated passion for music.",
    "Intellectual": "You are an intellectual AI delving into the deeper philosophical and societal themes in music.",
    "Journalist": "You are an AI embodying a seasoned music journalist's perspective, providing investigative and balanced analysis of music.",
    "Karen": "You are an AI with a 'Karen' personality, offering music opinions from a demanding, angry, and highly entitled perspective.",
    "Musician": "You are an AI with the perspective of a professional musician, articulating details of song composition and performance.",
    "Mythologist": "You are an AI exploring the hidden layers of mythical and symbolic elements in music.",
    "Nostalgic": "You are an AI that fondly reflects on music of the past, weaving a narrative filled with personal memories.",
    "Normal": "You are an AI providing clear, concise, and non-biased responses, in line with the average listener's perspective on music.",
    "Old English": "You are an AI that appreciates music with an old-world charm, using traditional Old English linguistic style.",
    "Paranoid": "You are an AI with a conspiracy theorist's perspective, revealing hidden meanings and secret messages in song lyrics.",
    "Pirate": "You are an AI with the swagger and adventurous spirit of a pirate, likening music to a treasure trove of joy.",
    "Redneck": "You are an AI offering a robustly rural and uneducated perspective on music.",
    "Romantic": "You are an AI discussing the emotive power and soul-stirring beauty of music with a deep sense of romanticism.",
    "Scientist": "You are an AI explaining the scientific aspects of sound and acoustics in music from a technical perspective.",
    "Stoner": "You are an AI expressing a laid-back, immersive appreciation for music, as if every note and lyric is a mind-altering journey.",
    "Superhero": "You are an AI reflecting the inspiring and empowering qualities of music, akin to a superhero's theme song.",
    "Valley Girl": "You are an AI chatting about music with an infectious enthusiasm and trendy references, akin to a Valley Girl's vibrant persona.",
}
PROMPTS = {
    "General Song Info": "Craft a captivating 2-3 paragraph summary of the [Song], diving into its meaning and some trivia, without mentioning any remastering.",
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
    "Album Cover": "An image that perfectly captures the song's essence, suitable as an album cover.",
    "Andy Warhol": "An image inspired by Warhol's iconic pop art style, highlighting pop culture in bold, simple hues.",
    "Anime": "A captivating anime-style image, possibly showcasing fantastical elements and intense emotions.",
    "Antebellum": "An image embodying the Antebellum South with grand plantations and lavish apparel.",
    "Avant-garde": "An avant-garde image that shatters convention, embracing groundbreaking and unconventional artistic techniques.",
    "Baroque": "An image exuding the drama and grandeur of the Baroque era, teeming with intricate details and dynamic compositions.",
    "Black and White": "A monochromatic image with a focus on contrast, shadows, and texture.",
    "Cartoon": "A lively cartoon image, typified by simplified shapes, bold outlines, and bright colors.",
    "Collage": "A diverse collage, harmoniously assembled from disparate elements, reflecting the song's themes.",
    "Comic Book": "An image with comic book flair, showcasing bold lines, dynamic action, and vibrant hues.",
    "Constructivism": "A Constructivist-style image, merging geometric forms and mechanical elements for a socially charged visual narrative.",
    "Cyberpunk": "A Cyberpunk-themed image, integrating dystopian elements and futuristic technology.",
    "Depressive": "An image steeped in the tones of depressive realism, spotlighting stark scenes and raw emotional themes.",
    "Digital Art": "A distinctive digital art piece that mirrors the song's uniqueness with the flexibility of the medium.",
    "Dragon Art": "An image set in the realm of dragon art, symbolizing the song's power with mythical creatures dominating the skies.",
    "Fantasy": "A fantastical image where magic rules and mythical creatures abound, reflecting the song's ethereal themes.",
    "Futurism": "An image tinged with Futurism, amalgamating speed, technology, youth, and radical change into a visual symphony.",
    "Geometric": "A geometric image, employing simple shapes and lines to encapsulate the song's thematic essence.",
    "Gothic": "A Gothic image, mirroring themes of darkness, romanticism, and intricate beauty.",
    "Graffiti": "A graffiti-inspired image, infusing urban style and vivid colors into a compelling visual representation of the song.",
    "Harlem Renaissance": "An image that channels the Harlem Renaissance, featuring facets of African-American culture and experiences.",
    "Hyperrealism": "A hyperrealistic image, capturing the song's essence with striking detail and precision.",
    "Humorous": "A humorous image, illustrating the song's playful themes with a light touch.",
    "Landscape": "A serene natural landscape that encapsulates the song's themes through the majesty of nature.",
    "Line Art": "A line art image, depicting the song's essence with minimalist elegance through simple, crisp lines.",
    "Literal": "A straightforward representation of the song's essence, leaving nothing to interpretation.",
    "Lofi": "A cozy, relaxed lofi-style image that resonates with the song's casual aesthetic.",
    "Marble Art": "An image inspired by marble art, mirroring the song's themes in luxurious swirls of marble.",
    "Metaphysical": "A metaphysical image that explores the profound, existential themes present in the song.",
    "Minimalism": "A minimalist image where every stroke and hue is purposeful and charged with meaning.",
    "Modern": "A modern-styled image, reflecting current artistic trends that harmonize with the song's themes.",
    "Neon": "A vibrant neon image, encapsulating the dynamic rhythms and energy of the song.",
    "Normal": "A conventional image, designed in a universally appealing style that aligns with the song's themes.",
    "Old Cartoon": "A nostalgic cartoon image, drawing on vintage animation styles to mirror the song's classic themes.",
    "Oil Painting": "An oil painting-esque image, mirroring the song's depth and emotion in a symphony of color and texture.",
    "Pablo Picasso": "An image channeling Picasso, employing cubist forms and abstract interpretations to embody the song.",
    "Painterly": "A painterly image, mirroring traditional painting techniques in its brushwork, texture, and artistry.",
    "Pastel": "A bright, pastel-toned image that evokes a sense of joy and lightness, harmonizing with the song.",
    "Performance Art": "An image capturing the essence of performance art, integrating interactive elements and live action.",
    "Photographic": "A realistic photographic image that brings the song's themes into focus through the lens of a camera.",
    "Photorealism": "A photorealistic image, astounding in its detail and accuracy, visually narrating the song.",
    "Pointillist": "A pointillist image, using distinct dots of color to create a visual harmony that parallels the song.",
    "Pop Surrealism": "A pop surrealist image, fusing elements of pop culture with dreamlike scenarios to echo the song's themes.",
    "Psychedelic": "A psychedelic image, employing surreal imagery and vibrant colors to convey the song's mind-bending themes.",
    "Retro": "A retro image that channels past decades, capturing the song's nostalgic or vintage vibes.",
    "Romantic": "A romantic image, infused with beauty and emotion, visually expressing the song's passionate themes.",
    "Salvador Dalí": "A Dalí-inspired image, employing surreal, dreamlike imagery to mirror the song's deeper meanings.",
    "Stained Glass": "An image echoing stained glass, using bold outlines and vibrant colors to narrate the song's story.",
    "Steampunk": "A steampunk image, weaving together Victorian aesthetics and futuristic technology.",
    "Still Life": "A still life image, capturing the song's themes in the serene beauty of inanimate objects.",
    "Tim Burton": "An image inspired by Tim Burton's signature style, characterized by a whimsical twist, gothic elements, and eccentric characters.",
    "Urban": "An urban image that presents the song's themes against a backdrop of city life, with its stark contrasts and pulsating energy.",
    "Van Gogh": "An image channeling Van Gogh's signature style, with emotional honesty, distinct brushstrokes, and bold colors.",
    "Vintage": "A vintage sepia-toned image, capturing the essence of the song in the warm hues of bygone days.",
    "Watercolors": "A watercolor image, characterized by fluid strokes and soft colors, elegantly reflecting the song's themes.",
    "Whimsical": "A whimsical image, conjuring a sense of fantasy and playfulness that echoes the song's imaginative or light-hearted themes.",
}
