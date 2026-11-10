from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import Optional

class PokemonFilterForm(FlaskForm):
    pokemon = StringField(
        "Filter by name:",
        filters=[lambda value: value.strip() if value else value],
        validators=[Optional()]
    )

    type = SelectField(
        "Filter by type:",
        choices=[],
        validators=[Optional()]
    )

    submit = SubmitField("Filter")