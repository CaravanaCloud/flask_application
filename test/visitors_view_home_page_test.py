from ward import test, fixture
from app import create_app
from flask import url_for


@fixture
def test_client():
    app = create_app()
    app.testing = True
    app_contenxt = app.test_request_context()
    app_contenxt.push()

    return app.test_client()

@test("visitante visita a página inicial e encontra a mensagem olá caravana")
def _(client=test_client):
    response = client.get(url_for("home.index"))
    
    assert "Olá, Caravana!" in response.get_data(as_text=True)

@test("visitante ver página sobre o projeto")
def _(client=test_client):
    response = client.get(url_for("home.about"))
    
    assert "about" in response.get_data(as_text=True)