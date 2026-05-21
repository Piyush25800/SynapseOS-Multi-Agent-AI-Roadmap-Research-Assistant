chat_memory = []

def save_memory(user, ai):

    chat_memory.append({
        "user": user,
        "ai": ai
    })

def get_memory():

    return chat_memory