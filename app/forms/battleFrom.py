from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class BattleForm(FlaskForm):
    pokemon = StringField(
        "Choose your Pokémon:",
        filters=[lambda value: value.strip() if value else value],
        validators=[
            DataRequired(message="You must enter a Pokémon name.")
        ]
    )

    submit = SubmitField("Battle")