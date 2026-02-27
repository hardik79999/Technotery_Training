# PIP is a package manager for Python packages, or modules if you like.

# Note: If you have Python version 3.4 or later, PIP is included by default.


# Check if PIP is Installed

"""
pip --version
"""

# Install PIP
"""
If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/ 
"""

# Download a package named "camelcase":
"""
pip install camelcase
"""


import camelcase

c = camelcase.CamelCase()

txt = "Hardik Bandhiya"
print(type(c)) # <class 'camelcase.main.CamelCase'>
print(c.hump(txt)) # Hardik Bandhiya


# Find Packages --------------------------------------------------------------------

"""
Find more packages at https://pypi.org/.
"""

# Remove a Package -----------------------------------------------------------------------

"""
pip uninstall camelcase
"""


# List Packages ----------------------------------------------------
"""
pip list
"""