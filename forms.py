from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField
from wtforms.validators import InputRequired

class PlayerForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    position = StringField("Position", validators=[InputRequired()])
    nil_value = FloatField("NIL Value")
    depth = IntegerField("Depth Chart Position", default=1)  # 👈 new line
    team_id = IntegerField("Team ID", validators=[InputRequired()])


class TeamForm(FlaskForm):
    name = StringField("Team Name", validators=[InputRequired()])
