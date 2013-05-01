
class guard(object):
    def __init__(self, fn):
        self.default = fn
        self.guards = []                
        self.rpredicates = {}
        
    def register_predicate(self, fn, prefix = "when_"):
        def when(*args, **kwargs):
            return self.fire_when(fn(*args,**kwargs))                            
        self.__dict__[ prefix + fn.__name__  ] = when
    
    def fire_when(self, pred):
        def newfn(fn):
            self.guards.append( (pred, fn))
            return fn
        return newfn
        
    
    def __call__(self, *args, **kwargs):
        for pred, fn in self.guards:
            if pred(*args, **kwargs):
                return  fn(*args,**kwargs)
        return self.default(*args, **kwargs)
    



def AND(*fn):   
    
    def newfn(*args, **kwargs):
        call = lambda x: x(*args, **kwargs)
        return all(map(call, fn))
    return newfn

def OR(*fn):   
    def newfn(*args, **kwargs):        
        call = lambda x: x(*args, **kwargs)
        return any(map(call, fn))
    return newfn
    
def EQUIV(fn1, fn2):   
    def fn(*args, **kwargs):
        return fn1(*args, **kwargs) == fn2(*args, **kwargs) 
    return fn
    
def NOT(pred):
    return lambda *args, **kwargs: not pred(*args,**kwargs)
    
    
def endswith_p(sfx):
    return lambda x: x.endswith(sfx)
    
@guard
def d(s):
    return "default_function"
  
d.register_predicate(endswith_p)  

@d.fire_when(AND( endswith_p("pdf"), endswith_p("f")))
def q(s):      
    return "pdf"


@d.fire_when(OR(endswith_p("txt"), endswith_p("md")))
def r(s):      
    return "txt"

@d.when_endswith_p("abc")
def r(s):      
    return "abc"
        
#print(d("abc.pdf"))
#print(d("abc.txt")) 
#print(d("abc.md"))
#print(d("abc.abc"))
    