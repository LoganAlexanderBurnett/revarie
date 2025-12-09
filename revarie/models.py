import numpy as np

def spherical(h, nug, sill, rang):
    variogram = nug + (sill - nug)*np.piecewise(h, [h <= rang,  h > rang],[lambda h: 1.5*(h/rang)-0.5*(h/rang)**3,1])
    return variogram

def exponential(h, nug, sill, rang):
    variogram = nug + (sill - nug)*(1.-np.exp(-3*h/rang))
    return variogram

def gaussian(h, nug, sill, rang):
    variogram =  nug + (sill - nug)*(1.-np.exp(-(2*h/rang)**2))
    return variogram

def kernel_matern32(h, sigma2, ell):
    r = np.sqrt(3.0) * h / ell
    return sigma2 * (1.0 + r) * np.exp(-r)

def kernel_matern52(h, sigma2, ell):
    r = np.sqrt(5.0) * h / ell
    return sigma2 * (1.0 + r + r**2 / 3.0) * np.exp(-r)

mtags = {"sph" : spherical,
        "exp" : exponential,
        "gaus" : gaussian
	"mat32": matern32
	"mat52": matern52
	}
