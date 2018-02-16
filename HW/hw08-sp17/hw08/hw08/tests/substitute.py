test = {
  'name': 'substitute',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'cases': [
        {
          'code': r"""
          scm> (substitute '(c a b) 'b 'l)
          (c a l)
          scm> (substitute '(f e a r s) 'f 'b)
          (b e a r s)
          scm> (substitute '(g (o) o (o)) 'o 'r)
          (g (r) r (r))
          """,
        },
        {
          'code': r"""
          scm> (substitute '((lead guitar) (bass guitar) (rhythm guitar) drums)
          ....               'guitar 'axe)
          ((lead axe) (bass axe) (rhythm axe) drums)
          scm> (substitute '(romeo romeo wherefore art thou romeo) 'romeo 'paris)
          (paris paris wherefore art thou paris)
          scm> (substitute '((to be) or not (to (be))) 'be 'eat)
          ((to eat) or not (to (eat)))
          scm> (substitute '(a b (c) d e) 'foo 'bar)
          (a b (c) d e)
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
