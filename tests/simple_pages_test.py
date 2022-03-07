"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/index")
    assert response.status_code == 308
    assert b'<a href="/about"><i class="fas fa-user-circle"></i><h3>About</h3></a>' in response.data
    assert b'<a href="/docker"><i class="fab fa-docker"></i><h3>Docker</h3></a>' in response.data
    assert b'<a href="/git"><i class="fab fa-github"></i><h3>Git</h3></a>' in response.data
    assert b'<a href="/cico"><i class="fas fa-sitemap" "></i><h3>CI/CO</h3></a>' in response.data
    assert b'<a href="/python"><i class="fab fa-python"></i><h3>Python</h3></a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/index")
    assert response.status_code == 200
    assert b"Index" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data

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
    response = client.get("/cico")
    assert response.status_code == 200
    assert b"CI / CO" in response.data

def test_request_python(client):
    """This makes the index page"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b"Python / Flask" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
