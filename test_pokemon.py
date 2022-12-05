from byu_pytest_utils import with_import, test_files, max_score


@max_score(6)
@with_import('pokemon')
def test_pokemon(longest_name):
    longest = longest_name(test_files / 'pokedex.json')
    crabominable = {
        'id': 740,
        'name': {
            'english': 'Crabominable',
            'japanese': 'ケケンカニ',
            'chinese': '好胜毛蟹',
            'french': 'Crabominable'
        },
        'type': ['Fighting', 'Ice'],
        'base': {'HP': 97, 'Attack': 132, 'Defense': 77, 'Sp. Attack': 62, 'Sp. Defense': 67, 'Speed': 43}
    }
    assert longest == crabominable
