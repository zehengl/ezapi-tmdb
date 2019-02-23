from . import polite

tv_episode_group_id = "5b1aa75ac3a368490e016641"


@polite
def test_get_tv_episode_group_details(tmdb):
    assert tmdb.get_tv_episode_group_details(tv_episode_group_id) is not None
