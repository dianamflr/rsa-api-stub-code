# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.inline_response_status200 import InlineResponseStatus200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRSAController(BaseTestCase):
    """RSAController integration test stubs"""

    def test_get_job(self):
        """Test case for get_job

        Get RSA Job Resource. Returns the status and RSA parameters of a job
        """
        response = self.client.open(
            '/rsa/jobs/{job_id}'.format(job_id='job_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_status(self):
        """Test case for get_job_status

        Get RSA Job status and status details
        """
        response = self.client.open(
            '/rsa/jobs/{job_id}/status'.format(job_id='job_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_jobs(self):
        """Test case for get_jobs

        Gets all RSA jobs. Filtering can be used to get a filtered list of jobs.
        """
        query_string = [('id', 'id_example'),
                        ('service', 'service_example'),
                        ('status', 'status_example'),
                        ('name', 'name_example'),
                        ('block', 'block_example'),
                        ('operator', 'operator_example'),
                        ('service_area', 'service_area_example'),
                        ('aggregation_level', 'aggregation_level_example'),
                        ('propagation_model_type', 'propagation_model_type_example'),
                        ('dataset_date', 'dataset_date_example'),
                        ('result_url', 'result_url_example')]
        response = self.client.open(
            '/rsa/jobs',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_job(self):
        """Test case for post_job

        Starts a New RSA Job
        """
        body = Body()
        response = self.client.open(
            '/rsa/jobs',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_stop_job(self):
        """Test case for stop_job

        Stops an RSA job
        """
        response = self.client.open(
            '/rsa/jobs/{job_id}'.format(job_id='job_id_example'),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
