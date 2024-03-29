"""Test f_lib.mixins._del_cached_prop."""

from __future__ import annotations

from functools import cached_property

from f_lib.mixins._del_cached_prop import DelCachedPropMixin


class TestDelCachedPropMixin:
    """Test DelCachedPropMixin."""

    class Kls(DelCachedPropMixin):
        """Used in tests."""

        counter = 0

        @cached_property
        def test_prop(self) -> str:
            """Test property."""
            self.counter += 1
            return "foobar"

    def test__del_cached_property(self) -> None:
        """Test _del_cached_property."""
        obj = self.Kls()
        # ensure suppression is working as expected
        assert obj.counter == 0
        assert not obj._del_cached_property("test_prop")
        assert obj.test_prop == "foobar"
        assert obj.counter == 1
        # ensure value is cached and not being evaluated each call
        assert obj.test_prop == "foobar"
        assert obj.counter == 1
        # this would fail if the suppresion was outside the loop
        assert not obj._del_cached_property("invalid", "test_prop")
        assert obj.test_prop == "foobar"
        assert obj.counter == 2
