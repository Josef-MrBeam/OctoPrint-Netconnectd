# coding=utf-8
import setuptools
import octoprint_setuptools
import versioneer

setuptools.setup(
    **octoprint_setuptools.create_plugin_setup_parameters(
        identifier="netconnectd",
        name="OctoPrint-Netconnectd",
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        description="Client for netconnectd that allows configuration of netconnectd through OctoPrint's settings dialog. It's only available for Linux right now.",
        author="Gina Häußge",
        mail="osd@foosel.net",
        url="http://github.com/OctoPrint/OctoPrint-Netconnectd",
        requires=["OctoPrint", "netifaces"],
    )
)
