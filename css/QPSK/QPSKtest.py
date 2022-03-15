from qpskmod import qpskmod
from qpskdemod import qpskdemod

y = qpskmod(100, 10, 100)
y1 = qpskdemod(y, 10, 100)
