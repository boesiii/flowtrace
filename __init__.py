# -*- coding: utf-8 -*-
"""
/***************************************************************************
 flowTrace
                                 A QGIS plugin
 Select line segments upstream of a selected line segment
                             -------------------
        begin                : 2014-02-20
        copyright            : (C) 2014 by Ed B
        email                : boesiii@yahoo.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load flowTrace class from file flowTrace
    from flowtrace import flowTrace
    return flowTrace(iface)
