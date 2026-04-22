engine = {
    "state": "running",
    "modules": [],
    "data": {}
}

def run_engine():
    while engine["state"] == "running":
        for module in engine["modules"]:
            module(engine)
