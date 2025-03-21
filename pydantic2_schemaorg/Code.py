from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Code(CreativeWork):
    """Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts,
     templates.

    See: https://schema.org/Code
    Model depth: 3
    """

    type_: str = Field(default="Code", alias="@type", const=True)
