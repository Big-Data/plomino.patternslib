# -*- coding: utf-8 -*-
#
# File: selection.py
#
# Copyright (c) 2012 by ['Fulvio Casali']
#
# Gnu Public License (GPL)
#

__author__ = """Fulvio Casali <fulviocasali@gmail.com>"""
__docformat__ = 'plaintext'

from zope.formlib import form
from zope.interface import implements
from zope import component
from zope.schema import getFields
from zope.schema.vocabulary import SimpleVocabulary
from dictionaryproperty import DictionaryProperty

from Products.CMFPlomino.fields.selection import ISelectionField as \
    ISelectionBase, SelectionField as SelectionFieldBase, SettingForm

class ISelectionField(ISelectionBase):
    """
    A new selection field, to add "Chosen"
    """
    widget = Choice(vocabulary=SimpleVocabulary.fromItems([("Chosen", "CHOSEN")
                                                           ]),
                    title=u'Widget',
                    description=u'Field rendering',
                    default="SELECT",
                    required=True)

class SelectionField(SelectionFieldBase):
    """
    """
    implements(ISelectionField)    

    plomino_field_parameters = {'interface': ISelectionField,
                                'label': "Chosen",
                                'index_type': "KeywordIndex"}
    
    read_template = PageTemplateFile('chosen_read.pt')
    edit_template = PageTemplateFile('chosen_edit.pt')

component.provideUtility(SelectionField, ISelectionField, 'CHOSEN')

for f in getFields(ISelectionField).values():
    setattr(SelectionField, f.getName(),
            DictionaryProperty(f, 'parameters'))

class SettingForm(SettingForm):
    """
    """
    form_fields = form.Fields(ISelectionField)
