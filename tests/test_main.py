def test_one(main):
    print("Starting test one")
    assert main.get_db_url() is not None
