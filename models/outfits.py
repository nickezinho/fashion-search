from core.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Outfit(Base):
    __tablename__ = "outfits"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    embedding = Column(String, nullable=True)
    pieces = relationship(
        "Piece", 
        secondary="outfit_pieces", 
        back_populates="outfits"
        )
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


