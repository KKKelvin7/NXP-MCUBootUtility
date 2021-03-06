# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class efuseWin_BootCfg1
###########################################################################

class efuseWin_BootCfg1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 860,370 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bSizer_byteIdx = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText_address = wx.StaticText( self, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_address.Wrap( -1 )

		self.m_staticText_address.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_address, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx0 = wx.StaticText( self, wx.ID_ANY, u"               0x460[7:0]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx0.Wrap( -1 )

		self.m_staticText_byteIdx0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx0, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx1 = wx.StaticText( self, wx.ID_ANY, u"               0x460[15:8]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx1.Wrap( -1 )

		self.m_staticText_byteIdx1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx1, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx2 = wx.StaticText( self, wx.ID_ANY, u"               0x460[23:16]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx2.Wrap( -1 )

		self.m_staticText_byteIdx2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx2, 0, wx.ALL, 5 )

		self.m_staticText_byteIdx3 = wx.StaticText( self, wx.ID_ANY, u"               0x460[31:24]", wx.DefaultPosition, wx.Size( 80,51 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_byteIdx3.Wrap( -1 )

		self.m_staticText_byteIdx3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer_byteIdx.Add( self.m_staticText_byteIdx3, 0, wx.ALL, 5 )


		wSizer_win.Add( bSizer_byteIdx, 1, wx.EXPAND, 5 )

		bSizer_bitIdx = wx.BoxSizer( wx.VERTICAL )

		wSizer_bitIdx = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_bitIdx7 = wx.StaticText( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx7.Wrap( -1 )

		self.m_staticText_bitIdx7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx7, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx6 = wx.StaticText( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx6.Wrap( -1 )

		self.m_staticText_bitIdx6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx6, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx5 = wx.StaticText( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx5.Wrap( -1 )

		self.m_staticText_bitIdx5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx5, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx4 = wx.StaticText( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx4.Wrap( -1 )

		self.m_staticText_bitIdx4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx4, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx3 = wx.StaticText( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx3.Wrap( -1 )

		self.m_staticText_bitIdx3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx3, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx2 = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx2.Wrap( -1 )

		self.m_staticText_bitIdx2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx2, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx1 = wx.StaticText( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx1.Wrap( -1 )

		self.m_staticText_bitIdx1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx1, 0, wx.ALL, 5 )

		self.m_staticText_bitIdx0 = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.m_staticText_bitIdx0.Wrap( -1 )

		self.m_staticText_bitIdx0.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		wSizer_bitIdx.Add( self.m_staticText_bitIdx0, 0, wx.ALL, 5 )

		self.m_staticText_bit7 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit7.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit7, 0, wx.ALL, 5 )

		self.m_staticText_bit6 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit6.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit6, 0, wx.ALL, 5 )

		self.m_staticText_bit5 = wx.StaticText( self, wx.ID_ANY, u"FORCE_COLD_BOOT", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit5.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit5, 0, wx.ALL, 5 )

		self.m_staticText_bit4 = wx.StaticText( self, wx.ID_ANY, u"BT_FUSE_SEL", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit4.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit4, 0, wx.ALL, 5 )

		self.m_staticText_bit3 = wx.StaticText( self, wx.ID_ANY, u"DIR_BT_DIS", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit3.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit3, 0, wx.ALL, 5 )

		self.m_staticText_bit2 = wx.StaticText( self, wx.ID_ANY, u"Boot_Freq", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit2.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit2, 0, wx.ALL, 5 )

		self.m_staticText_bit1 = wx.StaticText( self, wx.ID_ANY, u"SEC_CONFIG[1]", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit1.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit1, 0, wx.ALL, 5 )

		self.m_staticText_bit0 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit0.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit0, 0, wx.ALL, 5 )

		m_choice_bit7Choices = [ u"x - Unlock" ]
		self.m_choice_bit7 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit7Choices, 0 )
		self.m_choice_bit7.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit7, 0, wx.ALL, 5 )

		m_choice_bit6Choices = [ u"x - Unlock" ]
		self.m_choice_bit6 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit6Choices, 0 )
		self.m_choice_bit6.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit6, 0, wx.ALL, 5 )

		m_choice_bit5Choices = [ u"0 ", u"1" ]
		self.m_choice_bit5 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit5Choices, 0 )
		self.m_choice_bit5.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit5, 0, wx.ALL, 5 )

		m_choice_bit4Choices = [ u"0 ", u"1" ]
		self.m_choice_bit4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit4Choices, 0 )
		self.m_choice_bit4.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit4, 0, wx.ALL, 5 )

		m_choice_bit3Choices = [ u"0 ", u"1" ]
		self.m_choice_bit3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit3Choices, 0 )
		self.m_choice_bit3.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit3, 0, wx.ALL, 5 )

		m_choice_bit2Choices = [ u"0 - 396 / 132 MHz", u"1 - 264 / 132 MHz" ]
		self.m_choice_bit2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit2Choices, 0 )
		self.m_choice_bit2.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit2, 0, wx.ALL, 5 )

		m_choice_bit1Choices = [ u"0 ", u"1" ]
		self.m_choice_bit1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit1Choices, 0 )
		self.m_choice_bit1.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit1, 0, wx.ALL, 5 )

		m_choice_bit0Choices = [ u"x - Unlock" ]
		self.m_choice_bit0 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit0Choices, 0 )
		self.m_choice_bit0.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit0, 0, wx.ALL, 5 )

		self.m_staticText_bit15_14 = wx.StaticText( self, wx.ID_ANY, u"BEE_KEY1_SEL", wx.DefaultPosition, wx.Size( 170,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit15_14.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit15_14, 0, wx.ALL, 5 )

		self.m_staticText_bit13_12 = wx.StaticText( self, wx.ID_ANY, u"BEE_KEY0_SEL", wx.DefaultPosition, wx.Size( 170,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit13_12.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit13_12, 0, wx.ALL, 5 )

		self.m_staticText_bit11_8 = wx.StaticText( self, wx.ID_ANY, u"Reserved (SDR config)", wx.DefaultPosition, wx.Size( 345,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit11_8.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit11_8, 0, wx.ALL, 5 )

		m_choice_bit15_14Choices = [ u"00 -", u"01 -", u"10 -", u"11 -" ]
		self.m_choice_bit15_14 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 170,-1 ), m_choice_bit15_14Choices, 0 )
		self.m_choice_bit15_14.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit15_14, 0, wx.ALL, 5 )

		m_choice_bit13_12Choices = [ u"00 -", u"01 -", u"10 -", u"11 -" ]
		self.m_choice_bit13_12 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 170,-1 ), m_choice_bit13_12Choices, 0 )
		self.m_choice_bit13_12.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit13_12, 0, wx.ALL, 5 )

		m_choice_bit11_8Choices = [ u"xxxx - Unlock" ]
		self.m_choice_bit11_8 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 350,-1 ), m_choice_bit11_8Choices, 0 )
		self.m_choice_bit11_8.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit11_8, 0, wx.ALL, 5 )

		self.m_staticText_bit23_22 = wx.StaticText( self, wx.ID_ANY, u"JTAG_SMODE[1:0]", wx.DefaultPosition, wx.Size( 170,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit23_22.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit23_22, 0, wx.ALL, 5 )

		self.m_staticText_bit21 = wx.StaticText( self, wx.ID_ANY, u"WDOG_ENA", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit21.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit21, 0, wx.ALL, 5 )

		self.m_staticText_bit20 = wx.StaticText( self, wx.ID_ANY, u"SJC_DIS", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit20.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit20, 0, wx.ALL, 5 )

		self.m_staticText_bit19 = wx.StaticText( self, wx.ID_ANY, u"DAP_SJC_SWD", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit19.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit19, 0, wx.ALL, 5 )

		self.m_staticText_bit18 = wx.StaticText( self, wx.ID_ANY, u"SDP_READ_DIS", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit18.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit18, 0, wx.ALL, 5 )

		self.m_staticText_bit17 = wx.StaticText( self, wx.ID_ANY, u"SDP_DIS", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit17.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit17, 0, wx.ALL, 5 )

		self.m_staticText_bit16 = wx.StaticText( self, wx.ID_ANY, u"FORCE_INTERNAL_BOOT", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit16.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit16, 0, wx.ALL, 5 )

		m_choice_bit23_22Choices = [ u"00 -", u"01 -", u"10 -", u"11 -" ]
		self.m_choice_bit23_22 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 170,-1 ), m_choice_bit23_22Choices, 0 )
		self.m_choice_bit23_22.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit23_22, 0, wx.ALL, 5 )

		m_choice_bit21Choices = [ u"'0' - Disabled", u"'1' - Enabled" ]
		self.m_choice_bit21 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit21Choices, 0 )
		self.m_choice_bit21.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit21, 0, wx.ALL, 5 )

		m_choice_bit20Choices = [ u"'0' - Disabled", u"'1' - Enabled" ]
		self.m_choice_bit20 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit20Choices, 0 )
		self.m_choice_bit20.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit20, 0, wx.ALL, 5 )

		m_choice_bit19Choices = [ u"'0' - Disabled", u"'1' - Enabled" ]
		self.m_choice_bit19 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit19Choices, 0 )
		self.m_choice_bit19.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit19, 0, wx.ALL, 5 )

		m_choice_bit18Choices = [ u"'0' - Disabled", u"'1' - Enabled" ]
		self.m_choice_bit18 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit18Choices, 0 )
		self.m_choice_bit18.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit18, 0, wx.ALL, 5 )

		m_choice_bit17Choices = [ u"'0' - Disabled", u"'1' - Enabled" ]
		self.m_choice_bit17 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit17Choices, 0 )
		self.m_choice_bit17.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit17, 0, wx.ALL, 5 )

		m_choice_bit16Choices = [ u"0 - ", u"1 - " ]
		self.m_choice_bit16 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit16Choices, 0 )
		self.m_choice_bit16.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit16, 0, wx.ALL, 5 )

		self.m_staticText_bit31_30 = wx.StaticText( self, wx.ID_ANY, u"SD_PWR_CYCLE_SELECTION", wx.DefaultPosition, wx.Size( 170,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit31_30.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit31_30, 0, wx.ALL, 5 )

		self.m_staticText_bit29 = wx.StaticText( self, wx.ID_ANY, u"PWR_STABLE", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit29.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit29, 0, wx.ALL, 5 )

		self.m_staticText_bit28 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit28.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit28, 0, wx.ALL, 5 )

		self.m_staticText_bit27 = wx.StaticText( self, wx.ID_ANY, u"JTAG_HEO", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit27.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit27, 0, wx.ALL, 5 )

		self.m_staticText_bit26 = wx.StaticText( self, wx.ID_ANY, u"KTE", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit26.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit26, 0, wx.ALL, 5 )

		self.m_staticText_bit25 = wx.StaticText( self, wx.ID_ANY, u"Reserved", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit25.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit25, 0, wx.ALL, 5 )

		self.m_staticText_bit24 = wx.StaticText( self, wx.ID_ANY, u"DLL_ENA", wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SIMPLE )
		self.m_staticText_bit24.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_bit24, 0, wx.ALL, 5 )

		m_choice_bit31_30Choices = [ u"00 - 20ms", u"01 - 10ms", u"10 - 5ms", u"11 - 2.5ms" ]
		self.m_choice_bit31_30 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 170,-1 ), m_choice_bit31_30Choices, 0 )
		self.m_choice_bit31_30.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit31_30, 0, wx.ALL, 5 )

		m_choice_bit29Choices = [ u"0 - 5ms", u"1 - 2.5ms" ]
		self.m_choice_bit29 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit29Choices, 0 )
		self.m_choice_bit29.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit29, 0, wx.ALL, 5 )

		m_choice_bit28Choices = [ u"x - Unlock" ]
		self.m_choice_bit28 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit28Choices, 0 )
		self.m_choice_bit28.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit28, 0, wx.ALL, 5 )

		m_choice_bit27Choices = [ u"0 - ", u"1 - " ]
		self.m_choice_bit27 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit27Choices, 0 )
		self.m_choice_bit27.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit27, 0, wx.ALL, 5 )

		m_choice_bit26Choices = [ u"0 - ", u"1 - " ]
		self.m_choice_bit26 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit26Choices, 0 )
		self.m_choice_bit26.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit26, 0, wx.ALL, 5 )

		m_choice_bit25Choices = [ u"x - Unlock" ]
		self.m_choice_bit25 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit25Choices, 0 )
		self.m_choice_bit25.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit25, 0, wx.ALL, 5 )

		m_choice_bit24Choices = [ u"0 - Disable DLL for SD/eMMC", u"1 - Enable DLL for SD/Emmc" ]
		self.m_choice_bit24 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bit24Choices, 0 )
		self.m_choice_bit24.SetSelection( 0 )
		wSizer_bitIdx.Add( self.m_choice_bit24, 0, wx.ALL, 5 )

		self.m_staticText_null0BitIdx = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 420,-1 ), 0 )
		self.m_staticText_null0BitIdx.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_null0BitIdx, 0, wx.ALL, 5 )

		self.m_button_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_bitIdx.Add( self.m_button_ok, 0, wx.ALL, 5 )

		self.m_button_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_bitIdx.Add( self.m_button_cancel, 0, wx.ALL, 5 )

		self.m_staticText_null1BitIdx = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 720,1 ), 0 )
		self.m_staticText_null1BitIdx.Wrap( -1 )

		wSizer_bitIdx.Add( self.m_staticText_null1BitIdx, 0, wx.ALL, 5 )


		bSizer_bitIdx.Add( wSizer_bitIdx, 1, wx.EXPAND, 5 )


		wSizer_win.Add( bSizer_bitIdx, 1, wx.EXPAND, 5 )


		self.SetSizer( wSizer_win )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.callbackClose )
		self.m_button_ok.Bind( wx.EVT_BUTTON, self.callbackOk )
		self.m_button_cancel.Bind( wx.EVT_BUTTON, self.callbackCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def callbackClose( self, event ):
		event.Skip()

	def callbackOk( self, event ):
		event.Skip()

	def callbackCancel( self, event ):
		event.Skip()


