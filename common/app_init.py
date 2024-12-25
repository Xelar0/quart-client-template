from common.ai.ai_assistant_service_impl import AiAssistantService
from common.auth.auth import authenticate
from common.repository.cyoda.cyoda_repository import CyodaRepository
from common.service.service import EntityServiceImpl

cyoda_token = authenticate()
ai_service = AiAssistantService()
entity_repository = CyodaRepository()
entity_service = EntityServiceImpl(entity_repository)