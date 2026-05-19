from pydantic import BaseModel, ConfigDict


class PieceCreate(BaseModel):
    name: str
    category: str
    color: str | None = None
    image_url: str | None = None
    embedding: list[float] | None = None

    model_config = ConfigDict(from_attributes=True)