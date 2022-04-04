import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.inline_response_status200 import InlineResponseStatus200  # noqa: E501
from swagger_server import util


def get_job(job_id):  # noqa: E501
    """Get RSA Job Resource. Returns the status and RSA parameters of a job

    Gets the job resource  The resultUrl, when appropriate, will contain a report of the RSA job. # noqa: E501

    :param job_id: ID of the RSA job
    :type job_id: str

    :rtype: List[Object]
    """
    return 'do some magic!'


def get_job_status(job_id):  # noqa: E501
    """Get RSA Job status and status details

    Gets the job status  The resultUrl, when appropriate, will contain a report of the RSA job. # noqa: E501

    :param job_id: ID of the RSA job
    :type job_id: str

    :rtype: InlineResponseStatus200
    """
    return 'do some magic!'


def get_jobs(id=None, service=None, status=None, name=None, block=None, operator=None, service_area=None, aggregation_level=None, propagation_model_type=None, dataset_date=None, result_url=None):  # noqa: E501
    """Gets all RSA jobs. Filtering can be used to get a filtered list of jobs.

    Gets all job resources based on filters. Any of the input parameters can be used as a filter. If filters are none, then all jobs will be fetched  The resultUrl, when appropriate, will contain a report of the RSA job. # noqa: E501

    :param id: ID of the RSA job
    :type id: str
    :param service: Service parameter of RSA job
    :type service: str
    :param status: Status of RSA job
    :type status: str
    :param name: Name of RSA job
    :type name: str
    :param block: Block parameter of RSA job
    :type block: str
    :param operator: Operator parameter of RSA job
    :type operator: str
    :param service_area: Service area paramter of RSA job
    :type service_area: str
    :param aggregation_level: Aggregation level paramter of RSA job
    :type aggregation_level: str
    :param propagation_model_type: Propagation model of RSA job
    :type propagation_model_type: str
    :param dataset_date: Date of RSA job
    :type dataset_date: str
    :param result_url: Result URL of RSA job
    :type result_url: str

    :rtype: List[Object]
    """
    return 'do some magic!'


def post_job(body=None):  # noqa: E501
    """Starts a New RSA Job

    Starts a new RSA job for the given parameters and returns the id of the newly  created job.  Prior to starting the job (e.g. just before executing), the job status  should become &#x60;inprogress&#x60; and following the successful completion and  saving of results, the job status will become &#x60;completed&#x60;. It is  expected that the RSA job would be in a &#x60;pending&#x60; state for only  moments.  The resultUrl, when appropriate, will contain a report of the RSA job. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponseStatus200
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def stop_job(job_id):  # noqa: E501
    """Stops an RSA job

    Stops an RSA job, and will return success if job has been successfully stopped. # noqa: E501

    :param job_id: ID of the RSA job
    :type job_id: str

    :rtype: None
    """
    return 'do some magic!'
