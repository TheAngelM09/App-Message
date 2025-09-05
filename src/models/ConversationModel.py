class ConversationModel():
    
    @classmethod
    def get(selft, db, company,phone):
        try:
            toConsult = db.cursor()
            toConsult.execute(f"""SELECT conversations.conversation FROM conversations, contacts, companies 
                WHERE conversations.id_company = companies.id AND conversations.id_contact = contacts.id 
                AND companies.id = %s AND contacts.phone = %s """, (company, phone,))
            data = toConsult.fetchone()
            if data != None:
                return data
            else:
                return None
        except Exception as e:
            return {'error': str(e)}
        
    @classmethod
    def getPrompt(selft, db, company, phone):
        try:
            toConsult = db.cursor()
            toConsult.execute(f"""SELECT process_conversation.prompt FROM process_conversation, companies, contacts 
                WHERE process_conversation.id_company = companies.id AND process_conversation.id_contact = contacts.id
                AND companies.id = %s AND contacts.phone = %s """, (company, phone,))
            data = toConsult.fetchone()
            if data != None:
                return data
            else:
                return None
        except Exception as e:
            return {'error': str(e)}