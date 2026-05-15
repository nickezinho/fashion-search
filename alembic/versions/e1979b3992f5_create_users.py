"""create users

Revision ID: e1979b3992f5
Revises: 2277af32ceeb
Create Date: 2026-05-14 16:00:20.649742

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1979b3992f5'
down_revision: Union[str, Sequence[str], None] = '2277af32ceeb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
