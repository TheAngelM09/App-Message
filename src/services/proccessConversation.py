from src.database.connection import get_connection
from src.models.ConversationModel import ConversationModel 

def proccessPrompt(company, phone, msg):

    db = get_connection()
    dataPrompt = ConversationModel.getPrompt(db, company, phone)
    message = {
        "role": "user",
        "content": msg
    }
    dataPrompt[0]["messages"].append(message)
    return dataPrompt
 
def proccesseConversation(company, phone, msg, time):

    db = get_connection()
    conversation = ConversationModel.get(db, company, phone)
    message = {
        "role": "user",
        "content": msg,
        "timpstamp": time
    }
    conversation[0].append(message)
    return conversation