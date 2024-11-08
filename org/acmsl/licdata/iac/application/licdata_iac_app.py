# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/iac/application/licdata_iac.py

This script defines the LicdataIac class.

Copyright (C) 2024-today acmsl's licdata-iac

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
import asyncio
from pythoneda.shared.application import enable, PythonEDA
from org.acmsl.licdata.iac.domain import LicdataIac
from org.acmsl.licdata.iac.domain import InfrastructureUpdateRequested
from org.acmsl.licdata.iac.infrastructure.cli import PulumiOptionsCli
from org.acmsl.licdata.iac.infrastructure.azure import PulumiAzureStackFactory
import pulumi
import pulumi_azure_native as azure_native
from typing import Dict


# @enable(AzureServerlessLicense)
@enable(PulumiOptionsCli)
@enable(PulumiAzureStackFactory)
class LicdataIacApp(PythonEDA):
    """
    Licdata Infrastructure as Code Application.

    Class name: LicdataIacApp

    Responsibilities:
        - Define the Licdata Infrastructure as Code Application.

    Collaborators:
        - Pulumi
        - Azure infrastructure
    """

    def __init__(self):
        """
        Creates a new LicdataIacApp instance.
        """
        # licdata_iac_banner is automatically generated by the Nix flake.
        try:
            from org.acmsl.licdata.iac.application.licdata_iac_banner import (
                LicdataIacBanner,
            )

            banner = LicdataIacBanner()
        except ImportError:
            banner = None

        super().__init__(banner, __file__)

    async def accept_pulumi_options(self, options: Dict):
        """
        Annotates the Pulumi options.
        :param options: Such options.
        :type options: Dict
        """
        updated = await LicdataIac.listen_InfrastructureUpdateRequested(
            InfrastructureUpdateRequested(
                options.get("stackName", None),
                options.get("projectName", None),
                options.get("location", None),
            )
        )
        if updated:
            await self.emit(updated)


if __name__ == "__main__":
    asyncio.run(LicdataIacApp.main("org.acmsl.licdata.iac.application.LicdataIacApp"))
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
