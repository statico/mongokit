#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2009-2010, Nicolas Clairon
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the University of California, Berkeley nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE REGENTS AND CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from mongokit.helpers import DotCollapsedDict

class MongoDocumentCursor(object):
    def __init__(self, cursor, cls):
        self._cursor = cursor
        self._collection = cursor._Cursor__collection
        self._db = self._collection.database
        self._class_object = cls

    def distinct(self, *args, **kwargs):
        return self._cursor.distinct(*args, **kwargs)

    def where(self, *args, **kwargs):
        return self.__class__(self._cursor.where(*args, **kwargs), self._class_object)

    def sort(self, *args, **kwargs):
        return self.__class__(self._cursor.sort(*args, **kwargs), self._class_object)

    def limit(self, *args, **kwargs):
        return self.__class__(self._cursor.limit(*args, **kwargs), self._class_object)

    def hint(self, *args, **kwargs):
        return self.__class__(self._cursor.hint(*args, **kwargs), self._class_object)

    def count(self, *args, **kwargs):
        return self._cursor.count(*args, **kwargs)
        
    def explain(self, *args, **kwargs):
        return self._cursor.explain(*args, **kwargs)

    def next(self, *args, **kwargs):
        data = self._cursor.next(*args, **kwargs)
        doc = self._class_object(data, collection=self._collection, generate_index=False)
        doc._build_footprint()
        return doc

    def skip(self, *args, **kwargs):
        return self.__class__(self._cursor.skip(*args, **kwargs), self._class_object)

    def clone(self, *args, **kwargs):
        return self.__class__(self._cursor.clone(), self._class_object)

    def explain(self, *args, **kwargs):
        return self._cursor.explain()

    def __iter__(self, *args, **kwargs):
        for obj in self._cursor:
            doc = self._class_object(obj, collection=self._collection, generate_index=False)
            doc._build_footprint()
            yield doc

    def rewind(self, *args, **kwargs):
        return self.__class__(self._cursor.rewind(*args, **kwargs), self._class_object)

