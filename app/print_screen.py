from dataclasses import dataclass

@dataclass
class Proxy:
    ip: str
    port: int
    country: str
    speed: int

    def __str__(self) -> str:
        return (f"IP               : {self.ip}\n"
                f"PORT             : {self.port}\n"
                f"COUNTRY          : {self.country}\n"
                f"CONNECTION SPEED : {self.speed} ms")