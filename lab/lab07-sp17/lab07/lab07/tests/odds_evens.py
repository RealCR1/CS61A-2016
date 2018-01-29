test = {
  'name': 'Odds and Evens',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class OddNaturalsIterator():
          ...     def __init__(self):
          ...         self.current = 1
          ...     def __next__(self):
          ...         result = self.current
          ...         self.current += 2
          ...         return result
          ...     def __iter__(self):
          ...         return self
          >>> odds = OddNaturalsIterator()
          >>> odd_iter1 = iter(odds)
          >>> odd_iter2 = iter(odds)
          >>> next(odd_iter1)
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> next(odd_iter1)
          9a023de211dac9bf8558350f5fa3bdca
          # locked
          >>> next(odd_iter1)
          b93035e430af620ab1eedc5adaea0a82
          # locked
          >>> next(odd_iter2)
          54668fb96734d9b52a588e4f9ab6ed24
          # locked
          >>> next(odd_iter1)
          0d66d07b30bc2b1b6722bd627905704c
          # locked
          >>> next(odd_iter2)
          44567d7ece823e5a44bf86d110909d16
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> class EvenNaturalsIterator():
          ...     def __init__(self):
          ...         self.current = 0
          ...     def __next__(self):
          ...         result = self.current
          ...         self.current += 2
          ...         return result
          ...     def __iter__(self):
          ...         return EvenNaturalsIterator()
          >>> evens = EvenNaturalsIterator()
          >>> even_iter1 = iter(evens)
          >>> even_iter2 = iter(evens)
          >>> next(even_iter1)
          67a37433345d12b97afe4885b1fa6019
          # locked
          >>> next(even_iter1)
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> next(even_iter1)
          f2991d685f624ad59b79213e20800653
          # locked
          >>> next(even_iter2)
          67a37433345d12b97afe4885b1fa6019
          # locked
          >>> next(even_iter2)
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> class DoubleIterator:
          ...     def __init__(self):
          ...         self.current = 2
          ...     def __next__(self):
          ...         result = self.current
          ...         self.current += result
          ...         return result
          ...     def __iter__(self):
          ...         return DoubleIterator()
          >>> doubleI = DoubleIterator()
          >>> dIter = iter(doubleI)
          >>> next(doubleI)
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> next(doubleI)
          f2991d685f624ad59b79213e20800653
          # locked
          >>> next(dIter)
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> next(dIter)
          f2991d685f624ad59b79213e20800653
          # locked
          >>> next(doubleI)
          2ce69256b3a4325ad04f8cf5c5dd6244
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> class ThreeIterator:
          ...     def __init__(self):
          ...         self.current = 10
          ...     def __next__(self):
          ...         result = self.current
          ...         self.current -= 3
          ...         return result
          ...     def __iter__(self):
          ...         return self
          >>> threeI = ThreeIterator()
          >>> tIter = iter(threeI)
          >>> next(threeI)
          700368183fe24919898aaeca9b976fbd
          # locked
          >>> next(threeI)
          54668fb96734d9b52a588e4f9ab6ed24
          # locked
          >>> next(tIter)
          f2991d685f624ad59b79213e20800653
          # locked
          >>> next(tIter)
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> next(threeI)
          c68f0f58dc96a43cc84e484d0ec63e61
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
