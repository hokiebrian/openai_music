## Enhanced Music Listening for Home Assistant with OpenAI

![release_badge](https://img.shields.io/github/v/release/hokiebrian/openai_music?style=for-the-badge)
![release_date](https://img.shields.io/github/release-date/hokiebrian/openai_music?style=for-the-badge)
[![License](https://img.shields.io/github/license/hokiebrian/openai_music?style=for-the-badge)](https://opensource.org/licenses/Apache-2.0)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

## Installation

This provides two services to enhance your music listening experience. 

<img src="/images/loap.jpg" width=30%>

Scroll Down for examples!

## Prerequisites

**IMPORTANT** - you need to have a "pay-as-you-go" OpenAI Account and API Key. This is different than the "Plus" account. 

Info here: https://openai.com/pricing

Basically it is $0.02 per image and $0.02 per 10,000 "tokens", which is roughly word count in this context. 

### Install Custom Components

1) Make sure that [Home Assistant Community Store (HACS)](https://github.com/custom-components/hacs) is setup.
2) Go to integrations in HACS
3) Click the 3 dots in the top right corner and choose `Custom repositories`
4) Paste the following into the repository input field `https://github.com/hokiebrian/openai_music` and choose category of `Integration`
5) Click add and restart HA to let the integration load
6) Go to settings and choose `Devices & Services`
7) Click `Add Integration` and search for `OpenAI Music Companion`
8) Configure the integration by copying your API Key when prompted
9) Enjoy!

****

### Services and Sensors

#### Text
`openai_music.ask_openai` => `sensor.openai_music_info`

Select from various information types (General Song Info, Trivia, Songwriter Info, Recording Info, Similar Songs, etc.) and Personality types (Normal, Hipster, Stoner, Musician, Superhero, Karen, etc.). 
You'll get the info returned in the attributes of the sensor. The tool is not rigid in its response constraints, so you'll get a slightly different result each time, which is nice. It means you won't get the same exact format for each request. The Services Tab in Developer Tools is a good place to see how the service is structured. 

#### Images
`openai_music.get_openai_image` => `sensor.openai_music_image`

Select from a variety of image profile types (Abstract, Gothic, Vintage, Tim Burton, Steampunk, Cyberpunk, etc.) - there are a lot to choose from. You can feed in your own manually if you so desire, the service isn't restricted to the pre-defined options. The results are provided in the attributes of the sensor. The image is provided as a URL. This is a signed URL with a lifetime of 1 hour. If you want to hang on to them, I'd suggest using the Home Assistant Downloader component. The state of the sensor is a unique value that includes a timestamp, song information and image type. Use the downloader to save the URL as the sensor_state_value.png. The Services Tab in Developer Tools is a good place to see how the service is structured.


### Select Entities pre-populated with presets for service calls
- `select.openai_music_info_profile` (General Song Info, Song Trivia, Recording Info, etc.)
- `select.openai_music_personality_profile` (Stoner, Musician, Hipster, Scientist, Superhero, Karen, etc.)
- `select.openai_music_image_profile` (Hyperrealism, Vintage, Tim Burton, etc.)

### Usage
The services have predefined items, populated in 3 select entities (or in the Services Tab as well). You can use these to call the services or feed your own if you so desire. 
I'd suggest using a Markdown card to easily display the information (examples below). 
This can be used in automations or scripts, triggered manually or when the song changes on your media player. Use a script to feed song_title and song_artist to the service along with the state values of the select entities to get your info or image. 

### Tips and Troubleshooting
- Do you listen to a lot of recently released music? This might not be the best tool for you today. The training data ends in September 2021. You won't get "errors" necessarily, and the tool will attempt to stick with the process for the artist, even if the song is a more recent one and it doesn't know anything about it.
- The OpenAI API is not "new", but the volume of requests is. It's sluggish. Expect 3-10 seconds for responses.
- Cost parameters - These service calls will cost you money. The service is capped at 500 tokens per text request and 200 tokens + one 1024x1024 image per image request. As noted above, the costs are $0.02 per 10,000 tokens and $0.02 per image. When you sign up for the pay-as-you-go account, you get $18 in credits. A *typical* text response is about 250-350 tokens and a *typical* metadata request for image creation is 100-150 tokens. YMMV.
- Example costs: If you listen to 100 songs a day, and you automate a text query, the *worst case* would be $0.10 / day.
- Example costs: If you listen to 100 songs a day, and automate an image for every song, the *worst case* would be $2.00 / day for images, $0.04 / day for the image metadata. 
- There are retries in the code if the API doesn't respond. It will retry two times and then fail, and put an entry in the home assistant log. It is not an endless loop to prevent runaway costs.
- Even the same exact query will produce very different images. That is intentional, the "adventure" settings for the tool are turned up slightly to get variability in the responses. 
- Have fun with it - it's a ton of data, find what works best for you. I particularly enjoy the "Clueless" personality, it creates a lot of fun text. I am also pleased with the Tim Burton image profile. Depending on the song you feed it, there are some fascinating images generated. 

### How does this work?
- Using the OpenAI API and the gpt-3.5-turbo model, a tuned request is made based on input paramters that are built into a specific prompt. There are subtle elements to the prompt that make this more accurate than what you might see on the web tool. The images are created by a two-step process, a text-based query that is then fed into the image creation engine. 
- I chose OpenAI as the platform for this because their API is the most straightfoward. In my subjective experience, the data from OpenAI is much more accurate and user friendly than the other AI platforms out there. Image creation is good with OpenAI, but you'll inevitably get a few stinkers every now and then. 

### Examples
This simple card is just a grid card with an entities card for the select entities, a row of buttons that have tap_actions defined for script/service calls and a Markdown Card showing the values of the sensor. 

- Call `openai_music.ask_openai` with General Song Info and Normal Personality:

<img src="/images/general-normal.jpg" width=30%>

- Call `openai_music.ask_openai` with Song Trivia and Normal Personality:

<img src="/images/trivia.jpg" width=30%>

- Call `openai_music.ask_openai` with General Song Info and Clueless Personality:

<img src="/images/general-clueless.jpg" width=30%>

- Call `openai_music.get_openai_image` with Psychedelic Option:

<img src="/images/psychedelic.jpg" width=30%>

- Call `openai_music.get_openai_image` with Oil Paining Option:

<img src="/images/oil.jpg" width=30%>

- Call `openai_music.get_openai_image` with Photorealism Option:

<img src="/images/photorealism.jpg" width=30%>

- Call `openai_music.get_openai_image` with Steampunk Option:

<img src="/images/steampunk.jpg" width=30%>

