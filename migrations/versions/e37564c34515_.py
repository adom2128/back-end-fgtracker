"""empty message

Revision ID: e37564c34515
Revises: c3a2017ba24f
Create Date: 2023-08-01 10:06:17.564435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e37564c34515'
down_revision = 'c3a2017ba24f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('survey', 'testing')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('survey', sa.Column('testing', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
