from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class PRWForm(FlaskForm):
    class Meta:
        csrf = False

    dtheta = StringField(
        label="Delta Theta [1.0 - 30.0]",
        default="4",
        validators=[DataRequired()],
    )
    nsteps = StringField(
        label="No. of steps [1 - 10]",
        default="5",
        validators=[DataRequired()],
    )

    def validate_dtheta(form, field):
        dtheta = 0.0
        try:
            dtheta = float(field.data)
        except ValueError:
            raise ValidationError("Invalid angle")

        if dtheta < 1 or dtheta > 30:
            raise ValidationError("Invalid angle")

    def validate_nsteps(form, field):
        if not field.data.isdigit():
            raise ValidationError("Invalid steps.")
        nsteps = int(field.data)
        if nsteps < 1 or nsteps > 10:
            raise ValidationError("Invalid steps")
