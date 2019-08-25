from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL = "https://feeds.mozilla-podcasts.org/irl"
@plugin.route('/')
def main_menu():
    items = [
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://irlpodcast.org/images/episodes/S05E05/artwork.png"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://irlpodcast.org/images/episodes/S05E05/artwork.png"},
   ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup = mainaddon.get_soup(URL)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

if __name__ == '__main__':
    plugin.run()
