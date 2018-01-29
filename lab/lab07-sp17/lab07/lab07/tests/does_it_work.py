test = {
  'name': 'Does it work?',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '73021b3085330f2f6455d7ff990cfe70',
          'choices': [
            'No problem, this is a beautiful iterator!',
            'Uh oh, this is missing __next__.',
            'This "iterator" doesn\'t even define __iter__.'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Does IteratorA work?
          
          class IteratorA:
             def __init__(self):
                 self.start = 10
          
             def __next__(self):
                 if self.start > 100:
                     raise StopIteration
                 self.start += 20
                 return self.start
          
             def __iter__(self):
                 return self
          """
        },
        {
          'answer': '8090c5c07311c7650cc04ccff59cd0d1',
          'choices': [
            'No problem, this is a beautiful iterator!',
            'Uh oh, this is missing __next__.',
            'This "iterator" doesn\'t even define __iter__.'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Does IteratorB work?
          
          class IteratorB:
              def __init__(self):
                  self.start = 5
          
              def __iter__(self):
                  return self
          """
        },
        {
          'answer': '8f33bcd5656894a4ebd68f56475df77d',
          'choices': [
            'No problem, this is a beautiful iterator!',
            'Uh oh, this is missing __next__.',
            'This "iterator" doesn\'t even define __iter__.'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Does IteratorC work?
          
          class IteratorC:
              def __init__(self):
                  self.start = 5
          
              def __next__(self):
                  if self.start == 10:
                      raise StopIteration
                  self.start += 1
                  return self.start
          """
        },
        {
          'answer': '73021b3085330f2f6455d7ff990cfe70',
          'choices': [
            'No problem, this is a beautiful iterator!',
            'Uh oh, this is missing __next__.',
            'This "iterator" doesn\'t even define __iter__.'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Does IteratorD work?
          
          class IteratorD:
              def __init__(self):
                  self.start = 1
          
              def __next__(self):
                  self.start += 1
                  return self.start
          
              def __iter__(self):
                  return self
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
