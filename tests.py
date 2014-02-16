import unittest
import streamFuncs

class allTests(unittest.TestCase):
  def test_getTwitchStreams(self):
    self.assertEqual(len(streamFuncs.getTwitchStreams()[u'streams']), 25)

if __name__ == '__main__':
  unittest.main()
