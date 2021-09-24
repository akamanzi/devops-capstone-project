import pytest
from app import app as flask_app
from flask import template_rendered
@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

def test_home_page(app, client):
  response = client.get('/')
  assert response.status_code == 200
  assert response.content_type == 'text/html; charset=utf-8'

def test_render_template(client, captured_templates):
  response = client.get("/")
  assert len(captured_templates) == 1
  assert response.status_code == 200
  template, context = captured_templates[0]
  assert template.name == "index.html"