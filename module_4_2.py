def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()
# inner_function нельзя вызвать, потому что она находится в пространстве имен test_function