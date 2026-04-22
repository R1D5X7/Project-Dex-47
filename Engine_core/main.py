from core.engine import engine, run_engine
from templates.basic_template import load_template

load_template(engine)
run_engine()

print("Final:", engine)
