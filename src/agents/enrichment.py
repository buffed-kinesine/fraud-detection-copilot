from crewai import Agent, Task, Crew
from langchain.llms import OpenAI
import logging

logger = logging.getLogger(__name__)


class FraudEnrichmentAgent:
    def __init__(self):
        self.llm = OpenAI(temperature=0.1)
        
        self.enrichment_agent = Agent(
            role='Fraud Data Enrichment Specialist',
            goal='Enriquecer casos de fraude con información contextual adicional',
            backstory='Eres un especialista en enriquecimiento de datos con experiencia en agregar contexto valioso a casos de fraude para mejorar la investigación.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def enrich_case(self, fraud_case):
        """Enriquecer un caso de fraude con información adicional."""
        enrichment_task = Task(
            description=f"""
            Enriquece el siguiente caso de fraude con información contextual:
            
            Caso: {fraud_case}
            
            Agrega:
            - Contexto histórico
            - Patrones similares
            - Información geográfica relevante
            - Análisis temporal
            - Conexiones con otros casos
            
            Proporciona información enriquecida que ayude en la investigación.
            """,
            agent=self.enrichment_agent,
            expected_output="Caso enriquecido con información contextual adicional"
        )
        
        crew = Crew(
            agents=[self.enrichment_agent],
            tasks=[enrichment_task],
            verbose=True
        )
        
        result = crew.kickoff()
        return result

