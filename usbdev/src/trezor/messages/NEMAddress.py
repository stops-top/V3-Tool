# Automatically generated by pb2py
# fmt: off
import protobuf as p


class NEMAddress(p.MessageType):
    MESSAGE_WIRE_TYPE = 68

    def __init__(
        self,
        address: str = None,
    ) -> None:
        self.address = address

    @classmethod
    def get_fields(cls):
        return {
            1: ('address', p.UnicodeType, 0),  # required
        }
