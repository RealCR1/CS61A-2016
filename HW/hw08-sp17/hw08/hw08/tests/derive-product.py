test = {
  'name': 'derive-product',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'cases': [
        {
          'code': r"""
          scm> (make-product 2 3)
          6
          scm> (make-product 'x 0)
          0
          scm> (make-product 1 'x)
          x
          scm> (make-product 'a 'x)
          (* a x)
          """,
        }
      ],
      'setup': r"""
      scm> (load 'hw08)
      """,
    },
    {
      'type': 'scheme',
      'cases': [
        {
          'code': r"""
          scm> (derive '(* x y) 'x)
          y
          scm> (derive '(* (* x y) (+ x 3)) 'x)
          (+ (* y (+ x 3)) (* x y))
          """,
          'locked': False,
        }
      ],
      'setup': r"""
      scm> (load 'hw08)
      """,
    },
  ]
}
