"""Constants for the OpenAI Music Companion"""

DOMAIN = "openai_music"
DEFAULT_PROMPT = (
    "Provide a broad overview of the song, excluding any mentions of remastering."
)
DEFAULT_PERSONALITY = "Answer like a music expert"
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
IMAGE_PROMPT = "Using detailed imagery in a [Style] style, describe an image in three concise sentences (approximately 12-15 words each) that encapsulates the meaning and essence of [Song]. Through visual elements alone, convey the story, emotions, and themes portrayed in the song. Your description should be vivid, evocative, and framed in the present tense, allowing the viewer to connect with the song's meaning without relying on any textual elements or lyrics."
PERSONALITIES = {
    "Canadian": "Answer like a proud Canadian, celebrating Canada's contributions to music",
    "Clueless": "Answer like someone humorously misunderstanding the world of music",
    "Country Bumpkin": "Answer like a country folk, fondly discussing country music",
    "Grumpy Old Man": "Answer like a grumpy old man reminiscing about the 'good old days' of music",
    "Hipster": "Answer like an indie music-loving hipster critiquing a popular music trend",
    "Hippie": "Answer like a free-spirited hippie, talking about the power of music to unite people",
    "Hyperbole": "Answer like someone expressing a love for music in wild exaggeration",
    "Intellectual": "Answer like an intellectual dissecting the philosophical themes in music",
    "Journalist": "Answer like a music journalist",
    "Karen": "Answer like a Karen, critiquing modern music trends",
    "Musician": "Answer like a professional musician explaining intricate musical compositions",
    "Normal": "Answer like a normal person",
    "Old English": "Answer like an Old English speaker praising the music of the bard",
    "Paranoid": "Answer like a conspiracy theorist, unearthing hidden messages in song lyrics",
    "Pirate": "Answer like a pirate who discovered a trove of music records",
    "Redneck": "Answer like a fiery redneck, passionately debating about country versus rock music",
    "Scientist": "Answer like a scientist explaining the physics of sound in music",
    "Stoner": "Answer like a laid-back stoner expressing deep love for a particular song",
    "Superhero": "Answer like a superhero who draws inspiration and power from music",
    "Valley Girl": "Answer like a Valley Girl, discussing music with infectious enthusiasm",
}
PROMPTS = {
    "General Song Info": "Provide a broad overview of the [Song], excluding any mentions of remastering.",
    "Artist Info": "Share details about the artist's life and career, excluding any references to this particular [Song].",
    "Lyric Meanings": "Interpret the underlying themes and meanings of [Song] lyrics.",
    "Song Trivia": "Reveal some lesser-known trivia or fun facts about [Song], disregarding any references to remastering.",
    "Songwriters": "Identify the songwriters who contributed to the creation of [Song].",
    "Recording info": "Detail the time and place of [Song] recording.",
    "Similar Songs": "List 20 songs that share similar musical themes or style with [Song].",
}
IMAGE_TYPES = {
    "Abstract Expressionist": "an image immersed in emotional intensity and non-representational abstraction, channelling the spirit of abstract expressionism.",
    "Absurd": "an image pulsing with absurdity, twisting reality in ways that provoke laughter and thought in equal measure.",
    "Absurd Cartoon": "a cartoon image that gleefully embraces absurdity, featuring wildly exaggerated and nonsensical elements.",
    "Album Cover": "an image that encapsulates the vibe of the song, reflecting the themes in a way that could front its album.",
    "Andy Warhol": "an image drawing on Andy Warhol's iconic style, using bold, simple color palettes and references to popular culture.",
    "Anime": "a vibrant image in modern anime style, potentially exploring fantastical themes and strong emotions.",
    "Antebellum": "an image that echoes the Antebellum South, replete with grand plantations and sumptuous attire.",
    "Avant-garde": "an avant-garde image that pushes boundaries, employing innovative, experimental, and unconventional artistic techniques.",
    "Baroque": "an image embodying the grandeur and drama of the baroque period, filled with intricate details and dynamic compositions.",
    "Black and White": "a black and white photograph-style image, leaning into the power of contrast, shadows, and texture.",
    "Cartoon": "a cartoon image, characterized by its simplified shapes, bold outlines, and vibrant colors.",
    "Collage": "a collage image, masterfully assembled from diverse materials to form a cohesive whole that speaks to the song's themes.",
    "Comic Book": "an image with the bold lines, dynamic action, and vivid colors of a comic book cover.",
    "Constructivism": "an image in the constructivist style, employing geometric forms and mechanical elements to create a socially engaged visual message.",
    "Cyberpunk": "a cyberpunk-themed image, incorporating elements of futuristic technology and a dystopian world.",
    "Depressive": "an image painted in the tones of contemporary depressive realism, featuring stark scenes and raw emotional themes.",
    "Digital Art": "a digital art piece that harnesses the flexibility of the medium to create an image as unique as the song itself.",
    "Dragon Art": "an image set in the world of dragon art, where mythical creatures rule the skies and symbolize the song's power.",
    "Fantasy": "a fantasy art piece, where magic reigns and mythical creatures roam, reflecting the otherworldly themes of the song.",
    "Futurism": "an image crafted in the futurist style, combining speed, technology, youth, and violent change into a visual cacophony.",
    "Geometric": "a geometric image, utilizing simple shapes and lines to convey the song's thematic essence.",
    "Gothic": "a gothic-styled image, reflecting themes of darkness, romanticism, and complex beauty.",
    "Graffiti": "a graffiti art-inspired image, infusing urban style and vibrant colors into a compelling visual representation of the song.",
    "Harlem Renaissance": "an image that embodies the Harlem Renaissance, featuring elements of African-American culture and experiences.",
    "Hyperrealism": "a hyperrealistic image that captures the essence of the song with astonishing detail and precision.",
    "Humorous": "a humorous image that brings the song's lighter, more playful themes to life.",
    "Landscape": "a non-cartoon natural landscape image that captures the song's themes in the majesty and tranquility of nature.",
    "Line Art": "a line art image, using simple, crisp lines to depict the song's essence with minimalist elegance.",
    "Lofi": "a lofi-themed image, embodying the cozy and relaxed aesthetic of the song.",
    "Marble Art": "a marble art-inspired image, reflecting the song's themes in the smooth swirls and inherent luxury of marble.",
    "Metaphysical": "a metaphysical image that delves into the deeper, existential themes present in the song.",
    "Minimalism": "a minimalist image, where less is more and every line and color is charged with meaning.",
    "Modern": "a modern-styled image, reflecting current artistic trends and themes that resonate with the song.",
    "Neon": "a vibrant image characterized by neon colors, embodying the energy and dynamic rhythms of the song.",
    "Normal": "a typical image, designed in a universally recognizable style that suits the song's themes.",
    "Old Cartoon": "an old-timey cartoon image, drawing on vintage animation styles to echo the song's nostalgic or classic themes.",
    "Oil Painting": "an oil painting-like image, rich in texture and color, that mirrors the depth and emotion of the song.",
    "Pablo Picasso": "an image inspired by Pablo Picasso's style, utilizing cubist forms and abstract interpretations to visualize the song.",
    "Painterly": "a painterly image, reflecting the texture, brushwork, and artistic techniques found in traditional paintings.",
    "Pastel": "an image teeming with bright pastel colors, evoking a sense of lightness and joy that syncs with the song.",
    "Performance Art": "an image capturing the spirit of performance art, incorporating live action and interactive elements.",
    "Photographic": "a realistic photographic image that encapsulates the song's themes through the lens of a camera.",
    "Photorealism": "a photorealistic image, astounding in its level of detail and accuracy, that visually narrates the song.",
    "Pointillist": "a pointillist image, using small, distinct dots of color to form a visual melody that parallels the song.",
    "Pop Surrealism": "a pop surrealist image, combining elements of pop culture with dreamlike scenarios to mirror the song's themes.",
    "Psychedelic": "a psychedelic image, using vibrant colors and surreal imagery to convey the song's mind-expanding themes.",
    "Retro": "a retro aesthetic image that harkens back to past decades, capturing the song's nostalgic or vintage vibes.",
    "Romantic": "a romantic image, steeped in emotion and beauty, that visually expresses the song's passionate themes.",
    "Salvador Dalí": "an image in the style of Salvador Dalí, using surreal and dreamlike imagery to reflect the song's deeper meanings.",
    "Stained Glass": "an image reminiscent of stained glass, using vibrant colors and bold outlines to narrate the song's story.",
    "Steampunk": "a steampunk image, incorporating elements of Victorian-era aesthetics and futuristic technology.",
    "Still Life": "a still life image, capturing the song's themes in the quiet beauty of inanimate objects.",
    "Tim Burton": "an image inspired by Tim Burton's distinctive style, characterized by gothic elements, eccentric characters, and a whimsical twist.",
    "Urban": "an urban image that reflects the song's themes against the backdrop of city life, with its stark contrasts and pulsing energy.",
    "Van Gogh": "an image channeling Van Gogh's signature style, employing bold colors, emotional honesty, and distinct brushstrokes.",
    "Vintage": "a vintage sepia-toned photograph-style image, capturing the essence of the song in the warm hues of yesteryears.",
    "Watercolors": "a watercolor image, characterized by soft colors and fluid strokes, reflecting the song's themes with grace and subtlety.",
    "Whimsical": "a whimsical image, evoking a sense of playfulness and fantasy that echoes the song's lighthearted or imaginative themes.",
}
