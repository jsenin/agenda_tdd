from expects import expect, have_keys, be, have_properties, equal
from doublex import Spy, when
from doublex_expects import have_been_called_with

A_NAME = 'a_name'
A_SURNAME = 'a_surname'
A_PHONE_NUMBER = 'a_phone_number'
AN_EMAIL = 'an_email'

from sqlite_repository import SqliteRepository

with describe('Sqlite Repository'):
    with context('Storing a contact'):
        with it('save it to persistence'):
            repository = SqliteRepository()

            repository.put(A_NAME, A_SURNAME, A_PHONE_NUMBER, AN_EMAIL)

            contacts = repository.find_all()
            expect(len(contacts)).to(be(1))

    with context('Searching a contact by email'):
        with it('returns previous stored value'):
            repository = SqliteRepository()
            repository.put(A_NAME, A_SURNAME, A_PHONE_NUMBER, AN_EMAIL)

            contact = repository.find_by_email(AN_EMAIL)

            expect(contact).to(have_keys(name=A_NAME, surname=A_SURNAME, phone_number=A_PHONE_NUMBER, email=AN_EMAIL))
