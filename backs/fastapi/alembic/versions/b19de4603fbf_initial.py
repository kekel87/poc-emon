"""initial

Revision ID: b19de4603fbf
Revises:
Create Date: 2021-10-29 16:02:48.636490

"""
import requests
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.

revision = "b19de4603fbf"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "pokemon",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column(
            "type_1",
            sa.Enum(
                "normal",
                "fire",
                "water",
                "grass",
                "flying",
                "fighting",
                "poison",
                "electric",
                "ground",
                "rock",
                "psychic",
                "ice",
                "bug",
                "ghost",
                "steel",
                "dragon",
                "dark",
                "fairy",
                name="type",
            ),
            nullable=False,
        ),
        sa.Column(
            "type_2",
            sa.Enum(
                "normal",
                "fire",
                "water",
                "grass",
                "flying",
                "fighting",
                "poison",
                "electric",
                "ground",
                "rock",
                "psychic",
                "ice",
                "bug",
                "ghost",
                "steel",
                "dragon",
                "dark",
                "fairy",
                name="type",
            ),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_pokemon_id"), "pokemon", ["id"], unique=False)
    op.create_table(
        "team",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("owner", sa.String(), nullable=False),
        sa.Column("pokemon_1", sa.Integer(), nullable=False),
        sa.Column("pokemon_2", sa.Integer(), nullable=True),
        sa.Column("pokemon_3", sa.Integer(), nullable=True),
        sa.Column("pokemon_4", sa.Integer(), nullable=True),
        sa.Column("pokemon_5", sa.Integer(), nullable=True),
        sa.Column("pokemon_6", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["pokemon_1"],
            ["pokemon.id"],
        ),
        sa.ForeignKeyConstraint(
            ["pokemon_2"],
            ["pokemon.id"],
        ),
        sa.ForeignKeyConstraint(
            ["pokemon_3"],
            ["pokemon.id"],
        ),
        sa.ForeignKeyConstraint(
            ["pokemon_4"],
            ["pokemon.id"],
        ),
        sa.ForeignKeyConstraint(
            ["pokemon_5"],
            ["pokemon.id"],
        ),
        sa.ForeignKeyConstraint(
            ["pokemon_6"],
            ["pokemon.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_team_id"), "team", ["id"], unique=False)
    # ### end Alembic commands ###

    seed()


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_team_id"), table_name="team")
    op.drop_table("team")
    op.drop_index(op.f("ix_pokemon_id"), table_name="pokemon")
    op.drop_table("pokemon")
    # ### end Alembic commands ###


def seed() -> None:
    url = "https://beta.pokeapi.co/graphql/v1beta"
    query = """
    query {
        pokemon_v2_pokemon(where: {is_default: {_eq: true}}) {
            species_id: pokemon_species_id
            name
            types: pokemon_v2_pokemontypes {
                pokemon_v2_type {
                    name
                }
            }
        }
    }
    """

    resp = requests.post(url=url, json={"query": query})

    pkms = []
    for raw in resp.json().get("data").get("pokemon_v2_pokemon"):
        types = raw.get("types")
        pkms.append(
            {
                "id": raw.get("species_id"),
                "name": raw.get("name"),
                "type_1": types[0].get("pokemon_v2_type").get("name"),
                "type_2": types[1].get("pokemon_v2_type").get("name")
                if len(types) == 2
                else None,
            }
        )

    meta = sa.MetaData(bind=op.get_bind())
    meta.reflect(only=("pokemon", "team"))
    op.bulk_insert(sa.Table("pokemon", meta), pkms)
