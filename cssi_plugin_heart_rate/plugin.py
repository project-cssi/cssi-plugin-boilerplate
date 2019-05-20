from cssi.plugin import CSSIPlugin, ContributorPlugin, PluginType


class CSSIPluginHeartRate(CSSIPlugin, ContributorPlugin):
    def get_info(self):
        return {
            "name": "heart_rate_cssi_plugin",
            "type": PluginType.CONTRIBUTOR
        }

    def generate_final_score(self, scores):
        return 100

    def generate_unit_score(self, head_frame):
        return 2
