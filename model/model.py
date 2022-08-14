from marshmallow import schema, EXCLUDE, post_load, fields
from dataclasses import dataclass


@dataclass
class Modelo:
    age: str = None
    num_viewers: int = None
    broadcaster_username: str = None
    broadcaster_gender: str = None
    room_status: str = None

    def to_json(self):
        return {"model": self.broadcaster_username, "age": self.age, "gender": self.broadcaster_gender,
                "status": self.room_status, "viewers": self.num_viewers}


class ModelSchema(schema.Schema):

    class Meta:
        unknown = EXCLUDE

    age = fields.Int(allow_none=True)
    num_viewers = fields.Int()
    broadcaster_username = fields.Str()
    broadcaster_gender = fields.Str()
    room_status = fields.Str()

    @post_load
    def make_model(self, data, **kwargs):

        return Modelo(**data)
