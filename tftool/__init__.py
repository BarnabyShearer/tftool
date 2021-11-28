"""Ergonomic utilities for the terraform CLI."""

import json
import re
from typing import Any, Iterable, Optional, TextIO, Tuple

JSON = Any

RESOURCE_ID = {
    # From 0.2.4
    "codeship_project": "",  # unknown
    "codeship_encrypted": "",  # unknown
    # From 0.0.8
    "dockerhub_repository": "{namespace}/{name}",
    "dockerhub_token": "",  # unknown,
    # From 4.18.0
    "github_actions_environment_secret": "{secret_name}",
    "github_actions_organization_permissions": "",  # unknown
    "github_actions_organization_secret": "{secret_name}",
    "github_actions_organization_secret_repositories": "{secret_name}",
    "github_actions_runner_group": "",  # unknown
    "github_actions_secret": "",  # unimportable
    "github_app_installation_repository": "{installation_id}:{repository}",
    "github_branch": "{repository}:{branch}",
    "github_branch_default": "{repository}",
    "github_branch_protection": "{repository}:{pattern}",
    "github_branch_protection_v3": "{repository}:{branch}",
    "github_issue_label": "{terraform}:{name}",
    "github_membership": "",  # unknown
    "github_organization_block": "",  # unimportable
    "github_organization_project": "",  # unimportable
    "github_organization_webhook": "",  # unknown
    "github_project_card": "",  # unknown
    "github_project_column": "",  # unimportable
    "github_repository": "{name}",
    "github_repository_autolink_reference": "",  # unknown
    "github_repository_collaborator": "{repository}:{username}",
    "github_repository_deploy_key": "",  # unknown
    "github_repository_environment": "{repository}:{environment}",
    "github_repository_file": "{repository}/{file}",
    "github_repository_milestone": "",  # unknown
    "github_repository_project": "",  # unimportable
    "github_repository_pull_request": "",  # unimportable
    "github_repository_webhook": "",  # unknown
    "github_team": "",  # unknown
    "github_team_membership": "{teamid}:{username}",
    "github_team_repository": "{team_id}:{repository}",
    "github_team_sync_group_mapping": "{team_slug}",
    "github_user_gpg_key": "",  # unimportable
    "github_user_invitation_accepter": "",  # unimportable
    "github_user_ssh_key": "",  # unknown
    # From 2.6.1
    "kubernetes_api_service": "{metadata[name]}",
    "kubernetes_certificate_signing_request": "",  # unimportable
    "kubernetes_cluster_role": "{metadata[name]}",
    "kubernetes_cluster_role_binding": "{metadata[name]}",
    "kubernetes_config_map": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_cron_job": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_csi_driver": "{metadata[name]}",
    "kubernetes_daemonset": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_default_service_account": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_deployment": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_endpoints": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_horizontal_pod_autoscaler": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_ingress": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_ingress_class": "{metadata[name]}",
    "kubernetes_job": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_limit_range": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_manifest": "apiVersion={manifest[apiVersion]}"
    ",kind={manifest[kind]}"
    ",namespace={manifest[metadata][namespace]}"
    ",name={manifest[metadata][name]}",
    "kubernetes_mutating_webhook_configuration": "{metadata[name]}",
    "kubernetes_namespace": "{metadata[name]}",
    "kubernetes_network_policy": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_persistent_volume": "{metadata[name]}",
    "kubernetes_persistent_volume_claim": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_pod": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_pod_disruption_budget": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_pod_security_policy": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_priority_class": "{metadata[name]}",
    "kubernetes_replication_controller": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_resource_quota": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_role": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_role_binding": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_secret": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_service": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_service_account": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_stateful_set": "{metadata[namespace]}/{metadata[name]}",
    "kubernetes_storage_class": "{metadata[name]}",
    "kubernetes_validating_webhook_configuration": "{metadata[name]}",
    # From 0.2.1
    "pgp_key": "",  # unimportable
    # From v0.1.1
    "macaroons_pypi_token": "",  # unimportable
    # From 0.1.1
    "readthedocs_project": "",  # unknown
    # From 0.1.2
    "scram_password": "",  # unimportable
}


def _filter(
    plan: TextIO,
    regex: Optional[str],
    creates: bool,
    updates: bool,
    destroys: bool,
    noops: bool,
) -> Iterable[Tuple[str, str]]:
    for resource in json.load(plan)["resource_changes"]:
        if resource["mode"] == "managed":
            if {"create": creates, "update": updates, "no-op": noops, "delete": destroys}[
                resource["change"]["actions"][0]
            ]:
                if not regex or re.search(regex, resource["address"]):
                    if resource["type"] in RESOURCE_ID:
                        id = RESOURCE_ID[resource["type"]].format(
                            **resource["change"]["after"]
                        )
                    else:
                        id = resource.get("index", resource["name"])
                    yield (resource["address"], id)
