from .rules import BusinessRule
from .exceptions import BusinessRuleException

class ValidateRulesMixin:
    def validate_rule(self, regla: BusinessRule):
        if not regla.is_valid():
            raise BusinessRuleException(regla)