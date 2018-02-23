import json
import pytest
from aiohttp import web
from agenda_create_action import AgendaCreateAction
from agenda_service import AgendaService
from sqlite_repository import SqliteRepository

A_NAME = 'a_name'
A_SURNAME = 'a_surname'
A_PHONE_NUMBER = 'a_phone_number'
AN_EMAIL = 'an_email'


def create_action_factory():
    repository = SqliteRepository()
    agenda_service = AgendaService(repository)
    return AgendaCreateAction(agenda_service)

async def post_agenda_handler(request):
    data = (await request.post())
    create_action = create_action_factory()
    contact = create_action.execute(data)
    return web.json_response(contact)

def create_app():
    app = web.Application()
    app.router.add_post('/agenda', post_agenda_handler)
    return app

@pytest.fixture
def cli(loop, aiohttp_client):
    app = create_app()
    return loop.run_until_complete(aiohttp_client(app))

async def test_creating_agenda_returns_ok_and_object(cli):
    resp = await cli.post('/agenda',
                          data={'name': A_NAME,
                                'surname': A_SURNAME,
                                'phone_number': A_PHONE_NUMBER,
                                'email': AN_EMAIL
                                })
    assert resp.status == 200
    # assert await resp.text() == 'thanks for the data'
    # assert cli.server.app['value'] == 'foo'
