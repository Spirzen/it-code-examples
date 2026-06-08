class RegistryMeta(type):
    registry = {}
    
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if name != 'BasePlugin':
            RegistryMeta.registry[name] = cls
        return cls

class BasePlugin(metaclass=RegistryMeta):
    pass

class PluginA(BasePlugin):
    pass

class PluginB(BasePlugin):
    pass

print(RegistryMeta.registry)  # {'PluginA': <class '__main__.PluginA'>, 'PluginB': <class '__main__.PluginB'>}
