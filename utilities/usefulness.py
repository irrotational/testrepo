class thing:
    def __init__(self,name):
        self.name = name

    def say_hi(self,your_name):
        print( "Hi, my name is %s, and your name is %s" % (self.name,your_name) )

    def __repr__(self):
        repr_str = "'thing' instance, with name : %s" % self.name
        return repr_str

class bigthing(thing):
    def __init__(self,name,bigname):
        thing.__init__(self,name)
        self.bigname = bigname

    def say_hi(self,your_name):
        print( "Hi %s, I am a bigthing, my name is %s, and my bigname is %s" % (your_name,self.name,self.bigname) )