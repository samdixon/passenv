import passenv.api

c = passenv.api.Create('test-name', '1', 'project-name', 'onepassword')

def test_create():
    print("Testing Create")
    print("--------------")
    assert c.name == 'test-name'
    assert c.key == '1'
    assert c.project == 'project-name'
    assert c.password_manager == 'onepassword'
