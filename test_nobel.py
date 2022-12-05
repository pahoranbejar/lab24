from byu_pytest_utils import with_import, max_score, test_files


@max_score(6)
@with_import('nobel')
def test_longest_name_small(longest_name):
    observed = longest_name(test_files / "nobel-small.json")
    expected = "Abdulrazak Gurnah"
    assert observed == expected


@max_score(6)
@with_import('nobel')
def test_longest_name(longest_name):
    observed = longest_name(test_files / "nobel.json")
    expected = "Paul Henri d'Estournelles de Constant"
    assert observed == expected


@max_score(6)
@with_import('nobel')
def test_most_recipients_small(most_recipients):
    observed = most_recipients(test_files / "nobel-small.json")
    expected = "2021"
    assert observed == expected


@max_score(6)
@with_import('nobel')
def test_most_recipients(most_recipients):
    observed = most_recipients(test_files / "nobel.json")
    expected = "2001"
    assert observed == expected
