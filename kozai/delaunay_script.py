#! /usr/bin/env python

'''
Evolve a triple from the command line.
'''

def process_command_line(argv):
  '''Process the command line.'''
  
  if argv is None:
    argv = sys.argv[1:]

  # Configure the command line options
  parser = argparse.ArgumentParser()

  def_trip = Triple()
  parser.add_argument('-m', '--m1', dest='m1', type=float, 
    default=def_trip.m1, help = 
    'Mass of star 1 in inner binary in solar masses [%g]' % def_trip.m1,
    metavar='\b')
  parser.add_argument('-n', '--m2', dest='m2', type=float, 
    default=def_trip.m2, help = 
    'Mass of star 2 in inner binary in solar masses [%g]' % def_trip.m2,
    metavar='\b')
  parser.add_argument('-o', '--m3', dest='m3', type=float, 
    default=def_trip.m3, help = 
    'Mass of tertiary in solar masses [%g]' % def_trip.m3, metavar='\b')
  parser.add_argument('-r', '--r1', dest='r1', type=float, 
    default=def_trip.r1, help = 
    'Radius of star 1 of the inner binary in R_Sun [%g]' % def_trip.r1,
    metavar='\b')
  parser.add_argument('-s', '--r2', dest='r2', type=float, 
    default=def_trip.r2, help = 
    'Radius of star 2 of the inner binary in R_Sun [%g]' % def_trip.r2,
    metavar='\b')
  parser.add_argument('-a', '--a1', dest='a1', type=float, 
    default=def_trip.a1, help = 
    'Inner semi-major axis in au [%g]' % def_trip.a1, metavar='\b')
  parser.add_argument('-b', '--a2', dest='a2', type=float, 
    default=def_trip.a2, help = 
    'Outer semi-major axis in au [%g]' % def_trip.a2, metavar='\b')
  parser.add_argument('-g', '--g1', dest='g1', type=float, 
    default=def_trip.g1, help = 
    'Inner argument of periapsis in degrees [%g]' % def_trip.g1,
    metavar='\b')
  parser.add_argument('-G', '--g2', dest='g2', type=float, 
    default=def_trip.g2, help = 
    'Outer argument of periapsis in degrees [%g]' % def_trip.g2,
    metavar='\b')
  parser.add_argument('-e', '--e1', dest='e1', type=float, 
    default=def_trip.e1, help = 
    'Inner eccentricity [%g]' % def_trip.e1, metavar='\b')
  parser.add_argument('-f', '--e2', dest='e2', type=float, 
    default=def_trip.e2, help = 
    'Outer eccentricity [%g]' % def_trip.e2, metavar='\b')
  parser.add_argument('-i', '--inc', dest='inc', type=float,
    default=def_trip.inc, help = 
    'Inclination of the third body in degrees [%g]' % def_trip.inc,
    metavar='\b')
  parser.add_argument('-t', '--tstop', dest='tstop', type=float, 
    default=def_trip.tstop, help = 'Total time of integration in years [%g]' 
    % def_trip.tstop, metavar='\b')
  parser.add_argument('-C', '--cpu', dest='cputstop', type=float, 
    default=def_trip.cputstop, help = 
    'cpu time limit in seconds, if -1 then no limit [%g]' %
    def_trip.cputstop, metavar='\b')
  parser.add_argument('-F', '--freq', dest='outfreq', type=int, 
    default=def_trip.outfreq, help = 'Output frequency [%g]' % 
    def_trip.outfreq, metavar='\b')
  parser.add_argument('-A', '--abstol', dest='atol', type=float, 
    default=def_trip.atol, help = 'Absolute accuracy [%g]' % 
    def_trip.atol, metavar='\b')
  parser.add_argument('-R', '--reltol', dest='rtol', type=float, 
    default=def_trip.rtol, help = 'Relative accuracy [%g]' % 
    def_trip.rtol, metavar='\b')
  parser.add_argument('--noquad', dest='quad', action='store_false',
    default=def_trip.quadrupole, help = 'Turn off quadrupole terms')
  parser.add_argument('--nooct', dest='oct', action='store_false',
    default=def_trip.octupole, help = 'Turn off octupole terms')
  parser.add_argument('-c', '--GR', dest='gr', action='store_true', 
    default = def_trip.gr, help = 'Turn on general relativity terms')
  parser.add_argument('-x', '--hex', dest='hex', action='store_true',
    default = def_trip.hexadecapole, help = 'Turn on hexadecapole terms')

  arguments = parser.parse_args()
  return arguments

def main(argv=None):
  args = process_command_line(argv)
  t = Triple(m1=args.m1, m2=args.m2, m3=args.m3, r1=args.r1, r2=args.r2,
        a1=args.a1, a2=args.a2, argperi1=args.g1, argperi2=args.g2,
        e1=args.e1, e2=args.e2, inc=args.inc, tstop=args.tstop,
        cputstop=args.cputstop, outfreq=args.outfreq, atol=args.atol,
        rtol=args.rtol, quadrupole=args.quad, octupole=args.oct,
        hexadecapole=args.hex, gr=args.gr)

  t.integrate()
  return 0

if __name__=='__main__':
  status = main()
  sys.exit(status)
