from pydantic import BaseModel, ConfigDict

class OutfitCreate(BaseModel):
    title: str
    description: str
    image_url: str | None = None
    embedding: list[float] | None = None

    model_config = ConfigDict(from_attributes=True)
    