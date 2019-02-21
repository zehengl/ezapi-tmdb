from . import polite

company_id = 1  # Lucasfilm


@polite
def test_get_company_details(tmdb):
    assert tmdb.get_company_details(company_id) is not None


@polite
def test_get_company_alternative_names(tmdb):
    assert tmdb.get_company_alternative_names(company_id) is not None


@polite
def test_get_company_images(tmdb):
    assert tmdb.get_company_images(company_id) is not None
