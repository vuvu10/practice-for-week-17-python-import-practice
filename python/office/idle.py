# Your code here
import random

def chat():
    coworkers = ['Jack', 'Lenny', 'Michelle', 'Andrea']
    chatee = random.choice(coworkers)
    print(f'Chatting with {chatee}...')
    print('Done')

def getWater():
    print('Getting water...')
    print('That was refreshing.')
    
def useSocialMedia():
    socialMedia = ['Facebook', 'Twitter', 'YouTube', 'Reddit']
    choice = random.choice(socialMedia)
    print(f'Using {choice}...')
    print('Done')