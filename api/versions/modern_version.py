from rest_framework.versioning import URLPathVersioning


class ModernAPIVersion(URLPathVersioning):
    default_version = "v2"
    allowed_versions = ["v1", "v2"]
    version_param = "version"