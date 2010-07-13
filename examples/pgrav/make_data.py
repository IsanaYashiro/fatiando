import logging
logging.basicConfig()

import numpy
import pylab

from fatiando.data.gravity import TensorComponent
from fatiando.utils.geometry import Prism


x = numpy.arange(-500, 1550, 100, 'f')
y = numpy.arange(-500, 1550, 100, 'f')
X, Y = pylab.meshgrid(x, y)


prisma = Prism(dens=1000, x1=200, x2=800, y1=400, y2=600, z1=600, z2=800)

stddev = 0.05

# Create the data classes and generate synthetic data
zzdata = TensorComponent(component='zz')
zzdata.synthetic_prism(prisms=[prisma], X=X, Y=Y, z=-150, stddev=stddev, \
                       percent=False)
zzdata.dump("gzz_data.txt")

xxdata = TensorComponent(component='xx')
xxdata.synthetic_prism(prisms=[prisma], X=X, Y=Y, z=-150, stddev=stddev, \
                       percent=False)
xxdata.dump("gxx_data.txt")

yydata = TensorComponent(component='yy')
yydata.synthetic_prism(prisms=[prisma], X=X, Y=Y, z=-150, stddev=stddev, \
                       percent=False)
yydata.dump("gyy_data.txt")

xydata = TensorComponent(component='xy')
xydata.synthetic_prism(prisms=[prisma], X=X, Y=Y, z=-150, stddev=stddev, \
                       percent=False)
xydata.dump("gxy_data.txt")

xzdata = TensorComponent(component='xz')
xzdata.synthetic_prism(prisms=[prisma], X=X, Y=Y, z=-150, stddev=stddev, \
                       percent=False)
xzdata.dump("gxz_data.txt")

yzdata = TensorComponent(component='yz')
yzdata.synthetic_prism(prisms=[prisma], X=X, Y=Y, z=-150, stddev=stddev, \
                       percent=False)
yzdata.dump("gyz_data.txt")

# Make nice plots
pylab.figure()
pylab.title("Synthetic $g_{zz}$")
pylab.contourf(X, Y, zzdata.togrid(*X.shape), 30)
pylab.colorbar()

pylab.figure()
pylab.title("Synthetic $g_{xx}$")
pylab.contourf(Y, X, xxdata.togrid(*X.shape), 30)
pylab.colorbar()

pylab.figure()
pylab.title("Synthetic $g_{xy}$")
pylab.contourf(Y, X, xydata.togrid(*X.shape), 30)
pylab.colorbar()

pylab.figure()
pylab.title("Synthetic $g_{xz}$")
pylab.contourf(Y, X, xzdata.togrid(*X.shape), 30)
pylab.colorbar()

pylab.figure()
pylab.title("Synthetic $g_{yy}$")
pylab.contourf(Y, X, yydata.togrid(*X.shape), 30)
pylab.colorbar()

pylab.figure()
pylab.title("Synthetic $g_{yz}$")
pylab.contourf(Y, X, yzdata.togrid(*X.shape), 30)
pylab.colorbar()

pylab.show()