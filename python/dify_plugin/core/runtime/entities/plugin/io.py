from enum import Enum

from dify_plugin.core.server.__base.request_reader import RequestReader
from dify_plugin.core.server.__base.response_writer import ResponseWriter


class PluginInStream:
    class Event(Enum):
        Request = "request"
        BackwardInvocationResponse = "backwards_response"

        @classmethod
        def value_of(cls, v: str):
            for e in cls:
                if e.value == v:
                    return e
            raise ValueError(f"Invalid value for PluginInStream.Event: {v}")

    def __init__(
        self,
        session_id: str,
        event: Event,
        data: dict,
        reader: RequestReader,
        writer: ResponseWriter,
    ):
        self.session_id = session_id
        self.event = event
        self.data = data
        self.reader = reader
        self.writer = writer
