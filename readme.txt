GPT-4ALL Chatbot Discord Bot
Connecting GPT-4ALL Models to your Discord Server
This is a Python script that allows you to use your own customized GPT-4all model using the OpenAI API to interact with a Discord server. You can create a bot that responds in natural language to messages sent by users on the server.

Requirements
To run this script, you need to have the following installed:

GPT4all (https://gpt4all.io/index.html)
Discord API Module (https://discordpy.readthedocs.io/en/latest/)
openai module (https://openai.com/blog/openai-api)
Python 3.x or higher
Install these packages before running the script.

Installation Instructions
1. Install GPT4ALL on windows
2. Get your bot token and link from https://discord.com/developers/applications/
3. Use your bot's link to add it to your server 
4. Add in your token to the discord_client.py 
5. Double check that the model pointed to in aibot.py is your default model, and that your GPT4all is in server mode 
6. run discord_client.py 

Now has three modes: 
$newstory - creates new char
$hello - continues with story 
$instruct - standard chatbot 

Finally working with larger uncensored stable vicuna (as was the intent, see "vicky" names for functions lmao) though I'm sure some better prompt engineering would help make things smoother. 
I had to shorten the history function for instruct, but depending on the personality of your discord server users, you may be able to lengthen it back to 3k. 
Some of these functions are not done the most effecient way possible.... they're done the easiest way to change possible. Customization FTW! Maybe I can get it to play DND 
