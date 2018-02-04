test = {
  'name': 'What Would Scheme Print?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cons 1 2)
          6b39ef7e7fc4b14a386d119ced16ece6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cons 1 (cons 2 nil))
          5ceacf97ccefe7d64916c8d72dfb2b48
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (car (cons 1 (cons 2 nil)))
          7cd20da6435c318b417f99ab831ac85e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cdr (cons 1 (cons 2 nil)))
          36f31b0ebd049141c21558b1c3b4894d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (list 1 2 3)
          31df56b0e4230528bca8a8edc01115c8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (list 1 (cons 2 3))
          41491622701639b247a078bf147fb3d8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> '(1 2 3)
          31df56b0e4230528bca8a8edc01115c8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> '(2 . 3)
          520d602b89020504a7c70fc167d6403e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> '(2 . (3))  ; Recall dot notation rule
          3c66468104773f61b2e74f076c107115
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (equal? '(1 . (2 . 3)) (cons 1 (cons 2 (cons 3 nil))))
          a4015fdedc66a98a3d74622fb751ee0a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (equal? '(1 . (2 . 3)) (cons 1 (cons 2 3)))
          b2fd0f50cc6b6d79b0b844be1c0e8231
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (equal? '(1 . (2 . 3)) (list 1 (cons 2 3)))
          a4015fdedc66a98a3d74622fb751ee0a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cons 1 '(list 2 3))  ; Recall quoting
          9b9cf94f8db477d48f973c67acf1842a
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (cons (list 2 (cons 3 4)) nil)
          cff54d1b2a6472d414536960442f43a9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (car (cdr '(127 . ((131 . (137))))))
          add3bd19500cdc7abcbe33081f5ab21f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (equal? '(1 . ((2 . 3))) (cons 1 (cons (cons 2 3) nil)))
          b2fd0f50cc6b6d79b0b844be1c0e8231
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> '(cons 4 (cons (cons 6 8) ()))
          beed0382fff95ecdd5f05fad62b13daf
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
