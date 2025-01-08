from pydantic.v1 import PydanticValueError


class ISO8601DateError(PydanticValueError):
    code = "ISO9801"


class ISO8601DateInvalid(PydanticValueError):
    code = "ISO9801 invalid date"
