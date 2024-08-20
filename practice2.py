from Db_creation import messages, session



start = session.query(messages).filter(messages.id_) 
for data in start:
    print("here i amm please look at me\n\n\n",start)