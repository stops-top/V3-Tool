# Automatically generated by pb2py
# fmt: off
import protobuf as p


class CipheredKeyValue(p.MessageType):
    MESSAGE_WIRE_TYPE = 48

    def __init__(
        self,
        value: bytes = None,
    ) -> None:
        self.value = value

    @classmethod
    def get_fields(cls):
        return {
            1: ('value', p.BytesType, 0),
        }
