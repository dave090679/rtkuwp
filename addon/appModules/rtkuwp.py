# -*- encoding: utf-8 -*-
#appModules/avpui.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2012 NVDA Contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
import appModuleHandler
import api
import controlTypes
from NVDAObjects.UIA import ListItem, UIA
class rtkuwpuia(UIA):
	def _get_name(self):
		return self.UIAElement.CurrentAutomationId


class rtkuwplistitem(ListItem):
	def _get_name(self):
		l = list()
		for x in self.children:
			childname = x.name
			childrole = x.role
			if childname and childrole in [controlTypes.ROLE_STATICTEXT, controlTypes.ROLE_GROUPING]:
				l.append(childname) 
		return ', '.join(l)

class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.role == controlTypes.ROLE_LISTITEM:
			clslist.insert(0,rtkuwplistitem)
		elif obj.name == '':
			clslist.insert(0,rtkuwpuia)