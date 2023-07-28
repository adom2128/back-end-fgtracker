"""adds a date_fg_completed field

Revision ID: 0adfb95d726b
Revises: 84ef4e115f5e
Create Date: 2023-07-28 13:45:12.835804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0adfb95d726b'
down_revision = '84ef4e115f5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('survey', sa.Column('date_fg_completed', sa.Date(), nullable=True))
    op.add_column('survey', sa.Column('date_survey_completed', sa.Date(), nullable=False))
    op.drop_column('survey', 'date_completed')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('survey', sa.Column('date_completed', sa.DATE(), autoincrement=False, nullable=False))
    op.drop_column('survey', 'date_survey_completed')
    op.drop_column('survey', 'date_fg_completed')
    # ### end Alembic commands ###
