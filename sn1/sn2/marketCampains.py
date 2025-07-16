#!/usr/bin/env python3

from collections import Counter
from typing import List, Dict, Tuple

class CampaignAnalyzer:
    def __init__(self, email_campaign: List[str], social_campaign: List[str], webinar_attendees: List[str]):
        self.email_set = set(email_campaign)
        self.social_set = set(social_campaign)
        self.webinar_set = set(webinar_attendees)
        self.combined = email_campaign + social_campaign + webinar_attendees
        self.frequency_map = Counter(self.combined)

    def intersection_all(self) -> List[str]:
        """Users reached by all three campaigns."""
        return sorted(self.email_set & self.social_set & self.webinar_set)

    def email_exclusive(self) -> List[str]:
        """Users only in email_campaign."""
        return sorted(self.email_set - (self.social_set | self.webinar_set))

    def non_repeating_users(self) -> List[str]:
        """Users who appear in only one campaign."""
        return sorted([user for user, count in self.frequency_map.items() if count == 1])

    def email_social_diff(self) -> List[str]:
        """Users who appear in either email or social, but not both."""
        return sorted(self.email_set ^ self.social_set)

    def campaign_frequency_map(self) -> Dict[str, int]:
        """Returns frequency of user appearance across all campaigns."""
        return dict(self.frequency_map)

    def analyze(self) -> Dict[str, List[str] or Dict[str, int]]:
        """Aggregate method to return all analyses in one call."""
        return {
            "intersection_all": self.intersection_all(),
            "email_exclusive": self.email_exclusive(),
            "non_repeating_users": self.non_repeating_users(),
            "email_social_diff": self.email_social_diff(),
            "user_frequency": self.campaign_frequency_map()
        }


