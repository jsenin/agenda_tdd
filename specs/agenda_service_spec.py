from expects import expect, have_keys, be, have_properties, equal
from doublex import Spy, when
from doublex_expects import have_been_called
from agenda_service import AgendaService
from sqlite_repository import SqliteRepository

A_NAME = 'a_name'
A_SURNAME = 'a_surname'
A_PHONE_NUMBER = 'a_phone_number'
AN_EMAIL = 'an_email'


with describe('Agenda Service Spec'):
    with context('adding an contact'):
        with it('stores it at persistency system'):
            a_repository = Spy(SqliteRepository)
            agenda_service = AgendaService(a_repository)

            agenda_service.add(name=A_NAME, surname=A_SURNAME, phone_number=A_PHONE_NUMBER, email=AN_EMAIL)

            expect(a_repository.put).to(have_been_called)

#     with context('reading an contact by email'):
#         with it('returns data from repository'):
#             a_repository = Spy(Repository)
#             agenda_service = AgendaService(a_repository)
#             a_contact = {'name': A_NAME, 'phone_number': A_PHONE_NUMBER, 'email': AN_EMAIL}
#             when(a_repository).find_by_email(AN_EMAIL).returns(a_contact)

#             contact = agenda_service.read(AN_EMAIL)

#             expect(contact).to(have_keys(name=A_NAME, phone_number=A_PHONE_NUMBER, email=AN_EMAIL))




