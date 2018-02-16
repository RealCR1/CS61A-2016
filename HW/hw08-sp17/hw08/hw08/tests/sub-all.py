test = {
  'name': 'sub-all',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'cases': [
        {
          'code': r"""
          scm> (sub-all '(go ((bears))) '(go bears) '(big game))
          (big ((game)))
          """,
        },
        {
          'code': r"""
          scm> (sub-all '((4 calling birds) (3 french hens) (2 turtle doves))
          ....     '(1 2 3 4)
          ....     '(one two three four))
          ((four calling birds) (three french hens) (two turtle doves))
          """,
          'locked': False,
        },
      ],
      'setup': r"""
      scm> (load 'hw08)
      """,
    },
  ]
}
