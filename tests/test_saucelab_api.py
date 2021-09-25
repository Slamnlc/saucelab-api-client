import random
import string
import unittest

from parameterized import parameterized

from saucelab_api_client.models.accounts import TeamSearch, UserSearch
from saucelab_api_client.models.file import File
from saucelab_api_client.models.job import Job
from saucelab_api_client.models.platform import Status, AppiumPlatform, WebDriverPlatform
from saucelab_api_client.saucelab_api_client import SauceLab


class MainSauceLab(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sauce_lab = SauceLab()


class CreateSauceLab(MainSauceLab):
    def test_create_service(self):
        self.assertIsInstance(self.sauce_lab.platform.get_status(), Status)


class DeviceTests(MainSauceLab):

    @classmethod
    def setUpClass(cls) -> None:
        super(DeviceTests, cls).setUpClass()
        cls.devices = cls.sauce_lab.devices.devices_list()
        cls.random_device = random.choice(cls.devices)
        cls.jobs = cls.sauce_lab.devices.jobs()
        cls.random_job = random.choice(cls.jobs)

    def test_device_list(self):
        self.assertGreaterEqual(len(self.sauce_lab.devices.devices_list()), 200)

    def test_device_by_id(self):
        self.assertEqual(self.sauce_lab.devices.get_device_by_id(self.random_device.device_id).device_id,
                         self.random_device.device_id)

    def test_available_devices(self):
        self.assertIsInstance(self.sauce_lab.devices.available_devices(), (tuple, list))

    @parameterized.expand([
        [{'min_ram_size': 2000, 'is_tablet': False, 'os_type': 'ios'}],
        [{'min_cpu_cores': 6, 'is_tablet': True, 'os_type': 'android'}],
        [{'manufacturer': 'SamSung', 'max_cpu_cores': 6, 'min_sd_card_size': 2000}]
    ])
    def test_filter_devices(self, param):
        filter_devices = self.sauce_lab.devices.filter_devices(**param)
        for key, value in param.items():
            if key[:3] == 'min':
                self.assertTrue(all((device.__getattribute__(key[4:]) >= value for device in filter_devices)))
            elif key[:3] == 'max':
                self.assertTrue(all((device.__getattribute__(key[4:]) <= value for device in filter_devices)))
            else:
                self.assertTrue(all((str(device.__getattribute__(key)).lower() == str(value).lower()
                                     for device in filter_devices)))

    def test_jobs(self):
        self.assertTrue(all((isinstance(job, Job) for job in self.jobs)))

    def test_job_by_id(self):
        self.assertEqual(self.random_job.job_id, self.sauce_lab.devices.job_by_id(self.random_job.job_id).job_id)


class StorageTests(MainSauceLab):
    @classmethod
    def setUpClass(cls) -> None:
        super(StorageTests, cls).setUpClass()
        cls.files = cls.sauce_lab.storage.files()
        cls.random_file = random.choice(cls.files)
        cls.random_file_id = cls.random_file.file_id

    def test_files(self):
        self.assertTrue(all((isinstance(file, File) for file in self.files)))
        self.assertTrue(all(file.file_id is not None for file in self.files))

    def test_file_by_id(self):
        self.assertEqual(self.random_file_id, self.sauce_lab.storage.file_by_id(self.random_file_id).file_id)

    def test_edit_description(self):
        old_description = self.random_file.description
        new_description = f'New description {"".join(random.choices(string.ascii_letters, k=8))}'
        self.sauce_lab.storage.edit_description(self.random_file_id, new_description)
        self.assertEqual(self.sauce_lab.storage.file_by_id(self.random_file_id).description, new_description)
        self.sauce_lab.storage.edit_description(self.random_file_id, old_description)
        self.assertEqual(self.sauce_lab.storage.file_by_id(self.random_file_id).description, old_description)

    def test_search_by_bundle_id(self):
        files = self.sauce_lab.storage.file_by_bundle_id(self.random_file.metadata.identifier)
        if isinstance(files, (list, tuple)):
            self.assertGreater(len(files), 0)
            for file in files:
                self.assertIsInstance(file, File)
                self.assertEqual(file.metadata.identifier, self.random_file.metadata.identifier)
        else:
            self.assertEqual(files.metadata.identifier, self.random_file.metadata.identifier)


class PlatformTests(MainSauceLab):
    @classmethod
    def setUpClass(cls) -> None:
        super(PlatformTests, cls).setUpClass()

    def test_status(self):
        self.assertIsInstance(self.sauce_lab.platform.get_status(), Status)

    def test_platfroms(self):
        self.assertTrue(all((isinstance(platf, AppiumPlatform) for platf in
                             self.sauce_lab.platform.get_supported_platforms('appium'))))
        self.assertTrue(all((isinstance(platf, WebDriverPlatform) for platf in
                             self.sauce_lab.platform.get_supported_platforms('webdriver'))))

    def test_appium_end_support(self):
        self.assertIsInstance(self.sauce_lab.platform.get_end_of_life_date_appium_versions(), dict)


class TeamTests(MainSauceLab):
    @classmethod
    def setUpClass(cls) -> None:
        super(TeamTests, cls).setUpClass()
        cls.teams = cls.sauce_lab.accounts.account_team.teams()
        cls.random_team = random.choice(cls.teams)

    def test_get_teams(self):
        self.assertTrue(all((isinstance(team, TeamSearch) for team in self.teams)))
        self.assertTrue(all(team.team_id is not None for team in self.teams))

    def test_team_search(self):
        self.assertEqual(self.sauce_lab.accounts.account_team.get_team(self.random_team.team_id).team_id,
                         self.random_team.team_id)


class UserTests(MainSauceLab):
    @classmethod
    def setUpClass(cls) -> None:
        super(UserTests, cls).setUpClass()
        cls.users = cls.sauce_lab.accounts.account_user.all_users()
        cls.random_user = random.choice(cls.users)

    def test_all_users(self):
        self.sauce_lab.accounts.account_user.all_users()
        self.assertTrue(all((isinstance(user, UserSearch) for user in self.users)))
        self.assertTrue(all(user.user_id is not None for user in self.users))

    def test_user_search(self):
        self.assertEqual(self.sauce_lab.accounts.account_user.get_user(self.random_user.user_id).user_id,
                         self.random_user.user_id)

    def test_concurrency(self):
        self.assertIsInstance(self.sauce_lab.accounts.account_user.get_user_concurrency(self.random_user.username),
                              dict)


if __name__ == '__main__':
    unittest.main()
