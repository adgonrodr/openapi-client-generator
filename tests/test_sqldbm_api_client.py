"""Auto‐generated pytest tests for SqlDbmAPIClient, using the “rich” manifest."""
import pytest
from sqldbm_api_client.sqldbm_api_client import SqlDbmAPIClient
#
# —— module‐level helper types / fixtures ——
#
class FakeResponse:
    """
    A minimal stand‐in for requests.Response that supports:
      • .headers (a dict)
      • .text   (for YAML/XML payloads)
      • .json() (for JSON payloads)
    """
    def __init__(self, headers, body_text=None, body_json=None):
        self.headers = headers
        self._body_text = body_text
        self._body_json = body_json
    def raise_for_status(self):
        return None
    def json(self):
        if self._body_json is None:
            raise ValueError("Called .json() on non‐JSON response")
        return self._body_json
    @property
    def text(self):
        return self._body_text
@pytest.fixture
def patched_client(monkeypatch):
    """
    Returns a tuple (client, captured) where:
      • client.session.request has been monkeypatched to:
          – record all incoming arguments into `captured`
          – return FakeResponse based on the incoming Accept header
      • captured is a dict with keys: method, url, params, json, headers
    """
    client = SqlDbmAPIClient("http://api.example.com", token="TEST_TOKEN")
    captured = {}
    def fake_request(method, url, params=None, json=None, headers=None):
        # 1) Record everything the client passed
        captured.update({
            "method":  method,
            "url":     url,
            "params":  params or {},
            "json":    json,
            "headers": headers or {}
        })
        # 2) If the test wants YAML/XML, return FakeResponse with that mediaType
        accept = (headers or {}).get("Accept", "")
        if "application/x-yaml" in accept:
            return FakeResponse(
                headers={"Content-Type": "application/x-yaml"},
                body_text="dummy: yaml"
            )
        if "application/x-yaml" in accept:
            return FakeResponse(
                headers={"Content-Type": "application/x-yaml"},
                body_text="dummy: yaml"
            )
        if "application/x-yaml" in accept:
            return FakeResponse(
                headers={"Content-Type": "application/x-yaml"},
                body_text="dummy: yaml"
            )
        if "application/x-yaml" in accept:
            return FakeResponse(
                headers={"Content-Type": "application/x-yaml"},
                body_text="dummy: yaml"
            )
        if "application/json" in accept:
            return FakeResponse(
                headers={"Content-Type": "application/json"},
                body_text="dummy: yaml"
            )
        if "application/json" in accept:
            return FakeResponse(
                headers={"Content-Type": "application/json"},
                body_text="dummy: yaml"
            )
        if "application/json" in accept:
            return FakeResponse(
                headers={"Content-Type": "application/json"},
                body_text="dummy: yaml"
            )
        if "application/json" in accept:
            return FakeResponse(
                headers={"Content-Type": "application/json"},
                body_text="dummy: yaml"
            )
        if "application/json" in accept:
            return FakeResponse(
                headers={"Content-Type": "application/json"},
                body_text="dummy: yaml"
            )
        if "application/json" in accept:
            return FakeResponse(
                headers={"Content-Type": "application/json"},
                body_text="dummy: yaml"
            )
        if "application/x-yaml" in accept:
            return FakeResponse(
                headers={"Content-Type": "application/x-yaml"},
                body_text="dummy: yaml"
            )
        # 3) Otherwise, return a JSON response
        return FakeResponse(
            headers={"Content-Type": "application/json"},
            body_json={"ok": True}
        )
    monkeypatch.setattr(client.session, "request", fake_request)
    return client, captured
