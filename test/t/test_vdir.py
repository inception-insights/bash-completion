import pytest


class TestVdir(object):

    @pytest.mark.complete("vdir ")
    def test_1(self, completion):
        assert completion.list