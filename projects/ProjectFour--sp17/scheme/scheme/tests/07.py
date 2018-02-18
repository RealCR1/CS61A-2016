test = {
  'name': 'Problem 7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'Pair(A, nil), where: A is the quoted expression',
          'choices': [
            r"""
            Pair('quote', Pair(A, nil)), where:
                A is the quoted expression
            """,
            r"""
            [A], where:
                A is the quoted expression
            """,
            r"""
            Pair(A, nil), where:
                A is the quoted expression
            """,
            r"""
            A, where:
                A is the quoted expression
            """
          ],
          'hidden': False,
          'locked': False,
          'question': 'What is the structure of the expressions argument to do_quote_form?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (quote hello)
          hello
          scm> 'hello
          hello
          scm> ''hello
          (quote hello)
          scm> (quote (1 2))
          (1 2)
          scm> '(1 2)
          (1 2)
          scm> (quote (1 . 2))
          (1 . 2)
          scm> '(1 . (2))
          (1 2)
          scm> (car '(1 2 3))
          1
          scm> (cdr '(1 2))
          (2)
          scm> (car (car '((1))))
          1
          scm> (quote 3)
          3
          scm> (eval (cons 'car '('(4 2))))
          4
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> read_line(" (quote x) ")
          55894b325c4c2817733a8a1223c79f1e
          # locked
          >>> read_line(" 'x ")
          55894b325c4c2817733a8a1223c79f1e
          # locked
          # choice: Pair('x', nil)
          # choice: 'x'
          # choice: Pair('quote', 'x')
          # choice: Pair('quote', Pair('x', nil))
          >>> read_line(" (a b) ")
          6e7962ce0515005f1aa1ece26c1f9f99
          # locked
          # choice: Pair('a', Pair('b', nil))
          # choice: Pair('quote', Pair(Pair('a', Pair('b', nil)), nil))
          # choice: Pair('quote', Pair('a', 'b'))
          # choice: Pair('quote', Pair('a', Pair('b', nil)))
          >>> read_line(" '(a b) ")
          1af43453acd78705e072b903fe9ce759
          # locked
          # choice: Pair('a', Pair('b', nil))
          # choice: Pair('quote', Pair(Pair('a', Pair('b', nil)), nil))
          # choice: Pair('quote', Pair('a', 'b'))
          # choice: Pair('quote', Pair('a', Pair('b', nil)))
          >>> read_line(" '((a)) ")
          6b34a9dd52ff83f52d5e6953f2d7375f
          # locked
          # choice: Pair('quote', Pair(Pair('a', nil), nil))
          # choice: Pair('quote', Pair(Pair('a', nil), nil), nil)
          # choice: Pair('quote', Pair(Pair('a'), nil))
          # choice: Pair('quote', Pair(Pair('a'), nil), nil)
          # choice: Pair('quote', Pair(Pair(Pair('a', nil), nil), nil))
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
