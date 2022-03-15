from bpskmod import bpskmod
from bpskdemod import bpskdemod

y = bpskmod(10, 4000, 80000)
y1 = bpskdemod(y, 4000, 80000)
