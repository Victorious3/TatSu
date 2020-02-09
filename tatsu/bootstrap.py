#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by TatSu.
#
#    https://pypi.python.org/pypi/tatsu/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import generator_stop

import sys

from tatsu.buffering import Buffer
from tatsu.parsing import Parser
from tatsu.parsing import tatsumasu, leftrec, nomemo
from tatsu.parsing import leftrec, nomemo  # noqa
from tatsu.util import re, generic_main  # noqa


KEYWORDS = {
    None,
}  # type: ignore


class EBNFBootstrapBuffer(Buffer):
    def __init__(
        self,
        text,
        whitespace=None,
        nameguard=None,
        comments_re='\\(\\*((?:.|\\n)*?)\\*\\)',
        eol_comments_re='#([^\\n]*?)$',
        ignorecase=None,
        namechars='',
        **kwargs
    ):
        super().__init__(
            text,
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            namechars=namechars,
            **kwargs
        )


class EBNFBootstrapParser(Parser):
    def __init__(
        self,
        whitespace=None,
        nameguard=None,
        comments_re='\\(\\*((?:.|\\n)*?)\\*\\)',
        eol_comments_re='#([^\\n]*?)$',
        ignorecase=None,
        left_recursion=False,
        parseinfo=True,
        keywords=None,
        namechars='',
        tokenizercls=EBNFBootstrapBuffer,
        **kwargs
    ):
        if keywords is None:
            keywords = KEYWORDS
        super().__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            parseinfo=parseinfo,
            keywords=keywords,
            namechars=namechars,
            tokenizercls=tokenizercls,
            **kwargs
        )

    @tatsumasu()
    def _start_(self):  # noqa
        self._grammar_()

    @tatsumasu('Grammar')
    def _grammar_(self):  # noqa
        self._constant('TATSU')
        self.name_last_node('title')

        def block1():
            with self._choice():
                with self._option():
                    self._directive_()
                    self.add_last_node_to_name('directives')
                with self._option():
                    self._keyword_()
                    self.add_last_node_to_name('keywords')
                self._error('no available options')
        self._closure(block1)
        self._rule_()
        self.add_last_node_to_name('rules')

        def block6():
            with self._choice():
                with self._option():
                    self._rule_()
                    self.add_last_node_to_name('rules')
                with self._option():
                    self._keyword_()
                    self.add_last_node_to_name('keywords')
                self._error('no available options')
        self._closure(block6)
        self._check_eof()
        self.ast._define(
            ['title'],
            ['directives', 'keywords', 'rules']
        )

    @tatsumasu()
    def _directive_(self):  # noqa
        self._token('@@')
        with self._ifnot():
            self._token('keyword')
        self._cut()
        with self._group():
            with self._choice():
                with self._option():
                    with self._group():
                        with self._choice():
                            with self._option():
                                self._token('comments')
                            with self._option():
                                self._token('eol_comments')
                            self._error('no available options')
                    self.name_last_node('name')
                    self._cut()
                    self._cut()
                    self._token('::')
                    self._cut()
                    self._regex_()
                    self.name_last_node('value')
                with self._option():
                    with self._group():
                        self._token('whitespace')
                    self.name_last_node('name')
                    self._cut()
                    self._cut()
                    self._token('::')
                    self._cut()
                    with self._group():
                        with self._choice():
                            with self._option():
                                self._regex_()
                            with self._option():
                                self._token('None')
                            with self._option():
                                self._token('False')
                            with self._option():
                                self._constant('None')
                            self._error('no available options')
                    self.name_last_node('value')
                with self._option():
                    with self._group():
                        with self._choice():
                            with self._option():
                                self._token('nameguard')
                            with self._option():
                                self._token('ignorecase')
                            with self._option():
                                self._token('left_recursion')
                            with self._option():
                                self._token('parseinfo')
                            self._error('no available options')
                    self.name_last_node('name')
                    self._cut()
                    with self._group():
                        with self._choice():
                            with self._option():
                                self._token('::')
                                self._cut()
                                self._boolean_()
                                self.name_last_node('value')
                            with self._option():
                                self._constant(True)
                                self.name_last_node('value')
                            self._error('no available options')
                with self._option():
                    with self._group():
                        self._token('grammar')
                    self.name_last_node('name')
                    self._cut()
                    self._token('::')
                    self._cut()
                    self._word_()
                    self.name_last_node('value')
                with self._option():
                    with self._group():
                        self._token('namechars')
                    self.name_last_node('name')
                    self._cut()
                    self._token('::')
                    self._cut()
                    self._string_()
                    self.name_last_node('value')
                self._error('no available options')
        self._cut()
        self.ast._define(
            ['name', 'value'],
            []
        )

    @tatsumasu()
    def _keywords_(self):  # noqa

        def block0():
            self._keywords_()
        self._positive_closure(block0)

    @tatsumasu()
    def _keyword_(self):  # noqa
        self._token('@@keyword')
        self._cut()
        self._token('::')
        self._cut()

        def block0():
            self._literal_()
            self.add_last_node_to_name('@')
            with self._ifnot():
                with self._group():
                    with self._choice():
                        with self._option():
                            self._token(':')
                        with self._option():
                            self._token('=')
                        self._error('no available options')
        self._closure(block0)

    @tatsumasu()
    def _paramdef_(self):  # noqa
        with self._choice():
            with self._option():
                self._token('::')
                self._cut()
                self._params_()
                self.name_last_node('params')
            with self._option():
                self._token('(')
                self._cut()
                with self._group():
                    with self._choice():
                        with self._option():
                            self._kwparams_()
                            self.name_last_node('kwparams')
                        with self._option():
                            self._params_()
                            self.name_last_node('params')
                            self._token(',')
                            self._cut()
                            self._kwparams_()
                            self.name_last_node('kwparams')
                        with self._option():
                            self._params_()
                            self.name_last_node('params')
                        self._error('no available options')
                self._token(')')
            self._error('no available options')
        self.ast._define(
            ['kwparams', 'params'],
            []
        )

    @tatsumasu('Rule')
    def _rule_(self):  # noqa

        def block1():
            self._decorator_()
        self._closure(block1)
        self.name_last_node('decorators')
        self._name_()
        self.name_last_node('name')
        self._cut()
        with self._optional():
            with self._choice():
                with self._option():
                    self._token('::')
                    self._cut()
                    self._params_()
                    self.name_last_node('params')
                with self._option():
                    self._token('(')
                    self._cut()
                    with self._group():
                        with self._choice():
                            with self._option():
                                self._kwparams_()
                                self.name_last_node('kwparams')
                            with self._option():
                                self._params_()
                                self.name_last_node('params')
                                self._token(',')
                                self._cut()
                                self._kwparams_()
                                self.name_last_node('kwparams')
                            with self._option():
                                self._params_()
                                self.name_last_node('params')
                            self._error('no available options')
                    self._token(')')
                self._error('no available options')
        with self._optional():
            self._token('<')
            self._cut()
            self._known_name_()
            self.name_last_node('base')
        self._token('=')
        self._cut()
        self._expre_()
        self.name_last_node('exp')
        self._token(';')
        self._cut()
        self.ast._define(
            ['base', 'decorators', 'exp', 'kwparams', 'name', 'params'],
            []
        )

    @tatsumasu()
    def _decorator_(self):  # noqa
        self._token('@')
        with self._ifnot():
            self._token('@')
        self._cut()
        with self._group():
            with self._choice():
                with self._option():
                    self._token('override')
                with self._option():
                    self._token('name')
                with self._option():
                    self._token('nomemo')
                self._error('no available options')
        self.name_last_node('@')

    @tatsumasu()
    def _params_(self):  # noqa
        self._first_param_()
        self.add_last_node_to_name('@')

        def block1():
            self._token(',')
            self._literal_()
            self.add_last_node_to_name('@')
            with self._ifnot():
                self._token('=')
            self._cut()
        self._closure(block1)

    @tatsumasu()
    def _first_param_(self):  # noqa
        with self._choice():
            with self._option():
                self._path_()
            with self._option():
                self._literal_()
            self._error('no available options')

    @tatsumasu()
    def _kwparams_(self):  # noqa

        def sep0():
            self._token(',')

        def block0():
            self._pair_()
        self._positive_gather(block0, sep0)

    @tatsumasu()
    def _pair_(self):  # noqa
        self._word_()
        self.add_last_node_to_name('@')
        self._token('=')
        self._cut()
        self._literal_()
        self.add_last_node_to_name('@')

    @tatsumasu()
    def _expre_(self):  # noqa
        with self._choice():
            with self._option():
                self._choice_()
            with self._option():
                self._sequence_()
            self._error('no available options')

    @tatsumasu('Choice')
    def _choice_(self):  # noqa
        with self._optional():
            self._token('|')
            self._cut()
        self._sequence_()
        self.add_last_node_to_name('@')

        def block1():
            self._token('|')
            self._cut()
            self._sequence_()
            self.add_last_node_to_name('@')
        self._positive_closure(block1)

    @tatsumasu('Sequence')
    def _sequence_(self):  # noqa

        def block1():
            self._element_()
        self._positive_closure(block1)
        self.name_last_node('sequence')
        self.ast._define(
            ['sequence'],
            []
        )

    @tatsumasu()
    def _element_(self):  # noqa
        with self._choice():
            with self._option():
                self._rule_include_()
            with self._option():
                self._named_()
            with self._option():
                self._override_()
            with self._option():
                self._term_()
            self._error('no available options')

    @tatsumasu('RuleInclude')
    def _rule_include_(self):  # noqa
        self._token('>')
        self._cut()
        self._known_name_()
        self.name_last_node('@')

    @tatsumasu()
    def _named_(self):  # noqa
        with self._choice():
            with self._option():
                self._named_list_()
            with self._option():
                self._named_single_()
            self._error('no available options')

    @tatsumasu('NamedList')
    def _named_list_(self):  # noqa
        self._name_()
        self.name_last_node('name')
        self._token('+:')
        self._cut()
        self._term_()
        self.name_last_node('exp')
        self.ast._define(
            ['exp', 'name'],
            []
        )

    @tatsumasu('Named')
    def _named_single_(self):  # noqa
        self._name_()
        self.name_last_node('name')
        self._token(':')
        self._cut()
        self._term_()
        self.name_last_node('exp')
        self.ast._define(
            ['exp', 'name'],
            []
        )

    @tatsumasu()
    def _override_(self):  # noqa
        with self._choice():
            with self._option():
                self._override_list_()
            with self._option():
                self._override_single_()
            with self._option():
                self._override_single_deprecated_()
            self._error('no available options')

    @tatsumasu('OverrideList')
    def _override_list_(self):  # noqa
        self._token('@+:')
        self._cut()
        self._term_()
        self.name_last_node('@')

    @tatsumasu('Override')
    def _override_single_(self):  # noqa
        self._token('@:')
        self._cut()
        self._term_()
        self.name_last_node('@')

    @tatsumasu('Override')
    def _override_single_deprecated_(self):  # noqa
        self._token('@')
        self._cut()
        self._term_()
        self.name_last_node('@')

    @tatsumasu()
    def _term_(self):  # noqa
        with self._choice():
            with self._option():
                self._void_()
            with self._option():
                self._gather_()
            with self._option():
                self._join_()
            with self._option():
                self._left_join_()
            with self._option():
                self._right_join_()
            with self._option():
                self._group_()
            with self._option():
                self._empty_closure_()
            with self._option():
                self._positive_closure_()
            with self._option():
                self._closure_()
            with self._option():
                self._optional_()
            with self._option():
                self._special_()
            with self._option():
                self._skip_to_()
            with self._option():
                self._lookahead_()
            with self._option():
                self._negative_lookahead_()
            with self._option():
                self._atom_()
            self._error('no available options')

    @tatsumasu('Group')
    def _group_(self):  # noqa
        self._token('(')
        self._cut()
        self._expre_()
        self.name_last_node('exp')
        self._token(')')
        self._cut()
        self.ast._define(
            ['exp'],
            []
        )

    @tatsumasu()
    def _gather_(self):  # noqa
        with self._if():
            with self._group():
                self._separator_()
                self._token('.{')
        self._cut()
        with self._group():
            with self._choice():
                with self._option():
                    self._positive_gather_()
                with self._option():
                    self._normal_gather_()
                self._error('no available options')

    @tatsumasu('PositiveGather')
    def _positive_gather_(self):  # noqa
        self._separator_()
        self.name_last_node('sep')
        self._token('.{')
        self._expre_()
        self.name_last_node('exp')
        self._token('}')
        with self._group():
            with self._choice():
                with self._option():
                    self._token('+')
                with self._option():
                    self._token('-')
                self._error('no available options')
        self._cut()
        self.ast._define(
            ['exp', 'sep'],
            []
        )

    @tatsumasu('Gather')
    def _normal_gather_(self):  # noqa
        self._separator_()
        self.name_last_node('sep')
        self._token('.{')
        self._cut()
        self._expre_()
        self.name_last_node('exp')
        self._token('}')
        with self._optional():
            self._token('*')
            self._cut()
        self._cut()
        self.ast._define(
            ['exp', 'sep'],
            []
        )

    @tatsumasu()
    def _join_(self):  # noqa
        with self._if():
            with self._group():
                self._separator_()
                self._token('%{')
        self._cut()
        with self._group():
            with self._choice():
                with self._option():
                    self._positive_join_()
                with self._option():
                    self._normal_join_()
                self._error('no available options')

    @tatsumasu('PositiveJoin')
    def _positive_join_(self):  # noqa
        self._separator_()
        self.name_last_node('sep')
        self._token('%{')
        self._expre_()
        self.name_last_node('exp')
        self._token('}')
        with self._group():
            with self._choice():
                with self._option():
                    self._token('+')
                with self._option():
                    self._token('-')
                self._error('no available options')
        self._cut()
        self.ast._define(
            ['exp', 'sep'],
            []
        )

    @tatsumasu('Join')
    def _normal_join_(self):  # noqa
        self._separator_()
        self.name_last_node('sep')
        self._token('%{')
        self._cut()
        self._expre_()
        self.name_last_node('exp')
        self._token('}')
        with self._optional():
            self._token('*')
            self._cut()
        self._cut()
        self.ast._define(
            ['exp', 'sep'],
            []
        )

    @tatsumasu('LeftJoin')
    def _left_join_(self):  # noqa
        self._separator_()
        self.name_last_node('sep')
        self._token('<{')
        self._cut()
        self._expre_()
        self.name_last_node('exp')
        self._token('}')
        with self._group():
            with self._choice():
                with self._option():
                    self._token('+')
                with self._option():
                    self._token('-')
                self._error('no available options')
        self._cut()
        self.ast._define(
            ['exp', 'sep'],
            []
        )

    @tatsumasu('RightJoin')
    def _right_join_(self):  # noqa
        self._separator_()
        self.name_last_node('sep')
        self._token('>{')
        self._cut()
        self._expre_()
        self.name_last_node('exp')
        self._token('}')
        with self._group():
            with self._choice():
                with self._option():
                    self._token('+')
                with self._option():
                    self._token('-')
                self._error('no available options')
        self._cut()
        self.ast._define(
            ['exp', 'sep'],
            []
        )

    @tatsumasu()
    def _separator_(self):  # noqa
        with self._choice():
            with self._option():
                self._group_()
            with self._option():
                self._token_()
            with self._option():
                self._constant_()
            with self._option():
                self._any_()
            with self._option():
                self._pattern_()
            self._error('no available options')

    @tatsumasu('PositiveClosure')
    def _positive_closure_(self):  # noqa
        self._token('{')
        self._expre_()
        self.name_last_node('@')
        self._token('}')
        with self._group():
            with self._choice():
                with self._option():
                    self._token('-')
                with self._option():
                    self._token('+')
                self._error('no available options')
        self._cut()

    @tatsumasu('Closure')
    def _closure_(self):  # noqa
        self._token('{')
        self._expre_()
        self.name_last_node('@')
        self._token('}')
        with self._optional():
            self._token('*')
        self._cut()

    @tatsumasu('EmptyClosure')
    def _empty_closure_(self):  # noqa
        self._token('{')
        self._void()
        self.name_last_node('@')
        self._token('}')

    @tatsumasu('Optional')
    def _optional_(self):  # noqa
        self._token('[')
        self._cut()
        self._expre_()
        self.name_last_node('@')
        self._token(']')
        self._cut()

    @tatsumasu('Special')
    def _special_(self):  # noqa
        self._token('?(')
        self._cut()
        self._pattern('.*?(?!\\)\\?)')
        self.name_last_node('@')
        self._token(')?')
        self._cut()

    @tatsumasu('Lookahead')
    def _lookahead_(self):  # noqa
        self._token('&')
        self._cut()
        self._term_()
        self.name_last_node('@')

    @tatsumasu('NegativeLookahead')
    def _negative_lookahead_(self):  # noqa
        self._token('!')
        self._cut()
        self._term_()
        self.name_last_node('@')

    @tatsumasu('SkipTo')
    def _skip_to_(self):  # noqa
        self._token('->')
        self._cut()
        self._term_()
        self.name_last_node('@')

    @tatsumasu()
    def _atom_(self):  # noqa
        with self._choice():
            with self._option():
                self._cut_()
            with self._option():
                self._cut_deprecated_()
            with self._option():
                self._token_()
            with self._option():
                self._constant_()
            with self._option():
                self._call_()
            with self._option():
                self._pattern_()
            with self._option():
                self._eof_()
            self._error('no available options')

    @tatsumasu('RuleRef')
    def _call_(self):  # noqa
        self._word_()

    @tatsumasu('Void')
    def _void_(self):  # noqa
        self._token('()')
        self._cut()

    @tatsumasu('Cut')
    def _cut_(self):  # noqa
        self._token('~')
        self._cut()

    @tatsumasu('Cut')
    def _cut_deprecated_(self):  # noqa
        self._token('>>')
        self._cut()

    @tatsumasu()
    def _known_name_(self):  # noqa
        self._name_()
        self._cut()

    @tatsumasu()
    def _name_(self):  # noqa
        self._word_()

    @tatsumasu('Constant')
    def _constant_(self):  # noqa
        self._pattern('`')
        self._cut()
        self._literal_()
        self.name_last_node('@')
        self._pattern('`')

    @tatsumasu('Token')
    def _token_(self):  # noqa
        with self._choice():
            with self._option():
                self._string_()
            with self._option():
                self._raw_string_()
            self._error('no available options')

    @tatsumasu()
    def _literal_(self):  # noqa
        with self._choice():
            with self._option():
                self._string_()
            with self._option():
                self._raw_string_()
            with self._option():
                self._boolean_()
            with self._option():
                self._word_()
            with self._option():
                self._hex_()
            with self._option():
                self._float_()
            with self._option():
                self._int_()
            self._error('no available options')

    @tatsumasu()
    def _string_(self):  # noqa
        self._STRING_()

    @tatsumasu()
    def _raw_string_(self):  # noqa
        self._token('r')
        self._STRING_()
        self.name_last_node('@')

    @tatsumasu()
    def _STRING_(self):  # noqa
        with self._choice():
            with self._option():
                self._token('"')
                self._cut()
                self._pattern('([^"\\n]|\\\\"|\\\\\\\\)*')
                self.name_last_node('@')
                self._token('"')
                self._cut()
            with self._option():
                self._token("'")
                self._cut()
                self._pattern("([^'\\n]|\\\\'|\\\\\\\\)*")
                self.name_last_node('@')
                self._token("'")
                self._cut()
            self._error('no available options')

    @tatsumasu()
    def _hex_(self):  # noqa
        self._pattern('0[xX](\\d|[a-fA-F])+')

    @tatsumasu()
    def _float_(self):  # noqa
        self._pattern('[-+]?(?:\\d+\\.\\d*|\\d*\\.\\d+)(?:[Ee][-+]?\\d+)?')

    @tatsumasu()
    def _int_(self):  # noqa
        self._pattern('[-+]?\\d+')

    @tatsumasu()
    def _path_(self):  # noqa
        self._pattern('(?!\\d)\\w+(::(?!\\d)\\w+)+')

    @tatsumasu()
    def _word_(self):  # noqa
        self._pattern('(?!\\d)\\w+')

    @tatsumasu('Any')
    def _any_(self):  # noqa
        self._token('/./')

    @tatsumasu('Pattern')
    def _pattern_(self):  # noqa
        self._regexes_()

    @tatsumasu()
    def _regexes_(self):  # noqa

        def sep0():
            self._token('+')

        def block0():
            self._regex_()
        self._positive_gather(block0, sep0)

    @tatsumasu()
    def _regex_(self):  # noqa
        with self._choice():
            with self._option():
                self._token('/')
                self._cut()
                self._pattern('([^/\\\\]|\\\\/|\\\\.)*')
                self.name_last_node('@')
                self._token('/')
                self._cut()
            with self._option():
                self._token('?/')
                self._cut()
                self._pattern('(.|\\n)*?(?=/\\?)')
                self.name_last_node('@')
                self._pattern('/\\?+')
                self._cut()
            with self._option():
                self._token('?')
                self._STRING_()
                self.name_last_node('@')
            self._error('no available options')

    @tatsumasu()
    def _boolean_(self):  # noqa
        with self._choice():
            with self._option():
                self._token('True')
            with self._option():
                self._token('False')
            self._error('no available options')

    @tatsumasu('EOF')
    def _eof_(self):  # noqa
        self._token('$')
        self._cut()


