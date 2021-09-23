from saucelab_api_client.category import Base


class Insights(Base):
    __sub_host = '/v1/analytics'

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

        return self._session.request('get', f'{self.__sub_host}/tests', params=params)
