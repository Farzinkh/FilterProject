from IPython.display import display
import matplotlib.pyplot as plt
from sympy import symbols
from scipy import signal
import numpy as np
s=symbols("s")

def eliptic(n=5,rp=1,rs=10,wn=3911.5,btype='lowpass'):
    """ normal eliptic designer

    Args:
        n (int, optional): order_of_the_filter. Defaults to 5.
        rp (int, optional): The maximum ripple allowed below unity gain in the passband. Defaults to 1.
        rs (int, optional): The minimum attenuation required in the stop band. Defaults to 10.
        wn (float, optional): critical frequencies. Defaults to 3911.5.
        btype (str, optional): {‘lowpass’, ‘highpass’, ‘bandpass’, ‘bandstop’}. Defaults to 'low'.
    Returns:
        sympy functions: Numerator, denominator        
    """
    Numerator, denominator= signal.ellip(n, rp, rs,wn,btype, analog=True)

    denominator_ = sum(co*s**i for i, co in enumerate(reversed(denominator)))
    Numerator_ = sum(co*s**i for i, co in enumerate(reversed(Numerator))) 
    print("transfer function :")
    display(Numerator_ /denominator_)
    Zeros,poles,system_gain=signal.ellip(n, rp, rs,wn, 'low', analog=True,output='zpk')
    print("\n Zeros :",Zeros,"\n","Poles :",poles,"\n","Gain :",system_gain)

    wz, mag, phase =signal.bode((Numerator, denominator))
    fig = plt.figure(figsize=(12, 6))
    ax=fig.add_subplot(121)
    ax.semilogx(wz, mag)    # Bode magnitude plot
    plt.xscale('log')
    plt.title('Elliptic filter frequency response rs='+str(rs)+" rp="+str(rp))
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Magnitude [dB]')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.axvline(wn, color='red') # cutoff frequency
    plt.axhline(-1*rs, color='red') # rs
    plt.axhline(-1*rp, color='red') # rp

    ax2=fig.add_subplot(122)
    ax2.semilogx(wz, phase)  # Bode phase plot
    plt.xscale('log')
    plt.title('Elliptic filter frequency response rs='+str(rs)+" rp="+str(rp))
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Phase radians')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.axvline(wn, color='red') # cutoff frequency
    plt.show(block=False)
    return Numerator_, denominator_

def reversechebishev(n=5 ,rs=10,stopband=(3700,4000),btype="bandpass"):
    """ reverse chebishev designer

    Args:
        n (int, optional): order_of_the_filter. Defaults to 5.
        rs (int, optional): minimum attenuation required in the stop band. Defaults to 10.
        stopband (tuple, optional): stopband frequencies. Defaults to (3700,4000).
        btype (str, optional): {‘lowpass’, ‘highpass’, ‘bandpass’, ‘bandstop’}. Defaults to "bandpass".
    Returns:
        sympy functions: Numerator, denominator    
    """

    Numerator, denominator= signal.cheby2(n, rs, stopband, btype, analog=True)

    denominator_ = sum(co*s**i for i, co in enumerate(reversed(denominator)))
    Numerator_ = sum(co*s**i for i, co in enumerate(reversed(Numerator))) 
    print("transfer function :")
    display(Numerator_ /denominator_)
    Zeros,poles,system_gain=signal.cheby2(n, rs, stopband, 'bandstop', analog=True,output='zpk')
    print("\n Zeros :",Zeros,"\n","Poles :",poles,"\n","Gain :",system_gain)

    wz, mag, phase =signal.bode((Numerator, denominator))
    fig = plt.figure(figsize=(12, 6))
    ax=fig.add_subplot(121)
    ax.semilogx(wz, mag)    # Bode magnitude plot
    plt.xscale('log')
    plt.title('Chebyshev Type II magnitude response (rp=0.5)')
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Magnitude [dB]')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.axvline(np.sqrt(stopband[0]*stopband[1]), color='red') # cutoff frequency
    plt.axhline(-1*rs, color='red') # rp

    ax2=fig.add_subplot(122)
    ax2.semilogx(wz, phase)  # Bode phase plot
    plt.xscale('log')
    plt.title('Chebyshev Type II Phase response (rp=0.5)')
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Phase radians')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.axvline(np.sqrt(stopband[0]*stopband[1]), color='red') # cutoff frequency
    plt.axhline(-1*rs, color='red') # rp
    plt.show(block=False)
    return Numerator_, denominator_

