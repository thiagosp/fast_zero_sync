from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero_api.app import app


def test_read_root():
    client = TestClient(app)  # Arrange (Organização do teste)
    response = client.get('/')  # Act (Ação)
    assert response.status_code == HTTPStatus.OK # Assert / Afirmativo
    assert response.json() == 'Estou na raiz, teste swagger/' #Assert Afirmativo

#GIT - comando git init .
# Inicia um versionamento desse projeto / REepositório vazio