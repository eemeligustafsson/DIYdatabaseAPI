from extensions import db

instruction_list = []


def get_last_id():
    if instruction_list:
        last_instruction = instruction_list[-1]
    else:
        return 1
    return last_instruction.id + 1


class Instruction(db.Model):
    __tablename__ = 'instruction'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    steps = db.Column(db.Integer)
    tools = db.Column(db.String(50))
    cost = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))