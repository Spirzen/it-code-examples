
import json

from typing import List, Dict
from datetime import datetime, timedelta

class LogQualityAnalyzer:
    """Анализатор качества лог-записей."""
    
    REQUIRED_FIELDS = {"timestamp", "level", "message", "service"}
    RECOMMENDED_FIELDS = {"trace_id", "span_id", "request_id", "component"}
    
    def analyze_sample(self, log_lines: List[str]) -> Dict:
        """Анализ выборки лог-записей."""
        total = len(log_lines)
        structured = 0
        has_trace_context = 0
        has_required_fields = 0
        level_distribution = {}
        
        for line in log_lines:
            try:
                entry = json.loads(line)
                structured += 1
                
                # Проверка обязательных полей
                if self.REQUIRED_FIELDS.issubset(entry.keys()):
                    has_required_fields += 1
                
                # Проверка контекста трассировки
                if "trace_id" in entry or "span_id" in entry:
                    has_trace_context += 1
                
                # Распределение уровней
                level = entry.get("level", "UNKNOWN")
                level_distribution[level] = level_distribution.get(level, 0) + 1
                
            except json.JSONDecodeError:
                continue
        
        return {
            "total_lines": total,
            "structured_ratio": structured / total if total > 0 else 0,
            "required_fields_ratio": has_required_fields / structured if structured > 0 else 0,
            "trace_context_ratio": has_trace_context / structured if structured > 0 else 0,
            "level_distribution": level_distribution,
            "quality_score": self._calculate_quality_score(
                structured, has_required_fields, has_trace_context, total
            )
        }
    
    def _calculate_quality_score(self, structured, required, traced, total) -> float:
        """Расчёт интегральной оценки качества логов."""
        if total == 0:
            return 0.0
        
        structure_score = structured / total
        completeness_score = required / total if total > 0 else 0
        traceability_score = traced / total if total > 0 else 0
        
        # Взвешенная оценка
        return (
            structure_score * 0.4 +
            completeness_score * 0.35 +
            traceability_score * 0.25
        )
