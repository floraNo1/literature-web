"""empty message

Revision ID: 3cb874948f8b
Revises: fb4cb4d910c8
Create Date: 2024-01-29 20:31:22.816406

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3cb874948f8b'
down_revision = 'fb4cb4d910c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('savedrecs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Times_Cited_All_Databases', sa.String(length=255), nullable=False))
        batch_op.alter_column('Author_Full_Names',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255),
               nullable=False)
        batch_op.alter_column('Document_Type',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255),
               nullable=False)
        batch_op.alter_column('Author_Keywords',
               existing_type=mysql.LONGTEXT(charset='utf8mb4', collation='utf8mb4_0900_ai_ci'),
               type_=sa.Text(),
               nullable=False)
        batch_op.alter_column('Keywords_Plus',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255),
               nullable=False)
        batch_op.alter_column('Abstract',
               existing_type=mysql.LONGTEXT(charset='utf8mb4', collation='utf8mb4_0900_ai_ci'),
               type_=sa.Text(),
               nullable=False)
        batch_op.alter_column('Email_Addresses',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255),
               nullable=False)
        batch_op.alter_column('Times_Cited_WoS_Core',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255),
               nullable=False)
        batch_op.drop_column('Times_Cited,_All_Databases')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('savedrecs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Times_Cited,_All_Databases', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255), nullable=True))
        batch_op.alter_column('Times_Cited_WoS_Core',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255),
               nullable=True)
        batch_op.alter_column('Email_Addresses',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255),
               nullable=True)
        batch_op.alter_column('Abstract',
               existing_type=sa.Text(),
               type_=mysql.LONGTEXT(charset='utf8mb4', collation='utf8mb4_0900_ai_ci'),
               nullable=True)
        batch_op.alter_column('Keywords_Plus',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255),
               nullable=True)
        batch_op.alter_column('Author_Keywords',
               existing_type=sa.Text(),
               type_=mysql.LONGTEXT(charset='utf8mb4', collation='utf8mb4_0900_ai_ci'),
               nullable=True)
        batch_op.alter_column('Document_Type',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255),
               nullable=True)
        batch_op.alter_column('Author_Full_Names',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255),
               nullable=True)
        batch_op.drop_column('Times_Cited_All_Databases')

    # ### end Alembic commands ###
