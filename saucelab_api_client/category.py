from saucelab_api_client.models.device import Device
from saucelab_api_client.models.file import File
from saucelab_api_client.models.group import Group
from saucelab_api_client.models.job import Job
from saucelab_api_client.session import Session


class Base:
    def __init__(self, session):
        self._session: Session = session

    @staticmethod
    def valid(response, return_class, key: str = None):
        if isinstance(response, str):
            return response
        elif key:
            return return_class(response[key]) if isinstance(response[key], dict) else \
                [return_class(elem) for elem in response[key]]
        else:
            return return_class(response) if isinstance(response, dict) else [return_class(elem) for elem in response]


class RealDevices(Base):
    sub_host: str = '/v1/rdc'

    def devices_list(self) -> [Device]:
        """
        https://docs.saucelabs.com/dev/api/rdc/#get-devices

        Get the set of real devices located at the data center,
        as well as the operating system/browser combinations and identifying information for each device
        :return: List of devices on server
        """
        return [Device(device) for device in self._session.request('get', f'{self.sub_host}/devices')]

    def get_device_by_id(self, device_id: str) -> str or Device:
        """
        https://docs.saucelabs.com/dev/api/rdc/#get-a-specific-device

        Get information about the device specified in the request
        :param device_id: The unique identifier of a device in the Sauce Labs data center
        :return:
        """
        return self.valid(self._session.request('get', f'{self.sub_host}/devices/{device_id}'), Device)

    def available_devices(self) -> [str]:
        """
        https://docs.saucelabs.com/dev/api/rdc/#get-a-specific-device

        :return: list of Device IDs for all devices in the data center that are currently free for testing
        """
        return self._session.request('get', f'{self.sub_host}/devices/available')

    def jobs(self, offset: int = None, limit: int = None) -> str or [Job]:
        """
        https://docs.saucelabs.com/dev/api/rdc/#get-real-device-jobs

        Get a list of jobs that are actively running on real devices in the data center
        :param offset: The maximum number of jobs to return
        :param limit: Limit results to those following this index number
        :return:
        """
        params = dict()
        if offset:
            params['offset'] = offset
        if limit:
            params['limit'] = limit
        return self.valid(self._session.request('get', f'{self.sub_host}/jobs', params=params), Job, key='entities')

    def job_by_id(self, job_id: str) -> str or Job:
        """
        https://docs.saucelabs.com/dev/api/rdc/#get-a-specific-real-device-job

        Get information about a specific job running on a real device at the data center
        :param job_id: The unique identifier of a job running on a real device in the data center
        :return:
        """
        return self.valid(self._session.request('get', f'{self.sub_host}/jobs/{job_id}'), return_class=Job)


class Insights(Base):
    sub_host = '/v1/analytics'

    def test_results(self, start_time, end_time, scope=None, owner=None, status=None, build=None, from_=None,
                     max_results=None, missing_build=None, query=None, desc=None, error=None):
        """
        https://docs.saucelabs.com/dev/api/insights/#get-test-results

        Returns run data for all tests that match the request criteria
        :param start_time: The starting date of the period during which the test runs executed, in YYY-MM-DDTHH:MM:SSZ
                            or Unix time format.
        :param end_time: The ending date of the period during which the test runs executed, in YYY-MM-DDTHH:MM:SSZ
                            or Unix time format.
        :param scope: Specifies the scope of the owner parameter
        :param owner: The name of one or more users in the requestor's organization who executed the requested tests.
                            This parameter is required if the scope parameter is set to single.
        :param status: Limit results to only those with a specified status
        :param build: Limit results to those grouped by this build name
        :param from_: Begin results list from this record number
        :param max_results: The maximum number of results to return
        :param missing_build: Requires no value. If this parameter is included in the query string,
                            results will only include tests with no assigned build
        :param query: Limit results to only those with this test name
        :param desc: Set to true to sort results in descending order by creation time. Default value is false
        :param error: Limit results to only those that threw this error message
        :return:
        """
        main_dict = {
            'start': start_time, 'end': end_time, 'scope': scope, 'owner': owner, 'status': status,
            'build': build, 'from': from_, 'mainDocumentTransferSize': max_results, 'missing_build': missing_build,
            'query': query, 'desc': desc, 'error': error
        }

        params = {key: value for key, value in main_dict.items() if main_dict[key] is not None}

        return self._session.request('get', f'{self.sub_host}/tests', params=params)


