"""added default value to date_fg_completed

Revision ID: 6b49e2fea470
Revises: 0adfb95d726b
Create Date: 2023-07-31 12:41:50.786512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b49e2fea470'
down_revision = '0adfb95d726b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('survey', 'date_fg_completed',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('survey', 'date_fg_completed',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###