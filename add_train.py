import os, sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

from lib.record import Record
from lib.training import Training
from lib.trainings.run import Run