import zope.interface
  
  
class MyInterface(zope.interface.Interface):
    x = zope.interface.Attribute("foo")
    def method1(self, x):
        pass
    def method2(self):
        pass
      
print(type(MyInterface))
print(MyInterface.__module__)
print(MyInterface.__name__)
  
# get attribute
x = MyInterface['x']
print(x)
print(type(x))