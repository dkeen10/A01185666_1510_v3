from unittest import TestCase
from unittest.mock import patch

from dnd import generate_syllable, generate_name


class TestGenerateName(TestCase):

    @patch(generate_syllable, "ro")
    @patch(generate_syllable, "ba")
    @patch ("syllable", 2)
    def test_generate_name(self, syllable, mock_generate_syllable, moc_syllable):

