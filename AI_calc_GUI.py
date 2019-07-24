# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1118,234 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textHidari = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer7.Add( self.m_textHidari, 0, wx.ALL, 5 )

		self.m_textMigi = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer7.Add( self.m_textMigi, 0, wx.ALL, 5 )

		self.m_calcButton = wx.Button( self.m_panel1, wx.ID_ANY, u"&Calc", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_calcButton, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer7, 0, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		waSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.waLavel = wx.StaticText( self.m_panel1, wx.ID_ANY, u"和", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.waLavel.Wrap( -1 )

		waSizer.Add( self.waLavel, 0, wx.ALL, 5 )

		self.m_textWaAI = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TE_READONLY )
		waSizer.Add( self.m_textWaAI, 0, wx.ALL, 5 )

		self.m_textWaPC = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TE_READONLY )
		waSizer.Add( self.m_textWaPC, 0, wx.ALL, 5 )


		bSizer8.Add( waSizer, 1, wx.EXPAND, 5 )

		saSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.saLabel = wx.StaticText( self.m_panel1, wx.ID_ANY, u"差", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.saLabel.Wrap( -1 )

		saSizer.Add( self.saLabel, 0, wx.ALL, 5 )

		self.m_textSaAI = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TE_READONLY )
		saSizer.Add( self.m_textSaAI, 0, wx.ALL, 5 )

		self.m_textSaPC = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TE_READONLY )
		saSizer.Add( self.m_textSaPC, 0, wx.ALL, 5 )


		bSizer8.Add( saSizer, 1, wx.EXPAND, 5 )

		sekiSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.sekiLAbel = wx.StaticText( self.m_panel1, wx.ID_ANY, u"積", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sekiLAbel.Wrap( -1 )

		sekiSizer.Add( self.sekiLAbel, 0, wx.ALL, 5 )

		self.m_textSekiAI = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TE_READONLY )
		sekiSizer.Add( self.m_textSekiAI, 0, wx.ALL, 5 )

		self.m_textSekiPC = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TE_READONLY )
		sekiSizer.Add( self.m_textSekiPC, 0, wx.ALL, 5 )


		bSizer8.Add( sekiSizer, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer8, 0, wx.EXPAND, 5 )


		bSizer3.Add( bSizer9, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_calcButton.Bind( wx.EVT_BUTTON, self.CalcButtonPush )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def CalcButtonPush( self, event ):
		event.Skip()


