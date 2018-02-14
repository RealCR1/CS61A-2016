test = {
  'name': 'Sets',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> a = [1, 1, 2, 2, 3, 3]
          >>> a = set(a)
          >>> len(a)
          350815b30c2ebeb01da1870d87346e85
          # locked
          >>> sorted(a) # sorted(iterable) returns a new sorted list
          e750459b44661c8bec07948c01f391c8
          # locked
          >>> a.add(4)
          >>> a.add(4)
          >>> a.remove(4)
          >>> 4 in a
          5cab3718504a1a0efe676cfe3e714ac2
          # locked
          >>> a = {1, 4, 12, 1000}
          >>> sum(a)
          aa349c9b1fd4bdb31f8a6cc89e36cdd5
          # locked
          >>> b = {1, 2, 4}
          >>> sorted(a.intersection(b))
          18cf1ea53747a9f4749c22b4429f0a65
          # locked
          >>> sorted(a & b)
          18cf1ea53747a9f4749c22b4429f0a65
          # locked
          >>> sorted(a.union(b))
          2288f5824ccb6ad6d9376b602c32dd6b
          # locked
          >>> sorted(a | b)
          2288f5824ccb6ad6d9376b602c32dd6b
          # locked
          >>> sorted(a - b)
          9ae924172e4423ee31d8972db151ed05
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> fruits = set(['apple', 'banana', 'tomato', 'apple'])
          >>> pizza = set(['cheese', 'tomato', 'flour'])
          >>> 'pepperoni' in pizza
          5cab3718504a1a0efe676cfe3e714ac2
          # locked
          >>> fruits & pizza
          b0577b6fc75110023771963a9ca328cb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> t = [314, 15]
          >>> u = {89, 7, 15}
          >>> sorted(set(t) | u)
          2939edd9b032eab396a1259b5d0fce52
          # locked
          >>> u.add(6)
          >>> set(t) - u
          01d3b691cf21cdab10bebc853c3b6231
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
