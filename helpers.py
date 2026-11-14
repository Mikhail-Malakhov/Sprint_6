from datetime import date, timedelta


def future_date(days):
    """Дата через `days` дней от сегодняшней в формате поля «Когда привезти самокат»."""
    return (date.today() + timedelta(days=days)).strftime('%d.%m.%Y')
