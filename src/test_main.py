import pytest

from functions.functions import generate_list,read_file,validate_coincidence


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("data/Employees.txt", [
            'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
            'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00',
            'ANDRES=MO10:00-12:00,SU20:00-21:00'
        ]),
        ("data/Employees.csv",[
            'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
            'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00',
            'ANDRES=MO10:00-12:00,SU20:00-21:00',
            'MARCO=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00',
            'ALAN=TH12:00-14:00,SU20:00-21:00',
            'ISABELA=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'])
    ]
)
def test_read_file_data(filename, expected):
    list = []
    list = read_file(filename)
    assert list == expected,"It should return a list with data"

@pytest.mark.parametrize(
    "list, expected",
    [
        (
            [
                'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
                'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00', 'ANDRES=MO10:00-12:00,SU20:00-21:00'
            ],
            [
                {'employee': 'Rene', 'schedule': ['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00']},
                {'employee': 'Astrid', 'schedule': ['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00']}, 
                {'employee': 'Andres', 'schedule': ['MO10:00-12:00', 'SU20:00-21:00']}
            ]
        )
    ]
)
def test_generate_list(list, expected):
    assert generate_list(list) == expected, "It should return a list with dictionaries"


@pytest.mark.parametrize(
    "list, expected",
    [
        (
            [
                'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
                'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00', 'ANDRES=MO10:00-12:00,SU20:00-21:00'
            ],
            1
        )
    ]
)
def test_generate_list_with_value(list, expected):
    assert len(generate_list(list)) >= expected, "It should return a list at least one value"

@pytest.mark.parametrize(
    "list, expected",
    [
        (
            [],
            []
        )
    ]
)
def test_generate_list_empty(list, expected):
    assert generate_list(list) == expected, "It should return an empty list"

    
@pytest.mark.parametrize(
    "list, expected",
    [
        (
            [],
            []
        )
    ]
)
def test_validate_generate_list_empty(list, expected):
    assert validate_coincidence(list) == expected, "It should return an empty list"

@pytest.mark.parametrize(
    "list, expected",
    [
        (
            [
                {'employee': 'Rene', 'schedule': ['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00']},
                {'employee': 'Astrid', 'schedule': ['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00']}, 
                {'employee': 'Andres', 'schedule': ['MO10:00-12:00', 'SU20:00-21:00']}
            ],
            1
        )
    ]
)
def test_validate_generate_with_value(list, expected):
    assert len(validate_coincidence(list)) >= expected, "It should return a list at least one value"

@pytest.mark.parametrize(
    "list, expected",
    [
        (
            [
                {'employee': 'Rene', 'schedule': ['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00']},
                {'employee': 'Astrid', 'schedule': ['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00']}, 
                {'employee': 'Andres', 'schedule': ['MO10:00-12:00', 'SU20:00-21:00']}
            ],
            ['Rene - Astrid : 2 ', 'Rene - Andres : 2 ', 'Astrid - Andres : 2 '])
    ]
)
def test_validate_coincidence(list, expected):
    assert validate_coincidence(list) == expected, "It should return a list with coincidences in schedules"
