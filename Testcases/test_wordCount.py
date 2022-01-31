from WordCount import word_Count

def test_WordCount():
    out = word_Count("hello how are you?")
    assert out  == len("hello how are you?".split(" "))