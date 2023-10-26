# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from .types import (
    EmailFlag,
    EmailTry,
    Email,
    DomainStatistics,
    Domain,
    CreateEmailResponse,
    DomainLastStatusDkimRecord,
    DomainLastStatusSpfRecord,
    DomainReputation,
    DomainStatistics,
    Email,
    EmailTry,
    ListDomainsResponse,
    ListEmailsResponse,
    Statistics,
    CreateDomainRequest,
    CreateEmailRequestAddress,
    CreateEmailRequestAttachment,
    CreateEmailRequest,
)


def unmarshal_DomainReputation(data: Any) -> DomainReputation:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'DomainReputation' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("previous_score", None)
    args["previous_score"] = field

    field = data.get("previous_scored_at", None)
    args["previous_scored_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("score", None)
    args["score"] = field

    field = data.get("scored_at", None)
    args["scored_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("status", None)
    args["status"] = field

    return DomainReputation(**args)


def unmarshal_DomainStatistics(data: Any) -> DomainStatistics:
    if type(data) is not dict:
        raise TypeError(
            "Unmarshalling the type 'EmailTry' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("rank", None)
    args["rank"] = field

    field = data.get("code", None)
    args["code"] = field

    field = data.get("message", None)
    args["message"] = field

    field = data.get("tried_at", None)
    args["tried_at"] = parser.isoparse(field) if isinstance(field, str) else field

    return EmailTry(**args)


def unmarshal_Email(data: Any) -> Email:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Email' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("message_id", None)
    args["message_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("mail_from", None)
    args["mail_from"] = field

    field = data.get("mail_rcpt", None)
    args["mail_rcpt"] = field

    field = data.get("rcpt_to", None)
    args["rcpt_to"] = field

    field = data.get("rcpt_type", None)
    args["rcpt_type"] = field

    field = data.get("subject", None)
    args["subject"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("try_count", None)
    args["try_count"] = field

    field = data.get("last_tries", None)
    args["last_tries"] = (
        [unmarshal_EmailTry(v) for v in field] if field is not None else None
    )

    field = data.get("flags", None)
    args["flags"] = [EmailFlag(v) for v in field] if field is not None else None

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("status_details", None)
    args["status_details"] = field

    return Email(**args)


def unmarshal_DomainStatistics(data: Any) -> DomainStatistics:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainStatistics' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("sent_count", None)
    args["sent_count"] = field

    field = data.get("failed_count", None)
    args["failed_count"] = field

    field = data.get("canceled_count", None)
    args["canceled_count"] = field

    return DomainStatistics(**args)


def unmarshal_Domain(data: Any) -> Domain:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Domain' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("id", None)
    args["id"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("spf_config", None)
    args["spf_config"] = field

    field = data.get("dkim_config", None)
    args["dkim_config"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("reputation", None)
    args["reputation"] = (
        unmarshal_DomainReputation(field) if field is not None else None
    )

    field = data.get("revoked_at", None)
    args["revoked_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("spf_config", None)
    args["spf_config"] = field

    field = data.get("statistics", None)
    args["statistics"] = (
        unmarshal_DomainStatistics(field) if field is not None else None
    )

    field = data.get("status", None)
    args["status"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("organization_id", None)
    args["organization_id"] = field

    field = data.get("spf_config", None)
    args["spf_config"] = field

    field = data.get("next_check_at", None)
    args["next_check_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("last_valid_at", None)
    args["last_valid_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("revoked_at", None)
    args["revoked_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("last_error", None)
    args["last_error"] = field

    field = data.get("statistics", None)
    args["statistics"] = unmarshal_DomainStatistics(field)

    return Domain(**args)


def unmarshal_CreateEmailResponse(data: Any) -> CreateEmailResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'CreateEmailResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("emails", None)
    args["emails"] = [unmarshal_Email(v) for v in field] if field is not None else None

    return CreateEmailResponse(**args)


def unmarshal_DomainLastStatusDkimRecord(data: Any) -> DomainLastStatusDkimRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatusDkimRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status", None)
    args["status"] = field

    field = data.get("last_valid_at", None)
    args["last_valid_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("error", None)
    args["error"] = field

    return DomainLastStatusDkimRecord(**args)


def unmarshal_DomainLastStatusSpfRecord(data: Any) -> DomainLastStatusSpfRecord:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatusSpfRecord' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status", None)
    args["status"] = field

    field = data.get("last_valid_at", None)
    args["last_valid_at"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("error", None)
    args["error"] = field

    return DomainLastStatusSpfRecord(**args)


def unmarshal_DomainLastStatus(data: Any) -> DomainLastStatus:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'DomainLastStatus' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("domain_id", None)
    args["domain_id"] = field

    field = data.get("domain_name", None)
    args["domain_name"] = field

    field = data.get("spf_record", None)
    args["spf_record"] = unmarshal_DomainLastStatusSpfRecord(field)

    field = data.get("dkim_record", None)
    args["dkim_record"] = unmarshal_DomainLastStatusDkimRecord(field)

    return DomainLastStatus(**args)


def unmarshal_ListDomainsResponse(data: Any) -> ListDomainsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListDomainsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("domains", None)
    args["domains"] = (
        [unmarshal_Domain(v) for v in field] if field is not None else None
    )

    return ListDomainsResponse(**args)


def unmarshal_ListEmailsResponse(data: Any) -> ListEmailsResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListEmailsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("emails", None)
    args["emails"] = [unmarshal_Email(v) for v in field] if field is not None else None

    return ListEmailsResponse(**args)


def unmarshal_Statistics(data: Any) -> Statistics:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Statistics' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("new_count", None)
    args["new_count"] = field

    field = data.get("sending_count", None)
    args["sending_count"] = field

    field = data.get("sent_count", None)
    args["sent_count"] = field

    field = data.get("failed_count", None)
    args["failed_count"] = field

    field = data.get("canceled_count", None)
    args["canceled_count"] = field

    return Statistics(**args)


def marshal_CreateDomainRequest(
    request: CreateDomainRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.domain_name is not None:
        output["domain_name"] = request.domain_name

    if request.accept_tos is not None:
        output["accept_tos"] = request.accept_tos

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    return output


def marshal_CreateEmailRequestAddress(
    request: CreateEmailRequestAddress,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.email is not None:
        output["email"] = request.email

    if request.name is not None:
        output["name"] = request.name

    return output


def marshal_CreateEmailRequestAttachment(
    request: CreateEmailRequestAttachment,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.name is not None:
        output["name"] = request.name

    if request.type_ is not None:
        output["type"] = request.type_

    if request.content is not None:
        output["content"] = request.content

    return output


def marshal_CreateEmailRequest(
    request: CreateEmailRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.subject is not None:
        output["subject"] = request.subject

    if request.text is not None:
        output["text"] = request.text

    if request.html is not None:
        output["html"] = request.html

    if request.from_ is not None:
        output["from"] = (marshal_CreateEmailRequestAddress(request.from_, defaults),)

    if request.to is not None:
        output["to"] = [
            marshal_CreateEmailRequestAddress(item, defaults) for item in request.to
        ]

    if request.cc is not None:
        output["cc"] = [
            marshal_CreateEmailRequestAddress(item, defaults) for item in request.cc
        ]

    if request.bcc is not None:
        output["bcc"] = [
            marshal_CreateEmailRequestAddress(item, defaults) for item in request.bcc
        ]

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.attachments is not None:
        output["attachments"] = [
            marshal_CreateEmailRequestAttachment(item, defaults)
            for item in request.attachments
        ]

    if request.send_before is not None:
        output["send_before"] = request.send_before

    return output
