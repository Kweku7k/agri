"""empty message

Revision ID: 9fc257a78d03
Revises: 6056596193a8
Create Date: 2023-01-02 16:22:12.239667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fc257a78d03'
down_revision = '6056596193a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('cost', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event', 'cost')
    # ### end Alembic commands ###
