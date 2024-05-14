"""added patient tables

Revision ID: 3b30c89b283b
Revises: b07680fed333
Create Date: 2024-03-22 11:57:53.599996

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '3b30c89b283b'
down_revision = 'b07680fed333'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient', sa.Column('is_super_user', sa.Boolean(), nullable=False))
    op.add_column('user', sa.Column('is_super_user', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_super_user')
    op.drop_column('patient', 'is_super_user')
    # ### end Alembic commands ###