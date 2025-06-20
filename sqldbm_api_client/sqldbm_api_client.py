"""Auto‐generated API client from Swagger/OpenAPI manifests."""
import requests
from typing import Any, Dict, List, Optional
class SqlDbmAPIClient:
    """
    Wraps a requests.Session to call API endpoints.
    :param base_url: Base URL for API.
    :param token: Bearer token (if any).
    :param headers: Default headers (optional).
    """
    def __init__(self, base_url: str, token: Optional[str] = None, headers: Optional[Dict[str,str]] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        if token:
            # inject Bearer token if provided
            self.session.headers.update({"Authorization": f"Bearer {token}"})
        if headers:
            self.session.headers.update(headers)
    def get_projects_project_id_revisions_last_dbtyaml(
        self,
        project_id: int,
        format: str = 'Source',
        generate_data_types: bool = False,
        generate_constraints: bool = False,
    ) -> Any:
        """
        Generate dbt YAML for the latest revision
        :param project_id: No description.
        :type project_id: int
        :param format: Optional, default='Source'. No description.
        :type format: str
        :param generate_data_types: Optional, default=False. No description.
        :type generate_data_types: bool
        :param generate_constraints: Optional, default=False. No description.
        :type generate_constraints: bool
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/projects/{projectId}/revisions/last/dbtyaml"
        url = url.format(
            projectId=project_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        if format is not None:
            params['format'] = format
        if generate_data_types is not None:
            params['generateDataTypes'] = generate_data_types
        if generate_constraints is not None:
            params['generateConstraints'] = generate_constraints
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        content_type = response.headers.get("Content-Type", "")
        # if it's JSON, parse it; otherwise hand back raw text
        if "application/json" in content_type:
            return response.json()
        else:
            return response.text
    def get_projects_project_id_revisions_revision_id_dbtyaml(
        self,
        project_id: int,
        revision_id: int,
        format: str = 'Source',
        generate_data_types: bool = False,
        generate_constraints: bool = False,
    ) -> Any:
        """
        Generate dbt YAML for a specific revision
        :param project_id: No description.
        :type project_id: int
        :param revision_id: No description.
        :type revision_id: int
        :param format: Optional, default='Source'. No description.
        :type format: str
        :param generate_data_types: Optional, default=False. No description.
        :type generate_data_types: bool
        :param generate_constraints: Optional, default=False. No description.
        :type generate_constraints: bool
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/projects/{projectId}/revisions/{revisionId}/dbtyaml"
        url = url.format(
            projectId=project_id, 
            revisionId=revision_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        if format is not None:
            params['format'] = format
        if generate_data_types is not None:
            params['generateDataTypes'] = generate_data_types
        if generate_constraints is not None:
            params['generateConstraints'] = generate_constraints
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        content_type = response.headers.get("Content-Type", "")
        # if it's JSON, parse it; otherwise hand back raw text
        if "application/json" in content_type:
            return response.json()
        else:
            return response.text
    def get_projects_project_id_revisions_last_objects_dbtyaml(
        self,
        project_id: int,
        name: str,
        format: str = 'Model',
        case_sensitive: bool = False,
        generate_data_types: bool = False,
        generate_constraints: bool = False,
    ) -> Any:
        """
        Generate dbt YAML for a specific object of the latest revision by name
        :param project_id: No description.
        :type project_id: int
        :param name: No description.
        :type name: str
        :param format: Optional, default='Model'. No description.
        :type format: str
        :param case_sensitive: Optional, default=False. No description.
        :type case_sensitive: bool
        :param generate_data_types: Optional, default=False. No description.
        :type generate_data_types: bool
        :param generate_constraints: Optional, default=False. No description.
        :type generate_constraints: bool
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/projects/{projectId}/revisions/last/objects/dbtyaml"
        url = url.format(
            projectId=project_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        if name is not None:
            params['name'] = name
        if format is not None:
            params['format'] = format
        if case_sensitive is not None:
            params['caseSensitive'] = case_sensitive
        if generate_data_types is not None:
            params['generateDataTypes'] = generate_data_types
        if generate_constraints is not None:
            params['generateConstraints'] = generate_constraints
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        content_type = response.headers.get("Content-Type", "")
        # if it's JSON, parse it; otherwise hand back raw text
        if "application/json" in content_type:
            return response.json()
        else:
            return response.text
    def get_projects_project_id_revisions_revision_id_objects_dbtyaml(
        self,
        project_id: int,
        revision_id: int,
        name: str,
        format: str = 'Model',
        case_sensitive: bool = False,
        generate_data_types: bool = False,
        generate_constraints: bool = False,
    ) -> Any:
        """
        Generate dbt YAML for a specific object of a specific revision by name
        :param project_id: No description.
        :type project_id: int
        :param revision_id: No description.
        :type revision_id: int
        :param name: No description.
        :type name: str
        :param format: Optional, default='Model'. No description.
        :type format: str
        :param case_sensitive: Optional, default=False. No description.
        :type case_sensitive: bool
        :param generate_data_types: Optional, default=False. No description.
        :type generate_data_types: bool
        :param generate_constraints: Optional, default=False. No description.
        :type generate_constraints: bool
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/projects/{projectId}/revisions/{revisionId}/objects/dbtyaml"
        url = url.format(
            projectId=project_id, 
            revisionId=revision_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        if name is not None:
            params['name'] = name
        if format is not None:
            params['format'] = format
        if case_sensitive is not None:
            params['caseSensitive'] = case_sensitive
        if generate_data_types is not None:
            params['generateDataTypes'] = generate_data_types
        if generate_constraints is not None:
            params['generateConstraints'] = generate_constraints
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        content_type = response.headers.get("Content-Type", "")
        # if it's JSON, parse it; otherwise hand back raw text
        if "application/json" in content_type:
            return response.json()
        else:
            return response.text
    def get_projects(
        self,
    ) -> Any:
        """
        Get project list
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/projects"
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        return response.json()
    def get_projects_project_id_revisions(
        self,
        project_id: int,
    ) -> Any:
        """
        Get revision list
        :param project_id: No description.
        :type project_id: int
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/projects/{projectId}/revisions"
        url = url.format(
            projectId=project_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        return response.json()
    def get_projects_project_id_revisions_revision_id(
        self,
        project_id: int,
        revision_id: int,
    ) -> Any:
        """
        Get revision
        :param project_id: No description.
        :type project_id: int
        :param revision_id: No description.
        :type revision_id: int
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/projects/{projectId}/revisions/{revisionId}"
        url = url.format(
            projectId=project_id, 
            revisionId=revision_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        return response.json()
    def get_projects_project_id_revisions_last(
        self,
        project_id: int,
    ) -> Any:
        """
        Get the latest revision
        :param project_id: No description.
        :type project_id: int
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/projects/{projectId}/revisions/last"
        url = url.format(
            projectId=project_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        return response.json()
    def get_projects_project_id_revisions_revision_id_ddl(
        self,
        project_id: int,
        revision_id: int,
        accept: str = None,
    ) -> Any:
        """
        Get DDL
        :param project_id: No description.
        :type project_id: int
        :param revision_id: No description.
        :type revision_id: int
        :param accept: Optional, default=None. Accept
        :type accept: str
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/projects/{projectId}/revisions/{revisionId}/ddl"
        url = url.format(
            projectId=project_id, 
            revisionId=revision_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        if accept is not None:
            headers['Accept'] = accept
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        content_type = response.headers.get("Content-Type", "")
        # if it's JSON, parse it; otherwise hand back raw text
        if "application/json" in content_type:
            return response.json()
        else:
            return response.text
    def get_projects_project_id_revisions_last_ddl(
        self,
        project_id: int,
        accept: str = None,
    ) -> Any:
        """
        Get DDL for the latest revision
        :param project_id: No description.
        :type project_id: int
        :param accept: Optional, default=None. Accept
        :type accept: str
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/projects/{projectId}/revisions/last/ddl"
        url = url.format(
            projectId=project_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        if accept is not None:
            headers['Accept'] = accept
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        content_type = response.headers.get("Content-Type", "")
        # if it's JSON, parse it; otherwise hand back raw text
        if "application/json" in content_type:
            return response.json()
        else:
            return response.text
    def get_projects_project_id_environments(
        self,
        project_id: int,
    ) -> Any:
        """
        Get environment list
        :param project_id: No description.
        :type project_id: int
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/projects/{projectId}/environments"
        url = url.format(
            projectId=project_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        return response.json()
    def get_projects_project_id_alter(
        self,
        project_id: int,
        accept: str = None,
    ) -> Any:
        """
        Get alterscript for the latest revisions
        :param project_id: No description.
        :type project_id: int
        :param accept: Optional, default=None. Accept
        :type accept: str
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/projects/{projectId}/alter"
        url = url.format(
            projectId=project_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        if accept is not None:
            headers['Accept'] = accept
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        content_type = response.headers.get("Content-Type", "")
        # if it's JSON, parse it; otherwise hand back raw text
        if "application/json" in content_type:
            return response.json()
        else:
            return response.text
    def get_projects_project_id_alter_compare(
        self,
        project_id: int,
        revision_id: int = None,
        environment_id: int = None,
        with_revision_id: int = None,
        with_environment_id: int = None,
        accept: str = None,
    ) -> Any:
        """
        Get alterscript
        :param project_id: No description.
        :type project_id: int
        :param revision_id: Optional, default=None. No description.
        :type revision_id: int
        :param environment_id: Optional, default=None. No description.
        :type environment_id: int
        :param with_revision_id: Optional, default=None. No description.
        :type with_revision_id: int
        :param with_environment_id: Optional, default=None. No description.
        :type with_environment_id: int
        :param accept: Optional, default=None. Accept
        :type accept: str
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/projects/{projectId}/alter/compare"
        url = url.format(
            projectId=project_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        if revision_id is not None:
            params['revisionId'] = revision_id
        if environment_id is not None:
            params['environmentId'] = environment_id
        if with_revision_id is not None:
            params['withRevisionId'] = with_revision_id
        if with_environment_id is not None:
            params['withEnvironmentId'] = with_environment_id
        # Build header parameters
        headers: Dict[str, Any] = {}
        if accept is not None:
            headers['Accept'] = accept
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        content_type = response.headers.get("Content-Type", "")
        # if it's JSON, parse it; otherwise hand back raw text
        if "application/json" in content_type:
            return response.json()
        else:
            return response.text
    def get_projects_project_id_revisions_last_objects_ddl(
        self,
        project_id: int,
        name: str,
        case_sensitive: bool = False,
        accept: str = None,
    ) -> Any:
        """
        Get DDL for a specific object of the latest revision by name
        :param project_id: No description.
        :type project_id: int
        :param name: No description.
        :type name: str
        :param case_sensitive: Optional, default=False. No description.
        :type case_sensitive: bool
        :param accept: Optional, default=None. Accept
        :type accept: str
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/projects/{projectId}/revisions/last/objects/ddl"
        url = url.format(
            projectId=project_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        if name is not None:
            params['name'] = name
        if case_sensitive is not None:
            params['caseSensitive'] = case_sensitive
        # Build header parameters
        headers: Dict[str, Any] = {}
        if accept is not None:
            headers['Accept'] = accept
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        content_type = response.headers.get("Content-Type", "")
        # if it's JSON, parse it; otherwise hand back raw text
        if "application/json" in content_type:
            return response.json()
        else:
            return response.text
    def get_projects_project_id_revisions_revision_id_objects_ddl(
        self,
        project_id: int,
        revision_id: int,
        name: str,
        case_sensitive: bool = False,
        accept: str = None,
    ) -> Any:
        """
        Get DDL for a specific object of a specific revision by name
        :param project_id: No description.
        :type project_id: int
        :param revision_id: No description.
        :type revision_id: int
        :param name: No description.
        :type name: str
        :param case_sensitive: Optional, default=False. No description.
        :type case_sensitive: bool
        :param accept: Optional, default=None. Accept
        :type accept: str
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/projects/{projectId}/revisions/{revisionId}/objects/ddl"
        url = url.format(
            projectId=project_id, 
            revisionId=revision_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        if name is not None:
            params['name'] = name
        if case_sensitive is not None:
            params['caseSensitive'] = case_sensitive
        # Build header parameters
        headers: Dict[str, Any] = {}
        if accept is not None:
            headers['Accept'] = accept
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        content_type = response.headers.get("Content-Type", "")
        # if it's JSON, parse it; otherwise hand back raw text
        if "application/json" in content_type:
            return response.json()
        else:
            return response.text
    def get_flows(
        self,
    ) -> Any:
        """
        Returns Tx Flow list.
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/flows"
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        return response.json()
    def get_flows_flow_id(
        self,
        flow_id: str,
    ) -> Any:
        """
        Returns Tx Flow for Tx project by ID.
        :param flow_id: No description.
        :type flow_id: str
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/flows/{flowId}"
        url = url.format(
            flowId=flow_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        return response.json()
    def get_runs(
        self,
        run_type: str = None,
        designation_type: str = None,
        designation_name: str = None,
        status: str = None,
        start_time_more_than_or_equal: str = None,
        start_time_less_than_or_equal: str = None,
        end_time_more_than_or_equal: str = None,
        end_time_less_than_or_equal: str = None,
        duration_more_than_or_equal: int = None,
        duration_less_than_or_equal: int = None,
        triggered_by: str = None,
        commit_id: str = None,
        commit_date_more_than_or_equal: str = None,
        commit_date_less_than_or_equal: str = None,
        committed_by: str = None,
        commit_message: str = None,
        flow_id: str = None,
        tx_object_id: str = None,
    ) -> Any:
        """
        Returns Tx Runs list.
        :param run_type: Optional, default=None. No description.
        :type run_type: str
        :param designation_type: Optional, default=None. No description.
        :type designation_type: str
        :param designation_name: Optional, default=None. No description.
        :type designation_name: str
        :param status: Optional, default=None. No description.
        :type status: str
        :param start_time_more_than_or_equal: Optional, default=None. No description.
        :type start_time_more_than_or_equal: str
        :param start_time_less_than_or_equal: Optional, default=None. No description.
        :type start_time_less_than_or_equal: str
        :param end_time_more_than_or_equal: Optional, default=None. No description.
        :type end_time_more_than_or_equal: str
        :param end_time_less_than_or_equal: Optional, default=None. No description.
        :type end_time_less_than_or_equal: str
        :param duration_more_than_or_equal: Optional, default=None. No description.
        :type duration_more_than_or_equal: int
        :param duration_less_than_or_equal: Optional, default=None. No description.
        :type duration_less_than_or_equal: int
        :param triggered_by: Optional, default=None. No description.
        :type triggered_by: str
        :param commit_id: Optional, default=None. No description.
        :type commit_id: str
        :param commit_date_more_than_or_equal: Optional, default=None. No description.
        :type commit_date_more_than_or_equal: str
        :param commit_date_less_than_or_equal: Optional, default=None. No description.
        :type commit_date_less_than_or_equal: str
        :param committed_by: Optional, default=None. No description.
        :type committed_by: str
        :param commit_message: Optional, default=None. No description.
        :type commit_message: str
        :param flow_id: Optional, default=None. No description.
        :type flow_id: str
        :param tx_object_id: Optional, default=None. No description.
        :type tx_object_id: str
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/runs"
        # Build query parameters
        params: Dict[str, Any] = {}
        if run_type is not None:
            params['runType'] = run_type
        if designation_type is not None:
            params['designationType'] = designation_type
        if designation_name is not None:
            params['designationName'] = designation_name
        if status is not None:
            params['status'] = status
        if start_time_more_than_or_equal is not None:
            params['startTimeMoreThanOrEqual'] = start_time_more_than_or_equal
        if start_time_less_than_or_equal is not None:
            params['startTimeLessThanOrEqual'] = start_time_less_than_or_equal
        if end_time_more_than_or_equal is not None:
            params['endTimeMoreThanOrEqual'] = end_time_more_than_or_equal
        if end_time_less_than_or_equal is not None:
            params['endTimeLessThanOrEqual'] = end_time_less_than_or_equal
        if duration_more_than_or_equal is not None:
            params['durationMoreThanOrEqual'] = duration_more_than_or_equal
        if duration_less_than_or_equal is not None:
            params['durationLessThanOrEqual'] = duration_less_than_or_equal
        if triggered_by is not None:
            params['triggeredBy'] = triggered_by
        if commit_id is not None:
            params['commitId'] = commit_id
        if commit_date_more_than_or_equal is not None:
            params['commitDateMoreThanOrEqual'] = commit_date_more_than_or_equal
        if commit_date_less_than_or_equal is not None:
            params['commitDateLessThanOrEqual'] = commit_date_less_than_or_equal
        if committed_by is not None:
            params['committedBy'] = committed_by
        if commit_message is not None:
            params['commitMessage'] = commit_message
        if flow_id is not None:
            params['flowId'] = flow_id
        if tx_object_id is not None:
            params['txObjectId'] = tx_object_id
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        return response.json()
    def post_runs(
        self,
        body: Dict[str, Any],
    ) -> Any:
        """
        Triggers new run by flow id
        :param body: Request body as a dict matching the schema.
        :type body: Dict[str, Any]
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/runs"
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = body
        # Perform request
        response = self.session.request(
            method="POST",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        return response.json()
    def get_runs_run_id(
        self,
        run_id: str,
    ) -> Any:
        """
        Returns Tx Run by ID.
        :param run_id: No description.
        :type run_id: str
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/runs/{runId}"
        url = url.format(
            runId=run_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        return response.json()
    def get_runs_run_id_status(
        self,
        run_id: str,
    ) -> Any:
        """
        Returns Tx Run status by ID.
        :param run_id: No description.
        :type run_id: str
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/runs/{runId}/status"
        url = url.format(
            runId=run_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        return response.json()
    def post_runs_run_id_cancel(
        self,
        run_id: str,
    ) -> Any:
        """
        Cancel existing run by run id
        :param run_id: No description.
        :type run_id: str
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/runs/{runId}/cancel"
        url = url.format(
            runId=run_id
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="POST",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        return response.json()
    def get_tx_environment(
        self,
    ) -> Any:
        """
        Returns Tx Environment details for particular Tx project.
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/tx_environment"
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        return response.json()
    def get_tx_objects(
        self,
    ) -> Any:
        """
        Returns Tx objects list.
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/tx_objects"
        # Build query parameters
        params: Dict[str, Any] = {}
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        return response.json()
    def get_tx_objects_object_name(
        self,
        object_name: str,
        case_sensitive: bool = False,
    ) -> Any:
        """
        Returns Tx object details by name for particular Tx project.
        :param object_name: No description.
        :type object_name: str
        :param case_sensitive: Optional, default=False. No description.
        :type case_sensitive: bool
        :return: Parsed response (JSON or raw text).
        :rtype: Any
        """
        # Build URL
        url = self.base_url + "/tx_objects/{objectName}"
        url = url.format(
            objectName=object_name
        )
        # Build query parameters
        params: Dict[str, Any] = {}
        if case_sensitive is not None:
            params['caseSensitive'] = case_sensitive
        # Build header parameters
        headers: Dict[str, Any] = {}
        # Request body (if any)
        json_data = None
        # Perform request
        response = self.session.request(
            method="GET",
            url=url,
            params=params,
            json=json_data,
            headers=headers
        )
        response.raise_for_status()
        # Determine return based on response mediaType
        content_type = response.headers.get("Content-Type", "")
        # if it's JSON, parse it; otherwise hand back raw text
        if "application/json" in content_type:
            return response.json()
        else:
            return response.text