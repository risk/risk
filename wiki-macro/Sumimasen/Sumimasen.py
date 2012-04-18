#!/usr/bin/env python
# -*- coding: utf-8 -*-

from trac.wiki.macros import WikiMacroBase

class SumimasenMacro(WikiMacroBase):

    def expand_macro(self, formatter, name, args):
        arguments = args.split(',')
        if len(arguments) != 1:
            return "Sumimasen Error: Invalid arguments"
        else:
            return main(count=int(arguments[0]))

def main(count):

    html = u''

    for i in range(count):
        html += u'ホント'

    html += u'すみません'

    return html


if __name__ == '__main__':
    print main(100)

