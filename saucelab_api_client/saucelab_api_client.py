from saucelab_api_client.category import RealDevices, Insights, Storage
from saucelab_api_client.session import Session


class SauceLab(Session):

    @property
    def devices(self):
        return RealDevices(self)

    @property
    def insights(self):
        return Insights(self)

    @property
    def storage(self):
        return Storage(self)
