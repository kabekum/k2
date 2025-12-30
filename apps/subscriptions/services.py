class SubscriptionService:

    @staticmethod
    def can_create_user(firm):
        sub = firm.subscription
        return firm.user_set.count() < sub.plan.max_users

    @staticmethod
    def can_create_matter(firm):
        sub = firm.subscription
        return firm.matter_set.count() < sub.plan.max_matters
