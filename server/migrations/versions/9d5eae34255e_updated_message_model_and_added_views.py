"""updated message model and added views

Revision ID: 9d5eae34255e
Revises: 18f4aa33d3e8
Create Date: 2024-12-03 18:02:46.332213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d5eae34255e'
down_revision = '18f4aa33d3e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('body', sa.String(), nullable=True))
    op.add_column('messages', sa.Column('username', sa.String(), nullable=True))
    op.add_column('messages', sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    op.add_column('messages', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'updated_at')
    op.drop_column('messages', 'created_at')
    op.drop_column('messages', 'username')
    op.drop_column('messages', 'body')
    # ### end Alembic commands ###
