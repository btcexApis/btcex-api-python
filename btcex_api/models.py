from pydantic import BaseModel


class JsonRpcRequestParams(BaseModel):
    id: str
    jsonrpc: str = '2.0'
    method: str
    params: dict
