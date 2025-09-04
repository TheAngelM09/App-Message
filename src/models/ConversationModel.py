class ConversationModel():
    
    @classmethod
    def get(selft, db, phone):
        try:
            consultar = db.cursor()
            consultar.execute(f"""SELECT conversations.conversation FROM conversations, contacts, companies 
                WHERE conversations.id_company = companies.id AND conversations.id_contact = contacts.id 
                AND contacts.phone = %s """, (phone,))
            datos = consultar.fetchone()
            if datos != None:
                return datos
            else:
                return None
        except Exception as e:
            return {'error': str(e)}