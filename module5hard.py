class User:

    def __init__(self, nickname, age, password):
        self.nickname = nickname
        self.age = age
        self.password = hash(password)

class Video:

    adult_mode = False
    time_now = 0

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class UrTube:
    
