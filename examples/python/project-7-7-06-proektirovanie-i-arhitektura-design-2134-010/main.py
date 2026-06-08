
import dns.resolver

class ResilientResolver:
    def __init__(self):
        self.resolvers = [
            dns.resolver.Resolver(configure=False),
            dns.resolver.Resolver(configure=False),
        ]
        # Публичные DNS-серверы
        self.resolvers[0].nameservers = ['8.8.8.8', '8.8.4.4']
        self.resolvers[1].nameservers = ['1.1.1.1', '1.0.0.1']
        self.resolvers[0].timeout = 2.0
        self.resolvers[1].timeout = 2.0
    
    def resolve(self, hostname):
        """Попытка разрешения через несколько серверов."""
        for resolver in self.resolvers:
            try:
                answers = resolver.resolve(hostname, 'A')
                return [rdata.address for rdata in answers]
            except Exception:
                continue
        raise ResolutionFailed(f"Не удалось разрешить {hostname}")
