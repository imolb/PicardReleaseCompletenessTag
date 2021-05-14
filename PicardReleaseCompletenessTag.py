PLUGIN_NAME = "Release Completeness Tag"
PLUGIN_AUTHOR = "imolb"
PLUGIN_DESCRIPTION = """
Set a user defined tag TXXX:releasecompleteness if a release is complete i.e. 
all tracks of the release exists.
This is useful to filter in the playback app for only complete releases
(requires an app capable of filtering by user defined tags).
"""
PLUGIN_VERSION = '0.1'
PLUGIN_API_VERSIONS = ['2.0', '2.1', '2.2']
PLUGIN_LICENSE = "GPL-3.0-or-later"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-3.0.html"

USER_DEFINED_TAG_NAME = "releasecompleteness"

from picard.file import register_file_post_addition_to_track_processor, register_file_post_removal_from_track_processor


def set_release_completeness_tag(track, file_input):
    album = track.album
    for file in album.iterfiles():
        if album.is_complete():
            file.metadata[USER_DEFINED_TAG_NAME] = "complete"
        else:
            file.metadata[USER_DEFINED_TAG_NAME] = "not complete"


register_file_post_addition_to_track_processor(set_release_completeness_tag)
register_file_post_removal_from_track_processor(set_release_completeness_tag)
