#!/usr/bin/env python

# ----------------------------------------------------------------------
# This file is part of PEframe.
#
# PEframe is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# PEframe is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PEframe. If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------

import os

import loadfile

try:
	import pefile
	import peutils
except ImportError:
	print 'Error: import pefile or peutils modules failed.'
	exit(0)

# Load array by file alerts.txt
fn_apialert	= os.path.abspath('signatures' + os.sep + 'alerts.txt') #	return pathname
alerts 		= loadfile.get(fn_apialert)

def get(pe):
	apialert_found = []
	if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
		for lib in pe.DIRECTORY_ENTRY_IMPORT:
			for imp in lib.imports:
				for alert in alerts:
					if alert: # remove 'null'
						if str(imp.name).startswith(alert):
							apialert_found.append(imp.name)

	return sorted(set(apialert_found))
