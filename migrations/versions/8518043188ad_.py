"""empty message

Revision ID: 8518043188ad
Revises: 4dad6b3a1bcd
Create Date: 2024-11-21 02:02:40.532910

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8518043188ad'
down_revision: Union[str, None] = '4dad6b3a1bcd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('chat',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.Uuid(), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('text', sa.String(length=4096), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chat.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('post', sa.Column('comments', sa.Uuid(), nullable=True))
    op.create_foreign_key('post_comments_fkey', 'post', 'chat', ['comments'], ['id'])


def downgrade() -> None:
    op.drop_constraint('post_comments_fkey', 'post', type_='foreignkey')
    op.drop_column('post', 'comments')
    op.drop_table('comment')
    op.drop_table('chat')