def test_get_projects_project_id_revisions_last_dbtyaml(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    project_id = 1
    format = "Source"
    generate_data_types = False
    generate_constraints = False
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_projects_project_id_revisions_last_dbtyaml(project_id, format, generate_data_types, generate_constraints)
    # 4) Build the expected URL
    expected_url = client.base_url + "/projects/{projectId}/revisions/last/dbtyaml"
    expected_url = expected_url.format(
        projectId=project_id
    )
    # 5) Build expected params dict
    expected_params = {}
    if format is not None:
        expected_params["format"] = format
    if generate_data_types is not None:
        expected_params["generateDataTypes"] = generate_data_types
    if generate_constraints is not None:
        expected_params["generateConstraints"] = generate_constraints
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # If the operation’s 200 response is application/x-yaml, we should get .text
    if "application/x-yaml" in (captured["headers"].get("Accept", "") or ""):
        assert response == "dummy: yaml"
    else:
        assert response == {"ok": True}
def test_get_projects_project_id_revisions_revision_id_dbtyaml(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    project_id = 1
    revision_id = 1
    format = "Source"
    generate_data_types = False
    generate_constraints = False
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_projects_project_id_revisions_revision_id_dbtyaml(project_id, revision_id, format, generate_data_types, generate_constraints)
    # 4) Build the expected URL
    expected_url = client.base_url + "/projects/{projectId}/revisions/{revisionId}/dbtyaml"
    expected_url = expected_url.format(
        projectId=project_id, 
        revisionId=revision_id
    )
    # 5) Build expected params dict
    expected_params = {}
    if format is not None:
        expected_params["format"] = format
    if generate_data_types is not None:
        expected_params["generateDataTypes"] = generate_data_types
    if generate_constraints is not None:
        expected_params["generateConstraints"] = generate_constraints
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # If the operation’s 200 response is application/x-yaml, we should get .text
    if "application/x-yaml" in (captured["headers"].get("Accept", "") or ""):
        assert response == "dummy: yaml"
    else:
        assert response == {"ok": True}
def test_get_projects_project_id_revisions_last_objects_dbtyaml(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    project_id = 1
    name = "test"
    format = "Source"
    case_sensitive = False
    generate_data_types = False
    generate_constraints = False
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_projects_project_id_revisions_last_objects_dbtyaml(project_id, name, format, case_sensitive, generate_data_types, generate_constraints)
    # 4) Build the expected URL
    expected_url = client.base_url + "/projects/{projectId}/revisions/last/objects/dbtyaml"
    expected_url = expected_url.format(
        projectId=project_id
    )
    # 5) Build expected params dict
    expected_params = {}
    if name is not None:
        expected_params["name"] = name
    if format is not None:
        expected_params["format"] = format
    if case_sensitive is not None:
        expected_params["caseSensitive"] = case_sensitive
    if generate_data_types is not None:
        expected_params["generateDataTypes"] = generate_data_types
    if generate_constraints is not None:
        expected_params["generateConstraints"] = generate_constraints
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # If the operation’s 200 response is application/x-yaml, we should get .text
    if "application/x-yaml" in (captured["headers"].get("Accept", "") or ""):
        assert response == "dummy: yaml"
    else:
        assert response == {"ok": True}
def test_get_projects_project_id_revisions_revision_id_objects_dbtyaml(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    project_id = 1
    revision_id = 1
    name = "test"
    format = "Source"
    case_sensitive = False
    generate_data_types = False
    generate_constraints = False
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_projects_project_id_revisions_revision_id_objects_dbtyaml(project_id, revision_id, name, format, case_sensitive, generate_data_types, generate_constraints)
    # 4) Build the expected URL
    expected_url = client.base_url + "/projects/{projectId}/revisions/{revisionId}/objects/dbtyaml"
    expected_url = expected_url.format(
        projectId=project_id, 
        revisionId=revision_id
    )
    # 5) Build expected params dict
    expected_params = {}
    if name is not None:
        expected_params["name"] = name
    if format is not None:
        expected_params["format"] = format
    if case_sensitive is not None:
        expected_params["caseSensitive"] = case_sensitive
    if generate_data_types is not None:
        expected_params["generateDataTypes"] = generate_data_types
    if generate_constraints is not None:
        expected_params["generateConstraints"] = generate_constraints
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # If the operation’s 200 response is application/x-yaml, we should get .text
    if "application/x-yaml" in (captured["headers"].get("Accept", "") or ""):
        assert response == "dummy: yaml"
    else:
        assert response == {"ok": True}
def test_get_projects(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_projects()
    # 4) Build the expected URL
    expected_url = client.base_url + "/projects"
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # No special mediaType was declared → always JSON
    assert response == {"ok": True}
def test_get_projects_project_id_revisions(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    project_id = 1
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_projects_project_id_revisions(project_id)
    # 4) Build the expected URL
    expected_url = client.base_url + "/projects/{projectId}/revisions"
    expected_url = expected_url.format(
        projectId=project_id
    )
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # No special mediaType was declared → always JSON
    assert response == {"ok": True}
def test_get_projects_project_id_revisions_revision_id(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    project_id = 1
    revision_id = 1
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_projects_project_id_revisions_revision_id(project_id, revision_id)
    # 4) Build the expected URL
    expected_url = client.base_url + "/projects/{projectId}/revisions/{revisionId}"
    expected_url = expected_url.format(
        projectId=project_id, 
        revisionId=revision_id
    )
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # No special mediaType was declared → always JSON
    assert response == {"ok": True}
def test_get_projects_project_id_revisions_last(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    project_id = 1
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_projects_project_id_revisions_last(project_id)
    # 4) Build the expected URL
    expected_url = client.base_url + "/projects/{projectId}/revisions/last"
    expected_url = expected_url.format(
        projectId=project_id
    )
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # No special mediaType was declared → always JSON
    assert response == {"ok": True}
def test_get_projects_project_id_revisions_revision_id_ddl(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    project_id = 1
    revision_id = 1
    accept = "test"
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_projects_project_id_revisions_revision_id_ddl(project_id, revision_id, accept)
    # 4) Build the expected URL
    expected_url = client.base_url + "/projects/{projectId}/revisions/{revisionId}/ddl"
    expected_url = expected_url.format(
        projectId=project_id, 
        revisionId=revision_id
    )
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    if accept is not None:
        expected_headers["Accept"] = accept
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # If the operation’s 200 response is application/json, we should get .text
    if "application/json" in (captured["headers"].get("Accept", "") or ""):
        assert response == "dummy: yaml"
    else:
        assert response == {"ok": True}
def test_get_projects_project_id_revisions_last_ddl(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    project_id = 1
    accept = "test"
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_projects_project_id_revisions_last_ddl(project_id, accept)
    # 4) Build the expected URL
    expected_url = client.base_url + "/projects/{projectId}/revisions/last/ddl"
    expected_url = expected_url.format(
        projectId=project_id
    )
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    if accept is not None:
        expected_headers["Accept"] = accept
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # If the operation’s 200 response is application/json, we should get .text
    if "application/json" in (captured["headers"].get("Accept", "") or ""):
        assert response == "dummy: yaml"
    else:
        assert response == {"ok": True}
def test_get_projects_project_id_environments(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    project_id = 1
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_projects_project_id_environments(project_id)
    # 4) Build the expected URL
    expected_url = client.base_url + "/projects/{projectId}/environments"
    expected_url = expected_url.format(
        projectId=project_id
    )
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # No special mediaType was declared → always JSON
    assert response == {"ok": True}
def test_get_projects_project_id_alter(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    project_id = 1
    accept = "test"
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_projects_project_id_alter(project_id, accept)
    # 4) Build the expected URL
    expected_url = client.base_url + "/projects/{projectId}/alter"
    expected_url = expected_url.format(
        projectId=project_id
    )
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    if accept is not None:
        expected_headers["Accept"] = accept
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # If the operation’s 200 response is application/json, we should get .text
    if "application/json" in (captured["headers"].get("Accept", "") or ""):
        assert response == "dummy: yaml"
    else:
        assert response == {"ok": True}
def test_get_projects_project_id_alter_compare(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    project_id = 1
    revision_id = 1
    environment_id = 1
    with_revision_id = 1
    with_environment_id = 1
    accept = "test"
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_projects_project_id_alter_compare(project_id, revision_id, environment_id, with_revision_id, with_environment_id, accept)
    # 4) Build the expected URL
    expected_url = client.base_url + "/projects/{projectId}/alter/compare"
    expected_url = expected_url.format(
        projectId=project_id
    )
    # 5) Build expected params dict
    expected_params = {}
    if revision_id is not None:
        expected_params["revisionId"] = revision_id
    if environment_id is not None:
        expected_params["environmentId"] = environment_id
    if with_revision_id is not None:
        expected_params["withRevisionId"] = with_revision_id
    if with_environment_id is not None:
        expected_params["withEnvironmentId"] = with_environment_id
    # 6) Build expected headers
    expected_headers = {}
    if accept is not None:
        expected_headers["Accept"] = accept
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # If the operation’s 200 response is application/json, we should get .text
    if "application/json" in (captured["headers"].get("Accept", "") or ""):
        assert response == "dummy: yaml"
    else:
        assert response == {"ok": True}
def test_get_projects_project_id_revisions_last_objects_ddl(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    project_id = 1
    name = "test"
    case_sensitive = False
    accept = "test"
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_projects_project_id_revisions_last_objects_ddl(project_id, name, case_sensitive, accept)
    # 4) Build the expected URL
    expected_url = client.base_url + "/projects/{projectId}/revisions/last/objects/ddl"
    expected_url = expected_url.format(
        projectId=project_id
    )
    # 5) Build expected params dict
    expected_params = {}
    if name is not None:
        expected_params["name"] = name
    if case_sensitive is not None:
        expected_params["caseSensitive"] = case_sensitive
    # 6) Build expected headers
    expected_headers = {}
    if accept is not None:
        expected_headers["Accept"] = accept
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # If the operation’s 200 response is application/json, we should get .text
    if "application/json" in (captured["headers"].get("Accept", "") or ""):
        assert response == "dummy: yaml"
    else:
        assert response == {"ok": True}
def test_get_projects_project_id_revisions_revision_id_objects_ddl(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    project_id = 1
    revision_id = 1
    name = "test"
    case_sensitive = False
    accept = "test"
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_projects_project_id_revisions_revision_id_objects_ddl(project_id, revision_id, name, case_sensitive, accept)
    # 4) Build the expected URL
    expected_url = client.base_url + "/projects/{projectId}/revisions/{revisionId}/objects/ddl"
    expected_url = expected_url.format(
        projectId=project_id, 
        revisionId=revision_id
    )
    # 5) Build expected params dict
    expected_params = {}
    if name is not None:
        expected_params["name"] = name
    if case_sensitive is not None:
        expected_params["caseSensitive"] = case_sensitive
    # 6) Build expected headers
    expected_headers = {}
    if accept is not None:
        expected_headers["Accept"] = accept
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # If the operation’s 200 response is application/json, we should get .text
    if "application/json" in (captured["headers"].get("Accept", "") or ""):
        assert response == "dummy: yaml"
    else:
        assert response == {"ok": True}
def test_get_flows(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_flows()
    # 4) Build the expected URL
    expected_url = client.base_url + "/flows"
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # No special mediaType was declared → always JSON
    assert response == {"ok": True}
def test_get_flows_flow_id(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    flow_id = "test"
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_flows_flow_id(flow_id)
    # 4) Build the expected URL
    expected_url = client.base_url + "/flows/{flowId}"
    expected_url = expected_url.format(
        flowId=flow_id
    )
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # No special mediaType was declared → always JSON
    assert response == {"ok": True}
def test_get_runs(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    run_type = "Run"
    designation_type = "Flow"
    designation_name = "test"
    status = "Success"
    start_time_more_than_or_equal = "test"
    start_time_less_than_or_equal = "test"
    end_time_more_than_or_equal = "test"
    end_time_less_than_or_equal = "test"
    duration_more_than_or_equal = 1
    duration_less_than_or_equal = 1
    triggered_by = "test"
    commit_id = "test"
    commit_date_more_than_or_equal = "test"
    commit_date_less_than_or_equal = "test"
    committed_by = "test"
    commit_message = "test"
    flow_id = "test"
    tx_object_id = "test"
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_runs(run_type, designation_type, designation_name, status, start_time_more_than_or_equal, start_time_less_than_or_equal, end_time_more_than_or_equal, end_time_less_than_or_equal, duration_more_than_or_equal, duration_less_than_or_equal, triggered_by, commit_id, commit_date_more_than_or_equal, commit_date_less_than_or_equal, committed_by, commit_message, flow_id, tx_object_id)
    # 4) Build the expected URL
    expected_url = client.base_url + "/runs"
    # 5) Build expected params dict
    expected_params = {}
    if run_type is not None:
        expected_params["runType"] = run_type
    if designation_type is not None:
        expected_params["designationType"] = designation_type
    if designation_name is not None:
        expected_params["designationName"] = designation_name
    if status is not None:
        expected_params["status"] = status
    if start_time_more_than_or_equal is not None:
        expected_params["startTimeMoreThanOrEqual"] = start_time_more_than_or_equal
    if start_time_less_than_or_equal is not None:
        expected_params["startTimeLessThanOrEqual"] = start_time_less_than_or_equal
    if end_time_more_than_or_equal is not None:
        expected_params["endTimeMoreThanOrEqual"] = end_time_more_than_or_equal
    if end_time_less_than_or_equal is not None:
        expected_params["endTimeLessThanOrEqual"] = end_time_less_than_or_equal
    if duration_more_than_or_equal is not None:
        expected_params["durationMoreThanOrEqual"] = duration_more_than_or_equal
    if duration_less_than_or_equal is not None:
        expected_params["durationLessThanOrEqual"] = duration_less_than_or_equal
    if triggered_by is not None:
        expected_params["triggeredBy"] = triggered_by
    if commit_id is not None:
        expected_params["commitId"] = commit_id
    if commit_date_more_than_or_equal is not None:
        expected_params["commitDateMoreThanOrEqual"] = commit_date_more_than_or_equal
    if commit_date_less_than_or_equal is not None:
        expected_params["commitDateLessThanOrEqual"] = commit_date_less_than_or_equal
    if committed_by is not None:
        expected_params["committedBy"] = committed_by
    if commit_message is not None:
        expected_params["commitMessage"] = commit_message
    if flow_id is not None:
        expected_params["flowId"] = flow_id
    if tx_object_id is not None:
        expected_params["txObjectId"] = tx_object_id
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # No special mediaType was declared → always JSON
    assert response == {"ok": True}
def test_post_runs(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    # 2) Prepare dummy requestBody if needed
    body = {}
    # 3) Call the client method
    response = client.post_runs(body)
    # 4) Build the expected URL
    expected_url = client.base_url + "/runs"
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "POST"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # No special mediaType was declared → always JSON
    assert response == {"ok": True}
def test_get_runs_run_id(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    run_id = "test"
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_runs_run_id(run_id)
    # 4) Build the expected URL
    expected_url = client.base_url + "/runs/{runId}"
    expected_url = expected_url.format(
        runId=run_id
    )
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # No special mediaType was declared → always JSON
    assert response == {"ok": True}
def test_get_runs_run_id_status(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    run_id = "test"
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_runs_run_id_status(run_id)
    # 4) Build the expected URL
    expected_url = client.base_url + "/runs/{runId}/status"
    expected_url = expected_url.format(
        runId=run_id
    )
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # No special mediaType was declared → always JSON
    assert response == {"ok": True}
def test_post_runs_run_id_cancel(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    run_id = "test"
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.post_runs_run_id_cancel(run_id)
    # 4) Build the expected URL
    expected_url = client.base_url + "/runs/{runId}/cancel"
    expected_url = expected_url.format(
        runId=run_id
    )
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "POST"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # No special mediaType was declared → always JSON
    assert response == {"ok": True}
def test_get_tx_environment(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_tx_environment()
    # 4) Build the expected URL
    expected_url = client.base_url + "/tx_environment"
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # No special mediaType was declared → always JSON
    assert response == {"ok": True}
def test_get_tx_objects(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_tx_objects()
    # 4) Build the expected URL
    expected_url = client.base_url + "/tx_objects"
    # 5) Build expected params dict
    expected_params = {}
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # No special mediaType was declared → always JSON
    assert response == {"ok": True}
def test_get_tx_objects_object_name(patched_client):
    client, captured = patched_client
    # 1) Prepare dummy args for all parameters
    object_name = "test"
    case_sensitive = False
    # 2) Prepare dummy requestBody if needed
    # 3) Call the client method
    response = client.get_tx_objects_object_name(object_name, case_sensitive)
    # 4) Build the expected URL
    expected_url = client.base_url + "/tx_objects/{objectName}"
    expected_url = expected_url.format(
        objectName=object_name
    )
    # 5) Build expected params dict
    expected_params = {}
    if case_sensitive is not None:
        expected_params["caseSensitive"] = case_sensitive
    # 6) Build expected headers
    expected_headers = {}
    # 7) Assertions
    assert captured["method"] == "GET"
    assert captured["url"] == expected_url
    assert captured["params"] == expected_params
    assert captured["headers"] == expected_headers
    # If the operation’s 200 response is application/x-yaml, we should get .text
    if "application/x-yaml" in (captured["headers"].get("Accept", "") or ""):
        assert response == "dummy: yaml"
    else:
        assert response == {"ok": True}