"""empty message

Revision ID: 3b2735b3ccc8
Revises: 
Create Date: 2023-08-07 10:21:57.863999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b2735b3ccc8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('survey',
    sa.Column('survey_id', sa.Integer(), nullable=False),
    sa.Column('company', sa.String(length=100), nullable=False),
    sa.Column('topic', sa.String(length=100), nullable=False),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.Column('date_survey_completed', sa.DateTime(), nullable=False),
    sa.Column('payment', sa.Numeric(), nullable=False),
    sa.Column('stage', sa.String(length=100), nullable=False),
    sa.Column('date_fg_completed', sa.DateTime(), nullable=True),
    sa.Column('payment_received', sa.Boolean(), nullable=False),
    sa.Column('payment_expiration_date', sa.DateTime(), nullable=True),
    sa.Column('payment_left', sa.Numeric(), nullable=True),
    sa.PrimaryKeyConstraint('survey_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('survey')
    # ### end Alembic commands ###