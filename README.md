# Tuition Booking Bot

A simple Telegram Bot for booking tuition sessions.

## About The Project

A Telegram bot created to expedite the process of booking tuition sessions for tutees as well as consolidating the scheduling for the tutor in one place.

## Getting Started

### Prerequisites

You can easily install the prerequisites for the Telegram Bot by downloading the requirements.txt and running the following in the shell:

   ```sh
   $ pip install -r requirements.txt
   ```

### Installation

1. Download the Tuition Bot package and place it in your environment directory.

2. Interact with the [BotFather](https://telegram.me/botfather) to create your bot and obtain the Access Token.

3. Paste your Access Token into the `'TOKEN'` variable in the following line in `main.py`. 
   ```sh
   application = ApplicationBuilder().token('TOKEN').build()
   ```
For more detailed instructions on how to set up a Telegram Bot, visit the [tutorial website](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot).

## Roadmap

- [ ] A function for users to delete the previous bookings.
- [x] Checking mechanisms to ensure a proper format of date and time is observed.
- [x] Serialization to have a persistent list of schedules.