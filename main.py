import requests
import json

print('Discord wehbook sender')

print('\n')

#User inputs
webhook = input('Enter your webhook: ')
message = input('Enter your message: ')

#Sending the discord message
def send_discord_message(webhook, message):
    data = {
        'content': message
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(webhook, data=json.dumps(data), headers=headers)
    if response.status_code == 204:
        print('Message sent successfully.')
    else:
        print(f'Failed to send message. Status code: {response.status_code}')
        
send_discord_message(webhook, message)
