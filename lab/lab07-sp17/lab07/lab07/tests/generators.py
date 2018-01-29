test = {
  'name': 'Generators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def generator():
          ...     print("Starting here")
          ...     i = 0
          ...     while i < 6:
          ...         print("Before yield")
          ...         yield i
          ...         print("After yield")
          ...         i += 1
          >>> g = generator() # what type of object is this?
          >>> g == iter(g) # equivalent of g.__iter__()
          a60487f0dcc07e26f48fbf3cf021859d
          # locked
          >>> next(g) # equivalent of g.__next__()
          8e1a785c4684c82f3dbcd8c2dfb8816f
          45a5c789d101431e6829dcf99ad79522
          67a37433345d12b97afe4885b1fa6019
          # locked
          >>> next(g)
          d9fee1558dd630d5324d80e1d3ef6714
          45a5c789d101431e6829dcf99ad79522
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> next(g)
          d9fee1558dd630d5324d80e1d3ef6714
          45a5c789d101431e6829dcf99ad79522
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def generator():
          ...     print("Starting")
          ...     i = 2
          ...     while i < 6:
          ...         print("foo", i)
          ...         yield i
          ...         i += 1
          ...         print("bar")
          ...         yield i*2
          ...         i += 2
          >>> h = generator()
          >>> iter(h) == h
          a60487f0dcc07e26f48fbf3cf021859d
          # locked
          >>> next(h)
          c76bdaec19b0eeaf118a6ea61b55396c
          903a9300dbe57c71939b2fb26f55bae9
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> next(h)
          815bef1327d762bf8c7adf656d04db44
          5c5050141c04dffb4cedd647366d0e59
          # locked
          >>> next(h)
          0d59a64ffa258b73c865ddc857e5227c
          b93035e430af620ab1eedc5adaea0a82
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
