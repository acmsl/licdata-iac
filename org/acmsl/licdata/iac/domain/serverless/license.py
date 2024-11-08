# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/iac/domain/serverless/license.py

This script defines the License class.

Copyright (C) 2024-today acmsl's licdata

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.shared import Port


class License(Port):
    """
    Serverless package for License code.

    Class name: License

    Responsibilities:
        - Provide the serverless package with License code.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new Serverless instance.
        """
        super().__init__()


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
