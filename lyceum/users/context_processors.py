from users.models import Profile
from datetime import datetime

def get_birthday_people(request):
    birthday_people = Profile.objects.filter(
        birthday__endswith=datetime.now().strftime("-%m-%d"),
        private_profile=False,
    ).prefetch_related('user')
    return {'birthday_people': birthday_people}