class Storage(Base):
    sub_host = '/v1/storage'

    def files(self, q=None, kind=None, file_id=None, team_id=None, page=None, per_page=None) -> str or [File]:
        """
        https://docs.saucelabs.com/dev/api/storage/#get-app-storage-files

        Returns the set of files that have been uploaded to Sauce Storage by the requestor
        :param q: Any search term (such as build number or file name) by which you want to filter results
        :param kind: The application type associated with the file, such as android or ios
        :param file_id: One or more specific IDs of the files to return
        :param team_id: One or more IDs of teams with which the files are shared
        :param page: Return results beginning with a specific page. Default is 1
        :param per_page: The maximum number of results to show per page
        :return:
        """
        main_dict = {
            'q': q, 'kind': kind, 'file_id': file_id, 'team_id': team_id, 'page': page, 'per_page': per_page
        }
        params = {key: value for key, value in main_dict.items() if main_dict[key] is not None}
        return self.valid(self._session.request('get', f'{self.sub_host}/files', params=params), File, 'items')

    def groups(self, q=None, kind=None, group_id=None, page=None, per_page=None) -> str or [Group]:
        """
        https://docs.saucelabs.com/dev/api/storage/#get-app-storage-groups

        Returns an array of groups (applications containing multiple files) currently in storage for the authenticated requestor
        :param q: Any search term (such as build number or file name) by which you want to filter results
        :param kind: The application type associated with the group, such as android or ios
        :param group_id: One or more specific IDs of the groups to return
        :param page: Return results beginning with a specific page. Default is 1
        :param per_page: The maximum number of results to show per page
        :return:
        """
        main_dict = {
            'q': q, 'kind': kind, 'group_id': group_id, 'page': page, 'per_page': per_page
        }
        params = {key: value for key, value in main_dict.items() if main_dict[key] is not None}

        return self.valid(self._session.request('get', f'{self.sub_host}/groups', params=params), Group, 'items')

    def upload(self, app_path: str) -> File:
        """
        https://docs.saucelabs.com/dev/api/storage/#upload-file-to-app-storage

        Uploads an application file to Sauce Storage for the purpose of mobile application testing and returns a
        unique file ID assigned to the app.
        Sauce Storage supports app files in *.apk, *.aab, *.ipa, or *.zip format, up to 4GB
        :param app_path: app file path
        :return: File object of uploaded app
        """
        if app_path.split('.')[-1] in ('apk', 'aab', 'ipa', 'zip'):
            files = {'payload': open(app_path, 'rb')}
            self._session.request('post', f'{self.sub_host}/upload', files=files)
        else:
            raise FileNotFoundError('File to send must have following extension: apk, aab, ipa, zip')

    def delete_by_file_id(self, file_id: str) -> File:
        """
        https://docs.saucelabs.com/dev/api/storage/#delete-an-app-storage-file

        Deletes the specified file from Sauce Storage
        :param file_id: The Sauce Labs identifier of the stored file
        :return:
        """
        self._session.request('delete', f"{self.sub_host}/files/{file_id}")

    def delete_all_files_by_bundle_id(self, bundle_id: str) -> [File]:
        """

        :param bundle_id:
        :return:
        """
        tuple(self.delete_by_file_id(app_id) for app_id in (app.id for app in self.files()
                                                            if app.metadata.identifier == bundle_id))