def chebishev(n=5,ps=1,stopband=(3700,4000),btype='bandstop'):
    """ normal chebishev designer

    Args:
        n (int, optional): order_of_the_filter. Defaults to 5.
        ps (int, optional): The maximum ripple allowed below unity gain in the passband. Defaults to 1.
        stopband (tuple, optional): stopband domain. Defaults to (3700,4000).
        btype (str, optional): {‘lowpass’, ‘highpass’, ‘bandpass’, ‘bandstop’}. Defaults to 'bandstop'.

    Returns:
        sympy functions: Numerator, denominator
    """
    Numerator, denominator = signal.cheby1(n, ps, stopband, btype, analog=True)
    denominator_ = sum(co*s**i for i, co in enumerate(reversed(denominator)))
    Numerator_ = sum(co*s**i for i, co in enumerate(reversed(Numerator))) 
    print("transfer function :")
    display(Numerator_ /denominator_)
    Zeros,poles,system_gain=signal.cheby1(n, ps, stopband, btype, analog=True,output='zpk')
    print("\n Zeros :",Zeros,"\n","Poles :",poles,"\n","Gain :",system_gain)
    #w, h = signal.freqs(Numerator, denominator)

    wz, mag, phase =signal.bode((Numerator, denominator))
    fig = plt.figure(figsize=(12, 6))
    ax=fig.add_subplot(121)
    ax.semilogx(wz, mag)    # Bode magnitude plot
    plt.xscale('log')
    plt.title('Chebyshev Type I magnitude response (rp=0.5)')
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Magnitude [dB]')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.axvline(np.sqrt(stopband[0]*stopband[1]), color='red') # cutoff frequency
    plt.axhline(-1*ps, color='red') # rp

    ax2=fig.add_subplot(122)
    ax2.semilogx(wz, phase)  # Bode phase plot
    plt.xscale('log')
    plt.title('Chebyshev Type I Phase response (rp=0.5)')
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Phase radians')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.axvline(np.sqrt(stopband[0]*stopband[1]), color='red') # cutoff frequency
    plt.axhline(-1*ps, color='red') # rp
    plt.show(block=False)
    return Numerator_, denominator_

def butterworthandbessel(n=4, wn=100, btype='lowpass'):
    """ butterworth and bessel on same plot

    Args:
        n (int, optional): [description]. Defaults to 4.
        wn (int, optional): The critical frequency. Defaults to 100.
        n (int, optional): order_of_the_filter. Defaults to 5.
        ps (int, optional): The maximum ripple allowed below unity gain in the passband. Defaults to 1.
        btype (str, optional): {‘lowpass’, ‘highpass’, ‘bandpass’, ‘bandstop’}. Defaults to 'bandstop'.

    Returns:
        sympy functions: butterNumerator, butterdenominator ,besselNumerator, besseldenominator
    """
    fig = plt.figure(figsize=(12, 6))
    ax=fig.add_subplot(121)
    butterNumerator, butterdenominator= signal.butter(n, wn,btype, analog=True)
    w1, h1 = signal.freqs(butterNumerator, butterdenominator)
    plt.semilogx(w1, 20 * np.log10(np.abs(h1)), color='silver', ls='dashed')
    besselNumerator, besseldenominator= signal.bessel(n,wn,btype, analog=True, norm='phase')
    w2, h2 = signal.freqs(besselNumerator, besseldenominator)
    ax.semilogx(w2, 20 * np.log10(np.abs(h2)))
    plt.title('Bessel filter magnitude response (with Butterworth)')
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Amplitude [dB]')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.axvline(wn, color='red')  # cutoff frequency
    plt.axhline(-n, color='red')  # -3 dB magnitude

    ax2=fig.add_subplot(122)
    ax2.semilogx(w1, np.unwrap(np.angle(h1)), color='silver', ls='dashed')
    ax2.semilogx(w2, np.unwrap(np.angle(h2)))
    plt.axvline(wn, color='red')  # cutoff frequency
    plt.axhline(-np.pi, color='red')  # phase midpoint
    plt.title('Bessel filter phase response (with Butterworth)')
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Phase [radians]')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.legend(["Butterworth", "Bessel/Thomson"], loc ="lower right") 
    plt.show()

    return butterNumerator, butterdenominator ,besselNumerator, besseldenominator
      