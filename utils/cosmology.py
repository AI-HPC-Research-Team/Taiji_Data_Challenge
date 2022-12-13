import math
import scipy
from constant import Constant


class Cosmology(object):
    @staticmethod
    def H(zp, w):
        fn = 1. / (Constant.H0 *
                   math.sqrt(Constant.Omegam * math.pow(1. + zp, 3.) + Constant.Omegalam * math.pow(1. + zp, 3. * w)))
        return (fn)

    @staticmethod
    def DL(zup, w):
        '''
        Usage: DL(3,w=0)[0]
        '''
        pd = scipy.integrate.quad(Cosmology.H, 0., zup, args=(w))[0]
        res = (1. + zup) * pd     # in Mpc
        return res * Constant.C_SI * 1.e-3, pd * Constant.C_SI * 1.e-3