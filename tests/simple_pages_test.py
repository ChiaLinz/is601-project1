"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'Docker' in response.data
    assert b'Git' in response.data
    assert b'CI/CD' in response.data
    assert b'Python' in response.data
    assert b'OOP' in response.data
    assert b'AAA' in response.data
    assert b'OOP' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index" in response.data

def test_request_docker(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_git(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_cico(client):
    """This makes the index page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"CI / CD" in response.data

def test_request_python(client):
    """This makes the index page"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b"Python / Flask" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404

def test_request_oop(client):
    """This makes the index page"""
    response = client.get("/oop")
    assert response.status_code == 200
    assert b"OOP" in response.data

def test_request_aaa(client):
    """This makes the index page"""
    response = client.get("/aaa")
    assert response.status_code == 200
    assert b"AAA" in response.data
def test_request_cdemo(client):
    """This makes the index page"""
    response = client.get("/cdemo")
    assert response.status_code == 200
    assert b"OOP" in response.data