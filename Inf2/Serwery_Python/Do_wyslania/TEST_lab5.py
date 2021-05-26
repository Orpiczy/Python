print("       trapz {:.8f}  {:.20f}".format(sum([elem.total_seconds() for key, elem in t_intY_trapz.items()]), intY_trapz[2**19+1], '\n'))
