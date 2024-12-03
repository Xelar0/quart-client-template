from typing import Any, List

from common.repository.crud_repository import CrudRepository
from common.repository.cyoda.cyoda_repository import CyodaRepository
from common.service.entity_service_interface import EntityService

repository: CrudRepository = CyodaRepository()
class EntityServiceImpl(EntityService):

    def get_item(self, token: str, entity_model: str, entity_version: str, id: str) -> Any:
        """Retrieve a single item based on its ID."""
        meta = repository.get_meta(token, entity_model, entity_version)
        resp = repository.find_by_id(meta, id)
        return resp

    def get_items(self, token: str, entity_model: str, entity_version: str) -> List[Any]:
        """Retrieve multiple items based on their IDs."""
        meta = repository.get_meta(token, entity_model, entity_version)
        resp = repository.find_all(meta)
        return resp

    def get_single_item_by_condition(self, token: str, entity_model: str, entity_version: str, condition: Any) -> List[Any]:
        """Retrieve multiple items based on their IDs."""
        resp = self._find_by_criteria(token, entity_model, entity_version, condition)
        return resp[0]

    def get_items_by_condition(self, token: str, entity_model: str, entity_version: str, condition: Any) -> List[Any]:
        """Retrieve multiple items based on their IDs."""
        resp = self._find_by_criteria(token, entity_model, entity_version, condition)
        return resp

    def add_item(self, token: str, entity_model: str, entity_version: str, entity: Any) -> Any:
        """Add a new item to the repository."""
        meta = repository.get_meta(token, entity_model, entity_version)
        resp = repository.save(meta, entity)
        return resp

    def update_item(self, token: str, entity_model: str, entity_version: str, id: str, entity: Any, meta: Any) -> Any:
        """Update an existing item in the repository."""
        meta = meta.update(repository.get_meta(token, entity_model, entity_version))
        resp = repository.update(meta, id, entity)
        return resp

    def _find_by_criteria(self, token, entity_model, entity_version, condition):
        meta = repository.get_meta(token, entity_model, entity_version)
        resp = repository.find_all_by_criteria(meta, condition)
        if (resp['page']['totalElements'] == 0):
            return []
        resp = resp["_embedded"]["objectNodes"]
        return resp