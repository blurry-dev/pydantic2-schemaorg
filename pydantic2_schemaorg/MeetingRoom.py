from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Room import Room


class MeetingRoom(Room):
    """A meeting room, conference room, or conference hall is a room provided for singular events such as business
     conferences and meetings (source: Wikipedia, the free encyclopedia, see <a href=\"http://en.wikipedia.org/wiki/Conference_hall\">http://en.wikipedia.org/wiki/Conference_hall</a>).
     <br /><br /> See also the <a href=\"/docs/hotels.html\">dedicated document on the use of schema.org for
     marking up hotels and other forms of accommodations</a>.

    See: https://schema.org/MeetingRoom
    Model depth: 5
    """

    type_: str = Field(default="MeetingRoom", alias="@type", const=True)
