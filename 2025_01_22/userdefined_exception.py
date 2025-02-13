class MyError(Exception):
    # def __init__(self, message):
    #     self.message = message
    #     super().__init__(self.message)
    print("This is a user-defined exception")

try:
    raise MyError()
except MyError as e:
    print(e)
