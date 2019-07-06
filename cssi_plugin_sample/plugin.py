import logging
from cssi.plugin import CSSIPlugin, ContributorPlugin, PluginType

logger = logging.getLogger(__name__)


class CSSIPluginSample(CSSIPlugin, ContributorPlugin):
    def get_info(self):
        return {
            "name": "cssi_plugin_sample",
            "type": PluginType.CONTRIBUTOR
        }

    def generate_final_score(self, **kwargs):
        """Generates the final score for the plugin

        Args:
            kwargs: The set of unit scores are sent using the arg `scores`.
                ex: [
                        {"score": 2, "timestamp": "2019-05-28 16:32:45"},
                        {"score": 2, "timestamp": "2019-05-28 16:32:46"}
                    ]

        Returns:
            float: Final score for the plugin

        Examples:
            Read the kwargs and extract the scores argument values. And then use
            the unit scores to calculate the final score.
            >>> scores = []
            >>> if kwargs is not None:
            >>>     for key, value in kwargs.items():
            >>>         if key == "scores":
            >>>             scores = value
            >>>
            >>> # Iterate scores array and calculate the final score
            >>> for score in scores:
            >>>     unit_score = score["score"]
            >>>     # Rest of the logic here
        """

        logger.debug("Generating plugin final score")

        # Return the calculated final score
        return 0

    def generate_unit_score(self, **kwargs):
        """Generates the unit score for the plugin

        Args:
            kwargs: The head frame and the scene frame is provided using the args
                `head_frame` and `scene_frame` respectively.

        Returns:
            float: Unit score for the plugin

        Examples:
            Read the kwargs and extract the head frame and scene frame.
            >>> head_frame = None
            >>> scene_frame = None
            >>> if kwargs is not None:
            >>>     for key, value in kwargs.items():
            >>>         if key == "head_frame":
            >>>             head_frame = value
            >>>         elif key == "scene_frame":
            >>>             scene_frame = value
        """

        logger.debug("Generating plugin final score")

        # Return the calculated unit score
        return 0
