from uuid import uuid4


class PluginSpecification:
    def __init__(self, spec):
        self._spec = spec

    def id(self) -> str:
        return str(uuid4())

    def name(self) -> str:
        return self._spec.get('name', '')

    def author(self) -> str:
        return self._spec.get('author', '')

    def description(self) -> str:
        return self._spec.get('description', '')

    def version(self) -> str:
        return self._spec.get('version', '')

    def release_notes(self) -> str:
        return self._spec.get('release_notes', '')
