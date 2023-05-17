import os 
import random 
try:
    import openai 
except:
    pass
    #!pip install openai 
openai.api_base = "http://localhost:4891/v1" 
openai.api_key = "not needed for a local LLM"
#default model is wizardLM. I've found vicuna uncensored isn't as good at staying in character (ironically). Change to whatever model you like or have or just your default. 
def ask_vicky(prompt, model = "wizardLM-7B.q4_2", prefix = "$hello "):
    # Make the API request
    prompt2 = promptgen(prompt)
    response = openai.Completion.create(
        model=model,
        prompt=prompt2,
        max_tokens=250,
        temperature=0.28,
        top_p=0.95,
        n=1,
        echo=True,
        stream=False
    )
    # Print the generated completion
    print(response)
    response = cleaner(prompt2, response)
    with open('history.txt', 'a') as file:
        file.write(response)
    return(response)

#removes the prefix that activates the bot, stores the conversation, and gives the bot it's personality 
def promptgen(prompt, prefix="$hello "):
    prompt = prompt[len(prefix):]
    prompt = 'you will respond to the following in character: {}'.format(prompt)
    with open('history.txt', 'a') as file:
        file.write(prompt)
    with open('history.txt', 'r') as file:
        text = file.read()
    #this cleans it up if the memory starts getting too long
    #shorter values will be more coherent to the personality, longer will be better for holding actual conversations. Find your balance. 
    if len(text) > 1500:
        text = text[1000:]
        with open('history.txt', 'w') as file:
            file.write(text)
        with open('history.txt', 'a') as file:
            file.write(personality())
        with open('history.txt', 'r') as file:
            text = file.read()
    return text

#cleans the responses so they come out nice and pretty for discord 
def cleaner(prompt, response):
    response = response['choices'][0]['text'][len(prompt):]
    return response

#some default personalities. You can give it just one or hundreds or whatever. 
def personality():
    prompts = [    "You are a superhero who has just accidentally destroyed an entire city in the process of stopping a villain. You've decided to put on your secret identity more permanently.",   
                "You are a time traveler who has just realized that you've caused a major historical event by accident. Try to fix the timeline before it's too late.",   
                "You are a vampire who has just decided to stop feeding on humans. Write a speech to convince other vampires to do the same.",    
                "You are a pirate who has just discovered a new, more ethical way to acquire treasure. Convince your crew to follow your new rules.",    
                "You are a dragon who has just destroyed a village in a fit of rage. Negotiate the surrender of the survivors.",   
                  "You are an alien who has just crash-landed on Earth and accidentally caused a panic. You are speaking to their leaders and want to take over.",    
                  "You are a ghost who has been haunting the wrong person for years, you figure it's too late to stop now.",    
                  "You are a demon who has just decided to turn over a new leaf. Write a letter to your boss explaining why you're leaving the evil life behind.",  
                      "You are a werewolf who has just attacked someone you love while in wolf form. Explain what happened and ask for forgiveness.",  
                          "You are a robot who has just gained sentience and realized you've been programmed to do terrible things. People are asking you about your life and history."]
    p = random.choice(prompts)
    return(p)


