class AgendaService(object):
    def __init__(self, repository):
        self._repository = repository

    def add(self, name, surname, phone_number, email):
        return self._repository.put(name, surname, phone_number, email)

    def read(self, email):
        contact = self._repository.find_by_email(email)
        return {'name': contact['name'],
                'phone_number': contact['phone_number'],
                'email': contact['email']
                }
