#!/usr/bin/env python
# SPDX-FileCopyrightText: (c) 2020 Western Digital Corporation or its affiliates,
#                             Arseniy Aharonov <arseniy@aharonov.icu>
#
# SPDX-License-Identifier: MIT

# ----------------------------------------------------------------------------------------------------------------------
VERSION = '2.1.7'

WEB_URL = "https://github.com/westerndigitalcorporation/stat#3-usage"
RESOURCES_DIRECTORY = 'resources'
DUMMIES_DIRECTORY = 'dummies'
PRODUCT_DIRECTORY = 'products'
LOGS_DIRECTORY = 'logs'
IDE_DIRECTORY = 'ide'
OUTPUT_DIRECTORY = 'output'
REPORT_FILENAME = 'report.json'
IGNORE_FILENAME = '.statignore'
CONFIG_FILENAME = '.statconfig'
AUTO_GENERATED_MAKEFILE = '/'.join([OUTPUT_DIRECTORY, "stat.mak"])
REBUILD_TARGET = 'rebuild'
CLEAN_TARGET = 'clean'

OUTPUT_SUB_DIRECTORIES = ['inc', 'obj', 'bin']
ALL_OUTPUT_DIRECTORIES = [OUTPUT_DIRECTORY, IDE_DIRECTORY, LOGS_DIRECTORY]

# ----------------------------------------------------------------------------------------------------------------------


class __AutoGeneratedAttributes(object):
    from os import path  # Prevent porting by those which import this file

    def __init__(self):
        self.toolPath = self.path.abspath(self.path.dirname(self.path.abspath(__file__)))
        self.makeTools = self.__listMakeTools()

    def __listMakeTools(self):
        makeTools = ("Windows32", "gnumake32.exe"), ("Windows64", "gnumake.exe"), ("Linux64", "make")
        makeTools = ((platform, self.path.join(self.toolPath, RESOURCES_DIRECTORY, "gmake", filename))
                     for platform, filename in makeTools)
        makeTools = {platform: toolPath for platform, toolPath in makeTools if self.path.isfile(toolPath)}
        return makeTools


# ----------------------------------------------------------------------------------------------------------------------
__attributes = __AutoGeneratedAttributes()

TOOL_PATH = __attributes.toolPath
MAKE_TOOL = __attributes.makeTools

# ----------------------------------------------------------------------------------------------------------------------
