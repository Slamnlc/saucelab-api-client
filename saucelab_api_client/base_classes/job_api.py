from saucelab_api_client.category import Base


class JobsApi(Base):
    __sub_host = '/rest/v1'

    def get_user_jobs(self, username: str, limit: int = None, skip: int = None, from_: str = None, to: str = None):
        """
        https://docs.saucelabs.com/dev/api/jobs/#jobs-methods

        Get a list of recent jobs run by the specified user
        :param username: The username of the Sauce Labs user whose jobs you are looking up
        :param limit: The maximum number of jobs to return
        :param skip: Returns only the jobs beginning after this index number
        :param from_: Return only jobs that ran on or after this Unix timestamp
        :param to: Return only jobs that ran on or before this Unix timestamp
        :return:
        """
        params = {key.replace('_', ''): value for key, value in locals().items() if value}
        return self._session.request('get', f'{self.__sub_host}/{username}/jobs', params=params)

    def get_job_details(self, username: str, job_id: str):
        """
        https://docs.saucelabs.com/dev/api/jobs/#get-job-details

        Get detailed information about a specific job
        :param username: The username of the Sauce Labs user whose jobs you are looking up
        :param job_id: The Sauce Labs identifier of the job you are looking up
        :return:
        """
        return self._session.request('get', f'{self.__sub_host}/{username}/jobs/{job_id}')
