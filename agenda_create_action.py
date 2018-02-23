class AgendaCreateAction(object):
    def __init__(self, agenda_service):
        self._agenda_service = agenda_service

    def execute(self, data):
        name = data['name']
        surname = data['surname']
        phone_number = data['phone_number']
        email = data['email']
        contact = Contact(nane, surname, phone_number, email)
        return self._agenda_service.add(contact)

