from expects import expect, equal, have_properties
from doublex import Spy, when
from agenda_create_action import AgendaCreateAction
from agenda_service import AgendaService
from agenda_models import Contact

A_NAME = 'a_name'
A_SURNAME = 'a_surname'
A_PHONE_NUMBER = 'a_phone_number'
AN_EMAIL = 'an_email'


with describe('Agenda create action'):
    with context('creating a contact'):
        with it('returns the created contact'):
            contact = {'name': A_NAME,
                    'surname': A_SURNAME,
                    'phone_number': A_PHONE_NUMBER,
                    'email': AN_EMAIL
                    }
            an_agenda_service = Spy(AgendaService)
            a_contact = Contact(A_NAME, A_SURNAME, A_PHONE_NUMBER, AN_EMAIL)
            when(an_agenda_service).add(A_NAME, A_SURNAME, A_PHONE_NUMBER, AN_EMAIL).returns(a_contact)
            create_action = AgendaCreateAction(an_agenda_service)

            creation = create_action.execute(contact)

            expect(creation).to(have_properties(name=A_NAME))
