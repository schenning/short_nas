from skyfield.api import Topos, load, EarthSatellite
import matplotlib.pyplot as plt

# Load the TLE data
tle_line1 = "1 45135U 20008E   21029.25001157 -.00041413  00000-0 -11917+0 0  9996"
tle_line2 = "2 45135  87.8779  66.9060 0002236  85.5430 253.6085 13.10391727 51763"

ts = load.timescale()
satellite = EarthSatellite(tle_line1, tle_line2)

# Set up an observer location (e.g., a ground station)
observer = Topos(78.123, 15.123)

# Calculate the satellite's position at regular intervals
minutes = range(0, 1440, 5)  # for a day, every 5 minutes
times = ts.utc(2021, 1, 29, 0, minutes)
positions = observer.at(times).observe(satellite)

# Extract altitude and azimuth for plotting
altitudes, azimuths, distances = positions.apparent().altaz()

# Plot the ground track
plt.subplot(2, 1, 1)
plt.plot(minutes, altitudes.degrees)
plt.title('Altitude vs Time')
plt.xlabel('Time (minutes)')
plt.ylabel('Altitude (degrees)')

plt.subplot(2, 1, 2)
plt.plot(minutes, azimuths.degrees)
plt.title('Azimuth vs Time')
plt.xlabel('Time (minutes)')
plt.ylabel('Azimuth (degrees)')

plt.tight_layout()
plt.show()