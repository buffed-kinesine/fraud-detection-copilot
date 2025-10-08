from crewai import Agent, Task, Crew
from langchain.llms import OpenAI
import logging

logger = logging.getLogger(__name__)


class FraudAuditorAgent:
    def __init__(self, model=None):
        self.model = model
        self.llm = OpenAI(temperature=0.1)
        
        self.auditor_agent = Agent(
            role='Fraud Detection Auditor',
            goal='Analizar transacciones y detectar posibles fraudes',
            backstory='Eres un experto auditor financiero con años de experiencia en detección de fraudes. Tu trabajo es analizar transacciones y determinar si son fraudulentas basándote en patrones sospechosos.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def analyze_transaction(self, transaction):
        """Analizar una transacción individual."""
        analysis_task = Task(
            description=f"""
            Analiza la siguiente transacción para detectar posibles indicadores de fraude:
            
            Transacción: {transaction}
            
            Considera los siguientes factores:
            - Monto de la transacción
            - Tipo de transacción
            - Balances de origen y destino
            - Patrones sospechosos
            
            Proporciona:
            1. Nivel de riesgo (BAJO, MEDIO, ALTO)
            2. Razones para tu evaluación
            3. Recomendaciones de acción
            """,
            agent=self.auditor_agent,
            expected_output="Análisis detallado del riesgo de fraude con recomendaciones"
        )
        
        crew = Crew(
            agents=[self.auditor_agent],
            tasks=[analysis_task],
            verbose=True
        )
        
        result = crew.kickoff()
        return result
    
    def batch_analyze(self, transactions):
        """Analizar múltiples transacciones."""
        results = []
        for transaction in transactions:
            try:
                result = self.analyze_transaction(transaction)
                results.append({
                    'transaction': transaction,
                    'analysis': result
                })
            except Exception as e:
                logger.error(f"Error analizando transacción: {e}")
                results.append({
                    'transaction': transaction,
                    'error': str(e)
                })
        return results

