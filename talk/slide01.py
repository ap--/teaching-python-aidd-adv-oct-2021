"""
           ██████  ██    ██ ████████ ██   ██  ██████  ███    ██
           ██   ██  ██  ██     ██    ██   ██ ██    ██ ████   ██
           ██████    ████      ██    ███████ ██    ██ ██ ██  ██
           ██         ██       ██    ██   ██ ██    ██ ██  ██ ██
           ██         ██       ██    ██   ██  ██████  ██   ████
     █████  ██████  ██    ██  █████  ███    ██  ██████ ███████ ██████
    ██   ██ ██   ██ ██    ██ ██   ██ ████   ██ ██      ██      ██   ██
    ███████ ██   ██ ██    ██ ███████ ██ ██  ██ ██      █████   ██   ██
    ██   ██ ██   ██  ██  ██  ██   ██ ██  ██ ██ ██      ██      ██   ██
    ██   ██ ██████    ████   ██   ██ ██   ████  ██████ ███████ ██████

    ###### numpy, decorators, networking, and a few other things #####

                  Andreas Poehlmann --- 2021-10-21
"""



# === ME ==============================================================

from . import Degree, Career

__name__ = "Andreas Poehlmann"
__background__ = [
    Degree(field="Physics", type="MSc", specialization="Nonlinear Dynamics"),
    Degree(field="Behavioural Neuroscience", type="PhD", specialization="Visual System"),
    Career(job="Software Engineer"),
]
__position__ = "Research Engineer"
__group__ = "Machine Learning Research @ Bayer Pharmaceuticals Berlin"

__github__ = "www.github.com/ap--"



# === ORGANISATIONAL THINGS ===========================================

from . import Session
from datetime import date

session_info = {
    Session("today"): dict(
        date=date.today(),
        resources="https://github.com/ap--/teaching-python-aidd-adv-oct-2021",
    ),
    Session("Python Q&A"): dict(
        date=date(year=2021, month=10, day=26),
        resources="https://github.com/ap--/teaching-python-aidd-qa-oct-2021",
    )
}
