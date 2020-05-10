"""empty message

Revision ID: 300055eedf98
Revises: 1bea066b60a8
Create Date: 2020-05-09 20:34:02.463254

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '300055eedf98'
down_revision = '1bea066b60a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    op.alter_column('blogposts', 'category',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('blogposts_category_fkey', 'blogposts', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('blogposts_category_fkey', 'blogposts', 'categories', ['category'], ['id'])
    op.alter_column('blogposts', 'category',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_table('categories',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='categories_pkey')
    )
    # ### end Alembic commands ###