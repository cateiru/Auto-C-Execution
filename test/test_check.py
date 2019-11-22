from main import check


def test_brew_install():
    assert check.brew_install() is None


def test_gcc_install():
    assert check.gcc_install() is None
