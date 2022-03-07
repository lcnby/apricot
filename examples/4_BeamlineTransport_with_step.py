import apricot.BeamlineComponents as blc
import apricot.Beamline as bl
import apricot.Functions as fn
import apricot.Outputs as out

ParticleTpye = "electron"   # particle type
NumberOfParticles = 10000   # number of particle
BeamEnergy = 250e3          # beam energy keV
x_rms = 0.003               # sigma_x    m  
y_rms = 0.003               # sigma_y    m  
Emittance_x = 1e-6          # emittance x m.rad
Emittance_y = 1e-6          # emittance y m.rad
Alpha_x = -0.50             # alpha x unitless
Alpha_y = -0.50             # alpha y unitless

# Random beam generation
Beam = fn.RandomBeam( ParticleTpye, NumberOfParticles, BeamEnergy, x_rms, y_rms, Emittance_x, Emittance_y, Alpha_x, Alpha_y  )
# Creating beam graphs
out.getBeam( Beam, path="outputs", tag="Initial" )

# Createing a Drift Tube with a length of 0.2 m
drift = blc.DriftTube("drift",0.2)
# Creating a Quadrupole Magnet with a length of 0.5 m and a power of 0.4
quad = blc.QuadrupoleMagnet("quadrupole",0.5,0.4)
# Creating beamline
beamline = bl.Beamline( "beamline", [drift,quad,drift] )

# Running beam on beamline
fn.TransportBeam( Beam, beamline.Elements, 0.1 )
# Generating the outputs
out.getBeam( Beam, path="outputs", tag="Final" )
out.getBeamPositions( Beam, beamline.Elements, path="outputs/", tag="Final" )