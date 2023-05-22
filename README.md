## Enhanced Music Listening for Home Assistant with OpenAI

![release_badge](https://img.shields.io/github/v/release/hokiebrian/openai_music?style=for-the-badge)
![release_date](https://img.shields.io/github/release-date/hokiebrian/openai_music?style=for-the-badge)
[![License](https://img.shields.io/github/license/hokiebrian/openai_music?style=for-the-badge)](https://opensource.org/licenses/Apache-2.0)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

## Installation

This provides two services to enhance your music listening experience. 

## Prerequisites

IMPORTANT - you need to have a "pay-as-you-go" OpenAI Account and API Key. This is different than the "Plus" account. 

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

### Services and Sensors
`openai_music.ask_openai`
`sensor.openai_music_info`


`openai_music.get_openai_image`
`sensor.openai_music_image`

### Select Entities pre-populated with presets for service calls
`select.openai_music_info_profile`
`select.openai_music_personality_profile`
`select.openai_music_image_profile`


### Usage
The services have predefined items, populated in 3 select entities. You can use these to call the services or feed your own if you so desire. 
I'd suggest using a Markdown card to easily display the infomation (examples below).
