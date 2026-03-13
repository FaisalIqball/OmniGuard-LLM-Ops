import logging
from .pii_masking import Masker
from .hallucination_evaluator import HallucinationEvaluator

class OmniGuard:
    """The main entry point for OmniGuard protection."""
    
    def __init__(self):
        self.masker = Masker()
        self.evaluator = HallucinationEvaluator()
        self.logger = logging.getLogger("OmniGuard")

    def protect_input(self, text: str) -> str:
        self.logger.info("Scrubbing input for PII...")
        return self.masker.mask(text)

    def validate_output(self, original_input: str, llm_output: str) -> bool:
        self.logger.info("Evaluating output for hallucinations...")
        score = self.evaluator.score(original_input, llm_output)
        return score > 0.8  # Threshold for factual consistency