class EBNFBootstrapSemantics(object):
    def start(self, ast):  # noqa
        return ast

    def grammar(self, ast):  # noqa
        return ast

    def directive(self, ast):  # noqa
        return ast

    def keywords(self, ast):  # noqa
        return ast

    def keyword(self, ast):  # noqa
        return ast

    def paramdef(self, ast):  # noqa
        return ast

    def rule(self, ast):  # noqa
        return ast

    def decorator(self, ast):  # noqa
        return ast

    def params(self, ast):  # noqa
        return ast

    def first_param(self, ast):  # noqa
        return ast

    def kwparams(self, ast):  # noqa
        return ast

    def pair(self, ast):  # noqa
        return ast

    def expre(self, ast):  # noqa
        return ast

    def choice(self, ast):  # noqa
        return ast

    def sequence(self, ast):  # noqa
        return ast

    def element(self, ast):  # noqa
        return ast

    def rule_include(self, ast):  # noqa
        return ast

    def named(self, ast):  # noqa
        return ast

    def named_list(self, ast):  # noqa
        return ast

    def named_single(self, ast):  # noqa
        return ast

    def override(self, ast):  # noqa
        return ast

    def override_list(self, ast):  # noqa
        return ast

    def override_single(self, ast):  # noqa
        return ast

    def override_single_deprecated(self, ast):  # noqa
        return ast

    def term(self, ast):  # noqa
        return ast

    def group(self, ast):  # noqa
        return ast

    def gather(self, ast):  # noqa
        return ast

    def positive_gather(self, ast):  # noqa
        return ast

    def normal_gather(self, ast):  # noqa
        return ast

    def join(self, ast):  # noqa
        return ast

    def positive_join(self, ast):  # noqa
        return ast

    def normal_join(self, ast):  # noqa
        return ast

    def left_join(self, ast):  # noqa
        return ast

    def right_join(self, ast):  # noqa
        return ast

    def separator(self, ast):  # noqa
        return ast

    def positive_closure(self, ast):  # noqa
        return ast

    def closure(self, ast):  # noqa
        return ast

    def empty_closure(self, ast):  # noqa
        return ast

    def optional(self, ast):  # noqa
        return ast

    def special(self, ast):  # noqa
        return ast

    def lookahead(self, ast):  # noqa
        return ast

    def negative_lookahead(self, ast):  # noqa
        return ast

    def skip_to(self, ast):  # noqa
        return ast

    def atom(self, ast):  # noqa
        return ast

    def call(self, ast):  # noqa
        return ast

    def void(self, ast):  # noqa
        return ast

    def cut(self, ast):  # noqa
        return ast

    def cut_deprecated(self, ast):  # noqa
        return ast

    def known_name(self, ast):  # noqa
        return ast

    def name(self, ast):  # noqa
        return ast

    def constant(self, ast):  # noqa
        return ast

    def token(self, ast):  # noqa
        return ast

    def literal(self, ast):  # noqa
        return ast

    def string(self, ast):  # noqa
        return ast

    def raw_string(self, ast):  # noqa
        return ast

    def STRING(self, ast):  # noqa
        return ast

    def hex(self, ast):  # noqa
        return ast

    def float(self, ast):  # noqa
        return ast

    def int(self, ast):  # noqa
        return ast

    def path(self, ast):  # noqa
        return ast

    def word(self, ast):  # noqa
        return ast

    def any(self, ast):  # noqa
        return ast

    def pattern(self, ast):  # noqa
        return ast

    def regexes(self, ast):  # noqa
        return ast

    def regex(self, ast):  # noqa
        return ast

    def boolean(self, ast):  # noqa
        return ast

    def eof(self, ast):  # noqa
        return ast


def main(filename, start=None, **kwargs):
    if start is None:
        start = 'start'
    if not filename or filename == '-':
        text = sys.stdin.read()
    else:
        with open(filename) as f:
            text = f.read()
    parser = EBNFBootstrapParser()
    return parser.parse(text, rule_name=start, filename=filename, **kwargs)


if __name__ == '__main__':
    import json
    from tatsu.util import asjson

    ast = generic_main(main, EBNFBootstrapParser, name='EBNFBootstrap')
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(asjson(ast), indent=2))
    print()
