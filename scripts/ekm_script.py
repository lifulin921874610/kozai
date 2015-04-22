#! /usr/bin/env python

'''
ekm_script

Evolve TripleOctupole from the command line.
'''

def process_command_line(argv):
  '''Process the command line.'''
  
  if argv is None:
    argv = sys.argv[1:]

  # Configure the command line options
  parser = argparse.ArgumentParser()

  def_trip = Triple_octupole()
  parser.add_argument('-a', '--a1', dest='a1', type=float, 
    default=def_trip.a1, help = 
    'Inner semi-major axis in au [%g]' % def_trip.a1, metavar='\b')
  parser.add_argument('-b', '--a2', dest='a2', type=float, 
    default=def_trip.a2, help = 
    'Outer semi-major axis in au [%g]' % def_trip.a2, metavar='\b')
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
  parser.add_argument('-g', '--g1', dest='g1', type=float, 
    default=def_trip.omega, help = 
    'Inner argument of periapsis in degrees [%g]' % (def_trip.omega * 180 
      / np.pi), metavar='\b')
  parser.add_argument('-L', '--Omega', dest='Omega', type=float, 
    default=def_trip.Omega, help = 
    'Longitude of ascending node in degrees [%g]' % def_trip.Omega,
    metavar='\b')
  parser.add_argument('-t', '--end', dest='tstop', type=float, 
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
  parser.add_argument('--epsoct', dest='epsoct', type=float, help = 
    'Set epsilon_octupole parameter (override SMA and e2 settings)',
    metavar='\b')
  parser.add_argument('--phiq', dest='phiq', type=float, help =
    'Set the constant phi_q (override e1, g1, and Omega)', metavar='\b')
  parser.add_argument('--chi', dest='chi', type=float, help =
    'Set the constant chi (override e1, g1, and Omega)', metavar='\b')
  parser.add_argument('--algorithm', dest='algo', type=str,
    default=def_trip.integration_algo, help = 'Integration algorithm [%s]' 
    % def_trip.integration_algo)

  arguments = parser.parse_args()
  return arguments

def main(argv=None):
  args = process_command_line(argv)
  to = Triple_octupole(a1=args.a1, a2=args.a2, e1=args.e1, e2=args.e2, 
        inc=args.inc, argperi=args.g1, longascnode=args.Omega, 
        epsoct=args.epsoct, phiq=args.phiq, chi=args.chi, tstop=args.tstop,
        cputstop=args.cputstop, outfreq=args.outfreq, atol=args.atol, 
        rtol=args.rtol, integration_algo=args.algo)

  to.integrate()
  return 0

if __name__=='__main__':
  status = main()
  sys.exit(status)