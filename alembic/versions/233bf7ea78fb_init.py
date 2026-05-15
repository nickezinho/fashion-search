"""init

Revision ID: 233bf7ea78fb
Revises: e1979b3992f5
Create Date: 2026-05-14 16:02:04.143871

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '233bf7ea78fb'
down_revision: Union[str, Sequence[str], None] = 'e1979b3992f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
