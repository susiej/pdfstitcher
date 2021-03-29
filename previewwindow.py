# PDFStitcher is a utility to work with PDF sewing patterns.
# Copyright (C) 2021 Charlotte Curtis
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import wx
import wx.lib.scrolledpanel as scrolled
import utils

class PreviewWindow(wx.Frame):
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(PreviewWindow, self).__init__(*args, **kw)

        self.pnl = scrolled.ScrolledPanel(self)
        vert_sizer = wx.BoxSizer(wx.VERTICAL)

        self.pnl.SetSizer(vert_sizer)
    
        self.col_major = False
        self.right_to_left = False
        self.bottom_to_top = False
        
        self.cols = 0
        self.rows = 0
        self.page_range = []