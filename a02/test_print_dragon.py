from unittest import TestCase
from unittest.mock import patch
import io

from dnd import print_dragon

class TestPrintDragon(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_dragon(self, mock_stdout):
        print_dragon()
        expected = r"""


                        ___====-_  _-====___
                  _--^^^#####//      \\#####^^^--_
               _-^##########// (    ) \\##########^-_
              -############//  |\^^/|  \\############-
            _/############//   (@::@)   \\############\_
           /#############((     \\//     ))#############\
          -###############\\    (oo)    //###############-
         -#################\\  / VV \  //#################-
        -###################\\/      \//###################-
        #/|##########/\######(   /\   )######/\##########|\#_
       |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
       `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
          `   `  `      `   / | |  | | \   '      '  '   '
                           (  | |  | |  )
                          __\ | |  | | /__
                         (vvv(VVV)(VVV)vvv)
"""
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)


