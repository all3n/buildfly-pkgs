#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 wanghuacheng <wanghuacheng@wanghuacheng-PC>
#
# Distributed under terms of the MIT license.

"""

"""
from buildfly as *



def gen_boost_urls():
    versions = ["1.69.0","1.68.0","1.67.0",
            "1.66.0","1.65.1","1.65.0",
            "1.64.0","1.63.0","1.62.0","1.61.0","1.60.0",
            "1.59.0","1.58.0","1.57.0", "1.56.0", "1.55.0",
            "1.54.0", "1.53.0", "1.52.0", "1.51.0", "1.50.0",
            "1.49.0", "1.48.0", "1.47.0"
    ]
    version_url_map = {}
    for version in versions:
        version_url_map[version] = "https://sourceforge.net/projects/boost/files/boost/{version}/{filename}".format(
                    version=version,
                    filename="boost_"+version.replace(".", "_")+".tar.gz"
        )
    return version_url_map



def_urls(gen_boost_urls())

def_modules(["filesystem", "program_options" , "math"], "def")

def_cmds([
    "./bootstrap.sh --with-libraries=${INSTALL_MODULES} --prefix=${INSTALL_PREFIX}",
    "./b2 -j32 variant=release define=_GLIBCXX_USE_CXX11_ABI=0 install "
    ])
