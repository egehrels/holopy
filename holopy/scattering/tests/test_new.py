# Copyright 2011-2016, Vinothan N. Manoharan, Thomas G. Dimiduk,
# Rebecca W. Perry, Jerome Fung, and Ryan McGorty, Anna Wang
#
# This file is part of HoloPy.
#
# HoloPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HoloPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HoloPy.  If not, see <http://www.gnu.org/licenses/>.
"""
Base class for scattering theories.  Implements python-based
calc_intensity and calc_holo, based on subclass's calc_field

.. moduleauthor:: Thomas G. Dimiduk <tdimiduk@physics.harvard.edu>
"""

from holopy.scattering.scatterer import Sphere, Spheres
from holopy.scattering.theory import Mie, Multisphere

scatterer = Sphere(n = 1.6, r=.5, center=(5, 5, 5))
medium_index = 1.33
locations = RegularGrid(shape=(200, 200), spacing=.1, normals='z')
wavelen = 0.66

def test_calc_holo():
    holo = calc_holo(scatterer, medium_index, locations, wavelen)

def test_calc_field():
    field = calc_field(scatterer, medium_index, locations, wavelen)

def test_calc_cross_section():
    cross = calc_cross_section(scatterer, medium_index, wavelen)

def test_calc_intensity():
    intensity = calc_intensity(scatterer, medium_index, locations, wavelen)

def test_calc_scat_matrix():
    matr = calc_scat_matrix(scatterer, medium_index, locations, wavelen)

def test_determine_theory():
    assert_obj_equal(determine_theory(Sphere), Mie())
    assert_obj_equal(determine_theory(Spheres([Sphere(), Sphere()])), Multisphere())
    
