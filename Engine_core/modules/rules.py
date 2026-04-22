def rule_module(engine):
    if engine["data"]["value"] >= 10:
        engine["state"] = "win"
