# statement init yang akan otomatis menginisiasikan dan menjalankan modules agar dpt dipanggil secara singkat
from . import fisika
from . import adv_calc
from . import calcnums
from . import circle
from . import parabola

from .adv_calc import square, floor_division, modulus
from .calcnums import plus, minus, times, divide
from .fisika import resistant1, resistant2, pressure, weight, force
from .circle import circle
from .parabola import paraEquation
