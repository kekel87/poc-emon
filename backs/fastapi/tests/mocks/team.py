from src.schemas.team import Team, TeamSave

base = Team(id=1, name="Team base", owner="Owner", pokemon_1=1)
save = TeamSave(name="Team save", owner="New owner", pokemon_1=1, pokemon_2=1)

db = base.dict()
