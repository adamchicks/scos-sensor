import pytest

from results.models import TaskResult
from results.serializers import (TaskResultSerializer,
                                 TaskResultsOverviewSerializer)
from results.tests.utils import create_task_results


@pytest.mark.django_db
def test_task_result_serializer(user_client):
    create_task_results(1, user_client)
    tr = TaskResult.objects.get()
    context = {'request': None}
    r = TaskResultSerializer(tr, context=context)
    assert r.data['task_id'] == 1
    assert r.data['self'] == '/api/v1/results/test/1/'
    assert r.data['schedule_entry'] == '/api/v1/schedule/test/'
    assert r.data['detail'] == ''
    assert r.data['result'] == 'success'
    assert r.data['duration'] == '00:00:00.000001'


# FIXME: having problems reversing return-detail url, probably sth to do with
# url path versioning
@pytest.mark.xfail
@pytest.mark.django_db
def test_task_result_overview_serializer(user_client, rf):
    from schedule.models import ScheduleEntry

    create_task_results(1, user_client)
    entries = ScheduleEntry.objects.all()
    context = {'request': None}
    r = TaskResultsOverviewSerializer(entries, many=True, context=context)
    assert r.data
    # TODO: complete assertions
    assert r
