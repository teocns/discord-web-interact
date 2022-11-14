



class ContextsManager(object):
    


    contexts = {}
    
    def register(self, context):
        self.contexts[context] = context


    

    def register_many(self, cls, *args):
        for arg in args:
            self.register(cls(arg))