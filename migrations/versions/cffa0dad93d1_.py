"""empty message

Revision ID: cffa0dad93d1
Revises: ca4bb9050d4c
Create Date: 2023-01-04 01:27:41.195087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cffa0dad93d1'
down_revision = 'ca4bb9050d4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ticket', sa.Column('ticketCode', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ticket', 'ticketCode')
    # ### end Alembic commands ###
