# -*- coding: utf-8 -*-
"""
Module implementing the PyCirkuit exceptions
"""
# Copyright (C) 2018-2019 Orestes Mas
# This file is part of PyCirkuit.
#
# PyCirkuit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyCirkuit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyCirkuit.  If not, see <https://www.gnu.org/licenses/>.
#

# Third-party imports
from PyQt5.QtCore import QCoreApplication

# Translation function
_translate = QCoreApplication.translate

# Exceptions in pycirkuit are used mainly to display info to the user via MessageBoxes
# Thus, an exception must convey 3 infos:
# 1) The MessageBox Title, different for each kind of error
# 2) The main message, perhaps as short as possible
# 3) Additional info
class PyCirkuitError(Exception):
    def __init__(self, message, title=_translate("PyCirkuitError", "PyCirkuit Error",  "Exception title"), moreInfo=""):
        super().__init__(message)
        self.title=title
        self.moreInfo=moreInfo


# Tool exceptions
class PyCktDocNotFoundError(PyCirkuitError):
    def __init__(self, toolName):
        errMsg = _translate("ExternalTool", "Cannot find the {toolName} manual!\n\n", "Leave untranslated the variable name inside curly braces (included)")
        errMsg = errMsg.format(toolName=toolName)
        info = _translate("ExternalTool", "Please ensure that you have this application properly installed, including the documentation, in a standard location.\n\n")
        super().__init__(errMsg, title=_translate("ExternalTool", "File Not Found", "Exception title"), moreInfo=info)


class PyCktCMManNotFoundError(PyCirkuitError):
    def __init__(self, cmPath):
        errMsg  = _translate("ExternalTool", 'Cannot find the "Circuit Macros" documentation.\n\n', "Warning message")
        errMsg += _translate("ExternalTool", "You will have to search for it manually. It should be a PDF file located into {cmPath} folder or one of its subfolders.", "Message Box text. DO NOT translate '{cmPath}' variable.").format(cmPath=cmPath)
        super().__init__(errMsg, title=_translate("ExternalTool", "File Not Found", "Exception title"), moreInfo="")


class PyCktToolExecutionError(PyCirkuitError):
    def __init__(self, message, moreInfo=""):
        super().__init__(message, title=_translate("ExternalTool", "Tool Execution Error", "Exception title"), moreInfo=moreInfo)


class PyCktToolNotFoundError(PyCirkuitError):
    def __init__(self, executableName, longName):
        errMsg = _translate("ExternalTool", "Cannot find the {toolLongName}!\n\n", "Leave untranslated the variable name inside curly braces (included)")
        errMsg = errMsg.format(toolLongName=longName)
        info = _translate("ExternalTool", "Please ensure that you have this application properly installed and the executable \"{toolExecutableName}\" is in the PATH.\n\n", "Leave untranslated the variable name inside curly braces (included)")
        info += _translate("ExternalTool", "Cannot generate the preview.")
        info = info.format(toolExecutableName=executableName)
        super().__init__(errMsg, title=_translate("ExternalTool", "Tool Not Found", "Exception title"), moreInfo=info)


# Circuit Macros exceptions
class PyCktCMNotFoundError(PyCirkuitError):
    def __init__(self, message):
        super().__init__(message, title=_translate("ExternalTool", "Circuit Macros not found", "Exception title"))


class PyCktCMNewVersionAvailable(PyCirkuitError):
    def __init__(self, message):
        super().__init__(message, title=_translate("ExternalTool", "New Circuit Macros version available!", "Exception title"))


class PyCktCMFetchError(PyCirkuitError):
    def __init__(self, message):
        super().__init__(message, title=_translate("ExternalTool", "Circuit Macros not found", "Exception title"))
