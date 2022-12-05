from byu_pytest_utils import with_import, max_score, test_files


@max_score(0)
@with_import('airlines')
def test_greatest_ratio_small(greatest_ratio):
    observed = greatest_ratio(test_files / "airlines-small.json")
    expected = 'Boston, MA: Logan International'
    assert observed == expected


@max_score(0)
@with_import('airlines')
def test_greatest_ratio(greatest_ratio):
    observed = greatest_ratio(test_files / "airlines.json")
    expected = 'Atlanta, GA: Hartsfield-Jackson Atlanta International'
    assert observed == expected


@max_score(0)
@with_import('airlines')
def test_security_delays_small(security_delays):
    observed = security_delays(test_files / "airlines-small.json")
    expected = 2003
    assert observed == expected


@max_score(0)
@with_import('airlines')
def test_security_delays(security_delays):
    observed = security_delays(test_files / "airlines.json")
    expected = 2006
    assert observed == expected


@max_score(0)
@with_import('airlines')
def test_weather_delays_small(weather_delays):
    observed = weather_delays(test_files / "airlines-small.json")
    expected = ('Boston, MA: Logan International', 2003)
    assert observed == expected


@max_score(0)
@with_import('airlines')
def test_weather_delays(weather_delays):
    observed = weather_delays(test_files / "airlines.json")
    expected = ('Atlanta, GA: Hartsfield-Jackson Atlanta International', 2007)
    assert observed == expected
