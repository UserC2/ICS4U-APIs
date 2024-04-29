import math

class Vector:
    """A vector with a magnitude and angle (in degrees)."""

    def __init__(self, mag, degrees):
        self.mag = mag
        self.degrees = degrees
    
    def from_rect(self, rect):
        self.mag = math.sqrt(math.pow(rect[0], 2) + math.pow(rect[1], 2))
        self.degrees = math.degrees(math.atan2(rect[1], rect[0]))
        return self
    
    def as_rect(self):
        """Returns this vector as a tuple with cartesian coordinates."""
        radians = math.radians(self.degrees)
        x = self.mag * math.cos(radians)
        y = self.mag * math.sin(radians)
        return [x, y]
    
    def as_plotable(self):
        """
        Returns a vector with a modified angle so that it will convert to
        cartesian coordinates correctly if it was created with a compass
        heading instead of a polar angle.
        """
        degrees = (450 - self.degrees) % 360
        return Vector(self.mag, degrees)
    
    def add(self, other):
        """Add two vectors."""
        v1 = self.as_rect()
        v2 = other.as_rect()
        return Vector(0, 0).from_rect([v1[0] + v2[0], v1[1] + v2[1]])