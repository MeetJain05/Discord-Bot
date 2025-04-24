
# Discord Bot - Role Management and Polling

A simple Discord bot built using Python and the `discord.py` library that features role assignment, message censorship, direct messaging, polling, and custom commands.

## Features

- **Role Management**: Assigns and removes a secret role (`Knight`) for users.
- **Polls**: Users can create polls with a custom question.
- **Message Censorship**: The bot deletes messages containing inappropriate words like "shit".
- **Direct Messaging**: Sends direct messages to users based on their input.
- **Replying**: The bot replies to messages when the `!reply` command is used.
- **Permissions**: Certain commands are restricted to users with specific roles (e.g., `!secret` is only accessible to those with the "Knight" role).

## Requirements

- Python 3.x
- `discord.py` library
- `python-dotenv` library for managing environment variables

## Setup

### 1. Clone the repository
Clone this repository to your local machine using Git:

```bash
git clone https://github.com/your-username/discord-bot.git
cd discord-bot
```

### 2. Create a virtual environment (optional but recommended)
Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file
Create a `.env` file in the root of the project and add your Discord bot token:

```
DISCORD_TOKEN=your_discord_bot_token_here
```

Make sure to replace `your_discord_bot_token_here` with your actual Discord bot token.

### 5. Run the bot
Start the bot by running the following command:

```bash
python main.py
```

## Commands

- `!hello`: Greets the user with a message.
- `!assign`: Assigns the `Knight` role to the user.
- `!remove`: Removes the `Knight` role from the user.
- `!poll [question]`: Starts a poll with thumbs up/down reactions.
- `!dm [message]`: Sends a DM to the user with their message.
- `!reply`: Replies to the user’s message.
- `!secret`: Only accessible to users with the `Knight` role.

## License

This project is licensed under the [MIT License](LICENSE).
