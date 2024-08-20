chat_data = {}
ID = 0

def botData_db(bot_response, ID):
    if ID not in chat_data:
        chat_data[ID] = {"User": "", "Bot": ""}
    chat_data[ID]["Bot"] = bot_response
    return 

def userData_db(user_response, ID):
    if ID not in chat_data:
        chat_data[ID] = {"User": "", "Bot": ""}
    chat_data[ID]["User"] = user_response
    return

print(chat_data)