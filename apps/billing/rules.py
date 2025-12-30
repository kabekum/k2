from decimal import Decimal

class BillingRuleEngine:
    """
    Supports insurance & government billing constraints
    """

    @staticmethod
    def apply_rules(time_entries, max_daily_hours=8, rate_cap=None):
        total = Decimal('0.00')
        daily_hours = {}

        for entry in time_entries:
            date = entry.created_at.date()
            daily_hours.setdefault(date, Decimal('0.00'))
            daily_hours[date] += entry.hours

            if daily_hours[date] > max_daily_hours:
                entry.hours = max_daily_hours - (daily_hours[date] - entry.hours)

            rate = entry.user.profile.hourly_rate
            if rate_cap:
                rate = min(rate, rate_cap)

            total += entry.hours * rate

        return total
