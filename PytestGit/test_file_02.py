class TestClass:
    def test_one(self):
        x = "this"
        y="this"
        if x==y:
            print(False)
        assert True

    def test_two(self):
        x = "hello"
        y="hello"
        if x==y:
            print(False)
        assert True

    def test_sum(self):
        x=10
        y=20
        if x==y:
          assert False
        else:
            assert True