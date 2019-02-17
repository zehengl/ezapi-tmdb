def test_get_company_details(tmdb):
    assert tmdb.get_company_details(1) is not None


def test_get_company_alternative_names(tmdb):
    assert tmdb.get_company_alternative_names(1) is not None


def test_get_company_images(tmdb):
    assert tmdb.get_company_images(1) is not None
