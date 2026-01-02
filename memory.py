from typing import List, Dict, Any


class AgentMemory:
    """
    Simple in-memory storage for the agent.
    Keeps track of what has already been analyzed and shown.
    """

    def __init__(self):
        # Store path of the currently loaded dataset
        self.dataset_path = None

        # Store profiler output
        self.profile: Dict[str, Any] = {}

        # Store generated insights
        self.insights: List[Dict[str, Any]] = []

        # Track which insight types have already been rendered
        self.rendered_insight_types: set = set()

    def store_dataset(self, path: str):
        """
        Save the dataset path.
        """
        self.dataset_path = path

    def store_profile(self, profile: Dict[str, Any]):
        """
        Save the profiling result.
        """
        self.profile = profile

    def store_insights(self, insights: List[Dict[str, Any]]):
        """
        Save the generated insights.
        """
        self.insights = insights

    def mark_rendered(self, insight_type: str):
        """
        Mark an insight type as already visualized.
        """
        self.rendered_insight_types.add(insight_type)

    def is_rendered(self, insight_type: str) -> bool:
        """
        Check if an insight type has already been visualized.
        """
        return insight_type in self.rendered_insight_types
