from modules.update import update_module
from modules.rules import rule_module

def load_template(engine):
    engine["data"] = {
        "value": 0
    }

    engine["modules"] = [
        update_module,
        rule_module
    ]
