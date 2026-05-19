from core.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import Enum as SqlEnum
from enum import Enum
from sqlalchemy.orm import relationship

class Piece(Base):
    __tablename__ = "pieces"



    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    color = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    outfits = relationship(
        "Outfit", 
        secondary="outfit_pieces", 
        back_populates="pieces"
        )

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


class PiecePosition(Enum):
    TOP = "top"
    BOTTOM = "bottom"
    FOOTWEAR = "footwear"
    ACCESSORY = "accessory"


class OutfitPiece(Base):
    __tablename__ = "outfit_pieces"

    id = Column(Integer, primary_key=True, index=True)
    outfit_id = Column(Integer, ForeignKey("outfits.id"), nullable=False)
    piece_id = Column(Integer, ForeignKey("pieces.id"), nullable=False)

    position = Column(SqlEnum(PiecePosition), nullable=False)
    order_index = Column(Integer, nullable=False)

    outfit = relationship(
        "Outfit", 
        back_populates="pieces"
        )
    
    piece = relationship(
        "Piece", 
        back_populates="outfits"
        )
