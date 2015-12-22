class Retweet(object):
    text = ""
    id = 0
    retweet_count = 0
    user_name = ""
    
    def __init__(self, text, id, retweet_count, user_name):
        self.text = text
        self.id = id
        self.retweet_count = retweet_count
        self.user_name = user_name